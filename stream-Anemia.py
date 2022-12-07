import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('anemia_model.sav', 'rb'))

st.title('Prediksi Anemia')



Gender = st.number_input ('Input Nilai Gender')
Hemoglob = st.number_input ('Input Nilai Hemoglob')
MCH = st.number_input ('Input Nilai MCH')
MCHC = st.number_input ('Input Nilai MCHC')
MCV = st.number_input ('Input Nilai MCV')

anemia_diagnosis = ''

if st.button('Test Prediksi') :
    anemia_prediction = model.predict([[Gender, Hemoglob, MCH, MCHC, MCV]])

    if (anemia_prediction[0] == 0):
        anemia_diagnosis = 'Tidak Terkena Anemia'
    else :
        anemia_diagnosis = 'Terkena Anemia'
    
st.success(anemia_diagnosis)
