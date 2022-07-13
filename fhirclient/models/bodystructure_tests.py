#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2022-07-13.
#  2022, SMART Health IT.

import io
import json
import logging
import os
import typing
import unittest

from . import bodystructure

from .fhirdate import FHIRDate
import logging


class BodyStructureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodyStructure", js["resourceType"])
        return bodystructure.BodyStructure(js)
    
    def testBodyStructure1(self):
        inst = self.instantiate_from("bodystructure-example-fetus.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure1(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBodyStructure1(self, inst):
        self.assertEqual(inst.description, "EDD 1/1/2017 confirmation by LMP")
        self.assertEqual(inst.id, "fetus")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.location.coding[0].code, "83418008")
        self.assertEqual(inst.location.coding[0].display, "Entire fetus (body structure)")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Fetus")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodyStructure2(self):
        inst = self.instantiate_from("bodystructure-example-tumor.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure2(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBodyStructure2(self, inst):
        self.assertEqual(inst.description, "7 cm maximum diameter")
        self.assertEqual(inst.id, "tumor")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.image[0].contentType, "application/dicom")
        self.assertEqual(inst.image[0].url, "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details")
        self.assertEqual(inst.location.coding[0].code, "78961009")
        self.assertEqual(inst.location.coding[0].display, "Splenic structure (body structure)")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Spleen")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.coding[0].code, "4147007")
        self.assertEqual(inst.morphology.coding[0].display, "Mass (morphologic abnormality)")
        self.assertEqual(inst.morphology.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.morphology.text, "Splenic mass")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodyStructure3(self):
        inst = self.instantiate_from("bodystructure-example-skin-patch.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure3(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBodyStructure3(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(inst.description, "inner surface (volar) of the left forearm")
        self.assertEqual(inst.id, "skin-patch")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.location.coding[0].code, "14975008")
        self.assertEqual(inst.location.coding[0].display, "Forearm")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Forearm")
        self.assertEqual(inst.locationQualifier[0].coding[0].code, "419161000")
        self.assertEqual(inst.locationQualifier[0].coding[0].display, "Unilateral left")
        self.assertEqual(inst.locationQualifier[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[0].text, "Left")
        self.assertEqual(inst.locationQualifier[1].coding[0].code, "263929005")
        self.assertEqual(inst.locationQualifier[1].coding[0].display, "Volar")
        self.assertEqual(inst.locationQualifier[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[1].text, "Volar")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.text, "Skin patch")
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
                simplified_extensions = [k for k in simplified_js.keys() if k.startswith('extension_')]
                self.assertTrue(len(simplified_extensions) >= len(inst.extension), "Should simplify extensions.")
                for simplified_extension in simplified_extensions:
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