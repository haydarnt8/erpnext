# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Installation Note')


class TestInstallationNote(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestInstallationNote(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
