import requests


def translate_it(source_news, result_news, lang_in, lang_out):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    lang = lang_in + '-' + lang_out

    print('новость из ', lang_in, ':')
    with open(source_news) as news:
        text = news.read()

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    text = ' '.join( response.get('text', []))

    with open(result_news, 'w') as news_trans:
        news_trans.write(text)

    return text

#  коды языков:
#  es - испанский
#  de - немецкий
#  fr - французкий

# почему-то ошибка вылетает на  переводе с Испанского языка ?!
a = translate_it('ES.txt', 'ES_RU.txt', 'es', 'ru')
print(a)

a = translate_it('FR.txt', 'FR_RU.txt', 'fr', 'ru')
print(a)

a = translate_it('DE.txt', 'DE_RU.txt', 'de', 'ru')
print(a)
