frappe.ui.form.on('Sales Order', {
    customer : function(frm){
            frm.doc.items = [] 
            cur_frm.add_child("items");
            cur_frm.refresh_fields();
    }
});
cur_frm.cscript.onload = function(frm) {
    cur_frm.fields_dict['items'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
        return {
            query: "brandmatch.doctype_triggers.selling.sales_order.sales_order.item_query",
            filters: {'selling_price_list': cur_frm.doc.selling_price_list,'is_purchase_item': 1}
        }
    }
}

// frappe.ui.form.on('Sales Order Item', {
// 	setup: function(frm){
// 		frm.fields_dict['item_code'].get_query = function(doc){
// 			// console.log(doc.department);
// 			return { filters: [
// 				['Item Price', 'price_list', '=', frm.doc.customer],
// 		] };
// 		};
// 	},
// });

cur_frm.cscript.onload = function(frm) {
    cur_frm.fields_dict['customer_address'].get_query = function(doc) {
        return {
            query: "brandmatch.doctype_triggers.selling.sales_order.sales_order.get_customer_address",
            filters: {'customer': cur_frm.doc.customer}
        };
    };
};



