import tokenize

with open(__file__, 'rb') as myself:
    for token in tokenize.tokenize(myself.readline):
        print(token)
