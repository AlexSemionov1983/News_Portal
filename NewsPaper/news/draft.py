s = ('Редиска — один из самых ярких и бодрящих весенних овощей, который появляется на грядках раньше многих других '
     'культур. Свежая редиска радует насыщенным цветом, хрустящей текстурой и лёгкой остротой, благодаря которой она '
     'подходит и для салатов, и для самостоятельных закусок. Молодая редиска богата витаминами, особенно витамином C, '
     'а также минералами, которые помогают поддерживать иммунитет после зимы. На огороде редиска растёт быстро и '
     'неприхотливо: достаточно мягкой почвы и регулярного полива, чтобы уже через три недели собрать первый урожай. '
     'Многие отмечают, что редиска улучшает аппетит и стимулирует пищеварение, поэтому её часто добавляют в рацион в '
     'начале сезона. Несмотря на простоту, редиска остаётся одним из самых узнаваемых и любимых овощей, придавая '
     'блюдам свежесть и весеннее настроение.')


a = ('The hyacinth macaw (Anodorhynchus hyacinthinus), or hyacinthine macaw, is a parrot native to central and eastern '
     'South America. With a length (from the top of its head to the tip of its long pointed tail) of about one meter '
     'it is longer than any other species of parrot. It is the largest macaw and the largest flying parrot species. '
     '[a] While generally easily recognized, it could be confused with the smaller Lear\')s macaw. Habitat loss and '
     'the trapping of wild birds for the pet trade have taken a heavy toll on their population in the wild, so the '
     'species is classified as Vulnerable on the International Union for Conservation of Nature\'s Red List,[1] and it '
     'is protected by its listing on Appendix I of the Convention on International Trade in Endangered Species of Wild '
     'Fauna and Flora (CITES).')


def censor(txt: str):
    stop_words = ['редис', 'parrot',]
    stop_words.extend([word.title() for word in stop_words])
    for stop_word in stop_words:
        txt = txt.replace(stop_word, stop_word[0] + '*' * (len(stop_word) - 1))
    return txt


print(censor(s))
print(s.find('редис'))

print('редис' in 'редиска')
print('редиска'.replace('редис', '123'))
print(s.replace('редис', 'редис'[0] + '*' * (len('редис') - 1)))
print(censor(a))

print(a)
