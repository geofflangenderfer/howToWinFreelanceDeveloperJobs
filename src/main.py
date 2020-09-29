#!/usr/bin/env python3
#from top_emojis.CalculateEmojis import top_emojis.CalculateEmojis.CalculateEmojis
from TwitterSearch import TwitterSearch
from SaveTweets import SaveTweets
from CalculateEmojis import CalculateEmojis
from SaveNumberOfEmojis import SaveNumberOfEmojis

if __name__ == '__main__':
    authors = ['paulg', 'r00k', 'brennandunn', 'dvassallo', 'naval']
    for author in authors:
        search = TwitterSearch(author)
        SaveTweets(search.tweets)

    emojis = CalculateEmojis()
    SaveNumberOfEmojis(emojis)



