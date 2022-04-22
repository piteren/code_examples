import nltk

from ptools.textools.tokenization import whitspace_tokenizer


# returns BLEU value
def bleu(
        sen :str,
        ref :list or str,
        ngram=      None,                   # set to 1,2,3,4 to override weights
        weights=    (0.25,0.25,0.25,0.25)):

    if type(ref) is str: ref = [ref]
    reft = []
    for r in ref:
        reft.append(whitspace_tokenizer(r))
    cndt = whitspace_tokenizer(sen)

    if ngram:
        if ngram == 1: weights = (1,  0,    0,   0)
        if ngram == 2: weights = (0.5,0.5,  0,   0)
        if ngram == 3: weights = (0.33,0.33,0.33,0)

    sb = 0
    try: sb = nltk.translate.bleu_score.sentence_bleu(reft, cndt, weights=weights)
    except ValueError: pass

    return sb
