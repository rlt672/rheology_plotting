# -*- coding: utf-8 -*-
"""

Filename: PlotRheology.py
Author: Ryan L. Truby
Affiliation: Lewis Research Group, Harvard University
Data: 2015.02.01

Description:
    This library contains functions for plotting rheological data obtained on 
    the DHR-3 rheometer in Prof. Jennifer Lewis' lab at Havard University. The
    code was initially adapted from Joseph Muth's Python script, titled,
    "Rheology Reader.py"
    
    This code takes input files of ".xls" format.
    
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

# Directory variables
folder_name = 'rheology_data'
study_type = '_Stress Sweep' # include underscore in front of study type

# Excel file variables
file_type = '.xls'
sheet_name = 'Amplitude sweep - 1'
label_row = 1
skip_rows = [0, 2]

# Study variables
materials = ['Fugitive Ink', 'Catalytic Ink', 'PDMS Matrix', 'EcoFlex Matrix']
variables = ['Storage modulus', 'Loss modulus', 'Oscillatin strain rate', 'Oscillation stress', 'Oscillation stress']
ignored_var = ['Tan(delta)', 'Complex viscosity', 'Angular frequency', 'Time'] 

# Create file_names, a list that holds all of the file names with rheology data
current_dir = os.getcwd()
folder_dir = current_dir + '/' + folder_name
file_names = list()
for material in materials:
    file_name = folder_dir + '/' + material + study_type + file_type
    file_names.append(file_name)

# Import all of the Excels whose file names are in file_names
Fugitive_Ink = pd.read_excel(file_names[0], sheet_name, header = label_row, skiprows = skip_rows)
Catalytic_Ink = pd.read_excel(file_names[1], sheet_name, header = label_row, skiprows = skip_rows)
PDMS_Matrix = pd.read_excel(file_names[2], sheet_name, header = label_row, skiprows = skip_rows)
EcoFlex_Matrix = pd.read_excel(file_names[3], sheet_name, header = label_row, skiprows = skip_rows)

# Plot the Fugitive Ink Rheology: storage modulus vs. stress
x = Fugitive_Ink['Oscillation stress']
y = Fugitive_Ink['Storage modulus']
plt.plot(x, y)
 













