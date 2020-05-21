# -*- coding: utf-8 -*-

"""

Created on Fri Mar  6 09:00:07 2020

@author: jillian walbrun, cole thompson, rachel hefel, patrick hollander

Program 1

"""

import numpy as np


#Function for checking conditions and creating an array of the outputs
def reduceArray(ary, col, val):
    empty = True
    for i in range(np.shape(ary)[0]):
        if ary[i,col] == val:
            if empty:
                empty = False
                a2 = np.array([ary[i,:]])
            else:
                a2 = np.append(a2, [ary[i,:]], axis=0)
    if empty:
        return False
    else:
        return a2

#Function for counting matching values in columns
def countVals(ary, col, val):
    count = 0
    for v in ary[:,col]:
        if v == val:
            count += 1
    return count

#Main
def main():

    #read in training set, testing set, and attribute names
    trainData = np.genfromtxt('wine.train.csv', delimiter=',', dtype = 'str')
    testingData = np.genfromtxt('wine.test.csv', delimiter=',', dtype = 'str')
    nameData = np.genfromtxt('wine.names.csv', delimiter=',', dtype = 'str')

    #determine the number of training examples (number of rows in the file)
    totalTrain = np.shape(trainData)[0]
    
    #determine the number of columns (attributes + target column)
    colTrain = np.shape(trainData)[1]

    #determine the number of testing examples (number of rows in the file)
    totalTest = np.shape(testingData)[0]

    #determine the number of columns (attributes + target column)
    colTest = np.shape(testingData)[1]

    #determine the number of target classes (number of rows in the file)
    totalTarget = np.shape(nameData)[0]

    #determine the number of classifications
    colNames = np.shape(nameData)[1]

    print("The # of training examples: ", totalTrain)
    print("The # of testing examples: ", totalTest)
    print("The # of target classes: ",colNames-1)
    print("The # of columns in the test data: ", colTest)
    print("The # of columns in the train data: ", colTrain)
    print()

    print("Looping through the test rows: ")
    #Loop through the rows of the testing set(testing examples)
    testRow = 0
    j = 0
    classifiedCorrect = 0
    for j in testingData[j:,]:
        print("Test Row to classify: ",testingData[testRow,])
    
        #for each output class - last row of names data
        #count = 1  
        bestProduct = 0.0
        prevNumFound = 0.0
        for val in nameData[totalTarget - 1, 1:]:
            if val != 'X':
                outputClass = reduceArray(trainData, colTrain - 1, val)
                numColOutputClass = np.shape(outputClass)[1]
                #check outputClass for false -        
                numFound = np.shape(outputClass)[0]
                firstFraction = numFound / totalTrain
                product = firstFraction

                #print("First Fraction: ", firstFraction, " and np shape: ", np.shape(outputClass)[0]) #testing
           
                # Looping through the non-output attributes of each test row
                matches = 0
                ctr = 0
                for attrVal in testingData[testRow,:totalTarget - 1]:
                    matches = countVals(outputClass, ctr, attrVal)
                    product = product * matches / numFound
                    ctr = ctr + 1
                    
                #count = count + 1

                # print("Product for testRow: ",testRow," - ",product)
                #print("bestProduct: ",bestProduct,"Product: ",product)
                if bestProduct < product:
                    bestProduct = product
                    bestProdClass = outputClass[0,numColOutputClass - 1]
                    #break ties
                elif bestProduct == product:
                    if numFound < prevNumFound:
                        bestProduct = product
                        bestProdClass = outputClass[0,numColOutputClass - 1]
                  #  print("numFound: ",numFound," prevNumFound: ",prevNumFound,"bestprod",bestProduct)
                    
                prevNumFound = numFound
            
                #print("Best Product and Class: ",bestProduct," - ",bestProdClass," Actual: ",testingData[testRow,totalTarget - 1])
        if bestProdClass == testingData[testRow,totalTarget - 1]:
            classifiedCorrect = classifiedCorrect + 1
        
        print()
        testRow = testRow + 1
    #Print the % testing examples correctly classified 
    print("Classified Correctly: ", 100*(classifiedCorrect/totalTest),"%")

if __name__ == "__main__":

    main()