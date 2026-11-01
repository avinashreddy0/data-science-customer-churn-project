import pandas as pd
import numpy as np
import joblib
import streamlit as st


#loading data set

model = joblib.load(
    r'C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\customer_churn.pkl'
)

gender_encoder = joblib.load('gender.pkl')
city_encoder = joblib.load('city.pkl')
scaler = joblib.load('scaking.pkl')


#app heading with icon and 
st.set_page_config(
    'customer_churn_app',
    page_icon='🛃',
    layout='centered'
)

#heading
st.header('🛃:rainbow[welcome to customer_churn_app......]')
st.markdown('this app can predict weather customer is **:red[leavu] or :green[stay]** ')

with st.sidebar:
    st.header('**:green[DEVELOP BY❤️]**')
    st.divider()
    st.markdown('**Name:** :rainbow[INDURI AVINASH REDDY]')
    st.markdown('**email**:induriavinashreddy05@gmail.com')
    st.markdown('**phone number**:9346739650')
    st.markdown('**linkedin:**[Avinash Reddy](https://www.linkedin.com)')
    st.markdown('**GitHub**[https://github.com]')
    st.snow()
    df =  pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\govinda\clean.csv')
    




    st.divider()
    st.markdown('**:blue[DATA SCIENCE AND MACHINE LEARNING PROJECT]**')

st.divider()
#user input
#age,gender,city,total_orders,total_revenue,days_since_last_order,churn
col1,col2 = st.columns(2)
with col1:
    age=st.number_input(':red[age]',min_value=10,max_value=90)
    gender = st.selectbox(':red[gender]',['Male','Female'])
    citys = st.selectbox(':red[city]',['Mumbai','Benguluar','Hyderbad','Delhi','Chennai','Blr'])
with col2:
    total_orders = st.number_input(':red[total_orders]',min_value=1,max_value=100)
    total_revenues = st.number_input(':red[total_revenue]',min_value=1,max_value=1000000)
    last_orders_date = st.number_input(':red[days_since_last_order]',min_value=1,max_value=365)


#button
st.divider()
with st.form("prediction"):
      sumit = st.form_submit_button(':rainbow[predict]')
if sumit:
    gender = gender_encoder.transform([[gender]])[0][0]
    city = city_encoder.transform([[citys]])[0][0]
    input_data = np.array([[age,gender,city,total_orders,total_revenues,last_orders_date]])
    input_scaler = scaler.transform(input_data)
    prediction = model.predict(input_scaler)[0]
    prediction_prob = model.predict_proba(input_scaler)[0][1]



    if prediction == 1:
        st.error('this customer is likly **LEAVU**')
        st.progress(int(prediction_prob*100))
        st.balloons()
    else:
        st.success('this customer were **STAY**')
        st.progress(int(1-prediction_prob*100))
        st.snow()

st.caption('❤️ this streamlit app is made by data science and machine learing')
