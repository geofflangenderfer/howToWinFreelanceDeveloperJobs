#!/usr/bin/env python3
#from top_emojis.CalculateEmojis import top_emojis.CalculateEmojis.CalculateEmojis
import top_emojis.CalculateEmojis

if __name__ == '__main__':
    test = top_emojis.CalculateEmojis.CalculateEmojis()
    for tweet in test.tweets:
        print(tweet)

