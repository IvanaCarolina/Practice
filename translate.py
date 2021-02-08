# install translator
from translate import translator

translator = translator(to_lang='en')

translation = translator.translate('Hi')
