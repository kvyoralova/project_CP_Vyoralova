import streamlit as st
import speech_recognition as sr
import os
import streamlit.components.v1 as components

st.title('Pravografia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
st.subheader('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')

st.write("Скажи мені число від 1 до 10. Dimmi un numero da 1 a 10.")

def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # STREAMLIT AUDIO RECORDER Instance
    st_audiorec()
    
if __name__ == '__main__':
    # call main function
    audiorec_demo_app()

