// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Incorrect Serial No Valuation"] = {
	filters: [
		{
			label: __("Item Code"),
			fieldtype: "Link",
			fieldname: "item_code",
			options: "Item",
			get_query: function () {
				return {
					filters: {
						has_serial_no: 1,
					},
				};
			},
		},
		{
			label: __("From Date"),
			fieldtype: "Date",
			fieldname: "from_date",
			reqd: 1,
<<<<<<< HEAD
<<<<<<< HEAD
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[1],
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), with_dates=true)[1],
>>>>>>> 4496a6760e (fix: Default year start and end dates in reports)
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[1],
>>>>>>> 2341061852 (fix: Default year start and end date in reports)
		},
		{
			label: __("To Date"),
			fieldtype: "Date",
			fieldname: "to_date",
			reqd: 1,
<<<<<<< HEAD
<<<<<<< HEAD
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[2],
		},
	],
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), with_dates=true)[2],
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[2],
>>>>>>> 2341061852 (fix: Default year start and end date in reports)
		}
	]
>>>>>>> 4496a6760e (fix: Default year start and end dates in reports)
};
