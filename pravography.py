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
            

#def audioplayer(audio):
#  ipd.display(ipd.Audio(audio, autoplay=True))

def make_it_flash(text):
    for i in reversed(range(2)):
        sys.stdout.write('\r')
        sys.stdout.write(text if i % 2 else ' '*len(text))
        sys.stdout.flush()
        time.sleep(5)

def game(dataset, num, correctness_counter, wrong_words, language):
  image_dict = dataset[num]
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
  make_it_flash(translated_text)
  user_guess = st.text_input("\nА тепер спробуйте самі написати це слово! ")
  tool = language_tool_python.LanguageTool(language)
  matches = tool.check(user_guess)
  if matches == []:
    correctness_counter.append(user_guess)
  else:
    wrong_words.append(translated_text)
    
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
#st.write(address)
import re
regexpr = r'[A-Za-z]+'
actual_location = re.findall(regexpr, address))
country = actual_location[-1]
st.write(country)
