#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2022-06-20.
#  2022, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    
    resource_type = "ImmunizationRecommendation"

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['identifier'] = """Business identifier."""
    _attribute_docstrings['patient'] = """Who this profile is for."""
    _attribute_docstrings['date'] = """Date recommendation(s) created."""
    _attribute_docstrings['authority'] = """Who is responsible for protocol."""
    _attribute_docstrings['recommendation'] = """Vaccine administration recommendations."""

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
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date recommendation(s) created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['vaccineCode'] = """Vaccine  or vaccine group recommendation applies to."""
    _attribute_docstrings['targetDisease'] = """Disease to be immunized against."""
    _attribute_docstrings['contraindicatedVaccineCode'] = """Vaccine which is contraindicated to fulfill the recommendation."""
    _attribute_docstrings['forecastStatus'] = """Indicates the patient status with respect to the path to immunity for the target disease."""
    _attribute_docstrings['forecastReason'] = """Vaccine administration status reason."""
    _attribute_docstrings['dateCriterion'] = """Dates governing proposed immunization."""
    _attribute_docstrings['description'] = """Protocol details."""
    _attribute_docstrings['series'] = """Name of vaccination series."""
    _attribute_docstrings['doseNumberPositiveInt'] = """Recommended dose number within series."""
    _attribute_docstrings['doseNumberString'] = """Recommended dose number within series."""
    _attribute_docstrings['seriesDosesPositiveInt'] = """Recommended number of doses for immunity."""
    _attribute_docstrings['seriesDosesString'] = """Recommended number of doses for immunity."""
    _attribute_docstrings['supportingImmunization'] = """Past immunizations supporting recommendation."""
    _attribute_docstrings['supportingPatientInformation'] = """Patient observations supporting recommendation."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings

    _attribute_enums = {}
    """ Dictionary of enum configuration."""
    _attribute_enums['forecastStatus'] = {
        'url': 'http://terminology.hl7.org/CodeSystem/immunization-recommendation-status',
        'restricted_to': ['due', 'overdue', 'immune', 'contraindicated', 'complete'],
        'binding_strength': 'example',
        'class_name': 'CodeableConcept'
    }

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
        
        self.vaccineCode = None
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.targetDisease = None
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contraindicatedVaccineCode = None
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.forecastStatus = None
        """ Indicates the patient status with respect to the path to immunity
        for the target disease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.forecastReason = None
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateCriterion = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Protocol details.
        Type `str`. """
        
        self.series = None
        """ Name of vaccination series.
        Type `str`. """
        
        self.doseNumberPositiveInt = None
        """ Recommended dose number within series.
        Type `int`. """
        
        self.doseNumberString = None
        """ Recommended dose number within series.
        Type `str`. """
        
        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self.supportingImmunization = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False),
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("series", "series", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['code'] = """Type of date."""
    _attribute_docstrings['value'] = """Recommended date."""

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
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", fhirdate.FHIRDate, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
