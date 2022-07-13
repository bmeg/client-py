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

from . import coverageeligibilityresponse

from .fhirdate import FHIRDate
import logging


class CoverageEligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        return coverageeligibilityresponse.CoverageEligibilityResponse(js)
    
    def testCoverageEligibilityResponse1(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCoverageEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse2(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCoverageEligibilityResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Eligibiliy request could not be processed, please address errors before submitting.")
        self.assertEqual(inst.error[0].code.coding[0].code, "a001")
        self.assertEqual(inst.error[0].code.coding[0].system, "http://terminology.hl7.org/CodeSystem/adjudication-error")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2503")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812343")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "error")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse3(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-benefits-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCoverageEligibilityResponse3(self, inst):
        self.assertEqual(inst.contained[0].id, "coverage-1")
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2502")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812342")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].usedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].usedMoney.value, 3748.0)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].item[0].benefit[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].item[1].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].item[2].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[3].description, "Vision products and services such as exams, glasses and contact lenses.")
        self.assertTrue(inst.insurance[0].item[3].excluded)
        self.assertEqual(inst.insurance[0].item[3].name, "Vision")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.purpose[1], "benefits")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse4(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-benefits.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCoverageEligibilityResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2501")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].item[0].benefit[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].item[1].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].item[2].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[3].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[3].benefit[0].allowedMoney.value, 400)
        self.assertEqual(inst.insurance[0].item[3].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[3].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[3].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[3].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[3].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[3].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[3].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[4].benefit[0].allowedString, "shared")
        self.assertEqual(inst.insurance[0].item[4].benefit[0].type.coding[0].code, "room")
        self.assertEqual(inst.insurance[0].item[4].benefit[1].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[4].benefit[1].allowedMoney.value, 600)
        self.assertEqual(inst.insurance[0].item[4].benefit[1].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].code, "49")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].display, "Hospital Room and Board")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[4].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[4].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[4].term.coding[0].code, "day")
        self.assertEqual(inst.insurance[0].item[4].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[4].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[4].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.purpose[1], "benefits")
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
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