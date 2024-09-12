#!/usr/bin/env python
# coding: utf-8

# CODIGO DE EJECUCION

#1.LIBRERIAS
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def ejecutar_modelo(df):

   #2.CALIDAD DE VARIABLES

   if (df.llamar.iloc[0] == 'No') and (df.enviar_email.iloc[0] == 'No'):
      scoring = 0
      scoring_roi = 0

   else:                
      variables_finales = ['ambito',
                           'descarga_lm',
                           'fuente',
                           'ocupacion',
                           'paginas_vistas_visita',
                           'score_actividad',
                           'score_perfil',
                           'tiempo_en_site_total',
                           'ult_actividad',
                           'visitas_total']                     
                     
      df = df[variables_finales]

      #3.CARGA PIPES DE EJECUCION

      with open('03_Notebooks/03_Sistema/app_leadscoring/pipe_ejecucion.pickle', mode='rb') as file:
         pipe_ejecucion = pickle.load(file)

      #4.EJECUCION

      scoring = pipe_ejecucion.predict_proba(df)[:, 1]

      with open('03_Notebooks/03_Sistema/app_leadscoring/optimal_disc_threshold.pickle', mode='rb') as file:
         disc_threshold = pickle.load(file)

      scoring_roi = np.where(scoring > disc_threshold,1,0)

   return [scoring, scoring_roi]




