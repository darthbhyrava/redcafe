#!/usr/bin/python
import nltk

index = 0 
f1 = open('./sentiment_analysis/train/januzaj_train','r')
f2 = open('test_output','a+')
data = f1.read()
tmp = data.split("~~~")
for i in tmp:
    try:
        index = int(i[-4:])-1
    except:
        index += 1
    text = nltk.word_tokenize(i.decode('utf-8'))
    tagged = nltk.pos_tag(text)
    f2.write(str(index))
    f2.write(str(tagged))
    f2.write("\n\n")
    # print i[-4:]

# # print type(tagged)
# for i,j in tagged:
#     print type(i), type(j)
f1.close()