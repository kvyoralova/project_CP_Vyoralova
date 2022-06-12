import streamlit as st
from gtts import gTTS
import IPython.display as ipd 
from googletrans import Translator
import time
import sys
import language_tool_python
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import leafmap.foliumap as leafmap
import geopy
from geopy.geocoders import Nominatim


def geo():
    loc_button = Button(label="Отримати місцезнаходження пристрою", max_width=250)
    loc_button.js_on_event(
        "button_click",
        CustomJS(
            code="""
        navigator.geolocation.getCurrentPosition(
            (loc) => {
                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
            }
        )
        """
        ),
    )
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0,
    )
    if result:
        if "GET_LOCATION" in result:
            loc = result.get("GET_LOCATION")
            lat = loc.get("lat")
            lon = loc.get("lon")
            #st.write(f"Lat, Lon: {lat}, {lon}")
            latlon = str(lat) + ", " + str(lon)
            geoLoc = Nominatim(user_agent="GetLoc")
            locname = geoLoc.reverse(latlon)
            address = locname.address
            return address
            

def disappear(text):
    placeholder = st.empty()
    placeholder.text(text)
    time.sleep(7)
    placeholder.empty()

def game(dataset, num, correctness_counter, wrong_words, language):
  image_dict = dataset
  for image, text in image_dict.items():
    st.image(image)
    st.write(text)
  translator = Translator()
  lang = translator.translate(text, src="uk", dest=language) 
  translated_text = lang.text
  import re
  regexpr = r'[A-Za-z]+'
  correct_trans_words = re.findall(regexpr, image.lower())
  correct_translation = correct_trans_words[0]
  if language != 'it':
    eng = translator.translate(correct_translation, src="it", dest=language)
    correct_translation = eng.text
  else:
    pass
  if translated_text != correct_translation:
    translated_text = correct_translation
  else:
    pass
  tts=gTTS(text=translated_text, lang=language)
  tts.save('audio.mp3')
  st.write('Вимова цього слова: ')
  st.audio('audio.mp3')
  st.write("Тепер ви побачите, як пишеться це слово. Спробуй це запам’ятати! ")
  disappear(translated_text)
  user_guess = st.text_input("\nА тепер спробуйте самі написати це слово! ", value="", key=num+1)
  tool = language_tool_python.LanguageTool(language)
  matches = tool.check(user_guess)
  if matches == []:
    correctness_counter.append(user_guess)
  else:
    wrong_words.append(translated_text)
  st.empty(user_guess)
    
def final_message(percentuale, language):
  if percentuale > 60:
    message='хороша робота!'
    tts_uk=gTTS(text=message, lang='uk')
    tts_uk.save('audio_uk.mp3')
    st.audio('audio_uk.mp3')
    translator = Translator()
    tran_lang = translator.translate(text, src="uk", dest=language) 
    tran_message = tran_lang.text
    tts_lan=gTTS(text=tran_message, lang=language)
    tts_lan.save('audio_lan.mp3')
    st.audio('audio_lan.mp3')
    st.image('smile.png')
  else:
    message='спробуйте ще раз!'
    tts_uk=gTTS(text=message, lang='uk')
    tts_uk.save('audio_uk.mp3')
    st.audio('audio_uk.mp3')
    translator = Translator()
    tran_lang = translator.translate(text, src="uk", dest=language) 
    tran_message = tran_lang.text
    tts_lan=gTTS(text=tran_message, lang=language)
    tts_lan.save('audio_lan.mp3')
    st.audio('audio_lan.mp3')
    st.image('forza.jpeg')

st.caption("Натисніть кнопку, щоб отримати своє місцезнаходження та почати гру.")
st.caption("Press the button to get your location and start the game.")
st.caption("Premi il pulsante per ottenere la tua posizione e iniziare il gioco.")

address = geo()
import re
regexpr = r'[A-Za-z]+'
actual_location = re.findall(regexpr, address)
country = actual_location[-1]
if country == "Italia":
    language = "it"
    st.caption("Ви перебуваєте в Італії, тому програма працюватиме італійською мовою.")
    st.caption("Sei in Italia, quindi l'app verrà eseguita in italiano.")
else:
    language =  "en"
    st.caption("Ви перебуваєте за межами Італії, тому програма працюватиме англійською мовою.")
    st.caption("You are out of Italy, so the app will run in English.")
if language == 'it':
    st.title('Правоgrafia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
    st.header('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')
    st.caption("Ця програма орієнтована на українських дітей, які мають труднощі з основними італійськими орфографічними перешкодами.")
    st.caption("Questa applicazione è rivolta a bambini ucraini che hanno difficoltà con i principali ostacoli ortografici italiani.")
  
    st.subheader("Давай грати! Giochiamo!")
    number = st.text_input("Дай мені число від 1 до 10. Dammi un numero da 1 a 10. ", value="")
    st.write("Або натисніть тут, щоб отримати 5 випадкових зображень. Oppure clicca qui per avere 5 immagini casuali.")
    random = st.button("Tут. Qui.")
else:
    st.title('Правоgraphy: навчись добре писати англійською! Learn to write correctly in English!')
    st.header('Грайте, пишіть і вчіться! Play, write and learn!')
    st.caption("Це програма орієнтована на українських дітей, які мають труднощі з основними італійськими орфографічними перешкодами. В англійській версії орфографічні перешкоди не згруповані, як в італійській, а повідомляються у випадковому порядку; однак він залишається програмою, з якою користувач може практикувати.")
    st.caption("This application is aimed at Ukrainian children who have difficulty with the main Italian spelling obstacles. In the English version the spelling obstacles are not grouped as in Italian, but are reported in random order; however, it remains an application with which the user can practice.")
  
    st.subheader("Давай грати! Let's play!")
    number = st.text_input("Дай мені число від 1 до 10. Give me a number from 1 to 10. ", value="")
    st.write("Або натисніть тут, щоб отримати 5 випадкових зображень. Or click here to get 5 random images.")
    random = st.button("Tут. Here.")

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
random_dataset = numpy.random.choice(all_images, 5, False)

if number != ' ':
  image_dataset = chosen_dataset[number]
elif random:
  image_dataset = random_dataset
else:
  pass

correctness_counter = []
wrong_words = []

game(image_dataset[0], 0, correctness_counter, wrong_words, language)
game(image_dataset[1], 1, correctness_counter, wrong_words, language)
game(image_dataset[2], 2, correctness_counter, wrong_words, language)
game(image_dataset[3], 3, correctness_counter, wrong_words, language)
game(image_dataset[4], 4, correctness_counter, wrong_words, language)

if language == 'it':
  st.write('Ви правильно отримали', len(correctness_counter), 'з', len(image_dataset), 'слів!')
  st.write('Hai fatto giuste', len(correctness_counter), 'parole su ', len(image_dataset))
  if wrong_words != []:
    st.write("Це слова, які ви помилилися. Queste sono le parole che hai sbagliato.")
    for el in wrong_words:
      st.write(el)
else:
  st.write('Ви правильно отримали', len(correctness_counter), 'з', len(image_dataset), 'слів!')
  st.write('You got', len(correctness_counter), 'correct words out of', len(image_dataset), "1")
  if wrong_words != []:
    st.write("Це слова, які ви помилилися. Queste sono le parole che hai sbagliato.")
    for el in wrong_words:
      st.write(el)
    
percentuale = 100 * float(len(correctness_counter))/float(len(image_dataset))
final_message(percentuale, language)

