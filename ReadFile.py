import string
import nltk
import re
nltk.download('words')
import pandas as pd
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords,words
from nltk.stem.wordnet import  WordNetLemmatizer
#import enchant

#d = enchant.Dict("en_US")

lmtzr = WordNetLemmatizer()

words = words.words()


file1 = open("English.txt", 'r')
Lines = file1.readlines()
stop_words = stopwords.words("english")

#read class file and join with english.txt

classes_dict = {tp[0]:tp[2] for tp in pd.read_csv('Gold-Ingles.csv',header=None).to_numpy()}

only_letters = re.compile('^[a-z]+$')

def link(word):
    return 'http' in word or 'www' in word

def NormalizeRows():
    normalizedLines = []
    for line in Lines:
        line = line.split("\t")
        line[2] = ' '.join( [lmW for i in line[2].strip().split() if i not in stop_words and len(lmW:=lmtzr.lemmatize(i.lower()))>2 and only_letters.match(lmW) and not link(lmW)]) #and (lmW:=lmtzr.lemmatize(i)) in words] )
        line.append(classes_dict[line[0]])
        normalizedLines.append(line)

    return normalizedLines

print('before __name__ == "main"')

if __name__ == "__main__":
    normalizedLines = NormalizeRows()
    #print(normalizedLines)