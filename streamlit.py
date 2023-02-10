import streamlit as st

st.title('CO2 emission per capita predictor app')
st.markdown('A model that can predict the level of co2 emission per capita.')
st.header('CO2 Emission Variables')
col1, col2 = st.columns(2)


# display the front end aspect
# st.markdown(html_temp, unsafe_allow_html = True) 
  
# following lines create boxes in which user can enter data required to make prediction 
with col1:
  Total = st.selectbox('Total', step = 1)
  Coal = st.number_input('Coal', step = 1)
  Gas = st.number_input('Gas', step = 1)
    

with col2:
  Oil = st.number_input('Oil', step = 1)
  Cement = st.number_input('Cement', step = 1)
  Flaring = st.number_input('Flaring', step = 1)
    

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
      st.success('Below 25GT COe Continue reducing your CO2 Production by shifting to a decarbonization pathway')



