#!/usr/bin/env python
# coding: utf-8

# # 11. CODIGO DE RE-ENTRENAMIENTO

# **NOTA.-** Para poder usar este código de entrenamiento hay que lanzarlo desde exactamente el mismo entorno en el que fue creado.
# 
# Se puede instalar ese entorno en la nueva máquina usando el environment.yml que creamos en el set up del proyecto
# 
# Copiar el proyecto1.yml al directorio y en el terminal o anaconda prompt ejecutar:
# 
# conda env create --file proyecto1.yml --name proyecto1

# In[3]:


# IMPORTACIÓN DE PAQUETES

import numpy as np
import pandas as pd
import cloudpickle

#Automcompletar rápido
get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')

import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

# CÓDIGO DE RE-ENTRENAMIENTO

ruta_proyecto = 'C:/Users/pelop/OneDrive/Desktop/Curso Data Science Pedro/2 CURSO DATA SCIENCE/03_MACHINE_LEARNING/07_CASOS/01_LEADSCORING'

nombre_fichero_datos = 'Leads.csv'
ruta_completa = ruta_proyecto + '/02_Datos/01_Originales/' + nombre_fichero_datos
df = pd.read_csv(ruta_completa,index_col='id',sep=';')

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
target = 'compra'

x = df[variables_finales].copy()
y = df[target].copy()

nombre_pipe_entrenamiento = 'pipe_entrenamiento.pickle'
ruta_pipe_entrenamiento = ruta_proyecto + '/04_Modelos/' + nombre_pipe_entrenamiento
with open(ruta_pipe_entrenamiento, mode='rb') as file:
   pipe_entrenamiento = cloudpickle.load(file)

pipe_ejecucion = pipe_entrenamiento.fit(x,y)
nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'
ruta_pipe_ejecucion = ruta_proyecto + '/04_Modelos/' + nombre_pipe_ejecucion
with open(ruta_pipe_ejecucion, mode='wb') as file:
   cloudpickle.dump(pipe_ejecucion, file)


from sklearn.metrics import confusion_matrix
def max_roi(real,scoring):  
    #DEFINIMOS LA MATRIZ DE IMPACTO
    ITN = 0
    IFP = -5
    IFN = -49.99
    ITP = 44.99    
    
#DEFINIMOS LA FUNCION DEL VALOR ESPERADO
    def valor_esperado(matriz_conf):
        TN, FP, FN, TP = conf.ravel()
        VE = (TN * ITN) + (FP * IFP) + (FN * IFN) + (TP * ITP)
        return(VE)      
        
    #CREAMOS UNA LISTA PARA EL VALOR ESPERADO
    ve_list = []   
    
    #ITERAMOS CADA PUNTO DE CORTE Y RECOGEMOS SU VE
    for umbral in np.arange(0,1,0.01):
        predicho = np.where(scoring > umbral,1,0) 
        conf = confusion_matrix(real,predicho)
        ve_temp = valor_esperado(conf)
        ve_list.append(tuple([umbral,ve_temp]))
        
    #DEVUELVE EL RESULTADO
    df_temp = pd.DataFrame(ve_list, columns = ['umbral', 'valor_esperado'])
    for umbral in np.arange(0,1,0.01):
        predicho = np.where(scoring > umbral,1,0) 
        conf = confusion_matrix(real,predicho)
        ve_temp = valor_esperado(conf)
        ve_list.append(tuple([umbral,ve_temp]))  
        
    return(df_temp.iloc[df_temp.valor_esperado.idxmax(),0])
scoring = pipe_ejecucion.predict_proba(df)[:, 1]
disc_threshold = max_roi(y,scoring)
    
nombre_disc_threshold = 'optimal_disc_threshold.pickle'
ruta_disc_threshold = ruta_proyecto + '/04_Modelos/' + nombre_disc_threshold
with open(ruta_disc_threshold, mode='wb') as file:
    cloudpickle.dump(disc_threshold, file)

