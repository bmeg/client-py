#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2022-06-20.
#  2022, SMART Health IT.


from . import element

class UsageContext(element.Element):
    """ Describes the context of use for a conformance or knowledge resource.
    
    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['code'] = """Type of context being specified."""
    _attribute_docstrings['valueCodeableConcept'] = """Value that defines the context."""
    _attribute_docstrings['valueQuantity'] = """Value that defines the context."""
    _attribute_docstrings['valueRange'] = """Value that defines the context."""
    _attribute_docstrings['valueReference'] = """Value that defines the context."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings

    _attribute_enums = {}
    """ Dictionary of enum configuration."""

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
        
        self.code = None
        """ Type of context being specified.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value that defines the context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value that defines the context.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value that defines the context.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value that defines the context.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
