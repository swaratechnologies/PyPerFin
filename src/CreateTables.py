#!/usr/bin/env python
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

## @package CreateTables.py
# CreateTables is a API wrapper library to support list based table entries
#
# It provides a wrapper utility library over TableFactory.py for easily converting 
# lists and arryas into tables.



__author__ = "Swara Technologies"
__copyright__ = "Copyright 2013, Swara Technologies"
__credits__ = ["Swara Technologies"]
__license__ = "MIT License"
__maintainer__ = "Swara Technologies"
__email__ = "swaratechnologies@outlook.com"
__status__ = "Development"
__version__ = "0.1"

from TableFactory import *
from reportlab.pdfbase import _fontdata_enc_winansi
from reportlab.pdfbase import _fontdata_enc_macroman
from reportlab.pdfbase import _fontdata_enc_standard
from reportlab.pdfbase import _fontdata_enc_symbol
from reportlab.pdfbase import _fontdata_enc_zapfdingbats
from reportlab.pdfbase import _fontdata_enc_pdfdoc
from reportlab.pdfbase import _fontdata_enc_macexpert
from reportlab.pdfbase import _fontdata_widths_courier
from reportlab.pdfbase import _fontdata_widths_courierbold
from reportlab.pdfbase import _fontdata_widths_courieroblique
from reportlab.pdfbase import _fontdata_widths_courierboldoblique
from reportlab.pdfbase import _fontdata_widths_helvetica
from reportlab.pdfbase import _fontdata_widths_helveticabold
from reportlab.pdfbase import _fontdata_widths_helveticaoblique
from reportlab.pdfbase import _fontdata_widths_helveticaboldoblique
from reportlab.pdfbase import _fontdata_widths_timesroman
from reportlab.pdfbase import _fontdata_widths_timesbold
from reportlab.pdfbase import _fontdata_widths_timesitalic
from reportlab.pdfbase import _fontdata_widths_timesbolditalic
from reportlab.pdfbase import _fontdata_widths_symbol
from reportlab.pdfbase import _fontdata_widths_zapfdingbats

## Documentation for a function.
#
# More details.
def create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, datas, file_path, file_name, styles):
    """Create a set of sample tables"""

    # In practice, you'd most likely be embedding your HTML tables in
    # a web page template. For demonstration purposes, we'll create a
    # simple page with a few default styles.
    htmlheader = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
<title>Sample table</title>
<style type="text/css">
body { font-family: Helvetica,Arial,FreeSans; }
table.reporttable { border-style: solid; border-width: 1px; }
table.reporttable tr.tr_odd { background-color: #eee; }
table.reporttable tr.tr_even { background-color: #bbb; }
table.reporttable th { background-color: blue; color: white; }
table.reporttable td.cell_bold { font-weight: bold; }
table.reporttable td.cell_money { text-align: right; font-family: monospace; }
</style>
</head>
<body>
"""
    htmlfooter = """\
</body>
</html>"""

    #### Example of a typical "invoices" table
    
    entries = create_entries (fields, col_headings, datas)
    
    exec_str = ""
    for i in range(len(entries[0])):
         tmp_str = "ColumnSpec('col_%d', col_headings[%d], %s)" %(i,i,styles[i])
         if i != (len(entries[0])-1):
             tmp_str = tmp_str + ","
         exec_str = exec_str + tmp_str
    
    exec_str = "table_rows = RowSpec(" + exec_str + ")"
    
    exec(exec_str)

    lines = table_rows.makeall(entries)
    
    #for tableclass, extension in fileTypes:
    tableclass = fileTypes[0]
    extension =  fileTypes[1]
    f_name = '%s/%s.%s' %(file_path, file_name, extension)
    outfile = open(f_name, 'wb')
    if tableclass is HTMLTable:
        outfile.write(htmlheader)
    outfile.write(tableclass(title_name, subtitle_name,headers=table_rows).render(lines))
    if tableclass is HTMLTable:
         outfile.write(htmlfooter)

## Documentation for a function.
#
# More details.
def create_entries (fields, col_headings, data):
	entries = []
	data_line = []

	for j in range(len(data[0])):
		tmp_data = []
		for k in range(len(data)):
			tmp_data.append(data[k][j])
		data_line.append(tmp_data)
	
	#row_data = [col_headings]
	row_data = []
	
	for j in range(len(fields)):
		row_data.append([j+1, fields[j]])
		
	last_idx = len(row_data[0])
	

	for j in range(len(row_data)):
		tmp_data = data_line[j]
		for k in range(len(tmp_data)):
			row_data[j].insert(last_idx+1+k, tmp_data[k])
	
	for j in range(len(row_data)):		
		temp_list = {}
		for i in range(len(col_headings)):
			col_name = 'col_%s' %i
			val = row_data[j][i]
			list_element = {col_name:val}
			temp_list.update(list_element)
		entries.append(temp_list)	
				
									
	return(entries)

## Documentation for a function.
#
# More details.
if __name__ == '__main__':
	
	fields = ['salary', 'food', 'fuel', 'interest', 'rent', 'miscellaneous']
	fileTypes = ((PDFTable, 'pdf'), (HTMLTable, 'html'), (SpreadsheetTable, 'xls'))
	title_name = 'Summary of Expenses'
	subtitle_name = 'Detailed Monthly Breakup'
	col_headings = ['Serial Number', 'Category', 'Marc2013', 'Apr2013', 'July2013']
	file_path = './examples'
	file_name = "MyTables"

	data1 = [316, 542, 763, 4, 355, 99]
	data2 = [100, 200, 300, 400, 500, 768]
	data3 = [9100, 9200, 9300, 9400, 9500, 9768]
	
	#styles = ["money=True","money=True","money=True","money=True","money=True","money=True"]
	styles = ["bold=True, width=0.7","bold=True, width=0.7","money=True, width=0.7","money=True, width=0.7","money=True, width=0.7","money=True, width=0.7"]
	
	data = [data1, data2, data3]
	
	create_reports(fields, fileTypes, title_name, subtitle_name, col_headings, data, file_path, file_name, styles)
	
