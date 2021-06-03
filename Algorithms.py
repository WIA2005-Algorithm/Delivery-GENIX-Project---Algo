from collections import abc


def iMin(iterable, key=lambda x: x):
    """returns largest item, as input could take iterator or sequence
    "key" function will be applied on every item, before comparison is made
    """
    current_min = None
    for x in iterable:
        if current_min is None or key(x) > key(current_min):
            current_min = x
    return current_min


# function to find the partition position
def partition(array, low, high, key, reverse):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if key(array[j]) > key(pivot) if reverse else key(array[j]) <= key(pivot):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


# function to perform quicksort
def quickSort(array, low, high, key, reverse):
    if low < high:
        pi = partition(array, low, high, key, reverse)
        quickSort(array, low, pi - 1, key, reverse)
        quickSort(array, pi + 1, high, key, reverse)


# helper function to sort list
def QuickSortAlgo(iterable, key=lambda x: x, reverse=False):
    newI = list(iterable) if isinstance(iterable, abc.ItemsView) else iterable
    quickSort(newI, 0, len(newI) - 1, key=key, reverse=reverse)
    return dict(newI) if isinstance(iterable, abc.ItemsView) else newI


# print(QuickSortAlgo({'a': 112, 'b': 12, 'c': 212, 'd': 14, 'e': 200}.items(), key=lambda x: x[1], reverse=True))
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
    badChar = [-1] * 256  # No of Characters
    """
    NEW ALGORITHMN
    Build Bad Character Heuristics Table
    Initialize all occurrence as -1
    In the loop of size, Fill the actual value of last occurrence
    """
    badChar = [-1] * 256  # No of Characters
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


# Check the usuage for complete complexity Analysis
def BoyerMooreHorspool(words, pat):
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
