#!/usr/bin/env python
# coding: utf-8

# # CODIGO DE EJECUCION

# **NOTA.-** Para poder usar este código de ejecución hay que lanzarlo desde exactamente el mismo entorno en el que fue creado.
# 
# Se puede instalar ese entorno en la nueva máquina usando el environment.yml que creamos en el set up del proyecto
# 
# Copiar el proyecto1.yml al directorio y en el terminal o anaconda prompt ejecutar:
# 
# conda env create --file proyecto1.yml --name proyecto1

# In[5]:


import cloudpickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

ruta_proyecto = 'C:/Users/pelop/OneDrive/Desktop/Curso Data Science Pedro/2 CURSO DATA SCIENCE/03_MACHINE_LEARNING/07_CASOS/01_LEADSCORING'

nombre_fichero_datos = 'validacion.csv'
# Este sería el nuevo fichero que tenemos tras llevar el código en producción un tiempo
# (normalmente 1 mes). Nosotros lo separamos al principio en el segundo notebook porque
# no tenemos acceso a nuevos datos, pero la validación final se haría una vez puesto el
# modelo en marcha y en producción al menos 1 mes después. La métrica de AUC, MAE, ...
# para testar el modelo se hizo sobre la división de train-test con validación cruzada.

ruta_completa = ruta_proyecto + '/02_Datos/02_Validacion/' + nombre_fichero_datos
df = pd.read_csv(ruta_completa,index_col='id')

df.drop_duplicates(inplace = True)
df = df.loc[(df.no_llamar != 'OTROS') & (df.no_enviar_email != 'Yes') & (df.ult_actividad != 'Email Bounced')]
                     
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

nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'
ruta_pipe_ejecucion = ruta_proyecto + '/04_Modelos/' + nombre_pipe_ejecucion
with open(ruta_pipe_ejecucion, mode='rb') as file:
   pipe_ejecucion = cloudpickle.load(file)

scoring = pipe_ejecucion.predict_proba(df)[:, 1]

nombre_disc_threshold = 'optimal_disc_threshold.pickle'
ruta_disc_threshold = ruta_proyecto + '/04_Modelos/' + nombre_disc_threshold
with open(ruta_disc_threshold, mode='rb') as file:
   disc_threshold = cloudpickle.load(file)

scoring_roi = np.where(scoring > disc_threshold,1,0)


# In[6]:


scoring_roi

