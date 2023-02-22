import streamlit as st


st.set_page_config(
    page_title="MedNet/Code",
    page_icon="⌨️",
    layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



with st.container():
    
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 80px;'>Fonctions utilisées</h1>",
                unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: left; color: white; margin-bottom: 50px; font-size: 1.2rem'>La fonction ci-dessous à pour but de prendre une image en paramètre pour prédire une des classe suivantes : 'AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT' </p>",
                unsafe_allow_html=True)

    st.code('''def predict_img(img):
        img = Image.open(img)
        
        #Transform to gray (1 channel)
        img = ImageOps.grayscale(img)
        
        #Resize the img
        size = 64, 64
        img = img.resize(size)
        
        #Convert to a matrix 
        toTensor = tv.transforms.ToTensor()
        img = toTensor(img)
        img.shape
        
        #Reshape for the model
        img = img.reshape([1,1,64,64])
        img=scaleImage(img) 
        classname = ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']
        yOut = model(img)
        max_value, max_index = yOut.max(1)
        pred = classname[max_index.item()]
        return pred, max_index.item()'''
        )
    
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 80px; margin-top: 80px;'>Application</h1>",
                unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: left; color: white; margin-bottom: 50px'>Configuration</h2>",
                unsafe_allow_html=True)
    
    st.code('''
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
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)''')
    
    st.markdown("<h2 style='text-align: left; color: white; margin-bottom: 50px; margin-top: 50px'>Upload image</h2>",
                unsafe_allow_html=True)
    
    
    st.code('''uploaded_files = st.file_uploader(
        "", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])''')
    