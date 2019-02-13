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

Running the script

    ```
    python demo.py
    ```


"""


import nltk

nltk.data.path.append("/Users/joshuapowell/nltk_data/")

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print("tokens %s" % tokens)
