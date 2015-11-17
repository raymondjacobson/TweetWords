AMT_OF_WORD_TOKENS = 20000
OUTPUT_FILE = 'output.txt'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXX'

from TwitterSearch import *
try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['Paris'])
    tso.set_language('en')
    tso.set_include_entities(False)

    ts = TwitterSearch(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )

    data = ""
    total_words = 0
    for tweet in ts.search_tweets_iterable(tso):
        total_words += len(tweet['text'].split(' '))
        data += (tweet['text'] + "\n\n")
        if total_words >= AMT_OF_WORD_TOKENS:
            break

    with open(OUTPUT_FILE, 'w') as of:
        of.write(data.encode('utf8'))

except TwitterSearchException as e:
    print(e)
