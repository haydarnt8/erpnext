# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Email Digest')


class TestEmailDigest(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestEmailDigest(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
