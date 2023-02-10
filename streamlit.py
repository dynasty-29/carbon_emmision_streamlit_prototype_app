import streamlit as st

st.title('CO2 emission per capita predictor app')
st.markdown('A model that can predict the level of co2 emission per capita.')
st.header('CO2 Emission Variables')
col1, col2 = st.columns(2)


# display the front end aspect
# st.markdown(html_temp, unsafe_allow_html = True) 
  
# following lines create boxes in which user can enter data required to make prediction 
with col1:
   Total = st.selectbox('Total', min_value = 0, step = 1, max_value = 1000000)
   Coal = st.number_input('Coal', min_value = 0, step = 1, max_value = 1000000)
   Gas = st.number_input('Gas', min_value = 0, step = 1, max_value = 1000000)
    

with col2:
    Oil = st.number_input('Oil', min_value = 0, step = 1, max_value = 1000000)
    Cement = st.number_input('Cement', min_value = 0, step = 1, max_value = 1000000)
    Flaring = st.number_input('Flaring', min_value = 0, step = 1, max_value = 1000000)
    

result =""

import pickle
import streamlit as st
 

# load saved model
with open('carbonemissionmodel.pkl' , 'rb') as f:
    classifier = pickle.load(f)


    

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
      st.success('Below 25GT COe Continue reducing your CO2 Production by shifting to a decarbonization pathway')import streamlit as st


st.title('CO2 PER CAPITA Prediction ML App')
st.markdown('A model that can predict the level of CO2 EMISSION PER CAPITA .')
st.header('CO2 Emission Variables')
col1, col2 = st.columns(2)


# display the front end aspect
# st.markdown(html_temp, unsafe_allow_html = True) 
  
# following lines create boxes in which user can enter data required to make prediction 
with col1:
    department = st.selectbox('Department',('sewing','finishing'))
    quarter = st.number_input('Month Quarter', min_value = 1, step = 1, max_value = 4)
    team = st.number_input('Team Number', min_value = 1, step = 1, max_value = 12)
    targeted_productivity = st.number_input('Targeted Productivity', min_value = 0.00,  max_value = 10.00, step = 0.01)
    std_minute_value = st.number_input('Standard Minute Value', min_value = 0.00, step = 0.01)

with col2:
    work_in_progress = st.number_input('Work In Progress', min_value = 0.00, step = 0.01)
    over_time = st.number_input('Over Time', min_value = 0, step = 1)
    incentive = st.number_input('Incentive', min_value = 0.00, step = 0.01)
    idle_men = st.number_input('Idle Men', min_value = 0, step = 1)
    no_of_workers = st.number_input('Number of Workers', min_value = 0, step = 1)

result =""


