# -*- coding: utf-8 -*-

import pandas as pd

import csv


fileurl="https://raw.githubusercontent.com/Scienzainrete/covid-19/master/heat-map-regioni-casi-eta_per%20100k%20abitanti"

df_completo=pd.read_csv(fileurl)

df_abitanti=pd.read_csv('abitanti.csv')


for regione in df_abitanti.columns.values.tolist()[1:]:
	df_regione = df_completo[(df_completo["regione"]==regione)].reset_index(drop=True)

	df_casi=pd.DataFrame()
	df_casi["regione"] = df_regione["regione"]
	df_casi["età"] = df_regione["età"]
	
	for week in df_completo.columns.values.tolist()[2:]:
		df_casi[week] = (df_abitanti[regione]*df_regione[week].fillna(0)/100000).astype(int)
		
	
	df_casi.to_csv('casi_'+regione+'.csv', encoding='utf-8',  index=False)


