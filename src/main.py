#!/usr/bin/env python3
from TwitterSearch import TwitterSearch
from SaveTweets import SaveTweets

def main():
    authors = ['paulg', 'naval', 'r00k', 'patio11']#'brennandunn',
    for author in authors:
        search = TwitterSearch(author)
        SaveTweets(search.tweets)

if __name__ == '__main__':
    main()
