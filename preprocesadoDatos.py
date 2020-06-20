# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Plantilla de Pre Procesado

#Como instalar las librerias

import numpy as np              #LIBRERIA para el TRATAMIENTO DE NUMEROS, MATEMATICAS y demas
import matplotlib.pyplot as plt #SUB-LIBRERIA enfocada a la REPRESENTACION GRAFICA
import pandas as pd             #LIBRERIA para carga y manipular de DATOS

#importar el data set
dataset = pd.read_csv('datasets/Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
