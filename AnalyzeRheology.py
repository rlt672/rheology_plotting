# -*- coding: utf-8 -*-
"""

Filename: ImportRheology.py
Author: Ryan L. Truby
Affiliation: Lewis Research Group, Harvard University
Data: 2015.02.08

Description:
    This is the primary file used to analyze rheology data collected on
    the DHR-3 rheometer in Prof. Jennifer Lewis' lab at Havard University. 
    
    This code imports functions from several libraries, including:
        ImportRheology.py
        PlotRheology.py
    
"""

import numpy as np
import os
import matplotlib.pylab as plt
import pandas as pd
import ImportRheology

format = 'xls'
rheo_study = 'Amplitude sweep - 1'
data_folder = "rheology_data"
header = 1
skipped_rows = [0, 2]

files = ImportRheology.import_folder(data_folder, format)
#rheo_data = ImportRheology.compile_data(files, data_folder, rheo_study, header, skipped_rows)
rheo_data = ImportRheology.compile_data_panel(files, data_folder, rheo_study, header, skipped_rows)

print "\n%r" % rheo_data.items
