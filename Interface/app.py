import streamlit as st
from utils import predict_img

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


## third section ##

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 50px'>Upload any images</h1>",
            unsafe_allow_html=True)

container3 = st.container()

with container3:
    uploaded_files = st.file_uploader(
        "", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

    if st.button('Upload'):
        if uploaded_files is not None:
            # Create a list to hold the images
            image_list = []
            image_names = []

            # Loop through the uploaded files and add them to the list
            for uploaded_file in uploaded_files:
                
                image_list.append(uploaded_file)
                image_names.append(uploaded_file.name)

            # Create a grid to display the images
            col1, col2, col3= st.columns(3)

            with col1:
                st.subheader('Images')
                for image in image_list:
                    st.image(image, use_column_width=True)

            with col2:
                st.subheader('Images names')
                st.markdown(f"<h1 style='color: white; margin-top:180px'></h1>",
                            unsafe_allow_html=True)
                for name in image_names:
                    st.markdown(f"<h1 style='color: white; margin-bottom:350px'>{name}</h1>",
                                unsafe_allow_html=True)

            with col3:
                st.subheader('Detected Xray Class')
                st.markdown("<h1 style='color: white; margin-top:180px'></h1>",
                            unsafe_allow_html=True)
                for image in image_list:
                     st.markdown(f"<h1 style='color: white; margin-bottom:350px'>{predict_img(image)}</h1>",
                                unsafe_allow_html=True)


