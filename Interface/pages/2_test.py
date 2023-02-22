import streamlit as st

# Apllication

st.set_page_config(
    page_title="MedNet",
    page_icon="🖥",
    layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 50px'>Optimisation du modèles</h1>",
            unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: white; margin-bottom: 50px'>Tests effectués</h2>",
    unsafe_allow_html=True)

test = {"Learning rate" : [0.01, 0.01, 0.01, 0.01, 0.01], "maxEpochs" : [20, 20, 20, 20, 20], "t2vRatio" : [1.2, 1.3, 1.3, 1.5, 1.8], "t2vEpochs" : [3, 3, 3, 3, 3], "batchSize" : [300, 300, 400, 1500, 300], "Accuracy" : [99.42, 99.44, 99.49, 98.04, 99.65]}
st.dataframe(test, width=1500)