# -*- coding: utf-8 -*-
# Copyright (c) 2020, ossphin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class SubscriptionContractProgramBills(Document):
	def autoname(self):
		self.name = f"{self.item_name}-{self.item_group}"
