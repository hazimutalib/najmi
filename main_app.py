import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; '>Coalition Prediction </h1>", unsafe_allow_html=True)

df = pd.read_csv('generic_ballot_pollsNEW(1.0).csv')

col3, col1, col5 ,col2, col4 = st.beta_columns((1,3,0.25, 3,1))

state = col1.selectbox('State:', np.sort(df['state'].unique()))
parliament = col2.selectbox('Parliament:', np.sort(df[df['state'] == state ]['parliament'].unique()))

avg_error = df[df['parliament'] == parliament]['error'].mean()




gov_victories1 = 0
gov_victories2 = 0
gov_victories3 = 0
gov_victories4 = 0


if col1.button('Click'):
	for x in range(100000):
		error1 = np.random.normal(scale=avg_error)
		error2 = np.random.normal(scale=avg_error)
		error3 = np.random.normal(scale=avg_error)
		error4 = np.random.normal(scale=avg_error)

		adj_gov1 = df['gov'].mean() + error1
		adj_opp1 = df['opp'].mean() - error1

		adj_gov2 = df['gov'].mean() + error2
		adj_opp2 = df['opp'].mean() - error2

		adj_gov3 = df['gov'].mean() + error3
		adj_opp3 = df['opp'].mean() - error3

		adj_gov4 = df['gov'].mean() + error4
		adj_opp4 = df['opp'].mean() - error4

		if adj_gov1 > adj_opp1:
			gov_victories1 = gov_victories1 + 1

		if adj_gov2 > adj_opp2:
			gov_victories2 = gov_victories2 + 1


		if adj_gov3 > adj_opp3:
			gov_victories3 = gov_victories3 + 1

		if adj_gov4 > adj_opp4:
			gov_victories4 = gov_victories4 + 1

	col1.success("Trial 1: {}".format(gov_victories1 / 100000))
	col2.write('')
	col2.write('')
	col2.success("Trial 2: {}".format(gov_victories2 / 100000))
	col1.success("Trial 3: {}".format(gov_victories3 / 100000))
	col2.success("Trial 4: {}".format(gov_victories4 / 100000))




