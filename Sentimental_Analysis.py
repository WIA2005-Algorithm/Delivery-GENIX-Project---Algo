from RawData import Articles, stopwords
import re


def piFun(p):
    # Idea used is pi[i-1] <= pi[i] + 1
    pi = [0] * len(p)
    for i in range(1, len(p)):
        L = pi[i - 1]
        while L > 0 and p[i] != p[L]:
            L = pi[L - 1]
        if p[i] == p[L]:
            L += 1
        pi[i] = L
    return pi


def KMPSearch(pat, txt):
    lps = piFun(pat)
    j = 0  # index for pat[]
    for i in range(len(txt)):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == len(pat):
            return True
        # mismatch after j matches
        elif i < len(txt) and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


# Build Bad Character Heuristics Table
def badCharHeuristic(string, size):
    # Initialize all occurrence as -1
    badChar = [-1] * 256  # No of Characters
    for i in range(size):
        # Fill the actual value of last occurrence
        badChar[ord(string[i])] = i
    return badChar


def FilterWordIndices(words, pat):
    FinalisedIndexes = []
    """
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm & return the indices
    """
    m = len(pat)
    n = len(words)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == words[s + j]:
            j -= 1
        if j < 0:
            FinalisedIndexes.append(s)
            s += (m - badChar[ord(words[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(words[s + j])])
    return FinalisedIndexes


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
        indices = FilterWordIndices(textWordList.lower(), pat)
        if indices:
            textWordList = removeWords(textWordList, indices, len(pat) - 1)
    return textWordList.split()


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
            if KMPSearch(f'@{word}@', positiveWords):
                WordCategoryCount['positive'].append(word)
            elif KMPSearch(f"@{word}@", negativeWords):
                WordCategoryCount['negative'].append(word)
            else:
                WordCategoryCount['neutral'].append(word)
        file['wordCategoryCount'] = WordCategoryCount
        print(len(file['wordCategoryCount']['positive']),  "\t",len(file['wordCategoryCount']['negative']), "\t",len(file['wordCategoryCount']['neutral']))



# Aiman Complete this function!! Check the rawdata.py to know where or how positive, negative words & neutral words are stored
# Use variables to store result or print stateents
# Conclude using the data, display number of words in each category...etc etc..
# Apply these functions in order before running
# AnalyseArticles()
# AnalyseWordsCategories()
def Conclusion():
    AnalyseArticles()
    for file in Articles.values():
        for Category in file['wordCategoryCount']:
             if Category['positive']:
                temp = Category['positive']
             elif Category['negative']:
                temp2 = Category['negative']
             else:
                temp3 = Category['neutral']

    AnalyseWordsCategories()
    Print(temp.count())
    Print(temp2.count())
    Print(temp3.count())



