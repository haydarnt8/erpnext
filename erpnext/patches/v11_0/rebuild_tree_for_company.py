import frappe
from frappe.utils.nestedset import rebuild_tree


def execute():
	frappe.reload_doc("setup", "doctype", "company")
<<<<<<< HEAD
	rebuild_tree("Company", "parent_company")
=======
	rebuild_tree("Company")
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
