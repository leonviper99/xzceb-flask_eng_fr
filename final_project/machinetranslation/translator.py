"""Module That translates languages."""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
Language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

Language_translator.set_service_url(url)

def english_to_french(english_text):
    """a dummy docstring"""
    french = Language_translator.translate(
        text = english_text,model_id = 'en-fr').get_result()
    french_text = json.dumps(french, indent=2, ensure_ascii=False)
    return french_text

def french_to_english(french_text):
    """a dummy docstring"""
    english = Language_translator.translate(
        text = french_text,model_id = 'fr-en').get_result()
    english_text = json.dumps(english, indent=2, ensure_ascii=False)
    return english_text
