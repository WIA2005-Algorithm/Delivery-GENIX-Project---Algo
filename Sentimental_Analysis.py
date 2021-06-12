import Algorithms
from RawData import Articles, stopwords
import re


# After Successful Search, Remove the words from the string at indices
def removeWords(txt, indices, s):
    j = 0
    for i in indices:
        i -= j
        txt = txt[:i + 1] + txt[(i + 1 + s):]
        j += s
    return txt


# Filter Stop Words
def filterStopWords(textWordList):
    for word in stopwords:
        pat = " " + word + " "  # filtered word is identified by spaces first & last
        indices = Algorithms.BoyerMooreHorspool(textWordList.lower(), pat)
        if indices:
            textWordList = removeWords(textWordList, indices, len(pat) - 1)
    return textWordList.split()


# Count Word Frequency
def countWords(wordlist):
    freq = {}
    for word in wordlist:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq


def OpenWords(file='positive_words'):
    f = open(f'Articles/{file}.txt', "r+", encoding='UTF8')
    return '@' + '@'.join(f.read().split()) + '@'


def AnalyseArticles():
    for file in Articles.values():
        File = open(file["file"], "r+", encoding='UTF8')
        file["news"] = re.sub('[^a-zA-Z&]+', ' ', File.read())  # Removing punctuation marks
        file["filteredNews"] = filterStopWords(
            " " + file["news"] + " ")  # To make sure first & last word is word recognized
        file["wordFrequency"] = countWords(file["filteredNews"])
        File.close()


def AnalyseWordsCategories():
    positiveWords = OpenWords()
    negativeWords = OpenWords('negative_words')
    for file in Articles.values():
        WordCategoryCount = {'positive': [], 'negative': [], 'neutral': []}
        for word in file['wordFrequency']:
            if Algorithms.KMPSearch(f'@{word}@', positiveWords):
                WordCategoryCount['positive'].append(word)
            elif Algorithms.KMPSearch(f"@{word}@", negativeWords):
                WordCategoryCount['negative'].append(word)
            else:
                WordCategoryCount['neutral'].append(word)
        file['wordCategoryCount'] = WordCategoryCount


def Conclusion():
    RankValue = {}
    for name, file in Articles.items():
        RankValue[name] = [len(file['wordCategoryCount']['negative']) - len(file['wordCategoryCount']['positive'])]
    RankValue = Algorithms.QuickSortAlgo(RankValue.items(), key=lambda x: x[1])
    c = 1
    for detail in RankValue.values():
        detail.extend([c, '\u2705' if c == 1 else '\u274C'])
        c += 1
    return RankValue
