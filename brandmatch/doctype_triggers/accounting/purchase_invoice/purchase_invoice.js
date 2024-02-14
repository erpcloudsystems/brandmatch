frappe.ui.form.on('Purchase Invoice', {
    supplier : function(frm){
            frm.doc.items = [] 
            cur_frm.add_child("items");
            cur_frm.refresh_fields();
    }
});
cur_frm.cscript.onload = function(frm) {
    cur_frm.fields_dict['items'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
        return {
            query: "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.item_query",
            filters: {'supplier': cur_frm.doc.supplier,'is_purchase_item': 1}
        }
    }
}

