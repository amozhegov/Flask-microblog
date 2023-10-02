import json
import requests
from flask_babel import _
from app import app

def translate(text, source_lang, dest_lang):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
    not app.config ['MS_TRANSLATOR_KEY']:
        return _('The translation has gone wrong!')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'westeurope'}
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_lang, dest_lang), headers = auth, json = [{'Text': text}])
    if r.status_code != 200:
        return _('The translation has gone wrong!')
    return r.json()[0]['translations'][0]['text']