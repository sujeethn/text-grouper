# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import  pandas as pd
import numpy as np
import Levenshtein as Lv


df = pd.DataFrame(columns=['0','1','2','3'])
def print_hi(names):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi test, {names}')  # Press ⌘F8 to toggle the breakpoint.
    # Convert the text to a matrix of word counts
    name = [
        'This to test code',
        'This to test every code',
        'Not just test',
        'Just test',
        'This to test many code'
        ]
    vectorizer1 = CountVectorizer()
    X = vectorizer1.fit_transform(name)
    features = vectorizer1.get_feature_names()
    print(features)
    rown = X.shape[0]
    i = 1
    similarity = cosine_similarity(X[0:rown], X[0:rown])
    print('first',similarity)
    spsimilar = np.split(similarity, 1)
    df1 = pd.DataFrame(spsimilar[0]) #,columns=['0','1','2','3'],index=['0','1','2','3'])
    print(df1)
    dfo = pd.DataFrame()
    dfoi = -1
    print('--------')
    groupi = 0
    groupj = 0
    criteria = df1.iloc[:, ] >= .8
    for i,j in criteria.items():
        jj=0
        while jj < len(j) :
            if (j[jj]) :
                if (i!=jj) :
                   # print ('True',i,jj)
                    if(dfo is None) :
                        dfo.iloc[i][0] = 'Group1'
                        dfo.iloc[jj][0] = 'Group1'
                        print('dfo first',dfo)
                  #  elif (np.isnan(dfo.iloc[i][0]) and (not (np.isnan(dfo.iloc[jj][0])))) :
                   #     dfo.iloc[i][0] = dfo.iloc[jj][0]
                    #elif (np.isnan(dfo.iloc[jj][0]) and not np.isnan(dfo.iloc[i][0])):
                     #   dfo.iloc[jj][0] = dfo.iloc[i][0]

                    #pos = dfo.iloc[:, ] == i
                    #if(pos.empty ) :
                     #   print('Pos', pos)
                     #   groupj+=1
                      #  dfo.loc[groupi, groupj] = jj

                    #else :
                      #  if dfo.empty :
                     #       groupi = 0
                     #       groupj = 0

                      #      dfo.loc[groupi,groupj] = jj
                      #  else :
                      #      groupi+=1
                      #      groupj+=1
                       #     dfo.loc[groupi,groupj] = jj
                    #if np.isnan(idx) or idx is None:
                     #   dfo.loc[groupi, 0] = i
                    #else :
                     #   dfo.loc[groupi, idx + 1] = i
                    #dfo[groupi][groupj] = i

                    print(name[i])
                    print(name[jj])
                    print('***************')
                    groupi+=1
            jj+=1
    #print(criteria)
    # Calculate the cosine similarity between the two texts
   # similarity = cosine_similarity(X[1:2], X[3:4])

    # Print the similarity score
    #print(similarity)
    print (dfo)


def text_grouper():
   # import Levenshtein as Lv1
    inputD = ['This is the first text','first [not] match','This is the not first text','first no match','not match','not a match','not an match', 'This is this first text']
    dfinput = pd.DataFrame (inputD, columns = ['Text'])
    dfoutput = pd.DataFrame()
    dfoutindex = -1
    a1 = np.array('Group1')
    a2 = np.array('Group2')
    a3 = np.array('Group 3')
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


    def finalout(input) :
        print ('final out',dfoutput)
        i1=0
        while i1 < dfoutput.shape[0]:
            print('Group ', i1)
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
                if similarity > 0.8 :
                    group_similar(i,j)
            j+=1
        i+=1

    print('Input',dfinput)
   # print(getIndexes(dfinput,'first text jj this is')[0] if bool(getIndexes(dfinput,'first text jj this is')) else 'NA')


    finalout('test')


    #text1 = "This is the first text"
    #text2 = "This is the not first text"
    #similarity = calculate_similarity(text1, text2)
    #print(similarity)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm Charm is rhyme')
    text_grouper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
