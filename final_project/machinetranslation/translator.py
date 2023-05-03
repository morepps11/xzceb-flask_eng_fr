
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Jk04fiD14cRfRIQBHQjOVhAqh9aSoiMN45RfOsiyyD8Z') 
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
     authenticator=authenticator 
     )
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/240d5c4b-06e6-4ec8-a1bf-7bd02e1b6f2c')
      
      
      
def english_to_french(english_text):
    """Translation English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translations']
    return french_text


def  french_to_english(french_text):
    """Translation French to English"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translations']
    return english_text