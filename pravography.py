import streamlit as st
st.title('Pravografia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
st.write('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')

number = st.slider("Scegli un numero da 1 a 10", min_value=1, max_value=10)
random = st.button("Oppure clicca qui per avere 5 immagini casuali")
st.write(type(number))

#chosen_dataset = {'1':['nomi immagini con 1.'],
#                  '2':[],
#                  '3':[],
#                  '4':[],
#                  '5':[],
#                  '6':[],
#                  '7':[],
#                  '8':[],
#                  '9':[],
#                  '10':[]}
#random_dataset = unire tutte le liste dei values di chosen_dataset e scegliere 5 elementi casuali
