from PIL import Image
import streamlit as st

def start_home():
    st.write("DOA Analytics & Prediction System")
    st.write("-Present and Future through one click-")
    st.write("This is a Business Intelligence System which is able to show you data in the present and in the future to provide insights to make decisions!")
    image = Image.open(r'C:\Users\dell\Desktop\Projetos\python_bi\python_by_streamlit\folders\home\img.jpg')
    st.image(image, caption='')
    
      