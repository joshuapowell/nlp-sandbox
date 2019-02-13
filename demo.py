"""
Natural Language Toolkit.
http://www.nltk.org/

Getting Started:

    ```
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install nltk
    ```

Download the data.

    1. For this demonstration download the `punkt` data from 
    http://www.nltk.org/nltk_data/

    2. Move that data to `/Users/USERNAME/nltk_data/tokenizers`

    3. Next Download the `averaged_perceptron_tagger` data from
    http://www.nltk.org/nltk_data/

    4. Move that data to `/Users/USERNAME/nltk_data/taggers`

    5. Next download the `maxent_ne_chunker` data from
    http://www.nltk.org/nltk_data/

    6. Move that data to `/Users/USERNAME/nltk_data/chunkers`

    7. Next download the `Penn Treebank Sample` data from
    http://www.nltk.org/nltk_data/

    8. Move that data to `/Users/USERNAME/nltk_data/corpora`

Running the script

    ```
    python demo.py
    ```


"""


import nltk

from nltk.corpus import treebank


nltk.data.path.append("/Users/joshuapowell/nltk_data/")

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print("tokens %s" % tokens)

input()

tagged = nltk.pos_tag(tokens)

print("tagged %s" % tagged[0:6])

input()

entities = nltk.chunk.ne_chunk(tagged)

print("entities %s" % entities)

input()

t = treebank.parsed_sents('wsj_0001.mrg')[0]
print("t %s" % t)

input()

t.draw()
