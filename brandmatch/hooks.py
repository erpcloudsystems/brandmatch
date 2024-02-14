app_name = "brandmatch"
app_title = "Brandmatch"
app_publisher = "Mansy"
app_description = "Brand Match"
app_email = "ahmedmansy265@gmail.com"
app_license = "mit"

doc_events = {
		"Payment Entry": {
		"before_insert": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.before_insert",
		"after_insert": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.after_insert",
		"onload": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.onload",
		"before_validate": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.before_validate",
		"validate": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.validate",
		"on_submit": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.before_save",
		"before_cancel": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.before_cancel",
		"on_update": "brandmatch.doctype_triggers.accounting.payment_entry.payment_entry.on_update",
	},
	"Purchase Invoice": {
		"before_insert": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_insert",
		"after_insert": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.after_insert",
		"onload": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.onload",
		"before_validate": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_validate",
		"validate": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.validate",
		"on_submit": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_save",
		"before_cancel": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.before_cancel",
		"on_update": "brandmatch.doctype_triggers.accounting.purchase_invoice.purchase_invoice.on_update",
	},
	"Purchase Order": {
		"before_insert": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.before_insert",
		"after_insert": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.after_insert",
		"onload": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.onload",
		"before_validate": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.before_validate",
		"validate": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.validate",
		"on_submit": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.before_save",
		"before_cancel": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.before_cancel",
		"on_update": "brandmatch.doctype_triggers.accounting.purchase_order.purchase_order.on_update",
	},
	"Sales Order": {
		"before_insert": "brandmatch.doctype_triggers.selling.sales_order.sales_order.before_insert",
		"after_insert": "brandmatch.doctype_triggers.selling.sales_order.sales_order.after_insert",
		"onload": "brandmatch.doctype_triggers.selling.sales_order.sales_order.onload",
		"before_validate": "brandmatch.doctype_triggers.selling.sales_order.sales_order.before_validate",
		"validate": "brandmatch.doctype_triggers.selling.sales_order.sales_order.validate",
		"on_submit": "brandmatch.doctype_triggers.selling.sales_order.sales_order.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.selling.sales_order.sales_order.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.selling.sales_order.sales_order.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.selling.sales_order.sales_order.before_save",
		"before_cancel": "brandmatch.doctype_triggers.selling.sales_order.sales_order.before_cancel",
		"on_update": "brandmatch.doctype_triggers.selling.sales_order.sales_order.on_update",
	},
	"Delivery Note": {
		"before_insert": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.before_insert",
		"after_insert": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.after_insert",
		"onload": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.onload",
		"before_validate": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.before_validate",
		"validate": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.validate",
		"on_submit": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.before_save",
		"before_cancel": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.before_cancel",
		"on_update": "brandmatch.doctype_triggers.stock.delivery_note.delivery_note.on_update",
	},
	"Sales Invoice": {
		"before_insert": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.before_insert",
		"after_insert": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.after_insert",
		"onload": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.onload",
		"before_validate": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.before_validate",
		"validate": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.validate",
		"on_submit": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.on_submit",
		"on_cancel": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.on_cancel",
		"on_update_after_submit": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.on_update_after_submit",
		"before_save": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.before_save",
		"before_cancel": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.before_cancel",
		"on_update": "brandmatch.doctype_triggers.accounting.sales_invoice.sales_invoice.on_update",
	}}

doctype_js = {
	"Payment Entry" : "doctype_triggers/accounting/payment_entry/payment_entry.js",
	"Purchase Invoice" : "doctype_triggers/accounting/purchase_invoice/purchase_invoice.js",
	"Purchase Order" : "doctype_triggers/accounting/purchase_order/purchase_order.js",
	"Sales Order" : "doctype_triggers/selling/sales_order/sales_order.js",
	"Delivery Note" : "doctype_triggers/stock/delivery_note/delivery_note.js",
	"Sales Invoice" : "doctype_triggers/accounting/sales_invoice/sales_invoice.js"
}
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/brandmatch/css/brandmatch.css"
# app_include_js = "/assets/brandmatch/js/brandmatch.js"

# include js, css files in header of web template
# web_include_css = "/assets/brandmatch/css/brandmatch.css"
# web_include_js = "/assets/brandmatch/js/brandmatch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "brandmatch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "brandmatch/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "brandmatch.utils.jinja_methods",
# 	"filters": "brandmatch.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "brandmatch.install.before_install"
# after_install = "brandmatch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "brandmatch.uninstall.before_uninstall"
# after_uninstall = "brandmatch.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "brandmatch.utils.before_app_install"
# after_app_install = "brandmatch.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "brandmatch.utils.before_app_uninstall"
# after_app_uninstall = "brandmatch.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "brandmatch.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"brandmatch.tasks.all"
# 	],
# 	"daily": [
# 		"brandmatch.tasks.daily"
# 	],
# 	"hourly": [
# 		"brandmatch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"brandmatch.tasks.weekly"
# 	],
# 	"monthly": [
# 		"brandmatch.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "brandmatch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "brandmatch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "brandmatch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["brandmatch.utils.before_request"]
# after_request = ["brandmatch.utils.after_request"]

# Job Events
# ----------
# before_job = ["brandmatch.utils.before_job"]
# after_job = ["brandmatch.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"brandmatch.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

