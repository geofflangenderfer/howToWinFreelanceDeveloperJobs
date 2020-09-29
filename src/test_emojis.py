#!/usr/bin/env python3
import re


def remove_emojis(sample):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', sample)

def get_number_emojis(text):
    return len(text) - len(remove_emojis(text))

if __name__ == '__main__':
    text = u'This dog \U0001f602'
    print(f"There are {get_number_emojis(text)} emojis in {text}")


