import joblib
import streamlit as st 

model=joblib.load('model_logistic.pkl')


st.title('Diabetes Prediction')

st.write('My first streamlit ML project')

Pregnancies =st.number_input('Pregnancies',min_value=0)
Glucose=st.number_input('Glucose',min_value=0)
BloodPressure=st.number_input('BP',min_value=0)
SkinThickness=st.number_input('Sk',min_value=0)
Insulin=st.number_input('Insulin',min_value=0)
BMI=st.number_input('BMI',min_value=0.0)
DiabetesPedigreeFunction =st.number_input('DP',min_value=0.0)
Age=st.number_input('Age',min_value=0)


if st.button('Prediction'):
    input_list=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
    

    final_prediction=model.predict(input_list)

    if final_prediction[0]==1:
        st.error('person having Diabetes')
    else:
        st.success('No Diabetes')

