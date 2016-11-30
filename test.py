#!/usr/bin/python
import nltk

index = 0
file = open('./sentiment_analysis/train/januzaj_train','r')
data = file.read()
tmp = data.split("~~~")
for i in tmp:
    try:
        index = int(i[-4:])-1
    except:
        index += 1
    parsed = []
    text = nltk.word_tokenize(i.decode('utf-8'))
    tagged = nltk.pos_tag(text)
    parsed.extend((index, tagged))
    print parsed, "\n\n"
    # print i[-4:]

# # print type(tagged)
# for i,j in tagged:
#     print type(i), type(j)
file.close()