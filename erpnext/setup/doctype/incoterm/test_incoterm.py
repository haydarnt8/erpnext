# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestIncoterm(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestIncoterm(UnitTestCase):
	"""
	Unit tests for Incoterm.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestIncoterm(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
