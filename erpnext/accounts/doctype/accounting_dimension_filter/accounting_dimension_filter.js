// Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Accounting Dimension Filter', {
	onload: function(frm) {
		frm.set_query('applicable_on_account', 'accounts', function() {
			return {
				filters : {
					'company': frm.doc.company
				}
			}
		});

		frappe.db.get_list('Accounting Dimension',
			{fields: ['document_type']}).then((res) => {
			let options = ['Cost Center', 'Project'];

			res.forEach((dimension) => {
				options.push(dimension.document_type);
			});

			frm.set_df_property('accounting_dimension', 'options', options);
		});

		frm.trigger('setup_filters');
	},

	setup_filters: function(frm) {
		let filters = {};

		frappe.model.with_doctype(frm.doc.accounting_dimension, function() {
			if (frm.doc.accounting_dimension) {
				if (frappe.model.is_tree(frm.doc.accounting_dimension)) {
					filters['is_group'] = 0;
				}

				if (frappe.meta.has_field(frm.doc.accounting_dimension, 'company')) {
					filters['company'] = frm.doc.company;
				}

				frm.set_query('dimension_value', 'dimensions', function() {
					return {
						filters: filters
					}
				});
			}
		});
	},

	accounting_dimension: function(frm) {
		frm.clear_table("dimensions");
		let row = frm.add_child("dimensions");
		row.accounting_dimension = frm.doc.accounting_dimension;
		frm.refresh_field("dimensions");
		frm.trigger('setup_filters');
	},
});

frappe.ui.form.on('Allowed Dimension', {
	dimensions_add: function(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		row.accounting_dimension = frm.doc.accounting_dimension;
		frm.refresh_field("dimensions");
	}
});