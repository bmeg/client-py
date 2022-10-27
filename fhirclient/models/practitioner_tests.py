#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2022-10-13.
#  2022, SMART Health IT.

import io
import json
import logging
import os
import typing
import unittest

from . import practitioner

from .fhirdate import FHIRDate
import logging


class PractitionerTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Practitioner", js["resourceType"])
        return practitioner.Practitioner(js)
    
    def testPractitioner1(self):
        inst = self.instantiate_from("practitioner-example-f203-jvg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner1(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1983-04-20").date)
        self.assertEqual(inst.birthDate.as_json(), "1983-04-20")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678903")
        self.assertEqual(inst.identifier[1].system, "https://www.bigregister.nl/")
        self.assertEqual(inst.identifier[1].type.text, "BIG-nummer")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "12345678903")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].text, "Juri van Gelder")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner2(self):
        inst = self.instantiate_from("practitioner-example-f201-ab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner2(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].line[1], "C4 - Automatisering")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-12-24").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-12-24")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678901")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Bronsig")
        self.assertEqual(inst.name[0].given[0], "Arend")
        self.assertEqual(inst.name[0].prefix[0], "Dr.")
        self.assertEqual(inst.name[0].text, "Dokter Bronsig")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.qualification[0].code.coding[0].code, "41672002")
        self.assertEqual(inst.qualification[0].code.coding[0].display, "Pulmonologist")
        self.assertEqual(inst.qualification[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner3(self):
        inst = self.instantiate_from("practitioner-example-f202-lm.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner3(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].line[1], "C4 - Automatisering")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1960-06-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1960-06-12")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678902")
        self.assertEqual(inst.identifier[1].system, "https://www.bigregister.nl/")
        self.assertEqual(inst.identifier[1].type.text, "BIG-nummer")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "12345678902")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Maas")
        self.assertEqual(inst.name[0].given[0], "Luigi")
        self.assertEqual(inst.name[0].prefix[0], "Dr.")
        self.assertEqual(inst.name[0].text, "Luigi Maas")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner4(self):
        inst = self.instantiate_from("practitioner-example-xcda-author.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner4(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner4(self, inst):
        self.assertEqual(inst.id, "xcda-author")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Hippocrates")
        self.assertEqual(inst.name[0].given[0], "Harold")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner5(self):
        inst = self.instantiate_from("practitioner-example-f003-mv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner5(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner5(self, inst):
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "1105 AZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1963-07-01").date)
        self.assertEqual(inst.birthDate.as_json(), "1963-07-01")
        self.assertEqual(inst.communication[0].coding[0].code, "nl")
        self.assertEqual(inst.communication[0].coding[0].display, "Dutch")
        self.assertEqual(inst.communication[0].coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "846100293")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "243HID3RT938")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Versteegh")
        self.assertEqual(inst.name[0].given[0], "Marc")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205562431")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "m.versteegh@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205662948")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner6(self):
        inst = self.instantiate_from("practitioner-example-f002-pv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner6(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner6(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1979-04-29").date)
        self.assertEqual(inst.birthDate.as_json(), "1979-04-29")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "730291637")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "174BIP3JH438")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Voigt")
        self.assertEqual(inst.name[0].given[0], "Pieter")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205569336")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "p.voigt@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205669382")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner7(self):
        inst = self.instantiate_from("practitioner-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner7(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner7(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "PleasantVille")
        self.assertEqual(inst.address[0].line[0], "534 Erewhon St")
        self.assertEqual(inst.address[0].postalCode, "3999")
        self.assertEqual(inst.address[0].state, "Vic")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value, "23")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Careful")
        self.assertEqual(inst.name[0].given[0], "Adam")
        self.assertEqual(inst.name[0].prefix[0], "Dr")
        self.assertEqual(inst.qualification[0].code.coding[0].code, "BS")
        self.assertEqual(inst.qualification[0].code.coding[0].display, "Bachelor of Science")
        self.assertEqual(inst.qualification[0].code.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0360/2.7")
        self.assertEqual(inst.qualification[0].code.text, "Bachelor of Science")
        self.assertEqual(inst.qualification[0].identifier[0].system, "http://example.org/UniversityIdentifier")
        self.assertEqual(inst.qualification[0].identifier[0].value, "12345")
        self.assertEqual(inst.qualification[0].period.start.date, FHIRDate("1995").date)
        self.assertEqual(inst.qualification[0].period.start.as_json(), "1995")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner8(self):
        inst = self.instantiate_from("practitioner-example-f007-sh.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner8(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner8(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1971-11-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1971-11-07")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f007")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "874635264")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "567IUI51C154")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Heps")
        self.assertEqual(inst.name[0].given[0], "Simone")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "020556936")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "S.M.Heps@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205669283")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner9(self):
        inst = self.instantiate_from("practitioner-example-f204-ce.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner9(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner9(self, inst):
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1967-11-05").date)
        self.assertEqual(inst.birthDate.as_json(), "1967-11-05")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f204")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678904")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].text, "Carla Espinosa")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715262169")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner10(self):
        inst = self.instantiate_from("practitioner-example-xcda1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner10(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPractitioner10(self, inst):
        self.assertEqual(inst.id, "xcda1")
        self.assertEqual(inst.identifier[0].system, "http://healthcare.example.org/identifiers/staff")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "D234123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Dopplemeyer")
        self.assertEqual(inst.name[0].given[0], "Sherry")
        self.assertEqual(inst.telecom[0].system, "email")
        self.assertEqual(inst.telecom[0].value, "john.doe@healthcare.example.org")
        self.assertEqual(inst.text.status, "generated")

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
                # why are we skipping Coding test?
                continue

            is_date = 'FHIRDate' in value.__class__.__name__
            if is_date:
                simplified_value_is_date = 'FHIRDate' in simplified_js[name].__class__.__name__
                self.assertFalse(simplified_value_is_date, "Should simplify Date {} {} {}".format(name, value.__class__.__name__, vars(value)) )

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
                expected_extension_key_prefixes = [extension.url.split('/')[-1].replace('-', '_') for extension in inst.extension]
                actual_extension_keys = []
                for prefix in expected_extension_key_prefixes:
                    actual_extension_keys.extend([k for k in simplified_js.keys() if k.startswith(prefix)])
                assert len(actual_extension_keys) >= len(expected_extension_key_prefixes), "Did not find expected extension keys"
                # simplified_extensions = [k for k in simplified_js.keys() if k.startswith('extension_')]
                # self.assertTrue(len(simplified_extensions) >= len(inst.extension), "Should simplify extensions.")
                for simplified_extension in actual_extension_keys:
                    assert simplified_js[simplified_extension] is not None, f"Missing value for {simplified_extension}"
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
        # test values
        for simplified_key, simplified_values in flattened.items():
            if not simplified_values:
                continue
            if not isinstance(simplified_values, typing.List):
                simplified_values = [simplified_values]
            for simplified_value in simplified_values:
                simplified_value_is_fhir_resource = 'fhirclient.models' in simplified_value.__class__.__module__
                simplified_value_is_dict = isinstance(simplified_value, dict)
                if simplified_value_is_fhir_resource or simplified_value_is_dict:
                    msg = "Should simplify value {} {} {}".format(simplified_key, simplified_value.__class__.__name__, vars(simplified_value))
                    self.assertFalse(simplified_value_is_fhir_resource, msg)

        for flattened_key in flattened:
            dict_ = simplified_schema
            for flattened_key_part in flattened_key.split('|'):
                if flattened_key_part not in dict_ and flattened_key_part.isnumeric():
                    # traverse over list index
                    continue
                if flattened_key_part in dict_:
                    dict_ = dict_[flattened_key_part]
                    self.assertIsNotNone(dict_, "Should have a schema entry for {}".format(flattened_key_part))
                    if 'docstring' not in dict_:
                        logging.getLogger(__name__).warning(
                            "Missing docstring for resource_type:{} flattened_key:{} flattened_key_part:{} dict:{}".format(
                                inst.resource_type, flattened_key, flattened_key_part, dict_))
                break