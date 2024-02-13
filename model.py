import streamlit as st
from new import jarvis_vision,Jarvis
import PIL


def image_model():
   st.title("RAJPUT VISION")
   st.header("Upload Image From Browse Files")
   image  = st.file_uploader(label="UPLOAD IMAGE")
   st.header("Write Your Question Here")
   input = st.text_input(label="HERE")
   vision_exe = st.button(label="UPLOAD  IMAGE")
   if vision_exe == True:
       response = jarvis_vision(input=input,image=image)
       st.write(response)

def text_model():
   st.title("RAJPUT")
   user_input = st.text_input("Please enter your query here : ")
   button = st.button(label="SEND")
   if button == True:
      response = Jarvis(input_text=user_input)
      st.write(response)

