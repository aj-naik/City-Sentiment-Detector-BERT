import requests

class Translator:
    
    def __init__(self, api_key: str):
        self.api_key = api_key

class GoogleTranslate(Translator):

    api_endpoint = 'https://translation.googleapis.com/language/translate/v2'

    def __init__(self, api_key: str):
        Translator.__init__(self, api_key=api_key)

    def detect_language(self, input_text) -> str:
        request = requests.post(f'{self.api_endpoint}/detect', data={'q': input_text, 'key': self.api_key})
        data = request.json()
        language = data.get('data').get('detections')[0][0].get('language')

        return language


    def translate(self, input_text: str, target_lang: str, source_lang: str = "") -> str:
        request = requests.post(f'{self.api_endpoint}',
                                data={'q': input_text, 'source': source_lang,
                                      'target': target_lang, 'format': 'text',
                                      'key': self.api_key})
        data = request.json()
        translations = data.get('data').get('translations')
        text = translations[0].get('translatedText')

        return text
