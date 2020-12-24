import numpy as np
import re

def split_ques(question):

    words = re.sub(
        r"([.,'!?\"()*#:;])",
        '',
        question.lower()
    ).replace('-', ' ').replace('/', ' ').split()

    return words

def proc_ques(question, token_to_ix, max_token):
    ques_ix = np.zeros(max_token, np.int64)

    words = split_ques(question)

    for ix, word in enumerate(words):
        if word in token_to_ix:
            ques_ix[ix] = token_to_ix[word]
        else:
            ques_ix[ix] = token_to_ix['UNK']

        if ix + 1 == max_token:
            break

    return ques_ix