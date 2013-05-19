#!/usr/bin/env python
# Copyright (c) 2013 Swara Technologies
# Author: Swara Technologies
# email: swaratechnologies@outlook.com

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

## @package misc_utils.py
# This module contains miscellaneous utility functions.
#
# Utility functions defined here are:
#
# watermark_pdf
#
# add_footer_pdf
#
# merge_pdf
#
# find_curr_month
#
# comma_sep
#
# split_month
#
# get_input
#
# save_proj
#
# load_proj
#
# Watermark the pdf

## Documentation for a watermark_pdf.
#
# To watermark the pdf file with a logo.
def watermark_pdf(in_fname, op_fname, imgPath):
	from pyPdf import PdfFileWriter, PdfFileReader
	from reportlab.pdfgen import canvas
	from StringIO import StringIO
	
	output = PdfFileWriter()
	
	# Using ReportLab to insert image into PDF
	imgTemp1 = StringIO()
	imgDoc1 = canvas.Canvas(imgTemp1)
	
	# Draw image on Canvas and save PDF in buffer
	imgDoc1.drawImage(imgPath, 10, 320, 564, 270)    
	imgDoc1.save()
	
	overlay1 = PdfFileReader(StringIO(imgTemp1.getvalue())).getPage(0)
	output.addPage(overlay1)
	
	# Using ReportLab to insert image into PDF
	imgTemp2 = StringIO()
	imgDoc2 = canvas.Canvas(imgTemp2)
	
	# Draw image on Canvas and save PDF in buffer
	imgDoc2.drawImage(imgPath, 420, 770, 115, 55)    
	imgDoc2.save()
	
	overlay2 = PdfFileReader(StringIO(imgTemp2.getvalue())).getPage(0)
	
	in_file = PdfFileReader(file(in_fname,"rb"))
	n_pg = in_file.getNumPages()
	
	# Use PyPDF to merge the image-PDF into the template
	for i in range(n_pg):
		page = in_file.getPage(i)
		page.mergePage(overlay2)
		output.addPage(page)
	
	#Save the result
	
	outputStream = file(op_fname,"w")
	output.write(outputStream)
	outputStream.close()


## Documentation for a add_footer_pdf.
#
# More details.
def add_footer_pdf(in_fname, op_fname, imgPath):
	from pyPdf import PdfFileWriter, PdfFileReader
	from reportlab.pdfgen import canvas
	from StringIO import StringIO
	
	output = PdfFileWriter()
	
	# Using ReportLab to insert image into PDF
	imgTemp1 = StringIO()
	imgDoc1 = canvas.Canvas(imgTemp1)
	
	# Draw image on Canvas and save PDF in buffer
	imgDoc1.drawImage(imgPath, 210, 20, 155, 35)    
	imgDoc1.save()
	
	overlay1 = PdfFileReader(StringIO(imgTemp1.getvalue())).getPage(0)
	
	in_file = PdfFileReader(file(in_fname,"rb"))
	n_pg = in_file.getNumPages() - 1
	
	page = in_file.getPage(0)
	output.addPage(page)
	
	# Use PyPDF to merge the image-PDF into the template
	for i in range(n_pg):
		page = in_file.getPage(i+1)
		page.mergePage(overlay1)
		output.addPage(page)
		
		#Save the result
		
		outputStream = file(op_fname,"w")
		output.write(outputStream)
		outputStream.close()
		

## Documentation for a merge_pdf.
#
# More details.
# Merge two PDFs
def merge_pdf(outname, files_list, logo):
	from pyPdf import PdfFileReader, PdfFileWriter
	from reportlab.pdfgen import canvas
	from StringIO import StringIO
	from reportlab.lib.pagesizes import letter
	
	
	output = PdfFileWriter()
	
	# Using ReportLab to insert image into PDF
	imgTemp1 = StringIO()
	imgDoc1 = canvas.Canvas(imgTemp1)
	
	# Draw image on Canvas and save PDF in buffer
	imgDoc1.drawImage(logo, 10, 320, 564, 270)    
	imgDoc1.save()
	
	overlay1 = PdfFileReader(StringIO(imgTemp1.getvalue())).getPage(0)
	output.addPage(overlay1)
	
	# Using ReportLab to insert image into PDF
	imgTemp2 = StringIO()
	imgDoc2 = canvas.Canvas(imgTemp2)
	
	# Draw image on Canvas and save PDF in buffer
	imgDoc2.drawImage(logo, 420, 770, 115, 55)   
	imgDoc2.setStrokeColorRGB(0.5, 0.1,0.6)
	imgDoc2.setFillColorRGB(0,0,1)
	imgDoc2.setFont("Courier", 6)
	
	footer_msg = "This is a product of Swara Technologies. For more information, please visit"
	imgDoc2.drawString(45,40, footer_msg)
	
	footer_msg = "http://swaratechnologies.wordpress.com/"
	imgDoc2.setFont("Courier-Bold", 6)

	imgDoc2.drawString(45,33, footer_msg)
	
	footer_msg =  "or email us at: "
	imgDoc2.setFont("Courier", 6)
	imgDoc2.drawString(45,27, footer_msg)
	
	footer_msg = "swaratechnologies@outlook.com"
	imgDoc2.setFont("Courier-Bold", 6)
	imgDoc2.drawString(102,27, footer_msg)
	
	
	imgDoc2.save()
	
	overlay2 = PdfFileReader(StringIO(imgTemp2.getvalue())).getPage(0)
	
	no_pages = []
	if len(files_list) < 2:
		print "Nothing to merge"
		return
	
	for n in range(len(files_list)):
		eval_str = "pdf%d = PdfFileReader(file(files_list[n], 'rb'))" %n
		exec(eval_str)
		
		eval_str = "n_pg = pdf%d.getNumPages()" %n
		exec(eval_str)
		
		no_pages.append(n_pg)
		
	for n in range(len(files_list)):
		for p in range(no_pages[n]):
			eval_str = "page = pdf%d.getPage(%d)" %(n,p)
			exec(eval_str)
			page.mergePage(overlay2)
			output.addPage(page)
			
			
	outputStream = file(outname, "wb")
	output.write(outputStream)
	outputStream.close()
	
## Documentation for a comma_sep.
#
# More details.
def comma_sep (datas,dim):
	# format the data
	if dim == 2:
		for i in range(len(datas)):
			for j in range(len(datas[i])):
				datas[i][j] = '{:1,.2f}'.format(float(datas[i][j]))
	elif dim == 1:
		for j in range(len(datas)):
			datas[j] = '{:1,.2f}'.format(float(datas[j]))
			
	return(datas)
	
## Documentation for a find_curr_month.
#
# More details.
def find_curr_month ():
    import datetime
    now = datetime.datetime.now()
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    m = now.month
    y = now.year
    curr_m = months[ m - 1]
    ret_val = curr_m + str(y)
    return ret_val

## Documentation for a split_month.
#
# More details.
def split_month (m) :
	m = m[:3] + " " + m[5:]
	return(m)
	
## Documentation for a get_input.
#
# More details.
def get_input (options):
    check = False
    keys = options.keys()
    while check == False:
        try:
            input_cmd = int(raw_input('Please enter your choice: '))
            if input_cmd in keys:
                check = True
                break;
            else:
                print "This is not a valid input. Please re enter your choice"
        except ValueError:
            print "This is not a valid input. Please re enter your choice"
    return options[input_cmd]

## Documentation for a save_proj.
#
# More details.
def save_proj(filename, var):
	import pickle 
	f = file(filename, "wb")
	pickle.dump(var, f)
	f.close
	print 'data saved'

## Documentation for a load_proj.
#
# More details.
def load_proj(filename):
	import pickle
	f = file(filename, "rb")
	var = pickle.load(f)
	return var
	print 'Data Restored'
	
					