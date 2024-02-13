import streamlit as st
import tensorflow as tf

import pandas as pd
import numpy as np

model = tf.keras.models.load_model('marks_predictor_v2.h5')

def predict(hrs_std, prev_scr, ex_ac, sleep, qp):
    test = pd.DataFrame({'Hours Studied': [hrs_std], 'Previous Scores': [prev_scr], 'Extracurricular Activities': [ex_ac], 'Sleep Hours': [sleep], 'Sample Question Papers Practiced': [qp]})
    test_dict = {name: np.array(value) for name, value in test.items()}
    return model.predict(test_dict)[0][0]


st.title('Student Performance Predictor')
html_temp = """
            <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Student Performance Predictor</h2>
            </div>
            """
            
st.markdown(html_temp,unsafe_allow_html=True)

hrs_std = float(st.text_input("Hours Studied", "4"))
# Run predict as soon as enter is pressed

prev_scr = float(st.text_input("Previous Scores", "98"))
ex_ac = st.text_input("Extracurricular Activities (Yes or No)", "Yes")
sleep = float(st.text_input("Sleep Hours", "6"))
qp = float(st.text_input("Sample Question Papers Practiced", "7"))

result = ""

if st.button("Predict"):
    result = predict(hrs_std, prev_scr, ex_ac, sleep, qp)
    
st.success(f'The Predicted Score is: {round(result) if result else ""}')
