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

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 50px'>Brief Mednist</h1>",
             unsafe_allow_html=True)

container1 = st.container()

with container1:
    st.markdown("<p style='text-align: left; color: white; margin-bottom: 150px; font-size: 1.5rem;'>L’objectif étant de prouver les compétences techniques de notre start-up et de faire adhérer le corps médical au projet DATA Health HUB. Dans un souci d’accessibilité aux données, le POC se fera avec les données publiques du dataset MedNist. Nous partons d’une application existante développée par les équipes du CHRU, un algorithme développé via Pytorch qui propose déjà de beaux résultat</p>",
            unsafe_allow_html=True)
    