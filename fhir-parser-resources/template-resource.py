#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} ({{ profile.url }}) on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

{%- set imported = {} %}
{%- for klass in classes %}


{% if klass.superclass in imports and klass.superclass.module not in imported -%}
from . import {{ klass.superclass.module }}
{% set _ = imported.update({klass.superclass.module: True}) %}
{% endif -%}

class {{ klass.name }}({% if klass.superclass in imports %}{{ klass.superclass.module }}.{% endif -%}
    {{ klass.superclass.name|default('object')}}):
    """ {{ klass.short|wordwrap(width=75, wrapstring="\n    ") }}.
{%- if klass.formal %}
    
    {{ klass.formal|wordwrap(width=75, wrapstring="\n    ") }}
{%- endif %}
    """
{%- if klass.resource_type %}
    
    resource_type = "{{ klass.resource_type }}"
{%- endif %}

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
{%- for prop in klass.properties %}
    _attribute_docstrings['{{ prop.name }}'] = """{{ prop.formal if prop.enum else prop.short + '.' }}"""
{%- endfor %}

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings | {{klass.superclass.module}}.{{klass.superclass.name}}.attribute_docstrings()

    _attribute_types = {}
    """ Dictionary of attribute types."""
{%- for prop in klass.properties %}
    _attribute_types['{{ prop.name }}'] = '{% if prop.is_array %}List[{{ prop.class_name }}]{% else %}{{ prop.class_name }}{% endif %}'
{%- endfor %}

    @classmethod
    def attribute_types(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_types


    _attribute_enums = {}
    """ Dictionary of enum configuration."""
{%- for prop in klass.properties if prop.enum  %}
    _attribute_enums['{{ prop.name }}'] = {
        'url': '{{ prop.enum.definition.definition.compose["include"][0]["system"] }}',
        'restricted_to': {{ prop.enum.restricted_to | rejectattr("code", "undefined") | map(attribute='code') | list }},
        'binding_strength': '{{ prop.binding.strength }}',
        'class_name': '{{ prop.class_name }}'
    }
{%- endfor %}

    @classmethod
    def attribute_enums(cls):
        """Get dict of attributes with enums, Code or CodeableConcept."""
        return cls._attribute_enums

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
    {%- for prop in klass.properties %}
        {% set docstring = prop.formal if prop.enum else prop.short %}
        self.{{ prop.name }} = None
        """ {{ docstring | trim(chars=".") | wordwrap(67, wrapstring="\n        ") }}.
        {% if prop.is_array %}List of{% else %}Type{% endif %} `{{ prop.class_name }}`{% if prop.is_array %} items{% endif %}
        {%- if prop.reference_to_names|length > 0 %} referencing `{{ prop.reference_to_names|join(', ') }}`{% endif %}
        {%- if prop.json_class != prop.class_name %} (represented as `{{ prop.json_class }}` in JSON){% endif %}. """
    {%- endfor %}
        
        super({{ klass.name }}, self).__init__(jsondict=jsondict, strict=strict)
    
{%- if klass.properties %}
    
    def elementProperties(self):
        js = super({{ klass.name }}, self).elementProperties()
        {%- if 'element' == klass.module and 'Element' == klass.name %}
        {%- for imp in imports %}{% if imp.module not in imported %}
        from . import {{ imp.module }}
        {%- set _ = imported.update({imp.module: True}) %}
        {%- endif %}{% endfor %}
        {%- endif %}
        js.extend([
        {%- for prop in klass.properties %}
            ("{{ prop.name }}", "{{ prop.orig_name }}",
            {%- if prop.module_name %} {{ prop.module_name }}.{% else %} {% endif %}{{ prop.class_name }}, {# #}
            {{- prop.is_array }},
            {%- if prop.one_of_many %} "{{ prop.one_of_many }}"{% else %} None{% endif %}, {# #}
            {{- prop.nonoptional }}),
        {%- endfor %}
        ])
        return js
    
{%- endif %}
{%- endfor %}

{% if imports|length > 0 and imported|length != imports|length %}
import sys
{%- endif %}
{%- for imp in imports %}{% if imp.module not in imported %}
try:
    from . import {{ imp.module }}
except ImportError:
    {{ imp.module }} = sys.modules[__package__ + '.{{ imp.module }}']
{%- endif %}{% endfor %}

