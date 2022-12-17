# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # Convert the text to a matrix of word counts
    name = [name]
    vectorizer = CountVectorizer().fit_transform(name)

    # Calculate the cosine similarity between the two texts
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])

    # Print the similarity score
    print(similarity)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm Charm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
