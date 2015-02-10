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
import matplotlib
import matplotlib.pylab as plt
import matplotlib.font_manager as font_manager
import pandas as pd

################################################################################
# Define all variables
################################################################################
# Directory variables:
folder_name = 'rheology_data'   # name of folder w/ data, keep in Python folder
study_type = '_Stress Sweep'    # suffix on file name, include underscore 

# Excel file variables:
file_type = '.xls'              # file extension, keep .xls, might work w/ .xlsx
sheet_name = 'Amplitude sweep - 1'  # will change with rheology study type
label_row = 1                   # row w/ study variables, see variables below
skip_rows = [0, 2]              # skip these rows on Excel Files from TRIOS

# Study variables:
materials = ['Fugitive Ink', 'Catalytic Ink', 'PDMS Matrix', 'EcoFlex Matrix']
variables = ['Storage modulus', 'Loss modulus', 'Oscillatin strain rate',
    'Oscillation stress', 'Oscillation stress']
ignored_var = ['Tan(delta)', 'Complex viscosity', 'Angular frequency', 'Time']

# Plot variables:
size_of_font = 14               # this is the base font that should be used
axes_font_factor = 2            # changes axes font relative to size_of_font
legend_font_factor = -2         # changes legned font relative to size_of_font
line_width = 2                  # line width for plots

# Choose the fontpath you want for the plot's font.
# To see what fontpaths are available, uncomment the following code:
'''
for font in font_manager.findSystemFonts():
    print font
'''
# Often, just replace one font for another (eg, try changing Arial with Corbel)
fontpath = '/Library/Fonts/Microsoft/Arial.ttf'
prop = font_manager.FontProperties(fname = fontpath)
matplotlib.rcParams['font.family'] = prop.get_name()
################################################################################
def plot_data(folder_name, materials, study_type, file_type):
    # Create a list that holds all of the file names with rheology data
    current_dir = os.getcwd()
    folder_dir = current_dir + '/' + folder_name
    file_names = list()
    for material in materials:
        file_name = folder_dir + '/' + material + study_type + file_type
        file_names.append(file_name)

    # Import all of the Excels whose file names are in file_names
    Fugitive_Ink = pd.read_excel(file_names[0], sheet_name, header = label_row, 
        skiprows = skip_rows)
    Catalytic_Ink = pd.read_excel(file_names[1], sheet_name, header = label_row, 
        skiprows = skip_rows)
    PDMS_Matrix = pd.read_excel(file_names[2], sheet_name, header = label_row, 
        skiprows = skip_rows)
    EcoFlex_Matrix = pd.read_excel(file_names[3], sheet_name, header = label_row, 
        skiprows = skip_rows)

    # Plot the Fugitive Ink Rheology: storage modulus vs. stress
    x1 = Fugitive_Ink['Oscillation stress']
    y1 = Fugitive_Ink['Storage modulus']
    x2 = Catalytic_Ink['Oscillation stress']
    y2 = Catalytic_Ink['Storage modulus']
    x3 = PDMS_Matrix['Oscillation stress']
    y3 = PDMS_Matrix['Storage modulus']
    x4 = EcoFlex_Matrix['Oscillation stress']
    y4 = EcoFlex_Matrix['Storage modulus']

    Plot1 = plt.figure(figsize=[5.55, 4.75], tight_layout=True)
    plt.axis([1e-1, 1e3, 1e-1, 1e5])
    plt.loglog(x1, y1, '#ed4806', linewidth = line_width)
    plt.loglog(x2, y2, '#ed7e06', linewidth = line_width)
    plt.loglog(x3, y3, '#0a6e95', linewidth = line_width)
    plt.loglog(x4, y4, '#04a35f', linewidth = line_width)
    plt.xlabel('Shear Stress [Pa]', fontsize = size_of_font + axes_font_factor)
    plt.ylabel('G\' [Pa]', fontsize = size_of_font + axes_font_factor)
    # Uncomment for legend:
    '''
    plt.legend(['Fugitive Ink', 'Catalytic Ink', 'PDMS Matrix', 'EcoFlex Matrix'], 
        fontsize = size_of_font + legend_font_factor)
    '''
    plt.show()

plot_data(folder_name, materials, study_type, file_type)












