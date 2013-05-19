#!/usr/bin/env python
# Author: Swara Technologies
# email: swaratechnologies@outlook.com

# Copyright (c) 2013 Swara Technologies

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

## @package PyPerFin_classes.py
# Fundamental classes for the PyPerFin tool
#
# This module contains all the base classes and their corresponding methods
# needed for the storage and maintenance of data under various categories


## SPENDS_CATEGORY
#
# Defines the basic underlying class for expenses
class SPEND_CATEGORY:

    ## The constructor.
    def __init__(self, name):
        self.name = name
        self.value = 0.0;

    ## add_value
    # @param self The object pointer.
    # @param val Amount to be added to the category
    def add_value (self, val):
        self.value = self.value + val

## INCOME_CATEGORY
#
# Defines the basic underlying class for incomes
class INCOME_CATEGORY:

    ## The constructor.
    def __init__(self, name):
        self.name = name
        self.val = []
        self.src_of_incm = []
        self.dt_of_incm = []
        self.total_val = 0.0

    ## add_incm
    # @param self The object pointer.
    # @param val Amount to be added to the category
    # @param src_of_incm Name of the source of the incomes
    # @param dt_of_incm Date of the income
    def add_incm (self, val, src_of_incm, dt_of_incm):
        self.val.append(val)
        self.src_of_incm.append(src_of_incm)
        self.dt_of_incm.append(dt_of_incm)
        self.total_val = self.total_val + val

## INCOME
#
# Defines the list of items from where you earn your money.
# Used the class "INCOME_CATEGORY"
class INCOME:
    ## The constructor.
    def __init__(self, name):
        self.name = name
        self.salary = INCOME_CATEGORY('salary')
        self.dividend = INCOME_CATEGORY('dividend')
        self.interest = INCOME_CATEGORY('interest')
        self.share_trxn = INCOME_CATEGORY('share_trxn')
        self.bonus = INCOME_CATEGORY('bonus')
        self.total_val = 0.0

    ## get_total
    # @param self The object pointer.
    def get_total(self):
        self.total_val = self.salary.total_val + \
                         self.dividend.total_val + \
                         self.interest.total_val + \
                         self.share_trxn.total_val + \
                         self.bonus.total_val


## SPEND_ITEMS
#
# Defines the list of items where you spend your money.
# Used the class "SPEND_CATEGORY"
class SPEND_ITEMS:
    ## The constructor.
    def __init__(self, name):
        self.name = name
        self.food = SPEND_CATEGORY('food')
        self.fuel = SPEND_CATEGORY('fuel')
        self.vehicle = SPEND_CATEGORY('vehicle')
        self.commutation = SPEND_CATEGORY('commutation')
        self.rent = SPEND_CATEGORY('rent')
        self.electricity = SPEND_CATEGORY('electricity')
        self.water_bill = SPEND_CATEGORY('water_bill')
        self.investment = SPEND_CATEGORY('investment')
        self.tel_bills = SPEND_CATEGORY('tel_bills')
        self.insurance = SPEND_CATEGORY('insurance')
        self.stationaries = SPEND_CATEGORY('stationaries')
        self.emis = SPEND_CATEGORY('emis')
        self.medical = SPEND_CATEGORY('medical')
        self.misc = SPEND_CATEGORY('misc')
        self.total_val = 0.0

    ## get_total
    # @param self The object pointer.
    def get_total(self):
		self.total_val = self.food.value + self.fuel.value + self.vehicle.value + self.commutation.value + self.rent.value + self.electricity.value + self.water_bill.value + self.investment.value + self.tel_bills.value + self.insurance.value + self.stationaries.value + self.emis.value + self.medical.value + self.misc.value

## INV_TYPE_SUB_CATEGORY
#
# Defines the basic underlying object for Investment
class INV_TYPE_SUB_CATEGORY:
	
	## The constructor.
	def __init__(self, name):
		self.name = name
		self.val = 0.0
		self.notes = ""
		
	## add_notes
	# @param self The object pointer.
	def add_notes(self,note):
		self.notes = note


## INV_TYPE_CATEGORY
#
# Defines the list of items from where you invest your money.
# Used the class "INV_TYPE_SUB_CATEGORY"
class INV_TYPE_CATEGORY:
	
	## The constructor.
	def __init__(self, name):
		self.name = name
		self.total_bal = 0.0
		self.no_items = 0
		self.item1 = INV_TYPE_SUB_CATEGORY('item1')
		self.item2 = INV_TYPE_SUB_CATEGORY('item2')
		self.item3 = INV_TYPE_SUB_CATEGORY('item3')
		self.item4 = INV_TYPE_SUB_CATEGORY('item4')
		self.item5 = INV_TYPE_SUB_CATEGORY('item5')
		self.item6 = INV_TYPE_SUB_CATEGORY('item6')
		self.item7 = INV_TYPE_SUB_CATEGORY('item7')
		self.item8 = INV_TYPE_SUB_CATEGORY('item8')
		self.item9 = INV_TYPE_SUB_CATEGORY('item9')
		self.item10 = INV_TYPE_SUB_CATEGORY('item10')
		
	## get_total_bal
	# @param self The object pointer.
	def get_total_bal(self):
		self.total_bal = 0.0
		self.total_bal = self.total_bal + self.item1.val +  self.item2.val + self.item3.val + self.item4.val + self.item5.val + self.item6.val + self.item7.val + self.item8.val + self.item9.val + self.item10.val
		
		
		
## INVESTMENT_CATEGORY
#
# Defines the list of items where you invest your money.
# Used the class "INV_TYPE_CATEGORY"
class INVESTMENT_CATEGORY:

	## The constructor.
	def __init__(self, name):
		self.name = name
		self.total_val = 0.0
		self.typ1 = INV_TYPE_CATEGORY('typ1')
		self.typ2 = INV_TYPE_CATEGORY('typ2')
		self.typ3 = INV_TYPE_CATEGORY('typ3')
		self.typ4 = INV_TYPE_CATEGORY('typ4')
		self.typ5 = INV_TYPE_CATEGORY('typ5')
		self.typ6 = INV_TYPE_CATEGORY('typ6')
		self.typ7 = INV_TYPE_CATEGORY('typ7')
		self.typ8 = INV_TYPE_CATEGORY('typ8')
		self.typ9 = INV_TYPE_CATEGORY('typ9')
		self.typ10 = INV_TYPE_CATEGORY('typ10')
		self.typ11 = INV_TYPE_CATEGORY('typ11')
		self.typ12 = INV_TYPE_CATEGORY('typ12')
		self.typ13 = INV_TYPE_CATEGORY('typ13')
		self.typ14 = INV_TYPE_CATEGORY('typ14')
		self.typ15 = INV_TYPE_CATEGORY('typ15')

	## get_total_inv
	# @param self The object pointer.
	def get_total_inv(self):
		self.total_val = self.typ1.total_bal + self.typ2.total_bal + self.typ3.total_bal + self.typ4.total_bal + self.typ5.total_bal + self.typ6.total_bal + self.typ7.total_bal + self.typ8.total_bal + self.typ9.total_bal + self.typ10.total_bal \
		+ self.typ11.total_bal  + self.typ12.total_bal + self.typ13.total_bal + self.typ14.total_bal + self.typ15.total_bal
        
        

## MONTH_VIEW
#
# Defines the list of spends, incomes, investments in a month
# Used the class "INCOME", "INVESTMENT_CATEGORY" and "SPEND_ITEMS"
class MONTH:
	
    ## The constructor.
    def __init__(self, name):
        self.name = name
        self.dest_dir = '~/Documents/'
        self.ttl_incm = INCOME('ttl_incm')
        self.ttl_spend = SPEND_ITEMS('ttl_spend')
        self.ttl_investment = INVESTMENT_CATEGORY('ttl_investment')
