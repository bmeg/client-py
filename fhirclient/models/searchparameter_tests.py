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

from . import searchparameter

from .fhirdate import FHIRDate
import logging


class SearchParameterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SearchParameter", js["resourceType"])
        return searchparameter.SearchParameter(js)
    
    def testSearchParameter1(self):
        inst = self.instantiate_from("searchparameter-example-extension.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter1(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implSearchParameter1(self, inst):
        self.assertEqual(inst.base[0], "Patient")
        self.assertEqual(inst.code, "part-agree")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.description, "Search by url for a participation agreement, which is stored in a DocumentReference")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "DocumentReference.extension('http://example.org/fhir/StructureDefinition/participation-agreement')")
        self.assertEqual(inst.id, "example-extension")
        self.assertEqual(inst.name, "Example Search Parameter on an extension")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.target[0], "DocumentReference")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "reference")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-extension")
        self.assertEqual(inst.xpath, "f:DocumentReference/f:extension[@url='http://example.org/fhir/StructureDefinition/participation-agreement']")
        self.assertEqual(inst.xpathUsage, "normal")
    
    def testSearchParameter2(self):
        inst = self.instantiate_from("searchparameter-example-reference.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter2(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implSearchParameter2(self, inst):
        self.assertEqual(inst.base[0], "Condition")
        self.assertEqual(inst.chain[0], "name")
        self.assertEqual(inst.chain[1], "identifier")
        self.assertEqual(inst.code, "subject")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(inst.description, "Search by condition subject")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "Condition.subject")
        self.assertEqual(inst.id, "example-reference")
        self.assertEqual(inst.modifier[0], "missing")
        self.assertEqual(inst.name, "Example Search Parameter")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose, "Need to search Condition by subject")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.target[0], "Organization")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "reference")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-reference")
        self.assertEqual(inst.xpathUsage, "normal")
    
    def testSearchParameter3(self):
        inst = self.instantiate_from("searchparameter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter3(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implSearchParameter3(self, inst):
        self.assertEqual(inst.base[0], "Resource")
        self.assertEqual(inst.code, "_id")
        self.assertEqual(inst.comparator[0], "eq")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(inst.derivedFrom, "http://hl7.org/fhir/SearchParameter/Resource-id")
        self.assertEqual(inst.description, "Search by resource identifier - e.g. same as the read interaction, but can return included resources")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "id")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "United States of America (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.name, "ID-SEARCH-PARAMETER")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose, "Need to search by identifier for various infrastructural cases - mainly retrieving packages, and matching as part of a chain")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "token")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example")
        self.assertEqual(inst.useContext[0].code.code, "focus")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "positive")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://terminology.hl7.org/CodeSystem/variant-state")
        self.assertEqual(inst.version, "1")
        self.assertEqual(inst.xpath, "f:*/f:id")
        self.assertEqual(inst.xpathUsage, "normal")

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