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

from . import careplan

from .fhirdate import FHIRDate
import logging


class CarePlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CarePlan", js["resourceType"])
        return careplan.CarePlan(js)
    
    def testCarePlan1(self):
        inst = self.instantiate_from("careplan-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan1(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan1(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan1(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "359615001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Partial lobectomy of lung")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "ServiceRequest")
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-07-07T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.contained[0].id, "careteam")
        self.assertEqual(inst.contained[1].id, "goal")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP2934")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-07-07").date)
        self.assertEqual(inst.period.end.as_json(), "2013-07-07")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-07-06").date)
        self.assertEqual(inst.period.start.as_json(), "2011-07-06")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan2(self):
        inst = self.instantiate_from("careplan-example-f202-malignancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan2(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan2(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan2(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "367336001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Chemotherapy")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "ServiceRequest")
        self.assertEqual(inst.activity[0].detail.status, "in-progress")
        self.assertEqual(inst.contained[0].id, "doce")
        self.assertEqual(inst.contained[1].id, "cisp")
        self.assertEqual(inst.contained[2].id, "fluo")
        self.assertEqual(inst.contained[3].id, "tpf")
        self.assertEqual(inst.contained[4].id, "careteam")
        self.assertEqual(inst.contained[5].id, "goal")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan3(self):
        inst = self.instantiate_from("careplan-example-obesity-narrative.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan3(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan3(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan3(self, inst):
        self.assertEqual(inst.id, "obesity-narrative")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")
    
    def testCarePlan4(self):
        inst = self.instantiate_from("careplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan4(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan4(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan4(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "3141-9")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Weight Measured")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.activity[0].detail.code.coding[1].code, "27113001")
        self.assertEqual(inst.activity[0].detail.code.coding[1].display, "Body weight")
        self.assertEqual(inst.activity[0].detail.code.coding[1].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.frequency, 1)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.period, 1)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.periodUnit, "d")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.activity[0].detail.statusReason.text, "Achieved weight loss to mitigate diabetes risk.")
        self.assertEqual(inst.activity[0].outcomeCodeableConcept[0].coding[0].code, "161832001")
        self.assertEqual(inst.activity[0].outcomeCodeableConcept[0].coding[0].display, "Progressive weight loss")
        self.assertEqual(inst.activity[0].outcomeCodeableConcept[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Weight management plan")
        self.assertEqual(inst.contained[0].id, "p1")
        self.assertEqual(inst.created.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.created.as_json(), "2016-01-01")
        self.assertEqual(inst.description, "Manage obesity and weight loss")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.instantiatesUri[0], "http://example.org/protocol-for-obesity")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2017-06-01").date)
        self.assertEqual(inst.period.end.as_json(), "2017-06-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")
    
    def testCarePlan5(self):
        inst = self.instantiate_from("careplan-example-f201-renal.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan5(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan5(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan5(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "284093001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Potassium supplementation")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.activity[0].detail.dailyAmount.code, "258718000")
        self.assertEqual(inst.activity[0].detail.dailyAmount.system, "http://snomed.info/sct")
        self.assertEqual(inst.activity[0].detail.dailyAmount.unit, "mmol")
        self.assertEqual(inst.activity[0].detail.dailyAmount.value, 80)
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "NutritionOrder")
        self.assertEqual(inst.activity[0].detail.scheduledString, "daily")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "306005")
        self.assertEqual(inst.activity[1].detail.code.coding[0].display, "Echography of kidney")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(inst.activity[1].detail.kind, "ServiceRequest")
        self.assertEqual(inst.activity[1].detail.status, "completed")
        self.assertEqual(inst.contained[0].id, "careteam")
        self.assertEqual(inst.contained[1].id, "goal")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.intent, "proposal")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-13").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-13")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan6(self):
        inst = self.instantiate_from("careplan-example-GPVisit.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan6(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan6(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan6(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "nursecon")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.activity[0].detail.code.text, "Nurse Consultation")
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "Appointment")
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.end.date, FHIRDate("2013-01-01T10:50:00+00:00").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.end.as_json(), "2013-01-01T10:50:00+00:00")
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.date, FHIRDate("2013-01-01T10:38:00+00:00").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.as_json(), "2013-01-01T10:38:00+00:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "doccon")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.activity[1].detail.code.text, "Doctor Consultation")
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(inst.activity[1].detail.kind, "Appointment")
        self.assertEqual(inst.activity[1].detail.status, "scheduled")
        self.assertEqual(inst.contained[0].id, "p1")
        self.assertEqual(inst.contained[1].id, "careteam")
        self.assertEqual(inst.contained[2].id, "goal")
        self.assertEqual(inst.id, "gpvisit")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-01-01T10:30:00+00:00").date)
        self.assertEqual(inst.period.start.as_json(), "2013-01-01T10:30:00+00:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")
    
    def testCarePlan7(self):
        inst = self.instantiate_from("careplan-example-integrated.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan7(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan7(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan7(self, inst):
        self.assertEqual(inst.activity[0].detail.description, "Eve will review photos of high and low density foods and share with her parents")
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[0].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[0].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[0].detail.status, "not-started")
        self.assertEqual(inst.activity[0].progress[0].text, "Eve eats one meal a day with her parents")
        self.assertEqual(inst.activity[0].progress[0].time.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[0].progress[0].time.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[1].detail.description, "Eve will ask her dad to asist her to put the head of her bed on blocks")
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(inst.activity[1].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[1].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[1].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[1].detail.kind, "CommunicationRequest")
        self.assertEqual(inst.activity[1].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[1].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[1].detail.status, "not-started")
        self.assertEqual(inst.activity[1].progress[0].text, "Eve will sleep in her bed more often than the couch")
        self.assertEqual(inst.activity[1].progress[0].time.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[1].progress[0].time.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[2].detail.description, "Eve will reduce her intake of coffee and chocolate")
        self.assertFalse(inst.activity[2].detail.doNotPerform)
        self.assertEqual(inst.activity[2].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[2].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[2].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[2].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[2].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[2].detail.status, "in-progress")
        self.assertEqual(inst.activity[3].detail.description, "Eve will walk her friend's dog up and down a big hill 15-30 minutes 3 days a week")
        self.assertFalse(inst.activity[3].detail.doNotPerform)
        self.assertEqual(inst.activity[3].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[3].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[3].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[3].detail.scheduledPeriod.start.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[3].detail.scheduledPeriod.start.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[3].detail.status, "in-progress")
        self.assertEqual(inst.activity[3].progress[0].text, "Eve would like to try for 5 days a week.")
        self.assertEqual(inst.activity[3].progress[0].time.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[3].progress[0].time.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[3].progress[1].text, "Eve is still walking the dogs.")
        self.assertEqual(inst.activity[3].progress[1].time.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[3].progress[1].time.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[4].detail.description, "Eve will walk 3 blocks to her parents house twice a week")
        self.assertFalse(inst.activity[4].detail.doNotPerform)
        self.assertEqual(inst.activity[4].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[4].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[4].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[4].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[4].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[4].detail.status, "in-progress")
        self.assertEqual(inst.activity[4].progress[0].text, "Eve walked 4 times the last week.")
        self.assertEqual(inst.activity[4].progress[0].time.date, FHIRDate("2012-08-13").date)
        self.assertEqual(inst.activity[4].progress[0].time.as_json(), "2012-08-13")
        self.assertEqual(inst.activity[4].progress[1].text, "Eve did not walk to her parents the last week, but has plans to start again")
        self.assertEqual(inst.activity[4].progress[1].time.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[4].progress[1].time.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[5].detail.description, "Eve will use a calendar to check off after medications are taken")
        self.assertFalse(inst.activity[5].detail.doNotPerform)
        self.assertEqual(inst.activity[5].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[5].detail.extension[0].valueDate.date, FHIRDate("2012-08-13").date)
        self.assertEqual(inst.activity[5].detail.extension[0].valueDate.as_json(), "2012-08-13")
        self.assertEqual(inst.activity[5].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[5].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[5].detail.status, "in-progress")
        self.assertEqual(inst.activity[6].detail.description, "Eve will use her lights MWF after her shower for 3 minutes")
        self.assertFalse(inst.activity[6].detail.doNotPerform)
        self.assertEqual(inst.activity[6].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[6].detail.extension[0].valueDate.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[6].detail.extension[0].valueDate.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[6].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[6].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[6].detail.status, "in-progress")
        self.assertEqual(inst.activity[6].progress[0].text, "After restarting the vinegar soaks the psoriasis is improved and Eve plans to treat the remainder with light treatments.  She plans to start this week.")
        self.assertEqual(inst.activity[6].progress[0].time.date, FHIRDate("2012-08-13").date)
        self.assertEqual(inst.activity[6].progress[0].time.as_json(), "2012-08-13")
        self.assertEqual(inst.activity[6].progress[1].text, "Since her skin is improved Eve has not been using the light treatment as often, maybe once a week.  She would like to increase to 3 times a week again")
        self.assertEqual(inst.activity[6].progress[1].time.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[6].progress[1].time.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[7].detail.description, "Eve will use a calendar of a chart to help her remember when to take her medications")
        self.assertFalse(inst.activity[7].detail.doNotPerform)
        self.assertEqual(inst.activity[7].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[7].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[7].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[7].detail.scheduledPeriod.start.date, FHIRDate("2012-07-10").date)
        self.assertEqual(inst.activity[7].detail.scheduledPeriod.start.as_json(), "2012-07-10")
        self.assertEqual(inst.activity[7].detail.status, "in-progress")
        self.assertEqual(inst.activity[7].progress[0].text, "Eve created a chart as a reminer to take the medications that do not fit in her pill box")
        self.assertEqual(inst.activity[7].progress[0].time.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[7].progress[0].time.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[8].detail.description, "Eve will start using stretch bands and one step 2 days a week Mon/Wed 6-7am and maybe Friday afternoon")
        self.assertFalse(inst.activity[8].detail.doNotPerform)
        self.assertEqual(inst.activity[8].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[8].detail.extension[0].valueDate.date, FHIRDate("2012-08-23").date)
        self.assertEqual(inst.activity[8].detail.extension[0].valueDate.as_json(), "2012-08-23")
        self.assertEqual(inst.activity[8].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[8].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[8].detail.status, "on-hold")
        self.assertEqual(inst.activity[8].progress[0].text, "Will be able to esume exercise.")
        self.assertEqual(inst.activity[8].progress[0].time.date, FHIRDate("2012-07-30").date)
        self.assertEqual(inst.activity[8].progress[0].time.as_json(), "2012-07-30")
        self.assertEqual(inst.activity[8].progress[1].text, "Eve prefers to focus on walking at this time")
        self.assertEqual(inst.activity[8].progress[1].time.date, FHIRDate("2012-08-13").date)
        self.assertEqual(inst.activity[8].progress[1].time.as_json(), "2012-08-13")
        self.assertEqual(inst.activity[9].detail.description, "Eve will match a printed medication worksheet with the medication bottles at home")
        self.assertFalse(inst.activity[9].detail.doNotPerform)
        self.assertEqual(inst.activity[9].detail.extension[0].url, "http://example.org/fhir/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[9].detail.extension[0].valueDate.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[9].detail.extension[0].valueDate.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[9].detail.scheduledPeriod.start.date, FHIRDate("2012-07-10").date)
        self.assertEqual(inst.activity[9].detail.scheduledPeriod.start.as_json(), "2012-07-10")
        self.assertEqual(inst.activity[9].detail.status, "completed")
        self.assertEqual(inst.contained[0].id, "p1")
        self.assertEqual(inst.contained[1].id, "p2")
        self.assertEqual(inst.contained[2].id, "p3")
        self.assertEqual(inst.contained[3].id, "g1")
        self.assertEqual(inst.contained[4].id, "g2")
        self.assertEqual(inst.contained[5].id, "g3")
        self.assertEqual(inst.contained[6].id, "g4")
        self.assertEqual(inst.contained[7].id, "g5")
        self.assertEqual(inst.id, "integrate")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "Patient family is not ready to commit to goal setting at this time.  Goal setting will be addressed in the future")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan8(self):
        inst = self.instantiate_from("careplan-example-f003-pharynx.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan8(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan8(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan8(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "172960003")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Incision of retropharyngeal abscess")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "ServiceRequest")
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-06-27T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.contained[0].id, "careteam")
        self.assertEqual(inst.contained[1].id, "goal")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP3953")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-08T09:30:10+01:00").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-08T09:30:10+01:00")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-08T09:00:10+01:00").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-08T09:00:10+01:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan9(self):
        inst = self.instantiate_from("careplan-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan9(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan9(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan9(self, inst):
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "64915003")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Operation on heart")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.kind, "ServiceRequest")
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-06-27T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.contained[0].id, "careteam")
        self.assertEqual(inst.contained[1].id, "goal")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP2903")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2011-06-27").date)
        self.assertEqual(inst.period.end.as_json(), "2011-06-27")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-06-26").date)
        self.assertEqual(inst.period.start.as_json(), "2011-06-26")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan10(self):
        inst = self.instantiate_from("careplan-example-pregnancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan10(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan10(inst2)
        self.evaluate_simplified_json(inst2)
    
    def implCarePlan10(self, inst):
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "1an")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[1].detail.code.text, "First Antenatal encounter")
        self.assertEqual(inst.activity[1].detail.description, "The first antenatal encounter. This is where a detailed physical examination is performed.             and the pregnanacy discussed with the mother-to-be.")
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(inst.activity[1].detail.kind, "Appointment")
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.end.date, FHIRDate("2013-02-28").date)
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(), "2013-02-28")
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.start.date, FHIRDate("2013-02-14").date)
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(), "2013-02-14")
        self.assertEqual(inst.activity[1].detail.status, "scheduled")
        self.assertEqual(inst.activity[1].extension[0].url, "http://example.org/fhir/StructureDefinition/careplan#andetails")
        self.assertEqual(inst.activity[1].extension[0].valueUri, "http://orionhealth.com/fhir/careplan/1andetails")
        self.assertEqual(inst.activity[2].detail.code.coding[0].code, "an")
        self.assertEqual(inst.activity[2].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[2].detail.code.text, "Follow-up Antenatal encounter")
        self.assertEqual(inst.activity[2].detail.description, "The second antenatal encounter. Discuss any issues that arose from the first antenatal encounter")
        self.assertFalse(inst.activity[2].detail.doNotPerform)
        self.assertEqual(inst.activity[2].detail.kind, "Appointment")
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.end.date, FHIRDate("2013-03-14").date)
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(), "2013-03-14")
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.start.date, FHIRDate("2013-03-01").date)
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(), "2013-03-01")
        self.assertEqual(inst.activity[2].detail.status, "not-started")
        self.assertEqual(inst.activity[3].detail.code.coding[0].code, "del")
        self.assertEqual(inst.activity[3].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[3].detail.code.text, "Delivery")
        self.assertEqual(inst.activity[3].detail.description, "The delivery.")
        self.assertFalse(inst.activity[3].detail.doNotPerform)
        self.assertEqual(inst.activity[3].detail.kind, "Appointment")
        self.assertEqual(inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.end.date, FHIRDate("2013-09-14").date)
        self.assertEqual(inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(), "2013-09-14")
        self.assertEqual(inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.start.date, FHIRDate("2013-09-01").date)
        self.assertEqual(inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(), "2013-09-01")
        self.assertEqual(inst.activity[3].detail.status, "not-started")
        self.assertEqual(inst.contained[0].id, "p1")
        self.assertEqual(inst.contained[1].id, "pr1")
        self.assertEqual(inst.contained[2].id, "pr2")
        self.assertEqual(inst.contained[3].id, "careteam")
        self.assertEqual(inst.contained[4].id, "goal")
        self.assertEqual(inst.extension[0].url, "http://example.org/fhir/StructureDefinition/careplan#lmp")
        self.assertEqual(inst.extension[0].valueDateTime.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.extension[0].valueDateTime.as_json(), "2013-01-01")
        self.assertEqual(inst.id, "preg")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-10-01").date)
        self.assertEqual(inst.period.end.as_json(), "2013-10-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2013-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")

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