# naive_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018

"""
This is the main entry point for MP4. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""

import math

# global STEMMING
# global LOWER_CASE
# STEMMING = True
LOWER_CASE = True

def naiveBayes(train_set, train_labels, dev_set, smoothing_parameter, pos_prior):
    """
    train_set - List of list of words corresponding with each movie review
    example: suppose I had two reviews 'like this movie' and 'i fall asleep' in my training set
    Then train_set := [['like','this','movie'], ['i','fall','asleep']]

    train_labels - List of labels corresponding with train_set
    example: Suppose I had two reviews, first one was positive and second one was negative.
    Then train_labels := [1, 0]

    dev_set - List of list of words corresponding with each review that we are testing on
              It follows the same format as train_set

    smoothing_parameter - The smoothing parameter you provided with --laplace (1.0 by default)
    """
    # TODO: Write your code here

    smoothing_parameter = 0.1
    stopWords = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]
    for i in range(len(train_set)):
        n = 0
        while n in range(len(train_set[i])):
            if train_set[i][n] in stopWords:
                train_set[i].pop(n)
            else:
                n = n + 1
    for i in range(len(dev_set)):
        n = 0
        while n in range(len(dev_set[i])):
            if dev_set[i][n] in stopWords:
                dev_set[i].pop(n)
            else:
                n = n + 1
    for i in range(len(train_set)):
        if "a" in train_set[i] or "the" in train_set[i]:
            print("not success")


    positiveWordsNum = 0
    negativeWordsNum = 0
    for i in range(len(train_set)):
        if train_labels[i] == 1:
            positiveWordsNum += len(train_set[i])
        else:
            negativeWordsNum += len(train_set[i])
    # print(positiveWordsNum, negativeWordsNum)

    # check number of times W occurs in the documents
    posWordType = {}
    negWordType = {}
    for i in range(len(train_set)):
        for n in train_set[i]:
            if train_labels[i]:
                if n not in posWordType.keys():
                    posWordType[n] = [1, train_labels[i]]
                else:
                    posWordType[n][0] += 1
            else:
                if n not in negWordType.keys():
                    negWordType[n] = [1, train_labels[i]]
                else:
                    negWordType[n][0] += 1



    # Laplace
    count = 0
    for i in posWordType.keys():
        posWordType[i].append((posWordType[i][0] + smoothing_parameter) / (positiveWordsNum + smoothing_parameter *
                                                                           (len(posWordType.keys()) + 1)))
        count += posWordType[i][2]
    posUNK = smoothing_parameter / (positiveWordsNum + smoothing_parameter * (len(posWordType.keys()) + 1))
    logPosUNK = math.log(posUNK, 10)
    print(count + posUNK, posUNK)
    count = 0
    for i in negWordType.keys():
        negWordType[i].append((negWordType[i][0] + smoothing_parameter) / (negativeWordsNum + smoothing_parameter *
                                                                           (len(negWordType.keys()) + 1)))
        count += negWordType[i][2]
    negUNK = smoothing_parameter / (negativeWordsNum + smoothing_parameter * (len(negWordType.keys()) + 1))
    logNegUNK = math.log(negUNK, 10)
    print(count + negUNK, negUNK)




    returnPredictedLabels = []
    for review in dev_set:
        posPossibility = math.log(pos_prior, 10)
        negPossibility = math.log(1 - pos_prior, 10)
        for word in review:
            if word in posWordType.keys():
                posPossibility += math.log(posWordType[word][2], 10)
            else:
                posPossibility += logPosUNK
            if word in negWordType.keys():
                negPossibility += math.log(negWordType[word][2], 10)
            else:
                negPossibility += logNegUNK

        if posPossibility > negPossibility:
            returnPredictedLabels.append(1)
        else:
            returnPredictedLabels.append(0)


    # return predicted labels of development set
    return returnPredictedLabels
