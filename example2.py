import nltk

"""Download the PUNKT tokenizer

   :see https://www.nltk.org/data.html
"""
nltk.download('punkt')

"""Example sentence to run tokenization on.
"""
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

"""Tokenization.
"""
tokens = nltk.word_tokenize(sentence)

"""Print to terminal.
"""
print("Tokens: ", tokens)