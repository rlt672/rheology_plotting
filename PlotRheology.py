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



