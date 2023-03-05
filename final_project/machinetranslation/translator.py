"""Module That translates languages."""
import os
import json
from ibm_watson import LanguageTranslatorV3,ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
Language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

Language_translator.set_service_url(url)
# Language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """a dummy docstring"""
    french_text = Language_translator.translate(
        text = english_text,model_id = 'en-fr').get_result()
    # fr = str(french)
    # french_text = json.dumps(french, indent=2, ensure_ascii=False)
    
    try:
        return french_text.get("translations")[0].get("translation")
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def french_to_english(french_text):
    """a dummy docstring"""
    english_text = Language_translator.translate(
        text = french_text,model_id = 'fr-en').get_result()
    # english_text = json.dumps(english, indent=2, ensure_ascii=False)
    # return english_text
    
    try:
        return english_text.get("translations")[0].get("translation")
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)