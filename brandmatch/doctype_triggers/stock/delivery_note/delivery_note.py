from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.desk.reportview import get_filters_cond, get_match_cond
from frappe.utils import nowdate, unique


@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    pass
@frappe.whitelist()
def on_submit(doc, method=None):
    pass
@frappe.whitelist()
def on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass
    


# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def item_query(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
#     item_names = frappe.db.get_all("Item Customer Detail", {"customer_name": filters.get("customer", "")}, ["parent"])
#     item_names = [d.parent for d in item_names]
    
#     if txt in item_names:
#         items = frappe.db.get_all("Item", {"name": ['like', '%' + txt + '%']}, ["name", "description"])
#     # elif txt not in item_names and txt != "":
#     #     items = []
#     else:
#         items = frappe.db.get_all("Item", {"name": ["in", item_names]}, ["name", "description"])  # Get all items if no specific item_code is entered
    
#     results = [(item['name'], item.get('description', '')) for item in items]
#     return results
