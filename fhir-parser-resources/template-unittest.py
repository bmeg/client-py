#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

import io
import json
import logging
import os
import typing
import unittest

from . import {{ class.module }}

from .fhirdate import FHIRDate
import logging


class {{ class.name }}Tests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("{{ class.name }}", js["resourceType"])
        return {{ class.module }}.{{ class.name }}(js)
    
{%- for tcase in tests %}
    
    def test{{ class.name }}{{ loop.index }}(self):
        inst = self.instantiate_from("{{ tcase.filename }}")
        self.assertIsNotNone(inst, "Must have instantiated a {{ class.name }} instance")
        self.impl{{ class.name }}{{ loop.index }}(inst)
        
        js = inst.as_json()
        self.assertEqual("{{ class.name }}", js["resourceType"])
        inst2 = {{ class.module }}.{{ class.name }}(js)
        self.impl{{ class.name }}{{ loop.index }}(inst2)
        self.evaluate_simplified_json(inst2)
    
    def impl{{ class.name }}{{ loop.index }}(self, inst):
    {%- for onetest in tcase.tests %}
    {%- if "str" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, "{{ onetest.value|replace('\\n', '\\\\n')|replace('"', '\\"') }}")
    {%- else %}{% if "int" == onetest.klass.name or "float" == onetest.klass.name or "NSDecimalNumber" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, {{ onetest.value }})
    {%- else %}{% if "bool" == onetest.klass.name %}
        {%- if onetest.value %}
        self.assertTrue(inst.{{ onetest.path }})
        {%- else %}
        self.assertFalse(inst.{{ onetest.path }})
        {%- endif %}
    {%- else %}{% if "FHIRDate" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}.date, FHIRDate("{{ onetest.value }}").date)
        self.assertEqual(inst.{{ onetest.path }}.as_json(), "{{ onetest.value }}")
    {%- else %}
        # Don't know how to create unit test for "{{ onetest.path }}", which is a {{ onetest.klass.name }}
    {%- endif %}{% endif %}{% endif %}{% endif %}
    {%- endfor %}
{%- endfor %}

    def evaluate_simplified_json(self, inst):
        """Ensure simplified json."""
        simplified_js, simplified_schema = inst.as_simplified_json()
        self.assertIsNotNone(simplified_js, "Must create simplified json")

        # test simplify identifiers
        if hasattr(inst, 'identifier'):
            assert 'identifier' not in simplified_js
            if inst.identifier:
                simplified_identifiers = [k for k in simplified_js.keys() if k.startswith('identifier_')]
                if isinstance(inst.identifier, typing.List):
                    identifiers_with_values = [i for i in inst.identifier if i.value]
                else:
                    identifiers_with_values = [inst.identifier]
                self.assertEqual(len(identifiers_with_values), len(simplified_identifiers), "Should simplify identifiers.")

        # test simplify lists
        for name in vars(inst):

            if name == 'identifier':
                continue

            if name == 'extension':
                continue

            value = getattr(inst, name)
            is_coding = value.__class__.__name__ == 'Coding' or (isinstance(value, typing.List) and len(value) == 1 and value[0].__class__.__name__ == 'Coding')
            if is_coding:
                continue

            if isinstance(getattr(inst, name), typing.List) and len(getattr(inst, name)) == 1:
                # Properties that need to be renamed because of language keyword conflicts
                # see mapping
                if name not in simplified_js:
                    name = name.replace("_fhir", "")
                self.assertFalse(isinstance(simplified_js[name], typing.List), "Should simplify lists {}".format(name))

        # test simplify coding
        # meta has known coding attribute 'tags'
        if hasattr(inst, 'meta'):
            if inst.meta and inst.meta.tag and len(inst.meta.tag) > 0:
                simplified_tags = [k for k in simplified_js['meta'].keys() if k.startswith('tag_')]
                self.assertEqual(len(inst.meta.tag), len(simplified_tags), "Should simplify meta tags.")
                self.assertTrue('tag' not in simplified_js['meta'], "Should not have meta.tag")

        # test simplify extensions
        if hasattr(inst, 'extension'):
            if inst.extension and len(inst.extension) > 0:
                assert 'extension' not in simplified_js
                simplified_extensions = [k for k in simplified_js.keys() if k.startswith('extension_')]
                self.assertEqual(len(inst.extension), len(simplified_extensions), "Should simplify extensions.")

        # test simplify schema
        for k in simplified_js:
            assert k in simplified_schema, "Should have a schema definition for {}".format(k)

        # test simplified, flattened
        from flatten_json import flatten
        flattened = flatten(simplified_js, separator='|')
        for flattened_key in flattened:
            dict_ = simplified_schema
            for flattened_key_part in flattened_key.split('|'):
                if flattened_key_part not in dict_ and flattened_key_part.isnumeric():
                    # traverse over list index
                    continue
                dict_ = dict_[flattened_key_part]
                self.assertIsNotNone(dict_, "Should have a schema entry for {}".format(flattened_key_part))
                if 'docstring' not in dict_:
                    logging.getLogger(__name__).warning(
                        "Missing docstring for resource_type:{} flattened_key:{} flattened_key_part:{} dict:{}".format(
                            inst.resource_type, flattened_key, flattened_key_part, dict_))
                    break
