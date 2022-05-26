import streamlit as st
st.title('Pravografia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
st.write('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')

number = st.slider("Scegli un numero da 1 a 10", min_value=1, max_value=10)
random = st.button("Oppure clicca qui per avere 5 immagini casuali")
number = str(number)

chosen_dataset = {'1':[{'1. Arancia.jpeg':'апельсин'},
                       {'1. Bacio.jpeg':'поцілунок'},
                       {'1. Cetriolo.jpeg':'огірок'},
                       {'1. Ciuccio.jpeg':'пустушка'},
                       {'1. Dieci.jpeg':'десять'}]}
#                  '2':['prova', 'cane', 'gatto', 'akj', 'slkdf'],
#                  '3':[],
#                  '4':[],
#                  '5':[],
#                  '6':[],
#                  '7':[],
#                  '8':[],
#                  '9':[],
#                  '10':[]}

import numpy
all_images = list()
for myList in chosen_dataset.values():
  for image_dict in myList:
        all_images.append(image_dict)
print(all_images)
random_dataset = numpy.random.choice(all_images, 5, False)
print(random_dataset)

if number:
  image_dataset = chosen_dataset[number]
elif random:
  image_dataset = random_dataset
else:
  pass

for image_dict in image_dataset:
  for image, text in image_dict.items():
    st.image(image)
    st.write(text)
