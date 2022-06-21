#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2022-06-21.
#  2022, SMART Health IT.

import io
import json
import logging
import os
import typing
import unittest

from . import valueset

from .fhirdate import FHIRDate
import logging


class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ValueSet", js["resourceType"])
        return valueset.ValueSet(js)
    
    def testValueSet1(self):
        inst = self.instantiate_from("valueset-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet1(self, inst):
        self.assertTrue(inst.compose.inactive)
        self.assertEqual(inst.compose.include[0].concept[0].code, "14647-2")
        self.assertEqual(inst.compose.include[0].concept[0].display, "Cholesterol [Moles/Volume]")
        self.assertEqual(inst.compose.include[0].concept[1].code, "2093-3")
        self.assertEqual(inst.compose.include[0].concept[1].display, "Cholesterol [Mass/Volume]")
        self.assertEqual(inst.compose.include[0].concept[2].code, "35200-5")
        self.assertEqual(inst.compose.include[0].concept[2].display, "Cholesterol [Mass Or Moles/Volume]")
        self.assertEqual(inst.compose.include[0].concept[3].code, "9342-7")
        self.assertEqual(inst.compose.include[0].concept[3].display, "Cholesterol [Percentile]")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.compose.include[0].version, "2.36")
        self.assertEqual(inst.compose.lockedDate.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.compose.lockedDate.as_json(), "2012-06-13")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "This content from LOINC ® is copyright © 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use.")
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(inst.description, "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-extensional")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/identifiers/valuesets")
        self.assertEqual(inst.identifier[0].value, "loinc-cholesterol-int")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.purpose, "This value set was published by ACME Inc in order to make clear which codes are used for Cholesterol by AcmeClinicals (Adult Ambulatory care support in USA)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-extensional")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueQuantity.code, "a")
        self.assertEqual(inst.useContext[0].valueQuantity.comparator, ">")
        self.assertEqual(inst.useContext[0].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.useContext[0].valueQuantity.unit, "yrs")
        self.assertEqual(inst.useContext[0].valueQuantity.value, 18)
        self.assertEqual(inst.version, "20150622")
    
    def testValueSet2(self):
        inst = self.instantiate_from("valueset-example-hierarchical.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet2(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet2(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet2(self, inst):
        self.assertEqual(inst.compose.include[0].concept[0].code, "invalid")
        self.assertEqual(inst.compose.include[0].concept[1].code, "structure")
        self.assertEqual(inst.compose.include[0].concept[2].code, "required")
        self.assertEqual(inst.compose.include[0].concept[3].code, "value")
        self.assertEqual(inst.compose.include[0].concept[4].code, "processing")
        self.assertEqual(inst.compose.include[0].concept[5].code, "duplicate")
        self.assertEqual(inst.compose.include[0].concept[6].code, "not-found")
        self.assertEqual(inst.compose.include[0].concept[7].code, "conflict")
        self.assertEqual(inst.compose.include[0].concept[8].code, "lock")
        self.assertEqual(inst.compose.include[0].concept[9].code, "exception")
        self.assertEqual(inst.compose.include[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-rules")
        self.assertEqual(inst.compose.include[0].extension[0].valueCode, "groups-only")
        self.assertEqual(inst.compose.include[0].extension[1].extension[0].url, "display")
        self.assertEqual(inst.compose.include[0].extension[1].extension[0].valueString, "(Most common)")
        self.assertEqual(inst.compose.include[0].extension[1].extension[1].url, "member")
        self.assertEqual(inst.compose.include[0].extension[1].extension[1].valueCode, "login")
        self.assertEqual(inst.compose.include[0].extension[1].extension[2].url, "member")
        self.assertEqual(inst.compose.include[0].extension[1].extension[2].valueCode, "conflict")
        self.assertEqual(inst.compose.include[0].extension[1].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-group")
        self.assertEqual(inst.compose.include[0].extension[2].extension[0].url, "code")
        self.assertEqual(inst.compose.include[0].extension[2].extension[0].valueCode, "processing")
        self.assertEqual(inst.compose.include[0].extension[2].extension[1].url, "member")
        self.assertEqual(inst.compose.include[0].extension[2].extension[1].valueCode, "duplicate")
        self.assertEqual(inst.compose.include[0].extension[2].extension[2].url, "member")
        self.assertEqual(inst.compose.include[0].extension[2].extension[2].valueCode, "not-found")
        self.assertEqual(inst.compose.include[0].extension[2].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-group")
        self.assertEqual(inst.compose.include[0].extension[3].extension[0].url, "code")
        self.assertEqual(inst.compose.include[0].extension[3].extension[0].valueCode, "invalid")
        self.assertEqual(inst.compose.include[0].extension[3].extension[1].url, "member")
        self.assertEqual(inst.compose.include[0].extension[3].extension[1].valueCode, "structure")
        self.assertEqual(inst.compose.include[0].extension[3].extension[2].url, "member")
        self.assertEqual(inst.compose.include[0].extension[3].extension[2].valueCode, "required")
        self.assertEqual(inst.compose.include[0].extension[3].extension[3].url, "member")
        self.assertEqual(inst.compose.include[0].extension[3].extension[3].valueCode, "value")
        self.assertEqual(inst.compose.include[0].extension[3].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-group")
        self.assertEqual(inst.compose.include[0].extension[4].extension[0].url, "code")
        self.assertEqual(inst.compose.include[0].extension[4].extension[0].valueCode, "transient")
        self.assertEqual(inst.compose.include[0].extension[4].extension[1].url, "member")
        self.assertEqual(inst.compose.include[0].extension[4].extension[1].valueCode, "lock")
        self.assertEqual(inst.compose.include[0].extension[4].extension[2].url, "member")
        self.assertEqual(inst.compose.include[0].extension[4].extension[2].valueCode, "exception")
        self.assertEqual(inst.compose.include[0].extension[4].extension[3].url, "member")
        self.assertEqual(inst.compose.include[0].extension[4].extension[3].valueCode, "throttled")
        self.assertEqual(inst.compose.include[0].extension[4].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-group")
        self.assertEqual(inst.compose.include[0].extension[5].extension[0].url, "code")
        self.assertEqual(inst.compose.include[0].extension[5].extension[0].valueCode, "security")
        self.assertEqual(inst.compose.include[0].extension[5].extension[1].url, "member")
        self.assertEqual(inst.compose.include[0].extension[5].extension[1].valueCode, "login")
        self.assertEqual(inst.compose.include[0].extension[5].extension[2].url, "member")
        self.assertEqual(inst.compose.include[0].extension[5].extension[2].valueCode, "unknown")
        self.assertEqual(inst.compose.include[0].extension[5].url, "http://hl7.org/fhir/StructureDefinition/valueset-expand-group")
        self.assertEqual(inst.compose.include[0].system, "#hacked")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.contained[0].id, "hacked")
        self.assertEqual(inst.date.date, FHIRDate("2018-07-20").date)
        self.assertEqual(inst.date.as_json(), "2018-07-20")
        self.assertEqual(inst.description, "Demonstration of extensions that build a hierarchical contains")
        self.assertTrue(inst.expansion.contains[0].abstract)
        self.assertEqual(inst.expansion.contains[0].contains[0].code, "login")
        self.assertEqual(inst.expansion.contains[0].contains[0].display, "Login Required")
        self.assertEqual(inst.expansion.contains[0].contains[0].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[0].contains[1].code, "conflict")
        self.assertEqual(inst.expansion.contains[0].contains[1].display, "Edit Version Conflict")
        self.assertEqual(inst.expansion.contains[0].contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[0].display, "(Most common)")
        self.assertEqual(inst.expansion.contains[1].code, "processing")
        self.assertEqual(inst.expansion.contains[1].contains[0].code, "duplicate")
        self.assertEqual(inst.expansion.contains[1].contains[0].display, "Duplicate")
        self.assertEqual(inst.expansion.contains[1].contains[0].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[1].contains[1].code, "not-found")
        self.assertEqual(inst.expansion.contains[1].contains[1].display, "Not Found")
        self.assertEqual(inst.expansion.contains[1].contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[1].display, "Processing Failure")
        self.assertEqual(inst.expansion.contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertTrue(inst.expansion.contains[2].abstract)
        self.assertEqual(inst.expansion.contains[2].code, "invalid")
        self.assertEqual(inst.expansion.contains[2].contains[0].code, "structure")
        self.assertEqual(inst.expansion.contains[2].contains[0].display, "Structural Issue")
        self.assertEqual(inst.expansion.contains[2].contains[0].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[2].contains[1].code, "required")
        self.assertEqual(inst.expansion.contains[2].contains[1].display, "Required element missing")
        self.assertEqual(inst.expansion.contains[2].contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[2].contains[2].code, "value")
        self.assertEqual(inst.expansion.contains[2].contains[2].display, "Element value invalid")
        self.assertEqual(inst.expansion.contains[2].contains[2].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[2].display, "Invalid Content")
        self.assertEqual(inst.expansion.contains[2].system, "http://hl7.org/fhir/hacked")
        self.assertTrue(inst.expansion.contains[3].abstract)
        self.assertEqual(inst.expansion.contains[3].code, "transient")
        self.assertEqual(inst.expansion.contains[3].contains[0].code, "lock-error")
        self.assertEqual(inst.expansion.contains[3].contains[0].display, "Lock Error")
        self.assertEqual(inst.expansion.contains[3].contains[0].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[3].contains[1].code, "exception")
        self.assertEqual(inst.expansion.contains[3].contains[1].display, "Exception")
        self.assertEqual(inst.expansion.contains[3].contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[3].contains[2].code, "throttled")
        self.assertEqual(inst.expansion.contains[3].contains[2].display, "Throttled")
        self.assertEqual(inst.expansion.contains[3].contains[2].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[3].display, "Transient Issue")
        self.assertEqual(inst.expansion.contains[3].system, "http://hl7.org/fhir/hacked")
        self.assertTrue(inst.expansion.contains[4].abstract)
        self.assertEqual(inst.expansion.contains[4].code, "security")
        self.assertEqual(inst.expansion.contains[4].contains[0].code, "login")
        self.assertEqual(inst.expansion.contains[4].contains[0].display, "Login Required")
        self.assertEqual(inst.expansion.contains[4].contains[0].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[4].contains[1].code, "unknown")
        self.assertEqual(inst.expansion.contains[4].contains[1].display, "Unknown User")
        self.assertEqual(inst.expansion.contains[4].contains[1].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.contains[4].display, "Security Problem")
        self.assertEqual(inst.expansion.contains[4].system, "http://hl7.org/fhir/hacked")
        self.assertEqual(inst.expansion.identifier, "urn:uuid:42316ff8-2714-4680-9980-f37a6d1a71bc")
        self.assertEqual(inst.expansion.parameter[0].name, "excludeNotForUI")
        self.assertEqual(inst.expansion.parameter[0].valueUri, "false")
        self.assertEqual(inst.expansion.timestamp.date, FHIRDate("2018-07-20T23:14:07+10:00").date)
        self.assertEqual(inst.expansion.timestamp.as_json(), "2018-07-20T23:14:07+10:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-hierarchical")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "Example Hierarchical ValueSet")
        self.assertEqual(inst.publisher, "FHIR Project team")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-hierarchical")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet3(self):
        inst = self.instantiate_from("valueset-example-expansion.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet3(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet3(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet3(self, inst):
        self.assertEqual(inst.compose.include[0].filter[0].op, "=")
        self.assertEqual(inst.compose.include[0].filter[0].property, "parent")
        self.assertEqual(inst.compose.include[0].filter[0].value, "LP43571-6")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "This content from LOINC® is copyright © 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use.")
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(inst.description, "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.")
        self.assertEqual(inst.expansion.contains[0].code, "14647-2")
        self.assertEqual(inst.expansion.contains[0].display, "Cholesterol [Moles/volume] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[0].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[0].version, "2.50")
        self.assertTrue(inst.expansion.contains[1].abstract)
        self.assertEqual(inst.expansion.contains[1].contains[0].code, "2093-3")
        self.assertEqual(inst.expansion.contains[1].contains[0].display, "Cholesterol [Mass/volume] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[1].contains[0].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[1].contains[0].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].contains[1].code, "48620-9")
        self.assertEqual(inst.expansion.contains[1].contains[1].display, "Cholesterol [Mass/volume] in Serum or Plasma ultracentrifugate")
        self.assertEqual(inst.expansion.contains[1].contains[1].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[1].contains[1].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].contains[2].code, "9342-7")
        self.assertEqual(inst.expansion.contains[1].contains[2].display, "Cholesterol [Percentile]")
        self.assertEqual(inst.expansion.contains[1].contains[2].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[1].contains[2].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].display, "Cholesterol codes")
        self.assertTrue(inst.expansion.contains[2].abstract)
        self.assertEqual(inst.expansion.contains[2].contains[0].code, "2096-6")
        self.assertEqual(inst.expansion.contains[2].contains[0].display, "Cholesterol/Triglyceride [Mass Ratio] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[2].contains[0].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[2].contains[0].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[1].code, "35200-5")
        self.assertEqual(inst.expansion.contains[2].contains[1].display, "Cholesterol/Triglyceride [Mass Ratio] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[2].contains[1].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[2].contains[1].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[2].code, "48089-7")
        self.assertEqual(inst.expansion.contains[2].contains[2].display, "Cholesterol/Apolipoprotein B [Molar ratio] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[2].contains[2].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[2].contains[2].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[3].code, "55838-7")
        self.assertEqual(inst.expansion.contains[2].contains[3].display, "Cholesterol/Phospholipid [Molar ratio] in Serum or Plasma")
        self.assertEqual(inst.expansion.contains[2].contains[3].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[2].contains[3].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].display, "Cholesterol Ratios")
        self.assertEqual(inst.expansion.extension[0].url, "http://hl7.org/fhir/StructureDefinition/valueset-expansionSource")
        self.assertEqual(inst.expansion.extension[0].valueUri, "http://hl7.org/fhir/ValueSet/example-extensional")
        self.assertEqual(inst.expansion.identifier, "urn:uuid:42316ff8-2714-4680-9980-f37a6d1a71bc")
        self.assertEqual(inst.expansion.offset, 0)
        self.assertEqual(inst.expansion.parameter[0].name, "version")
        self.assertEqual(inst.expansion.parameter[0].valueString, "2.50")
        self.assertEqual(inst.expansion.timestamp.date, FHIRDate("2015-06-22T13:56:07Z").date)
        self.assertEqual(inst.expansion.timestamp.as_json(), "2015-06-22T13:56:07Z")
        self.assertEqual(inst.expansion.total, 8)
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-expansion")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "FHIR Project team")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-expansion")
        self.assertEqual(inst.version, "20150622")
    
    def testValueSet4(self):
        inst = self.instantiate_from("valueset-example-inactive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet4(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet4(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet4(self, inst):
        self.assertTrue(inst.compose.inactive)
        self.assertEqual(inst.compose.include[0].filter[0].op, "descendent-of")
        self.assertEqual(inst.compose.include[0].filter[0].property, "concept")
        self.assertEqual(inst.compose.include[0].filter[0].value, "_ActMoodPredicate")
        self.assertEqual(inst.compose.include[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.description, "HL7 v3 ActMood Predicate codes, including inactive codes")
        self.assertEqual(inst.expansion.contains[0].code, "CRT")
        self.assertEqual(inst.expansion.contains[0].display, "criterion")
        self.assertTrue(inst.expansion.contains[0].inactive)
        self.assertEqual(inst.expansion.contains[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.expansion.contains[1].code, "EXPEC")
        self.assertEqual(inst.expansion.contains[1].contains[0].code, "GOL")
        self.assertEqual(inst.expansion.contains[1].contains[0].display, "goal")
        self.assertEqual(inst.expansion.contains[1].contains[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.expansion.contains[1].contains[1].code, "RSK")
        self.assertEqual(inst.expansion.contains[1].contains[1].display, "risk")
        self.assertEqual(inst.expansion.contains[1].contains[1].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.expansion.contains[1].display, "expectation")
        self.assertEqual(inst.expansion.contains[1].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.expansion.contains[2].code, "OPT")
        self.assertEqual(inst.expansion.contains[2].display, "option")
        self.assertEqual(inst.expansion.contains[2].system, "http://terminology.hl7.org/CodeSystem/v3-ActMood")
        self.assertEqual(inst.expansion.identifier, "urn:uuid:46c00b3f-003a-4f31-9d4b-ea2de58b2a99")
        self.assertEqual(inst.expansion.timestamp.date, FHIRDate("2017-02-26T10:00:00Z").date)
        self.assertEqual(inst.expansion.timestamp.as_json(), "2017-02-26T10:00:00Z")
        self.assertEqual(inst.id, "inactive")
        self.assertEqual(inst.name, "Example-inactive")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Example with inactive codes")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/inactive")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet5(self):
        inst = self.instantiate_from("valueset-example-filter.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet5(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet5(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet5(self, inst):
        self.assertEqual(inst.compose.include[0].filter[0].op, "=")
        self.assertEqual(inst.compose.include[0].filter[0].property, "acme-plasma")
        self.assertEqual(inst.compose.include[0].filter[0].value, "true")
        self.assertEqual(inst.compose.include[0].system, "http://hl7.org/fhir/CodeSystem/example")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2018-11-01").date)
        self.assertEqual(inst.date.as_json(), "2018-11-01")
        self.assertEqual(inst.description, "ACME Codes for Cholesterol: Plasma only - demonstrating the use of a filter defined in a CodeSystem")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-filter")
        self.assertEqual(inst.name, "ACMECholCodesPlasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "ACME Codes for Cholesterol: Plasma only")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-filter")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet6(self):
        inst = self.instantiate_from("valueset-example-yesnodontknow.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet6(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet6(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet6(self, inst):
        self.assertEqual(inst.compose.include[0].valueSet[0], "http://terminology.hl7.org/ValueSet/v2-0136")
        self.assertEqual(inst.compose.include[1].concept[0].code, "asked-unknown")
        self.assertEqual(inst.compose.include[1].concept[0].display, "Don't know")
        self.assertEqual(inst.compose.include[1].system, "http://terminology.hl7.org/CodeSystem/data-absent-reason")
        self.assertEqual(inst.description, "For Capturing simple yes-no-don't know answers")
        self.assertEqual(inst.expansion.contains[0].code, "Y")
        self.assertEqual(inst.expansion.contains[0].display, "Yes")
        self.assertEqual(inst.expansion.contains[0].system, "http://terminology.hl7.org/CodeSystem/v2-0136")
        self.assertEqual(inst.expansion.contains[1].code, "N")
        self.assertEqual(inst.expansion.contains[1].display, "No")
        self.assertEqual(inst.expansion.contains[1].system, "http://terminology.hl7.org/CodeSystem/v2-0136")
        self.assertEqual(inst.expansion.contains[2].code, "asked-unknown")
        self.assertEqual(inst.expansion.contains[2].display, "Don't know")
        self.assertEqual(inst.expansion.contains[2].system, "http://terminology.hl7.org/CodeSystem/data-absent-reason")
        self.assertEqual(inst.expansion.identifier, "urn:uuid:bf99fe50-2c2b-41ad-bd63-bee6919810b4")
        self.assertEqual(inst.expansion.timestamp.date, FHIRDate("2015-07-14T10:00:00Z").date)
        self.assertEqual(inst.expansion.timestamp.as_json(), "2015-07-14T10:00:00Z")
        self.assertEqual(inst.id, "yesnodontknow")
        self.assertEqual(inst.name, "Yes/No/Don't Know")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet7(self):
        inst = self.instantiate_from("valueset-examplescenario-actor-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet7(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet7(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet7(self, inst):
        self.assertEqual(inst.compose.include[0].system, "http://hl7.org/fhir/examplescenario-actor-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].value, "fhir@lists.hl7.org")
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(inst.description, "The type of actor - system or human.")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[0].valueCode, "fhir")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status")
        self.assertEqual(inst.extension[1].valueCode, "trial-use")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[2].valueInteger, 0)
        self.assertEqual(inst.id, "examplescenario-actor-type")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:2.16.840.1.113883.4.642.3.858")
        self.assertTrue(inst.immutable)
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "ExampleScenarioActorType")
        self.assertEqual(inst.publisher, "HL7 (FHIR Project)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "ExampleScenarioActorType")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/examplescenario-actor-type")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet8(self):
        inst = self.instantiate_from("valueset-list-example-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet8(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet8(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet8(self, inst):
        self.assertEqual(inst.compose.include[0].system, "http://terminology.hl7.org/CodeSystem/list-example-use-codes")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(inst.description, "Example use codes for the List resource - typical kinds of use.")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[0].valueCode, "fhir")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status")
        self.assertEqual(inst.extension[1].valueCode, "draft")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(inst.id, "list-example-codes")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:2.16.840.1.113883.4.642.3.316")
        self.assertTrue(inst.immutable)
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "ExampleUseCodesForList")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Example Use Codes for List")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/list-example-codes")
        self.assertEqual(inst.version, "4.0.1")
    
    def testValueSet9(self):
        inst = self.instantiate_from("valueset-example-intensional.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet9(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet9(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implValueSet9(self, inst):
        self.assertEqual(inst.compose.exclude[0].concept[0].code, "5932-9")
        self.assertEqual(inst.compose.exclude[0].concept[0].display, "Cholesterol [Presence] in Blood by Test strip")
        self.assertEqual(inst.compose.exclude[0].system, "http://loinc.org")
        self.assertEqual(inst.compose.include[0].filter[0].op, "=")
        self.assertEqual(inst.compose.include[0].filter[0].property, "parent")
        self.assertEqual(inst.compose.include[0].filter[0].value, "LP43571-6")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "This content from LOINCÂ® is copyright Â© 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use")
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(inst.description, "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-intensional")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/identifiers/valuesets")
        self.assertEqual(inst.identifier[0].value, "loinc-cholesterol-ext")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-intensional")
        self.assertEqual(inst.version, "20150622")

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
                for simplified_extension in simplified_extensions:
                    assert simplified_js[simplified_extension], f"Missing value for {simplified_extension}"
                    assert 'fhirclient.models.coding.Coding' not in str(simplified_js[simplified_extension]), "Should simplify codes"
                    if simplified_js[simplified_extension] == 'NA':
                        logging.getLogger(__name__).warning(
                            "Extension.value is NA for resource_type:{} simplified_extension:{}".format(
                                inst.resource_type, simplified_extension))
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