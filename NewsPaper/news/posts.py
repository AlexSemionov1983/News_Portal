class PostText:
    def __init__(self, post_title, post_text):
        self.post_title = post_title
        self.post_text = post_text


hya_mac_tit = 'Hyacinth macaw'
hya_mac_txt = ('The hyacinth macaw (Anodorhynchus hyacinthinus), or hyacinthine macaw, is a parrot native to '
               'central and eastern South America. With a length (from the top of its head to the tip of its '
               'long pointed tail) of about one meter it is longer than any other species of parrot. It is the '
               'largest macaw and the largest flying parrot species. [a] While generally easily recognized, it '
               'could be confused with the smaller Lear\'s macaw. Habitat loss and the trapping of wild birds '
               'for the pet trade have taken a heavy toll on their population in the wild, so the species is '
               'classified as Vulnerable on the International Union for Conservation of Nature\'s Red List,[1] '
               'and it is protected by its listing on Appendix I of the Convention on International Trade in '
               'Endangered Species of Wild Fauna and Flora (CITES).')

mcDnews_tit = 'McDonald\'s Just Brought Back One of Its Most Popular Sandwiches Ever'
mcDnews_txt = (' Few seasonal launches at McDonald’s get fans fired up more than the Shamrock Shake’s return '
               'during St. Patrick’s Day. Yes, customers love it when the Holiday Pie and Spicy McNuggets come '
               'back, but those menu items are pretty unpredictable in availability. \n'
               'However, if you thought the Shamrock Shake had a cult following, it’s practically nothing '
               'compared to another menu item: the McRib. In 2020, Mickey D’s brought back its McRib sandwich '
               'nationwide for the first time in eight years. Since then, customers have again fallen for the '
               'saucy rib sandwich—so much so that McDonald’s added it to menus even after the famous '
               '"farewell tour." \n'
               'While McDonald\'s didn\'t discontinue the sandwich after its 2022 farewell tour, it didn’t return '
               'to nationwide menus in 2023, but in 2024 it did. Now, the McRib is officially back on menus—but '
               'there is a slight catch this year. ')

habr_artit = 'PostgreSQL Gains a Built-in UUIDv7 Generation Function for Primary Keys'
habr_artxt = ('In late September 2025, PostgreSQL 18 was released. It received the long-awaited built-in function '
              'uuidv7(). The uuidv7() function generates UUID version 7 (UUIDv7) identifiers of the binary data '
              'type uuid in accordance with the international standard RFC 9562. These identifiers are recommended '
              'for use as primary keys. If necessary, the timestamp with the time zone can be extracted from them '
              'using the uuid_extract_timestamp() function. \n'
              'UUIDv7 combines the global uniqueness of primary keys, a negligibly low probability of collisions '
              '(unacceptable random matches), and ordering by the generation timestamp. This is achieved without '
              'using centralized coordination or MAC addresses. The risk of collisions is no higher than with the '
              'previously most popular (random) UUID version 4 type.')

hyacint_mac = PostText(hya_mac_tit, hya_mac_txt)
mcDona_news = PostText(mcDnews_tit, mcDnews_txt)
habr_article = PostText(habr_artit, habr_artxt)

print(habr_article.post_text)

