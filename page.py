

import streamlit as st
from new import Jarvis,jarvis_vision
from model import image_model,text_model


page = st.sidebar.radio("Go to", ["Text Model","Image Model"])
if page == "Image Model":
    image_model()
elif page == "Text Model":
    text_model()
    
    


    
    




