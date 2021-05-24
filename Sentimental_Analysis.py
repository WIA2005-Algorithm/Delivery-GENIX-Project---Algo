from RawData import Articles, stopwords
import re


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


def AnalyseArticles():
    for file in Articles.values():
        File = open(file["file"], "r+", encoding='UTF8')
        file["news"] = re.sub('[^a-zA-Z&]+', ' ', File.read())  # Removing punctuation marks
        file["filteredNews"] = filterStopWords(
            " " + file["news"] + " ")  # To make sure first & last word is word recognized
        file["wordFrequency"] = countWords(file["filteredNews"])
        File.close()


# Binary Search with an addition of O(n/2)
# def binarySearch(wordlist, start, end, target):
#     if start < end:
#         mid = int(start + (end - start) / 2)
#         if wordlist[mid].lower() == target:
#             i, j = mid - 1, mid + 1
#             while i >= start and wordlist[mid].lower() == wordlist[i].lower():
#                 i -= 1
#             while j < end and wordlist[mid].lower() == wordlist[j].lower():
#                 j += 1
#             print(start, mid, end)
#             print(wordlist[i:j])
#             return i + 1, j
#         if wordlist[mid].lower() > target:
#             return binarySearch(wordlist, start, mid - 1, target)
#         return binarySearch(wordlist, mid + 1, end, target)
#     return -1
#
#
# # Search Stop Words using Exponential Searching
# def ExponentialSearching(wordlist, target):
#     if wordlist[0].lower() == target:
#         return 0
#     i = 1
#     while i < len(wordlist) and wordlist[i].lower() <= target:
#         i = i * 2
#     return binarySearch(wordlist, int(i / 2), min(i, len(wordlist) - 1), target)
#
#
# # function to find the partition position
# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j].lower() <= pivot.lower():
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1
#
#
# # function to perform quicksort
# def quickSort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quickSort(array, low, pi - 1)
#         quickSort(array, pi + 1, high)
#
#
# # helper function to sort list
# def SortList(wordlist):
#     quickSort(wordlist, 0, len(wordlist) - 1)
#     return wordlist
