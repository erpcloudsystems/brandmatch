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

    # Define the fields to search by
    search_fields = ["item_code", "item_description", "item_name"]

    # Build the WHERE clause for SQL query dynamically based on searchfield
    where_clause = f"price_list = %s AND ({' OR '.join([f'{field} LIKE %s' for field in search_fields])})"

    # Define the parameters for SQL query
    params = [selling_price_list] + [f"%{txt}%" for _ in range(len(search_fields))]

    # Execute SQL query to retrieve item information
    item_names = frappe.db.sql(f"""
        SELECT item_code, item_description
        FROM `tabItem Price`
        WHERE {where_clause}
    """, tuple(params), as_dict=True)

    # Format the results
    results = [(item.get('item_code'), item.get('item_description', '')) for item in item_names]

    return results


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_customer_address(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
    customer = filters.get("customer")
    search_value = "%%%s%%" % txt

    # Get Customer Address 
    address_names = frappe.db.get_all("Dynamic Link", {"link_name": customer}, ["parent"])
    address_names = [d.parent for d in address_names]
    
    # Define the fields to search by
    search_fields = ["name", "country"]

    # Build the WHERE clause for SQL query dynamically based on searchfield
    where_clause = f"name IN %(address_names)s AND ({' OR '.join([f'{field} LIKE %(search_value)s' for field in search_fields])})"

    # Define the parameters for SQL query
    params = {"address_names": address_names, "search_value": search_value}

    # Execute SQL query to retrieve address information
    addresses = frappe.db.sql(f"""
        SELECT name, country
        FROM `tabAddress`
        WHERE {where_clause}
    """, params, as_dict=True)
    
    results = [(address.get('name'), address.get('country')) for address in addresses]

    return results


    

