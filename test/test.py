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

## @Test test.py
# Test Script
#
# This is utility script to stress test the PyPerFin tool



import sys
import os
import random
from pprint import *
import string

TEST_CT = 100

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))
	


cwd = os.getcwd()
test_dir = '../src/'


exe_path = test_dir

os.chdir(exe_path)

#generate the executable

logfile = open('test.log', 'w')

# random number range for month
start_m = 0
stop_m = 11

# random number range for option
start_o = 1
stop_o = 3

# random number range for category
start_c = 1
stop_c = 14

# random number range for category
start_v = 0
stop_v = 100

# list of months
m_list = ["Jan2013", "Feb2013", "Mar2013", "Apr2013", "May2013", "Jun2013", "Jul2013", "Aug2013", "Sep2013", "Oct2013", "Nov2013", "Dec2013"]

# random number for date
start_d = 1
stop_d = 31

for ct in range(TEST_CT):
	# For choosing month
	pprint("=============== Test %d ===================" %ct)
	m_idx = random.randint(start_m, stop_m)
	m = m_list[m_idx]
	
	o = random.randint(start_o,stop_o)
	c = random.randint(start_c,stop_c)
	v = random.randint(start_v,stop_v)
	d = random.randint(start_d,stop_d)
	cm = id_generator()
	dt = "%d%s" %(d, m)
	
	if o == 1:
		c = (c % 4) + 1
		v = v * 100;
	elif o == 2:
		v = v * 25
	elif o == 3:
		c = (c % 10) + 1
		cm = random.randint(1,5)
		v = v * 50
	
	eval_str = "python PyPerFin_app.py --o %s --c %s --fm %s --v %s --d %s --cm %s" %(o, c, m, v, dt, cm)
	pprint(eval_str)
	os.system(eval_str)
	logfile.write(eval_str)
	logfile.write("\n")
	
logfile.close()
	
	
	