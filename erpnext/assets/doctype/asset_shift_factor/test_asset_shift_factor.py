# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAssetShiftFactor(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestAssetShiftFactor(UnitTestCase):
	"""
	Unit tests for AssetShiftFactor.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAssetShiftFactor(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
