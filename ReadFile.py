import string
import nltk
import pandas as pd
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.wordnet import  WordNetLemmatizer

lmtzr = WordNetLemmatizer()


file1 = open("English.txt", 'r')
Lines = file1.readlines()
stop_words = stopwords.words("english")

#read class file and join with english.txt

classes_dict = {tp[0]:tp[2] for tp in pd.read_csv('Gold-Ingles.csv',header=None).to_numpy()}


def NormalizeRows():
    normalizedLines = []
    for line in Lines:
        line = (''.join([i for i in line if i not in string.punctuation])).lower().split("\t")
        line[2] = ' '.join( [lmtzr.lemmatize(i) for i in line[2].strip().split() if i not in stop_words] )
        line.append(classes_dict[line[0]])
        normalizedLines.append(line)

    return normalizedLines

if __name__ == "__main__":
    normalizedLines = NormalizeRows()
    print(normalizedLines[0])