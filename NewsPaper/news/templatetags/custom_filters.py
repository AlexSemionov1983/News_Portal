from django import template

register = template.Library()


@register.filter()
def censor(txt: str):
    stop_words = ['редис', 'parrot',]
    stop_words.extend([word.title() for word in stop_words])
    for stop_word in stop_words:
        txt = txt.replace(stop_word, stop_word[0] + '*' * (len(stop_word) - 1))
    return txt
