from ReadFile import NormalizeRows
from math import log2
from collections import Counter
from dataclasses import dataclass
from random import shuffle

#change to object (id,language,text,tf_idf) to improve readability and optimize

normalizedLinesAge = NormalizeRows(1)
normalizedLinesGender = NormalizeRows(2)
print(f"Numero de instancias: {len(normalizedLinesAge)}")


def GetVocabulary(data_base):
    vocabulary = set()
    texts = [row[2] for row in data_base]
    for text in texts:
        text = text.split(" ")
        for word in text:
            vocabulary.add(word)
    return vocabulary

@dataclass
class DataBaseRow:
    id: str
    language: str
    text: str
    instance_class: str
    feature_list: []
@dataclass
class DataBase:
    data_base: []
    def get_feature_matrix(self):
        return [row.feature_list for row in self.data_base]
    def get_class_list(self):
        return [row.instance_class for row in self.data_base]

def GetDataBaseObjectWithWordVector(data_base):
    #return array of objects instead of matrix
    vocabulary = GetVocabulary(data_base)
    word_frequency_in_docs = {}
    document_count = len(data_base)
    for row in data_base:
        for i in set(row[2].split()):
            if i not in word_frequency_in_docs:
                word_frequency_in_docs[i] = 1
            else:
                word_frequency_in_docs[i] += 1
    word_weight = {k:log2(document_count/v) for k,v in word_frequency_in_docs.items()}
    data_base_out = []
    for row in data_base:
        word_frecuency = Counter(row[2].split())
        data_base_out.append(DataBaseRow(
            id=row[0]
            ,language=row[1]
            ,text=row[2]
            ,instance_class=row[3]
            ,feature_list=[(word_frecuency[word]*weight if word in word_frecuency else 0) for word,weight in word_weight.items()]))
    shuffle(data_base_out)
    return DataBase(data_base=data_base_out)
    #print(word_frequency_in_docs)

def GetAverageTextLengthAndWordCount(data_base):
    per_class = {}
    for row in data_base:
        class_name = row[3]
        text_length = len(row[2])
        word_count = len(row[2].split())
        if class_name in per_class:
            per_class[class_name][0]+= text_length
            per_class[class_name][1]+=1
            per_class[class_name][2]+=word_count
        else:
            per_class[class_name] = [text_length,1,word_count]
    return {k:(v[0]/v[1],v[2]) for k,v in per_class.items()}

avg_text_length_and_word_count_per_class = GetAverageTextLengthAndWordCount(normalizedLinesAge)
for k,v in avg_text_length_and_word_count_per_class.items():
    print(f'class={k} Avg Text Length: {v[0]} Word Count: {v[1]}')
data_base_age = GetDataBaseObjectWithWordVector(normalizedLinesAge)
vocabulary_age = GetVocabulary(normalizedLinesAge)

avg_text_length_and_word_count_per_class = GetAverageTextLengthAndWordCount(normalizedLinesGender)
for k,v in avg_text_length_and_word_count_per_class.items():
    print(f'class={k} Avg Text Length: {v[0]} Word Count: {v[1]}')
data_base_gender = GetDataBaseObjectWithWordVector(normalizedLinesGender)
vocabulary_gender = GetVocabulary(normalizedLinesGender)
#print(f"vocabulary: {vocabulary}")
if __name__ == "__main__":
    print(f"vocabulary: {vocabulary_age}")
