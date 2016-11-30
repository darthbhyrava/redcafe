#!/usr/bin/python
# Script to train classifier on training data, and classify the test data into corresponding sentiment class.
# Sriharsh Bhyravajjula, 2016

import nltk
import math

p_sent = [0.00, 0.00, 0.00, 0.00, 0.00]
word_counter= [{}, {}, {}, {}, {}]
total_word_counter = {}

# Calculating prior and likelihood
index = 0 
s_count = [0.00, 0.00, 0.00, 0.00, 0.00]
train_sentiment = 0.00
f1 = open('./train/rashford_train','r')
data = f1.read()
tmp = data.split("~~~")
for i in tmp:
    try:
        index = int(i[-4:])-1
    except:
        index += 1
    text = nltk.word_tokenize(i.decode('utf-8'))
    tagged = nltk.pos_tag(text)
    for i, j in tagged:
        if j=='CD':
            sent = int(i)
            train_sentiment += sent
            s_count[int(i)-1] += 1.00
            break
    # Calculating word counts under each sentiment
    for i, j in tagged:
        if i in word_counter[sent-1]:
            word_counter[sent-1][i] += 1.00
        else:
            word_counter[sent-1][i] = 1.00
p_sent = [s_count[0]/351, s_count[1]/351, s_count[2]/351, s_count[3]/351, s_count[4]/351]
# Calculating overall word counts
for i in range(len(word_counter)):
    for j in word_counter[i]:
        if j in total_word_counter:
            total_word_counter[j] += word_counter[i][j]
        else:
            total_word_counter[j] = word_counter[i][j]
f1.close()

# Classifying test data by assigning sentiments to each post
total_sentiment = 0.00
f2 = open('./test/rashford_test','r')
data = f2.read()
tmp = data.split("~~~")
for i in tmp:
    total_lhood = [0.00, 0.00, 0.00, 0.00, 0.00]
    max_l = -9999.00
    try:
        index = int(i[-4:])-1
    except:
        index += 1
    text = nltk.word_tokenize(i.decode('utf-8'))
    tagged = nltk.pos_tag(text)
    for key, value in tagged:
        lhood = [0.00, 0.00, 0.00, 0.00, 0.00]
        for k in range(5):
            try:
                lhood[k] = (word_counter[k][key]/total_word_counter[key])
            except:
                lhood[k] = 0.2
            total_lhood[k] += lhood[k]
    # print index, total_lhood
    for m in range(5):
        if (total_lhood[m])*(p_sent[m])>=max_l:
            max_l = (total_lhood[m])*(p_sent[m])
            max_s = m+1
    f3 = open('./results/rashford_final','a+')
    final_write = str(index) + "\t" + str(max_s) + "\n\n"
    f3.write(final_write)
    total_sentiment += max_s
total_sentiment /= 1750
train_sentiment /= 350
accuracy = 100 - ((total_sentiment - train_sentiment)/train_sentiment)*100
final_write = "Classified Sentiment:" + str(total_sentiment) + "\tAccuracy:" + str(accuracy)
f3.write(final_write)
f2.close()
f3.close()
