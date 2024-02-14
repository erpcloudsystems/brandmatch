// frappe.ui.form.on('Deliver Note', {
//     customer : function(frm){
//             frm.doc.items = [] 
//             cur_frm.add_child("items");
//             cur_frm.refresh_fields();
//     }
// });
// cur_frm.cscript.onload = function(frm) {
//     cur_frm.fields_dict['items'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
//         return {
//             query: "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.item_query",
//             filters: {'customer': cur_frm.doc.customer,'is_purchase_item': 1}
//         }
//     }
// }