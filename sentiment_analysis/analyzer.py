#!/usr/bin/python
# Script to train classifier on training data, and classify the test data into corresponding sentiment class.

# find p(word|sentiment) and p(sentiment)
# as a result, find p(sentiment|word) for all words in training data
import nltk

index = 0 
s_count = [0, 0, 0, 0, 0]
f1 = open('./train/januzaj_train','r')
data = f1.read()
tmp = data.split("~~~")
for i in tmp:
    try:
        index = int(i[-4:])-1
    except:
        index += 1
    text = nltk.word_tokenize(i.decode('utf-8'))
    tagged = nltk.pos_tag(text)
    for i,j in tagged:
        if j=='CD':
            s_count[int(i)-1] += 1
            break
print s_count

f1.close()