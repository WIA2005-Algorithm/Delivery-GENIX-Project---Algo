from collections import abc


def iMinMax(iterable, key=lambda x: x, Max=True):
    """returns largest item, as input could take iterator or sequence
    "key" function will be applied on every item, before comparison is made
    """
    current = None
    for x in iterable:
        if current is None or (key(x) > key(current) if Max else key(x) <= key(current)):
            current = x
    return key(current)


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
    dictionary = isinstance(iterable, abc.ItemsView)
    if dictionary:
        iterable = list(iterable)
    quickSort(iterable, 0, len(iterable) - 1, key=key, reverse=reverse)
    return dict(iterable) if dictionary else iterable


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
        elif i < len(txt) and pat[j] != txt[i]:
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
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


# Check the usuage for complete complexity Analysis
def BoyerMooreHorspool(text, pat):
    FinalisedIndexes = []
    """
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm & return the indices
    """
    m = len(pat)
    n = len(text)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            FinalisedIndexes.append(s)
            s += (m - badChar[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(text[s + j])])
    return FinalisedIndexes


def NormaliseData(iterable, Hub=lambda x: x, key=lambda x: x):
    """
    Helper Function to calculate Normalised Value of the Iterable passed
    based on Hub & Key
    :TODO Normalised = value - min(all values) / max(all values) - min (all values), Will Convert to 0-1 Scale
    """
    Min = iMinMax(iterable, key=key, Max=False)
    Sub = iMinMax(iterable, key=key) - Min
    newIterable = {}
    for x in iterable:
        newIterable[Hub(x)] = (key(x) - Min) / Sub  # [{'Hub': 'normalised values'}, {...}, {...} ...]
    return newIterable


def NormaliseDataRanking(DistanceIterable, ReviewsIterable, Hub=lambda x: x, Dist=lambda x: x, Review=lambda x: x):
    """
        Function to calculate Normalised Value & Group Rank them based on Hub Distance
        as well as Review Ratings based on Hub & Key
        :param ReviewsIterable: List of Dictionaries of Hubs for Review Ranking - Dictionaries represet each hub
        :param DistanceIterable: List of Dictionaries of Hubs for Distance Ranking - Dictionaries represet each hub
        :param Review: To access the review rating based on key
        :param Dist: To access the distance travelled based on key
        :param Hub: To access the hub passed based on key
        :return the sorted ranking of hubs based on Normalised/FinalValues based on both criterias
    """
    Distance_Weight, Review_Weight = 2, 1
    NDistance = NormaliseData(DistanceIterable, Hub=Hub, key=Dist)
    NReviews = NormaliseData(ReviewsIterable, Hub=Hub, key=Review)
    for normhub, routedHub in zip(NDistance.keys(), DistanceIterable):
        # ADDING IN THE MAIN DISCTIONARY INSIDE RAWDATA.PY
        routedHub['FinalDetails'] = [NDistance[normhub], NReviews[normhub],
                                     ((Distance_Weight * NDistance[normhub]) + (Review_Weight * NReviews[normhub])) / 2]
    DistanceIterable = QuickSortAlgo(DistanceIterable, key=lambda z: z['FinalDetails'][2])
    c = 1
    for detail in DistanceIterable:
        detail['FinalDetails'].extend([c, '\u2705' if c == 1 else '\u274C'])
        c += 1
    return DistanceIterable
