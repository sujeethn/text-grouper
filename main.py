# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
#import numpy as np
import Levenshtein as Lv


def text_grouper():
   # import Levenshtein as Lv1
    inputD = ['This is the first text','first [not] match','This is the not first text','first no match','not match','not a match','not an match', 'This is this first text']
    dfinput = pd.DataFrame (inputD, columns = ['Text'])
    dfoutput = pd.DataFrame()
    dfoutindex = -1
    sensitivity = 0.8

    def calculate_similarity(text1, text2):
        distance = Lv.distance(text1, text2)
        similarity = 1 - (distance / max(len(text1), len(text2)))
        return similarity


    def getIndexes(dfObj, value):
        # Empty list
        listOfPos = []

        # isin() method will return a dataframe with
        # boolean values, True at the positions
        # where element exists
        result = dfObj.isin([value])

        # any() method will return
        # a boolean series
        seriesObj = result.any()

        # Get list of columns where element exists
        columnNames = list(seriesObj[seriesObj == True].index)

        # Iterate over the list of columns and
        # extract the row index where element exists
        for col in columnNames:
            rows = list(result[col][result[col] == True].index)

            for row in rows:
                listOfPos.append((row, col))

        # This list contains a list tuples with
        # the index of element in the dataframe
        return listOfPos


    def group_similar(iindex,jindex):
        global dfoutindex
        iloc = getIndexes(dfoutput,iindex)[0][0] if bool(getIndexes(dfoutput,iindex)) else 'NA'
        jloc = getIndexes(dfoutput, jindex)[0][0] if bool(getIndexes(dfoutput, jindex)) else 'NA'
      #  print('dfout',dfoutput)
       # print('iloc',iloc)
       # print('jloc',jloc)
      #  print('iindex',iindex)
       # print('jindex',jindex)


        if (iloc == 'NA' and jloc == 'NA') :
            if(dfoutput.empty):
                dfoutindex = 0
            else :
                dfoutindex+=1

            dfoutput.loc[dfoutindex,0]=iindex
            dfoutput.loc[dfoutindex,1] = jindex

       #     print('dfout2', dfoutput)

        elif (iloc != jloc):
            if (iloc != 'NA') :
                dfoutput.loc[iloc, len(dfoutput.columns)] = jindex
            elif (jloc !='NA') :
                dfoutput.loc[jloc, len(dfoutput.columns)] = iindex
         #   print('dfout3', dfoutput)


    def finalout() :
    #    print ('final out',dfoutput)
        i1=0
        while i1 < dfoutput.shape[0]:
            print('Similar Group ', i1+1,'---------------')
            j1 = 0
            while j1 < dfoutput.shape[1]:
               # print ('final1',i1,'j',j1,'out',dfoutput.loc[i1][j1])
                if(not pd.isnull(dfoutput.loc[i1][j1])):
                   print( dfinput.iloc[int(dfoutput.loc[i1][j1])]['Text'])
                j1+=1
            i1+=1


    i=0
    while i < dfinput.shape[0] :
    #    print('inside i',i)
        j=0
        while j < dfinput.shape[0]:
            if i != j :
                similarity = calculate_similarity(dfinput.iloc[i]['Text'], dfinput.iloc[j]['Text'])
       #         print(f'1:',dfinput.iloc[i]['Text'],'2:', dfinput.iloc[j]['Text'])
       #         print('Similar',similarity)
                if similarity > sensitivity :
                    group_similar(i,j)
            j+=1
        i+=1

    print('Input***********')
    print(dfinput)


    print('Output**********')
    finalout()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    text_grouper()
