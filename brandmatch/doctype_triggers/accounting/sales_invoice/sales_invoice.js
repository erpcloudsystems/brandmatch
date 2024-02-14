// frappe.ui.form.on('Sales Invoice', {
//     customer : function(frm){
//             frm.doc.items = [] 
//             cur_frm.add_child("items");
//             cur_frm.refresh_fields();
//     }
// });
// cur_frm.cscript.onload = function(frm) {
//     cur_frm.fields_dict['items'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
//         return {
//             query: "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.item_query",
//             filters: {'customer': cur_frm.doc.customer,'is_purchase_item': 1}
//         }
//     }
// }

frappe.ui.form.on('Sales Invoice', {
    customer : function(frm){
            frm.doc.items = [] 
            cur_frm.add_child("items");
            cur_frm.refresh_fields();
    }
});
cur_frm.cscript.onload = function(frm) {
    cur_frm.fields_dict['items'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
        return {
            query: "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.item_query",
            filters: {'selling_price_list': cur_frm.doc.selling_price_list,'is_purchase_item': 1}
        }
    }
}