# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPlantFloor(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPlantFloor(UnitTestCase):
	"""
	Unit tests for PlantFloor.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPlantFloor(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
