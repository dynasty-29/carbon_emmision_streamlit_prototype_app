import xgboost as xgb
import streamlit as st
import pandas as pd

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache

st.title('CO2 emission per capita predictor app')
st.markdown('A model that can predict the level of co2 emission per capita.')
st.header('CO2 Emission Variables')
col1, col2 = st.columns(2)


# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
  
# following lines create boxes in which user can enter data required to make prediction 
with col1:
  Total = st.selectbox('Total:', min_value=0.0, max_value=1000000.0, value=1.0)
  Coal = st.number_input('Coal:', min_value=0.0, max_value=1000000.0, value=1.0)
  Gas = st.number_input('Gas:', min_value=0.0, max_value=1000000.0, value=1.0)
    

with col2:
  Oil = st.number_input('Oil:', min_value=0.0, max_value=1000000.0, value=1.0)
  Cement = st.number_input('Cement:', min_value=0.0, max_value=1000000.0, value=1.0)
  Flaring = st.number_input('Flaring:', min_value=0.0, max_value=1000000.0, value=1.0)
    

result =""

import pickle
import streamlit as st
 

# load saved model
with open('carbonemissionmodel.pkl' , 'rb') as f:
    carbonemissionmodel = pickle.load(f)


    

if st.button("CO2 EMISSION PER CAPITA"): 
    result = prediction(Total, Coal, Oil, Gas, Cement, Flaring) 
    if result >= 30:
      st.success('Your predicted CO2 Emission per capita is: {}'.format((result).round(2))) 
      st.success('High CO2 Emission Consider reducing your CO2 Production by shifting to a decarbonization pathway')    
   
    elif result >= 25:
      st.success('Your predicted CO2 Emission per capita is {}'.format((result).round(2)))
      st.success('Moderate CO2 Emission Consider reducing your CO2 Production by shifting to a decarbonization pathway')
    else:
      st.success('Your predicted CO2 Emission per capita is {}'.format((result).round(2)))
      st.success('Below 25GT CO2 Continue reducing your CO2 Production by shifting to a decarbonization pathway')



