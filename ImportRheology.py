# -*- coding: utf-8 -*-
"""

Filename: ImportRheology.py
Author: Ryan L. Truby
Affiliation: Lewis Research Group, Harvard University
Data: 2015.02.08

Description:
    This library contains functions for importing rheological data obtained on 
    the DHR-3 rheometer in Prof. Jennifer Lewis' lab at Havard University. The
    code was initially adapted from Joseph Muth's Python script, titled,
    "Rheology Reader.py"
    
    This code takes input files of formats listed in AnalyzeRheology.py.
    
    The xls file read should have the following format:
        Row 1: Title of sheet (e.g., "Amplitude sweep - 1")
        Row 2: Storage modulus | Loss modulus | Tan(delta) | Complex viscosity | 
                   Oscillation strain | Angular frequency | Time | Oscillation 
                   strain | Oscillation stress
        Row 3: Pa | Pa |  | Pa.s | 1/s | rad/s | s | % | Pa
        Row 4 to end: (All of the data) 
    
"""

import numpy as np
import os
import matplotlib.pylab as plt
import pandas as pd

def import_folder(folder_name, format):
    files = os.listdir(folder_name)
    print "\nThe files in folder %s are: \n%r" % (folder_name, files)
    files_of_format = [f for f in files if f[-3:] == format]
    print "\nThe files with format %r are: \n%r" % (format, files_of_format)
    return files_of_format

def compile_data(files, folder_name, sheet_name, header, skiprows):
    '''
    This function needs to be edited.
    '''
    currentdir = os.getcwd() + '/' + folder_name
    rheo_data = pd.DataFrame()
    for f in files:
        filedir = currentdir + '/' + f
        data = pd.read_excel(filedir, sheet_name, header = header, skiprows = skiprows)
        rheo_data = rheo_data.append(data, ignore_index = True)
    return rheo_data

def compile_data_panel(files, folder_name, sheet_name, header, skiprows):
    currentdir = os.getcwd() + '/' + folder_name
    rheo_data = dict()
    for f in files:
        filedir = currentdir + '/' + f
        data = pd.read_excel(filedir, sheet_name, header = header, skiprows = skiprows)
        rheo_data[f] = pd.DataFrame(data)
    compiled_data = pd.Panel(rheo_data)
    print "\nThe data is stored in a Panel data structure: \n%r" % compiled_data
    return compiled_data


#def import_filenames():
#    file_name = ''
#    file_name_list = list()
#    print "Enter names of Excel files (w/ extension) containing data (STOP to quit): "
#    while ((file_name != 'STOP') & (file_name != 'stop') & (file_name != 'Stop')):
#        file_name = raw_input()
#        if ((file_name != 'STOP') & (file_name != 'stop') & (file_name != 'Stop')):
#            file_name_list.append(file_name)
#    print '\nImporting the following files:\n%r' % file_name_list
#    return file_name_list
    
#def import_rheo_data(filename, pagename, skipped_rows, labels):
#    data_sets = list()
#    dataset = pd.read_excel(filename, pagename, header = labels, skiprows = skipped_rows)
#    return dataset  
    
    