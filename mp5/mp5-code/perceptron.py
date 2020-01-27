import numpy
# perceptron.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 10/27/2018

"""
This is the main entry point for MP5. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""

def classify(train_set, train_labels, dev_set, learning_rate,max_iter):
    """
    train_set - A Numpy array of 32x32x3 images of shape [7500, 3072].
                This can be thought of as a list of 7500 vectors that are each
                3072 dimensional.  We have 3072 dimensions because there are
                each image is 32x32 and we have 3 color channels.
                So 32*32*3 = 3072
    train_labels - List of labels corresponding with images in train_set
    example: Suppose I had two images [X1,X2] where X1 and X2 are 3072 dimensional vectors
             and X1 is a picture of a dog and X2 is a picture of an airplane.
             Then train_labels := [1,0] because X1 contains a picture of an animal
             and X2 contains no animals in the picture.

    dev_set - A Numpy array of 32x32x3 images of shape [2500, 3072].
              It is the same format as train_set
    """

    # TODO: Write your code here
    # print(max_iter)
    # print(len(train_set))

    # print(type(a))
    weight = []
    for i in range(len(train_set[0])):
        weight.append(0)
    bias = 0
    for iteration in range(max_iter):
        print(iteration)
        for p in range(len(train_set)):
            # print(p)
            data = train_set[p]
            result = bias
            result += numpy.dot(data, weight)
            if result >= 0:
                output = 1
            else:
                output = 0
            if output != train_labels[p]:
                if train_labels[p] == 0:
                    weight += learning_rate * (-1) * data
                    bias += learning_rate * (-1)
                else:
                    weight += learning_rate * 1 * data
                    bias += learning_rate * 1
    ret = []
    for data in dev_set:
        result = bias
        result += numpy.dot(data,weight)
        if result >= 0:
            ret.append(1)
        else:
            ret.append(0)

    return ret

def classifyEC(train_set, train_labels, dev_set,learning_rate,max_iter):
    # Write your code here if you would like to attempt the extra credit

    K = 1
    ret = []
    flag = 0
    # print(len(dev_set))
    for test in dev_set:
        print(flag)
        flag += 1
        compare = []
        yesCompare = []
        noCompare = []
        for train in train_set:
            sub = train - test
            sub = sub/10
            subSqrt = numpy.dot(sub, sub)
            compare.append(subSqrt)
        # print(len(compare))
        labels = list(train_labels)
        # print(train_labels)
        account = 0
        # for i in range(K-1):
        #     minValue = min(compare)
        #     idx = compare.index(minValue)
        #     compare.pop(idx)
        #     labels.pop(idx)
        # # print(account)
        # minValue = min(compare)
        # idx = compare.index(minValue)
        # print(idx)
        # if labels[idx]:
        #     ret.append(1)
        # else:
        #     ret.append(0)



        for i in range(K):
            minValue = min(compare)
            idx = compare.index(minValue)
            if labels[idx]:
                account += 1
            else:
                account -= 1
            compare.pop(idx)
            labels.pop(idx)
        # print(account)
        if account >= 0:
            ret.append(1)
        else:
            ret.append(0)




        # for i in range(len(train_labels)):
        #     if train_labels[i]:
        #         yesCompare.append(compare[i])
        #     else:
        #         noCompare.append(compare[i])
        # yesCompare.sort()
        # noCompare.sort()
        # if yesCompare[K] < noCompare[K]:
        #     ret.append(1)
        # else:
        #     ret.append(0)





    return ret
