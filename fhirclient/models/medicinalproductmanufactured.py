#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured) on 2022-06-22.
#  2022, SMART Health IT.


from . import domainresource

class MedicinalProductManufactured(domainresource.DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    
    resource_type = "MedicinalProductManufactured"

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['manufacturedDoseForm'] = """Dose form as manufactured and before any transformation into the pharmaceutical product."""
    _attribute_docstrings['unitOfPresentation'] = """The “real world” units in which the quantity of the manufactured item is described."""
    _attribute_docstrings['quantity'] = """The quantity or "count number" of the manufactured item."""
    _attribute_docstrings['manufacturer'] = """Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues)."""
    _attribute_docstrings['ingredient'] = """Ingredient."""
    _attribute_docstrings['physicalCharacteristics'] = """Dimensions, color etc.."""
    _attribute_docstrings['otherCharacteristics'] = """Other codeable characteristics."""

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
        
        self.manufacturedDoseForm = None
        """ Dose form as manufactured and before any transformation into the
        pharmaceutical product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitOfPresentation = None
        """ The “real world” units in which the quantity of the manufactured
        item is described.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity or "count number" of the manufactured item.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of the item (Note that this should be named
        "manufacturer" but it currently causes technical issues).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc.
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(MedicinalProductManufactured, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend([
            ("manufacturedDoseForm", "manufacturedDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + '.prodcharacteristic']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
