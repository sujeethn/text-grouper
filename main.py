# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import  pandas as pd
import numpy as np

df = pd.DataFrame(columns=['0','1','2','3'])
def print_hi(names):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi test, {names}')  # Press ⌘F8 to toggle the breakpoint.
    # Convert the text to a matrix of word counts
    name = [
        'This to test code',
        'This to test every code',
        'Not just test',
        'Just test'
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

    print('--------')
    groupi = 0
    criteria = df1.iloc[:, ] >= .8
    for i,j in criteria.items():
        jj=0
        while jj < len(j) :
            if (j[jj]) :
                if (i!=jj) :
                   # print ('True',i,jj)
                    print('Group',groupi)
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm Charm is rhyme')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
