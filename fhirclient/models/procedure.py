#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2022-10-13.
#  2022, SMART Health IT.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    
    resource_type = "Procedure"

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['identifier'] = """External Identifiers for this procedure."""
    _attribute_docstrings['instantiatesCanonical'] = """Instantiates FHIR protocol or definition."""
    _attribute_docstrings['instantiatesUri'] = """Instantiates external protocol or definition."""
    _attribute_docstrings['basedOn'] = """A request for this procedure."""
    _attribute_docstrings['partOf'] = """Part of referenced event."""
    _attribute_docstrings['status'] = """A code specifying the state of the procedure. Generally, this will be the in-progress or completed state."""
    _attribute_docstrings['statusReason'] = """Reason for current status."""
    _attribute_docstrings['category'] = """Classification of the procedure."""
    _attribute_docstrings['code'] = """Identification of the procedure."""
    _attribute_docstrings['subject'] = """Who the procedure was performed on."""
    _attribute_docstrings['encounter'] = """Encounter created as part of."""
    _attribute_docstrings['performedDateTime'] = """When the procedure was performed."""
    _attribute_docstrings['performedPeriod'] = """When the procedure was performed."""
    _attribute_docstrings['performedString'] = """When the procedure was performed."""
    _attribute_docstrings['performedAge'] = """When the procedure was performed."""
    _attribute_docstrings['performedRange'] = """When the procedure was performed."""
    _attribute_docstrings['recorder'] = """Who recorded the procedure."""
    _attribute_docstrings['asserter'] = """Person who asserts this procedure."""
    _attribute_docstrings['performer'] = """The people who performed the procedure."""
    _attribute_docstrings['location'] = """Where the procedure happened."""
    _attribute_docstrings['reasonCode'] = """Coded reason procedure performed."""
    _attribute_docstrings['reasonReference'] = """The justification that the procedure was performed."""
    _attribute_docstrings['bodySite'] = """Target body sites."""
    _attribute_docstrings['outcome'] = """The result of procedure."""
    _attribute_docstrings['report'] = """Any report resulting from the procedure."""
    _attribute_docstrings['complication'] = """Complication following the procedure."""
    _attribute_docstrings['complicationDetail'] = """A condition that is a result of the procedure."""
    _attribute_docstrings['followUp'] = """Instructions for follow up."""
    _attribute_docstrings['note'] = """Additional information about the procedure."""
    _attribute_docstrings['focalDevice'] = """Manipulated, implanted, or removed device."""
    _attribute_docstrings['usedReference'] = """Items used during procedure."""
    _attribute_docstrings['usedCode'] = """Coded items used during the procedure."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings | domainresource.DomainResource.attribute_docstrings()

    _attribute_types = {}
    """ Dictionary of attribute types."""
    _attribute_types['identifier'] = 'List[Identifier]'
    _attribute_types['instantiatesCanonical'] = 'List[str]'
    _attribute_types['instantiatesUri'] = 'List[str]'
    _attribute_types['basedOn'] = 'List[FHIRReference]'
    _attribute_types['partOf'] = 'List[FHIRReference]'
    _attribute_types['status'] = 'str'
    _attribute_types['statusReason'] = 'CodeableConcept'
    _attribute_types['category'] = 'CodeableConcept'
    _attribute_types['code'] = 'CodeableConcept'
    _attribute_types['subject'] = 'FHIRReference'
    _attribute_types['encounter'] = 'FHIRReference'
    _attribute_types['performedDateTime'] = 'FHIRDate'
    _attribute_types['performedPeriod'] = 'Period'
    _attribute_types['performedString'] = 'str'
    _attribute_types['performedAge'] = 'Age'
    _attribute_types['performedRange'] = 'Range'
    _attribute_types['recorder'] = 'FHIRReference'
    _attribute_types['asserter'] = 'FHIRReference'
    _attribute_types['performer'] = 'List[ProcedurePerformer]'
    _attribute_types['location'] = 'FHIRReference'
    _attribute_types['reasonCode'] = 'List[CodeableConcept]'
    _attribute_types['reasonReference'] = 'List[FHIRReference]'
    _attribute_types['bodySite'] = 'List[CodeableConcept]'
    _attribute_types['outcome'] = 'CodeableConcept'
    _attribute_types['report'] = 'List[FHIRReference]'
    _attribute_types['complication'] = 'List[CodeableConcept]'
    _attribute_types['complicationDetail'] = 'List[FHIRReference]'
    _attribute_types['followUp'] = 'List[CodeableConcept]'
    _attribute_types['note'] = 'List[Annotation]'
    _attribute_types['focalDevice'] = 'List[ProcedureFocalDevice]'
    _attribute_types['usedReference'] = 'List[FHIRReference]'
    _attribute_types['usedCode'] = 'List[CodeableConcept]'

    @classmethod
    def attribute_types(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_types


    _attribute_enums = {}
    """ Dictionary of enum configuration."""
    _attribute_enums['status'] = {
        'url': 'http://hl7.org/fhir/event-status',
        'restricted_to': ['preparation', 'in-progress', 'not-done', 'on-hold', 'stopped', 'completed', 'entered-in-error', 'unknown'],
        'binding_strength': 'required',
        'class_name': 'str'
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
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ A code specifying the state of the procedure. Generally, this will
        be the in-progress or completed state.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ When the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performedString = None
        """ When the procedure was performed.
        Type `str`. """
        
        self.performedAge = None
        """ When the procedure was performed.
        Type `Age` (represented as `dict` in JSON). """
        
        self.performedRange = None
        """ When the procedure was performed.
        Type `Range` (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Who recorded the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.asserter = None
        """ Person who asserts this procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False, "performed", False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performedAge", "performedAge", age.Age, False, "performed", False),
            ("performedRange", "performedRange", range.Range, False, "performed", False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['action'] = """Kind of change to device."""
    _attribute_docstrings['manipulated'] = """Device that was changed."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings | backboneelement.BackboneElement.attribute_docstrings()

    _attribute_types = {}
    """ Dictionary of attribute types."""
    _attribute_types['action'] = 'CodeableConcept'
    _attribute_types['manipulated'] = 'FHIRReference'

    @classmethod
    def attribute_types(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_types


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
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to "real" people rather than equipment.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['function'] = """Type of performance."""
    _attribute_docstrings['actor'] = """The reference to the practitioner."""
    _attribute_docstrings['onBehalfOf'] = """Organization the device or practitioner was acting for."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings | backboneelement.BackboneElement.attribute_docstrings()

    _attribute_types = {}
    """ Dictionary of attribute types."""
    _attribute_types['function'] = 'CodeableConcept'
    _attribute_types['actor'] = 'FHIRReference'
    _attribute_types['onBehalfOf'] = 'FHIRReference'

    @classmethod
    def attribute_types(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_types


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
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ The reference to the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
