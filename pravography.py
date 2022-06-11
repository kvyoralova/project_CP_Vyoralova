import streamlit as st
from gtts import gTTS
import IPython.display as ipd 
from googletrans import Translator
import time
import sys
import language_tool_python

def audioplayer(audio):
  ipd.display(ipd.Audio(audio, autoplay=True))

def make_it_flash(text):
    for i in reversed(range(2)):
        sys.stdout.write('\r')
        sys.stdout.write(text if i % 2 else ' '*len(text))
        sys.stdout.flush()
        time.sleep(5)


st.title('Правоgrafia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
st.subheader('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')

#st.write()
number = st.text_input("Скажи мені число від 1 до 10. Dimmi un numero da 1 a 10.", value="")
#audio input from microphone in ukrainian
#https://developers.deepgram.com/documentation/getting-started/streaming/ 

random = st.button("Або натисніть тут, щоб отримати 5 випадкових зображень. Oppure clicca qui per avere 5 immagini casuali.")

chosen_dataset = {'1':[{'1. Arancia.jpeg':'апельсин'},
                       {'1. Bacio.jpeg':'поцілунок'},
                       {'1. Cetriolo.jpeg':'огірок'},
                       {'1. Ciuccio.jpeg':'пустушка'},
                       {'1. Dieci.jpeg':'десять'}],
                  '2':[{'2. Banco.png':'парта'},
                       {'2. Carota.jpeg':'морква'},
                       {'2. Chiave.jpeg':'ключ'},
                       {'2. Cucina.jpeg':'кухня'},
                       {'2. Maschera.jpeg':'маска'}],
                  '3':[{'3. Aquilone.jpg':'змій'},
                       {'3. Cinque.png':"п'ять"},
                       {'3. Cuore.jpeg':'серце'},
                       {'3. Curva.jpeg':'поворот'},
                       {'3. Quaderno.jpeg':'зошит'}],
                  '4':[{'4. Ciliegia.jpeg':'вишня'},
                       {'4. Gelato.jpeg':'морозиво'},
                       {'4. Giornale.jpeg':'газета'},
                       {'4. Giraffa.jpeg':'жираф'},
                       {'4. Giugno.jpeg':'червень'}],
                  '5':[{'5. Fragola.jpeg':'полуниця'},
                       {'5. Funghi.jpeg':'гриби'},
                       {'5. Gallina.jpeg':'курка'},
                       {'5. Gufo.jpeg':'сова'},
                       {'5. Margherita.jpeg':'ромашка'}],
                  '6':[{'6. Gnomo.jpeg':'гном'},
                       {'6. Lavagna.jpeg':'дошка'},
                       {'6. Montagna.jpeg':'гора'},
                       {'6. Ragni.jpeg':'павуки'},
                       {'6. Spugne.jpeg':'губки'}],
                  '7':[{'7. Casa.png':'дім'},
                       {'7. Musica.jpeg':'музика'},
                       {'7. Persona.png':'особа'},
                       {'7. Seme.jpeg':'насіння'},
                       {'7. Susina.jpeg':'слива'}],
                  '8':[{'8. Calzino.jpeg':'носок'},
                       {'8. Zaino.png':'рюкзак'},
                       {'8. Zero.jpeg':'нуль'},
                       {'8. Zoo.jpg':'зоопарк'},
                       {'8. Zucca.jpeg':'гарбуз'}],
                  '9':[{'9. Biscotti.jpeg':'печиво'},
                       {'9. Cacca.jpeg':'какашка'},
                       {'9. Cavallo.jpeg':'кінь'},
                       {'9. Palla.jpeg':"м'яч"},
                       {'9. Penna.jpeg':'ручка'}],
                  '10':[{'10. Guscio.jpeg':'шкаралупа'},
                       {'10. Pesce.jpeg':'риба'},
                       {'10. Prosciutto.jpg':'шинка'},
                       {'10. Sciarpa.jpeg':'шарф'},
                       {'10. Scivolo.jpeg':'гірка'}]}

import numpy
all_images = list()
for myList in chosen_dataset.values():
  for image_dict in myList:
        all_images.append(image_dict)
print(all_images)
random_dataset = numpy.random.choice(all_images, 5, False)
print(random_dataset)

if number != ' ':
  image_dataset = chosen_dataset[number]
elif random:
  image_dataset = random_dataset
else:
  pass

for image_dict in image_dataset:
  for image, text in image_dict.items():
    st.image(image)
    #st.write('Як ви говорите те, що бачите українською? Come si dice in ucraino la cosa che vedi?')
    st.write(text)
    translator = Translator()
    lang = translator.translate("Пойдём в парк", src="uk", dest="it") 
    translated_text = lang.text
    text_to_speech = input("Give me some text you want me to read for you: ")
    tts=gTTS(text=translated_text, lang=it)
    tts.save('audio.mp3')
    print('Італійською ми говоримо так:')
    audioplayer('audio.mp3')
    
