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

## @package PyPerFin_app.py
# This is the application file for PyPerFin tool
#
# Application , argument parsing and report generation wrappers are
# defined here

## Documentation for a method: print_usage
# @param self The object pointer.
# @param expense expense amount to be added to the category

from sys import path
from os import getcwd
from os import system
from os import mkdir
from os.path import exists
from time import time

cwd = getcwd()
lib_path = cwd + '/../lib/'
if lib_path not in path:
	path.append(lib_path)
	
path.append(cwd)

import misc_utils as misc_utils
import PyPerFin_classes as PyPerFinC
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from CreateTables import *
from TableFactory import *
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


months_list = []
proj_path = './../docs/'
proj_bin_file = proj_path+ 'PyPerFin.bin'
outname = "Report.pdf"
outname = proj_path + outname

logo = proj_path + "../docs/swaratech.jpg"

fileTypes = ((PDFTable, 'pdf'))

action_commands = { 1: 'ADD_INC', \
                    2: 'ADD_SPN', \
                    3: 'ADD_INVST'}

add_inc_commands = {1: 'SALARY', \
                    2: 'DIVIDEND', \
                    3: 'INTEREST', \
                    4: 'SHARES', \
                    5: 'BONUS'}

add_spn_commands = {1: 'FOOD', \
                    2: 'FUEL', \
                    3: 'VEHICLE', \
                    4: 'COMMUTATION', \
                    5: 'RENT', \
                    6: 'ELECTRICITY', \
                    7: 'WATER_BILL', \
                    8: 'INVESTMENTS', \
                    9: 'TEL_BILLS', \
                    10: 'INSURANCE', \
                    11: 'STATIONARIES', \
                    12: 'EMIS', \
                    13: 'MEDICAL', \
                    14: 'MISC'}

add_invst_commands = {1: 'BANKS', \
					2: 'FD', \
					3: 'RD', \
					4: 'PPF', \
					5: 'MF', \
					6: 'LIC', \
					7: 'IND_EQUITY',\
					8: 'FOREIGN_EQUITY',\
					9: 'EPF',\
					10: 'INFRA_BONDS',\
					11: 'MISC'}

## Documentation for a function.
#
# More details.
def f_gen_rep_summary ():
	title_name = 'Expense Report'
	subtitle_name = 'Summary of Monthly Expenses'
	col_headings = ["#", "Month", "Income", "Spend", "Investments"]
	fields = []
	file_name = "SummaryReport"
	n = len(months_list)
	months_data = []
	styles = ["bold=True, width=0.3","bold=True, width=0.8","money=True, width=0.8","money=True, width=0.8", "money=True, width=0.7"]
	for idx in range(n):
		months_data.append(months_list[idx].ttl_incm.total_val)
		months_data.append(months_list[idx].ttl_spend.total_val)
		months_data.append(months_list[idx].ttl_investment.total_val)
		fields.append(misc_utils.split_month(months_list[idx].name))
	
	fields.append('TOTAL')
	datas = []
	y_data = []
	for i in [0,1,2]:
		datas.append([])
		y_data.append([])
	
	for i in [0,1,2]:
		datas[i] = months_data[i::3]
		y_data[i] = months_data[i::3]
		
	labels = ['Income', 'Expenditure', 'Investments']
	plot_data.append(y_data)
	plot_data.append(labels)
		
	# compute the totals
	datas[0].append(sum(datas[0][::-1]))
	datas[1].append(sum(datas[1][::-1]))
	datas[2].append(sum(datas[2][::-1]))
	
	datas = misc_utils.comma_sep(datas,2)
	
	#pprint(datas)
	#pprint(fields)
	#pprint(col_headings)
			
	create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, datas, proj_path, file_name, styles)
	
## Documentation for a function.
#
# More details.
def f_gen_rep_detailed_income ():

	title_name = 'Income Report'
	subtitle_name = 'Break-up details of Monthly Income'
	col_headings = ["#", "Month", "Type", "Amount", "Source", "Date"]
	fields = []
	datas = [] 
	file_name = "IncomeReport"
	data_incm_name = []
	data_incm_val = []
	data_comment = []
	data_dt_of_incm = []
	styles = ["bold=True, width=0.3","bold=True, width=0.7","bold=True, width=0.7","money=True, width=0.7", "width=0.7", "width=0.7"]
	for idx in range(len(months_list)):
		
		temp_month = months_list[idx]
		
		for keys in add_inc_commands.keys():
			incm_name = add_inc_commands[keys]
			
			if incm_name == 'SALARY':
				incm_type = temp_month.ttl_incm.salary
			elif incm_name == 'DIVIDEND':
				incm_type = temp_month.ttl_incm.dividend
			elif incm_name == 'INTEREST':
				incm_type = temp_month.ttl_incm.interest
			elif incm_name == 'SHARES':
				incm_type = temp_month.ttl_incm.share_trxn
			elif incm_name == 'BONUS':
				incm_type = temp_month.ttl_incm.bonus
			else:
				print "unsupported option"
				
			for sub_idx in range(len(incm_type.val)):
				data_incm_name.append(incm_name)
				data_incm_val.append(incm_type.val[sub_idx])
				data_comment.append(incm_type.src_of_incm[sub_idx])
				data_dt_of_incm.append(incm_type.dt_of_incm[sub_idx])
				fields.append(misc_utils.split_month(temp_month.name))

	
	datas.append(data_incm_name)
	datas.append(data_incm_val)
	datas.append(data_comment)
	datas.append(data_dt_of_incm)
	
	fields.append('TOTAL')
		# compute the totals
	datas[0].append("")
	datas[1].append(sum(datas[1][::-1]))
	datas[1] = misc_utils.comma_sep(datas[1],1)
	datas[2].append("")
	datas[3].append("")
	
	#pprint(fields)
	#pprint(datas)
	create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, datas, proj_path, file_name, styles)
	
## Documentation for a function.
#
# More details.
def f_gen_rep_detailed_spend ():
	title_name = 'Spend Report'
	subtitle_name = 'Break-up details of Monthly Expenses'
	col_headings = ["#", "Spend Category"]
	fields = []
	datas = [] 
	file_name = "spendReport"
	data_spend_val = []
	styles = ["bold=True, width=0.3","bold=True, width=0.9"]
	
	k = -1
	months_data = []
	
	for keys in add_spn_commands.keys():
		spend_name = add_spn_commands[keys]
		k = k + 1
		fields.append(spend_name)
		
		for idx in range(len(months_list)):
			
			temp_month = months_list[idx]
			
			if spend_name == 'FOOD':
				spend_type = temp_month.ttl_spend.food
			elif spend_name == 'FUEL':
				spend_type = temp_month.ttl_spend.fuel
			elif spend_name == 'VEHICLE':
				spend_type = temp_month.ttl_spend.vehicle
			elif spend_name == 'COMMUTATION':
				spend_type = temp_month.ttl_spend.commutation
			elif spend_name == 'RENT':
				spend_type = temp_month.ttl_spend.rent
			elif spend_name == 'ELECTRICITY':
				spend_type = temp_month.ttl_spend.electricity
			elif spend_name == 'WATER_BILL':
				spend_type = temp_month.ttl_spend.water_bill
			elif spend_name == 'INVESTMENTS':
				spend_type = temp_month.ttl_spend.investment
			elif spend_name == 'TEL_BILLS':
				spend_type = temp_month.ttl_spend.tel_bills
			elif spend_name == 'INSURANCE':
				spend_type = temp_month.ttl_spend.insurance
			elif spend_name == 'STATIONARIES':
				spend_type = temp_month.ttl_spend.stationaries
			elif spend_name == 'EMIS':
				spend_type = temp_month.ttl_spend.emis
			elif spend_name == 'MEDICAL':
				spend_type = temp_month.ttl_spend.medical
			elif spend_name == 'MISC':
				spend_type = temp_month.ttl_spend.misc
				
			else:
				print "unsupported option"
				
			months_data.append(spend_type.value)
	
	datas = []
	n = len(months_list)
	for i in range(n):
		col_headings.append(misc_utils.split_month(months_list[i].name))
		styles.append("width=0.5, money=True")
		datas.append([])
	
	if n != 1:
		for i in range(n):
			datas[i] = months_data[i::n]
	else:
		datas = [months_data]

	fields.append('TOTAL')
	# compute the totals
	y_data = []
	for j in range(len(datas)):
		datas[j].append(sum(datas[j][::-1]))
		y_data.append(datas[j][-1])
	
	horz_total = []
	for k in range(len(datas[0])):
		tmp_sum = 0
		for j in range(len(datas)):
			tmp_sum = tmp_sum + datas[j][k]
		horz_total.append(tmp_sum)
	
	col_headings.append('TOTAL')
	styles.append("width=0.5, money=True")
	datas.append(horz_total)
	datas = misc_utils.comma_sep(datas,2)
	#pprint(horz_total)
	#pprint(months_data)
	#pprint(datas)
	#pprint(col_headings)
	#pprint(fields)

	create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, datas, proj_path, file_name, styles)
	
## Documentation for a function.
#
# More details.
def f_gen_rep_detailed_invst ():
	title_name = 'Investments Report'
	subtitle_name = 'Break-up details of Monthly Investments'
	col_headings = ["#", "Category"]
	fields = []
	datas = [] 
	file_name = "InvestmentReport"
	data_invst_val = []
	styles = ["bold=True, width=0.15","bold=False, width=0.85"]
	
	months_data = []

	for keys in add_invst_commands.keys():
		invst_name = add_invst_commands[keys]
		fields.append(invst_name)
		
	for idx in range(len(months_list)):
		m = 0
		invst_val = []
		temp_month = months_list[idx]
		for keys in add_invst_commands.keys():
			m = m + 1
			tmp_invst = temp_month.ttl_investment
			
			# Parse the input and take appropriate action
			eval_str = "tmp_typ = tmp_invst.typ%d" %(m)
			exec(eval_str)
			
			invst_val.append(tmp_typ.total_bal)
		datas.append(invst_val)
		
		col_headings.append(misc_utils.split_month(months_list[idx].name))
		styles.append("width=0.5, money=True")


	fields.append('TOTAL')
	# compute the totals
	y_data = []
	for j in range(len(datas)):
		datas[j].append(sum(datas[j][::-1]))
		y_data.append(datas[j][-1])
		
	horz_total = []
	for k in range(len(datas[0])):
		tmp_sum = 0
		for j in range(len(datas)):
			tmp_sum = tmp_sum + datas[j][k]
		horz_total.append(tmp_sum)
			
	datas = misc_utils.comma_sep(datas,2)
	#pprint(datas)
	#pprint(styles)
	#pprint(col_headings)
	#pprint(fields)
			
	create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, datas, proj_path, file_name, styles)		

## Documentation for a function.
#
# More details.
def f_monthly_report ():
	
	no_types = 15
	
	no_months = len(months_list)
	cash = [0] * no_months
	non_bank_debt = [0] * no_months
	equity = [0] * no_months
	bank_debt = [0] * no_months
	x_data = []
	fname = proj_path + "Monthly_analysis.pdf"
	for idx in range(no_months):
		
		temp_month = months_list[idx]
		m_name = misc_utils.split_month(temp_month.name)
		tmp_invst = temp_month.ttl_investment
		x_data.append(misc_utils.split_month(temp_month.name))
		notes = []
		val = []
	
		for i in range(no_types):
			eval_str = "tmp_typ = tmp_invst.typ%d" %(i+1)
			exec(eval_str)
			
			eval_str = "no_items = tmp_typ.no_items"
			exec(eval_str)
			
			if no_items != 0:
				for j in range(tmp_typ.no_items):
					eval_str = "tmp_item = tmp_typ.item%d" %(j+1)
					exec(eval_str)
					
					if tmp_item.notes != '':
						notes.append(tmp_item.notes)
						val.append(tmp_item.val)
						
					if (tmp_item.notes[:-1] == "FD" or tmp_item.notes[:-1] == "RD"):
						bank_debt[idx] = bank_debt[idx] + tmp_item.val
					elif (tmp_item.notes[:-1] == "PPF" or tmp_item.notes[:-1] == "LIC" or tmp_item.notes[:-1] == "EPF" or tmp_item.notes[:-1] == "INFRA_BONDS"):
						non_bank_debt[idx] = non_bank_debt[idx] + tmp_item.val
					elif (tmp_item.notes[:-1] == "MF" or tmp_item.notes[:-1] == "IND_EQUITY" or tmp_item.notes[:-1] == "FOREIGN_EQUITY"):
						equity[idx] = equity[idx] + tmp_item.val
					elif (tmp_item.notes[:-1] == "BANKS"):
						cash[idx] = cash[idx] + tmp_item.val
							
							
	# Break up bar graph
	fig = plt.figure()	
	
	ind = np.arange(no_months)  # the x locations for the groups
	width = 0.2       # the width of the bars
	
	ax = fig.add_subplot(2,1,1)
	
	rects1 = ax.bar(ind, cash, width, color='b')
	rects2 = ax.bar(ind+width, equity, width, color='y')
	rects3 = ax.bar(ind+2*width, bank_debt, width, color='g')
	rects4 = ax.bar(ind+3*width, non_bank_debt, width, color='r')
	
	# add some
	ax.set_ylabel('Amount in Rupees', fontsize=10)
	ax.set_title('Monthly Trends', fontsize=10)
	ax.set_xticks(ind + 2.2*width)
	ax.set_xticklabels(x_data)
	
	ax.spines['right'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ("Cash", "Equity", "Bank Debt", "Non Bank Debt"), labelspacing=0.05,prop={'size':8} )
	
	plt.tick_params(axis='both', which='major', labelsize=9)
	plt.tick_params(axis='both', which='minor', labelsize=9)
	plt.grid('on')
	
	x_data = []
	temp_month = cm
	m_name = misc_utils.split_month(temp_month.name)
	tmp_invst = temp_month.ttl_investment
	
	notes = []
	val = []

	for i in range(no_types):
		eval_str = "tmp_typ = tmp_invst.typ%d" %(i+1)
		exec(eval_str)
		
		eval_str = "no_items = tmp_typ.no_items"
		exec(eval_str)
		
		if no_items != 0:
			for j in range(tmp_typ.no_items):
				eval_str = "tmp_item = tmp_typ.item%d" %(j+1)
				exec(eval_str)
				
				if tmp_item.notes != '':
					notes.append(tmp_item.notes)
					val.append(tmp_item.val)
					
	
	ind = np.arange(len(notes))  # the x locations for the groups
	width = 0.08       # the width of the bars
	
	ind = ind * 0.15
	ax = fig.add_subplot(2,1,2)
	
	rects1 = ax.bar(ind, val, width, color='y')
	
	# add some
	ax.set_ylabel('Amount in Rupees', fontsize=10)
	ax.set_title('Current Month analysis', fontsize=10)
	ax.set_xticks(ind + 0.05)
	ax.set_xticklabels(notes)
	
	ax.spines['right'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	
	plt.tick_params(axis='both', which='major', labelsize=9)
	plt.tick_params(axis='both', which='minor', labelsize=9)
	plt.xticks(rotation='vertical')
	plt.grid('on')
	#plt.show()
	plt.savefig(fname)
	
## Documentation for a function.
#
# More details.
def f_gen_charts(x_data, plot_data):
	fname = proj_path + "Graphs.pdf"
	x_range = range(len(x_data))
	plt.xticks(x_range, x_data)

	#=======
	N = len(x_data)
	
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2       # the width of the bars
	fig = plt.figure()
	
	ax = fig.add_subplot(1,1,1)
	rects1 = ax.bar(ind, plot_data[0][0], width, color='r')
	rects2 = ax.bar(ind+width, plot_data[0][1], width, color='y')
	rects3 = ax.bar(ind+2*width, plot_data[0][2], width, color='g')
	
	# add some
	ax.set_ylabel('Amount in Rupees', fontsize=10)
	ax.set_title('Monthly Trends', fontsize=10)
	ax.set_xticks(ind + 1.5*width)
	ax.set_xticklabels(x_data)
	
	ax.spines['right'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.legend( (rects1[0], rects2[0], rects3[0]), plot_data[1],labelspacing=0.05,prop={'size':8} )

	plt.tick_params(axis='both', which='major', labelsize=7)
	plt.tick_params(axis='both', which='minor', labelsize=7)
	plt.xticks(rotation='vertical')
	plt.grid('on')
	#plt.show()
	plt.savefig(fname)
	
## Documentation for a function.
#
# More details.
def f_gen_rep ():
	f_gen_rep_summary()
	f_gen_rep_detailed_income ()
	f_gen_rep_detailed_spend ()
	f_gen_rep_detailed_invst ()
	f_monthly_report ()
	
	n = len(months_list)
	x_data = []
	for i in range(n):
		x_data.append(misc_utils.split_month(months_list[i].name))
		
	f_gen_charts(x_data, plot_data)
		
	
	f1 = proj_path + "SummaryReport.pdf"
	f2 = proj_path + "IncomeReport.pdf"
	f3 = proj_path + "InvestmentReport.pdf"
	f4 = proj_path + "spendReport.pdf"
	f5 = proj_path + "Graphs.pdf"
	f6 = proj_path + "Monthly_analysis.pdf"
	
	files_list = [f1,f2,f3,f4,f5,f6]
		
	misc_utils.merge_pdf(outname, files_list, logo)
	
	for i in range(len(files_list)):
		system("rm -rf %s" %files_list[i]) 
		
	system("cp -rf %s %s" %(outname, dest_dir))
	
## Documentation for a function.
#
# More details.
def f_add_inc ():
    global cm
    global args
    print 'Adding Income now..'
    cmd = add_inc_commands[args.category]
    print "You have chosen: %s\n" % cmd

    val = args.value
    comment= args.comment
    dt_of_incm = args.date

    # Parse the input and take appropriate action
    if cmd == 'SALARY':
        cm.ttl_incm.salary.add_incm(val, comment, dt_of_incm)
    elif cmd == 'DIVIDEND':
        cm.ttl_incm.dividend.add_incm(val, comment, dt_of_incm)
    elif cmd == 'INTEREST':
        cm.ttl_incm.interest.add_incm(val, comment, dt_of_incm)
    elif cmd == 'SHARES':
        cm.ttl_incm.share_trxn.add_incm(val, comment, dt_of_incm)
    elif cmd == 'BONUS':
        cm.ttl_incm.bonus.add_incm(val, comment, dt_of_incm)
    else:
        print 'Not supported option'

    cm.ttl_incm.get_total()

## Documentation for a function.
#
# More details.
def f_add_invst ():
	global cm
	global args
	print 'Adding Investment now..'
	cmd = add_invst_commands[args.category]
	category = args.category
	print "You have chosen: %s\n" % cmd
	
	val = args.value
	comment = args.comment
	tmp_invst = cm.ttl_investment
	# Parse the input and take appropriate action
	eval_str = "tmp_invst.typ%d.item%d.add_notes('%s%d')" %(int(category), int(comment), cmd, int(comment))
	exec(eval_str)
	
	eval_str = "tmp_invst.typ%d.item%d.val = val" %(int(category), int(comment))
	exec(eval_str)
	
	eval_str = "tmp_invst.typ%d.get_total_bal()" %(int(category))
	exec(eval_str)
	
	eval_str = "no_items = tmp_invst.typ%d.no_items" %(int(category))
	exec(eval_str)
	
	eval_str = "tmp_invst.typ%d.no_items = max(no_items,%d)" %(int(category), int(comment))
	exec(eval_str)
	
	cm.ttl_investment.get_total_inv()

## Documentation for a function.
#
# More details.
def f_add_spn ():
    global cm
    global args
    cmd = add_spn_commands[args.category]
    print "You have chosen: %s\n" % cmd

    val = args.value
    print 'Adding Spend now..'

    if cmd == 'FOOD':
        cm.ttl_spend.food.add_value(val)
    elif cmd == 'FUEL':
        cm.ttl_spend.fuel.add_value(val)
    elif cmd == 'VEHICLE':
        cm.ttl_spend.vehicle.add_value(val)
    elif cmd == 'COMMUTATION':
        cm.ttl_spend.commutation.add_value(val)
    elif cmd == 'RENT':
        cm.ttl_spend.rent.add_value(val)
    elif cmd == 'ELECTRICITY':
        cm.ttl_spend.electricity.add_value(val)
    elif cmd == 'WATER_BILL':
        cm.ttl_spend.water_bill.add_value(val)
    elif cmd == 'INVESTMENTS':
        cm.ttl_spend.investment.add_value(val)
    elif cmd == 'TEL_BILLS':
        cm.ttl_spend.tel_bills.add_value(val)
    elif cmd == 'INSURANCE':
        cm.ttl_spend.insurance.add_value(val)
    elif cmd == 'STATIONARIES':
        cm.ttl_spend.stationaries.add_value(val)
    elif cmd == 'EMIS':
        cm.ttl_spend.emis.add_value(val)
    elif cmd == 'MEDICAL':
        cm.ttl_spend.medical.add_value(val)
    elif cmd == 'MISC':
        cm.ttl_spend.misc.add_value(val)

    cm.ttl_spend.get_total()

## Documentation for a function.
#
# More details.
def f_add_chrt ():
    global cm
    print 'Generating charts now..'

t0 = time()

git_ver = "v0.1"

banner = ""
banner = banner + "----------------------------------------------------------------\n"
banner = banner + "\t\t   *** PyPerFin *** \n"
banner = banner + "\n\t\t   version: " + git_ver
banner = banner + "\n\nDeveloped by Swara Technologies. For more information,"
banner = banner + "\nplease visit http://swaratechnologies.wordpress.com/ or email"
banner = banner + "\nus at swaratechnologies@outlook.com"
banner = banner + "\n----------------------------------------------------------------\n"

parser = ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

parser.add_argument('--option', '--o', type=int, default=None, help='Please enter one of the choices below as your input option:\n\
\t\t\t\tTo add an income:                1\n\
\t\t\t\tTo add a spend item:             2\n\
\t\t\t\tTo add investement:          	 3')
parser.add_argument('--value', '--v', type=float, default=0.0, help='Value field which takes the amount for either expense or income category option')
parser.add_argument('--category', '--c', type=int, default=1, help='Input option for sub categories:\n\
For Income Category:\n\
\t\t\t\tSALARY:        		1\n\
\t\t\t\tDIVIDEND:      		2\n\
\t\t\t\tINTEREST:      		3\n\
\t\t\t\tSHARES:    		4\n\
\t\t\t\tBONUS:         		5\n\
For Spend Category:\n\
\t\t\t\tFOOD:            	1\n\
\t\t\t\tFUEL:            	2\n\
\t\t\t\tVEHICLE:         	3\n\
\t\t\t\tCOMMUTATION:     	4\n\
\t\t\t\tRENT:            	5\n\
\t\t\t\tELECTRICITY:     	6\n\
\t\t\t\tWATER_BILL:      	7\n\
\t\t\t\tINVESTMENTS:     	8\n\
\t\t\t\tTEL_BILLS:       	9\n\
\t\t\t\tINSURANCE:       	10\n\
\t\t\t\tSTATIONARIES:    	11\n\
\t\t\t\tEMIS:            	12\n\
\t\t\t\tMEDICAL:            	13\n\
\t\t\t\tMISC:            	14\n\
For Investment Category:\n\
\t\t\t\tBANKS:			1\n\
\t\t\t\tFD:			2\n\
\t\t\t\tRD:			3\n\
\t\t\t\tPPF:			4\n\
\t\t\t\tMF:			5\n\
\t\t\t\tLIC:			6\n\
\t\t\t\tIND_EQUITY:		7\n\
\t\t\t\tFOREIGN_EQUITY:		8\n\
\t\t\t\tEPF:			9\n\
\t\t\t\tINFRA_BONDS:		10\n\
\t\t\t\tMISC:			11')

parser.add_argument('--comment', '--cm', type=str, default=None, help='Comments or Notes Field')
parser.add_argument('--date', '--d', type=str, default=None, help='Date of income')
parser.add_argument('--force_month', '--fm', type=str, default=None, help='Force a particular month for data updation. Ex: "Apr2013"')
parser.add_argument('--force_dest', '--fd', type=str, default=None, help='Force the destination directory for the report.')


args = parser.parse_args()

cmd = args.option
dest_dir = args.force_dest

if cmd != None:
	cmd = action_commands[cmd]
	print "You have chosen: %s\n" % cmd
	

if args.force_month == None:
	curr_month = misc_utils.find_curr_month ()
else:
	curr_month = args.force_month

plot_data = []


print banner

# Load the previous state
file_exists = exists(proj_bin_file)
if file_exists:
	months_list = misc_utils.load_proj(proj_bin_file)
else: 
	# check if the directory exists
	dir_exists = exists(proj_path)
	if dir_exists == False:
		mkdir(proj_path)
	
	print "pre loading the %s failed" %proj_bin_file


cm_present = False
cm_idx = None

if len(months_list) is not 0:
	for idx in range(len(months_list)):
		eval_str = "cm_present = '%s' in months_list[%d].name" %(curr_month, idx)
		exec(eval_str)
		
		
		if cm_present == True:
			cm_idx = idx
			break


if cm_present == False:
	#print "Current Month's data is Not present"
	
	# Define the Month class for the current month
	eval_str = "%s = PyPerFinC.MONTH('%s')" % (curr_month, curr_month)
	exec(eval_str)
	
	eval_str = "cm = %s" %(curr_month)
	exec(eval_str)
	
	#eval_str = "months_list.append(%s)" %(curr_month)
	#exec(eval_str)
	months_list.append(cm)
	
else:
	#print "Current Month's data is already present at the index: %d of the months_list" %cm_idx
	
	cm = months_list[cm_idx]
	print "Loading data for %s" % (curr_month)

if dest_dir == None:
	dest_dir = cm.dest_dir
else:
	cm.dest_dir = dest_dir


# Parse the input and take appropriate action
if cmd == 'ADD_INC':
    f_add_inc()
elif cmd == 'ADD_SPN':
    f_add_spn()
elif cmd == 'ADD_INVST':
    f_add_invst()
else:
    print 'Generating Report'

f_gen_rep()
	
# Save the changes
misc_utils.save_proj(proj_bin_file, months_list)


t1 = time()
total_time = t1 - t0

p_str = "Total Time taken = %f" %total_time 
pprint(p_str)
	