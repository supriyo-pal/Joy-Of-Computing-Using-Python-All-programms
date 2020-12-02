# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:26:21 2020

@author: Supriyo
"""

import gmplot
import csv
gmap= gmplot.GoogleMapPlotter(25.689169, 77.324448, 17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"

gmap.draw("mymap.html")
