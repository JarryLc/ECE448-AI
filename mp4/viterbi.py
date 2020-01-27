"""
This is the main entry point for MP4. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
import math


def baseline(train, test):
    '''
    TODO: implement the baseline algorithm.
    input:  training data (list of sentences, with tags on the words)
            test data (list of sentences, no tags on the words)
    output: list of sentences, each sentence is a list of (word,tag) pairs.
            E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
    '''
    # calculate P(t)
    tags = {}
    wordsOfTags = {}
    numberOfWords = 0
    for sentence in train:
        for element in sentence:
            numberOfWords += 1
            if element[1] not in tags.keys():
                tags[element[1]] = 1
            else:
                tags[element[1]] += 1
            # print(numberOfWords)
            if element[1] not in wordsOfTags.keys():
                wordsOfTags[element[1]] = {}
                wordsOfTags[element[1]][element[0]] = 1
            else:
                if element[0] not in wordsOfTags[element[1]].keys():
                    wordsOfTags[element[1]][element[0]] = 1
                else:
                    wordsOfTags[element[1]][element[0]] += 1
    print("done")
    pWT = {}
    for tag in wordsOfTags.keys():
        for word in wordsOfTags[tag].keys():
            pWT[(tag, word)] = math.log(wordsOfTags[tag][word] / sum(wordsOfTags[tag].values()))
    pT = {}
    for tag in tags.keys():
        pT[tag] = math.log(tags[tag] / numberOfWords)
    print("done")
    predicts = []
    for i in range(len(test)):
        # print(i)
        predicts.append([])
        for word in test[i]:
            maxPossibility = -100000
            flag = 0
            for tag in wordsOfTags.keys():
                if word not in wordsOfTags[tag].keys():
                    continue
                else:
                    possible = pWT[(tag, word)] + pT[tag]
                    flag = 1
                    # print(possible)
                if possible > maxPossibility:
                    maxPossibility = possible
                    maxTag = tag
            if flag == 0:
                predicts[i].append((word, 'NOUN'))
            else:
                predicts[i].append((word, maxTag))
    # raise Exception("You must implement me")
    return predicts


def viterbi(train, test):
    '''
    TODO: implement the Viterbi algorithm.
    input:  training data (list of sentences, with tags on the words)
            test data (list of sentences, no tags on the words)
    output: list of sentences with tags on the words
            E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
    '''

    initial = {}
    transition = {}
    wordsOfTags = {}
    listOfWord = {}
    for sentence in train:
        # initial
        initialElement = sentence[0]
        if initialElement[1] not in initial.keys():
            initial[initialElement[1]] = 1
        else:
            initial[initialElement[1]] += 1
        lastElement = initialElement
        for element in sentence:
            # transition
            if element[1] != 'START':
                if element[1] not in transition.keys():
                    transition[element[1]] = {}
                    transition[element[1]][lastElement[1]] = 1
                else:
                    if lastElement[1] not in transition[element[1]].keys():
                        transition[element[1]][lastElement[1]] = 1
                    else:
                        transition[element[1]][lastElement[1]] += 1
            lastElement = element
            # wordsOfTags, i.e. emission
            if element[1] not in wordsOfTags.keys():
                wordsOfTags[element[1]] = {}
                wordsOfTags[element[1]][element[0]] = 1
            else:
                if element[0] not in wordsOfTags[element[1]].keys():
                    wordsOfTags[element[1]][element[0]] = 1
                else:
                    wordsOfTags[element[1]][element[0]] += 1
            # listOfWord
            if element[0] not in listOfWord.keys():
                listOfWord[element[0]] = (1, element[1])
            else:
                listOfWord[element[0]] = (listOfWord[element[0]][0]+1, listOfWord[element[0]][1])
    # print(initial)
    # print(transition)
    print("done")

    laplaceScale = {}
    for word in listOfWord.keys():
        if listOfWord[word][0] == 1:
            if listOfWord[word][1] not in laplaceScale.keys():
                laplaceScale[listOfWord[word][1]] = 1
            else:
                laplaceScale[listOfWord[word][1]] += 1
    for tag in wordsOfTags.keys():
        if tag not in laplaceScale.keys():
            laplaceScale[tag] = 1
        else:
            laplaceScale[tag] = laplaceScale[tag] ** 2
    # print(laplaceScale)
    laplaceSum = sum(laplaceScale.values())
    for tag in laplaceScale.keys():
        laplaceScale[tag] = laplaceScale[tag]/laplaceSum


    # print(laplaceScale)

    pI = {}
    pTT = {}
    pWT = {}

    pTT_UNK = {}
    pWT_UNK = {}
    smoothI = 0.1
    smoothTT = 0.1
    smoothWT = 0.000000001
    orgSmoothWt = 0.000001

    # pI

    # for tag in wordsOfTags.keys():
    #     if tag not in initial.keys():
    #         pI[tag] = 0
    #     else:
    #         pI[tag] = initial[tag]/sum(initial.values())
    for tag in initial.keys():
        pI[tag] = (initial[tag] + smoothI) / (sum(initial.values()) + smoothI * 2)
        pI[tag] = math.log(pI[tag])
    pI_UNK = smoothI / (sum(initial.values()) + smoothI * 2)
    pI_UNK = math.log(pI_UNK)
    for tag in wordsOfTags.keys():
        if tag not in pI.keys():
            pI[tag] = pI_UNK
    print("pI & smooth done")

    # pTT
    # for taga in wordsOfTags.keys():
    #     for tagb in wordsOfTags.keys():
    #         if tagb not in transition.keys():
    #             pTT[(taga, tagb)] = 0
    #         else:
    #             if taga not in transition[tagb].keys():
    #                 pTT[(taga, tagb)] = 0
    #             else:
    #                 pTT[(taga, tagb)] = transition[tagb][taga] / sum(transition[tagb].values())
    for tagb in transition.keys():
        for taga in transition[tagb].keys():
            pTT[(taga, tagb)] = (transition[tagb][taga] + smoothTT) / (sum(transition[tagb].values()) +
                                                                       smoothTT*(len(transition[tagb].keys()) + 1))
            pTT[(taga, tagb)] = math.log(pTT[(taga, tagb)])
        pTT_UNK[tagb] = smoothTT / (sum(transition[tagb].values()) + smoothTT*(len(transition[tagb].keys()) + 1))
        pTT_UNK[tagb] = math.log(pTT_UNK[tagb])
        pTT_UNK['START'] = -1000
    for tagb in wordsOfTags.keys():
        for taga in wordsOfTags.keys():
            if (taga, tagb) not in pTT.keys():
                pTT[(taga, tagb)] = pTT_UNK[tagb]
    print("pTT & smooth done")
    # pWT
    for tag in wordsOfTags.keys():
        for word in wordsOfTags[tag].keys():
            smoothWT = orgSmoothWt * laplaceScale[tag]
            pWT[(tag, word)] = (wordsOfTags[tag][word] + smoothWT) / (sum(wordsOfTags[tag].values()) +
                                                                      smoothWT * (len(wordsOfTags[tag].keys()) + 1))
            pWT[(tag, word)] = math.log(pWT[(tag, word)])
        pWT_UNK[tag] = smoothWT / (sum(wordsOfTags[tag].values()) + smoothWT * (len(wordsOfTags[tag].keys()) + 1))
        # print(pWT_UNK[tag], smoothWT)
        pWT_UNK[tag] = math.log(pWT_UNK[tag])
    print("pWT & smooth done")

    predicts = []
    for i in range(len(test)):
        # print(i)
        predicts.append([])
        trellis = {}
        for m in range(len(test[i])):
            word = test[i][m]
            for tag in wordsOfTags.keys():
                if m == 0:
                    if word not in wordsOfTags[tag].keys():
                        temp = pWT_UNK[tag]
                    else:
                        temp = pWT[(tag, word)]
                    possible = temp + pI[tag]
                    trellis[(m, tag)] = (possible, 0)
                else:
                    maxPossible = -100000
                    maxLastTag = ''
                    for lastTag in wordsOfTags.keys():
                        if word not in wordsOfTags[tag].keys():
                            temp = pWT_UNK[tag]
                        else:
                            temp = pWT[(tag, word)]
                        possible = trellis[(m-1, lastTag)][0] + pTT[(lastTag, tag)] + temp
                        if possible > maxPossible:
                            maxPossible = possible
                            maxLastTag = lastTag
                    trellis[(m, tag)] = (maxPossible, maxLastTag)
        maxP = -100000
        maxT = ''
        m = len(test[i]) - 1
        for finalTag in wordsOfTags.keys():
            if trellis[(m, finalTag)][0] > maxP:
                maxP = trellis[(m, finalTag)][0]
                maxT = finalTag
        predicts[i].insert(0, (test[i][m], maxT))
        formerTag = trellis[(m, finalTag)][1]
        m -= 1
        while m >= 0:
            predicts[i].insert(0, (test[i][m], formerTag))
            formerTag = trellis[(m, formerTag)][1]
            m -= 1


    # print(predicts[0])





    return predicts
