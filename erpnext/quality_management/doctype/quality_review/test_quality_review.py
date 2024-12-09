# Copyright (c) 2018, Frappe and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

import frappe
=======
import unittest

import frappe
from frappe.tests import IntegrationTestCase
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)

from ..quality_goal.test_quality_goal import get_quality_goal
from .quality_review import review


<<<<<<< HEAD
class TestQualityReview(unittest.TestCase):
=======
class TestQualityReview(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	def test_review_creation(self):
		quality_goal = get_quality_goal()
		review()

		# check if review exists
		quality_review = frappe.get_doc("Quality Review", dict(goal=quality_goal.name))
		self.assertEqual(quality_goal.objectives[0].target, quality_review.reviews[0].target)
		quality_review.delete()

		quality_goal.delete()
