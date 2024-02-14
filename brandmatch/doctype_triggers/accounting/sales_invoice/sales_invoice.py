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
    for t in doc.items:
        item_price_hold = frappe.db.get_value("Item Price", {'item_code': t.item_code,'price_list': doc.selling_price_list}, "custom_hold")
        if item_price_hold ==1 :
            frappe.throw("تم ايقاف التعامل على السعر الخاص بالمنتج {0} في الصف {1}".format(t.item_code,t.idx))
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
    


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def item_query(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
    selling_price_list = filters.get("selling_price_list", "")

    # Execute SQL query to retrieve item information
    if txt:
        item_names = frappe.db.sql("""
            SELECT item_code, item_description
            FROM `tabItem Price`
            WHERE price_list = %s
            AND item_code LIKE %s
        """, (selling_price_list, f"%{txt}%"), as_dict=True)
    else:
        item_names = frappe.db.sql("""
            SELECT item_code, item_description
            FROM `tabItem Price`
            WHERE price_list = %s
        """, selling_price_list, as_dict=True)

    # Format the results
    results = [(item.get('item_code'), item.get('item_description', '')) for item in item_names]
    
    return results