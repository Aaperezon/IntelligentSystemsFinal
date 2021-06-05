from ReadFile import NormalizeRows





normalizedLines = NormalizeRows()
print(normalizedLines[0])
print(f"Numero de instancias: {len(normalizedLines)}")


def GetVocabulary(data_base):
    vocabulary = set()
    texts = [row[2] for row in data_base]
    for text in texts:
        text = text.split(" ")
        for word in text:
            vocabulary.add(word)
    return vocabulary

def VectorizeDataBase(data_base):
    vocabulary = GetVocabulary(data_base)
    word_frequency_in_docs = {}
    for row in data_base:
        for i in set(row[2].split()):
            if i not in word_frequency_in_docs:
                word_frequency_in_docs[i] = 1
            else:
                word_frequency_in_docs[i] += 1
    print(word_frequency_in_docs)

                
VectorizeDataBase(normalizedLines)
vocabulary = GetVocabulary(normalizedLines)
print(f"vocabulary: {vocabulary}")