CourierCompanies = {
    "City-Link-Express": {"name": "Port Klang", "location": (3.0319924887507144, 101.37344116244806)},
    "Pos-Laju": {"name": "Petaling Jaya", "location": (3.112924170027219, 101.63982650389863)},
    "GDEX": {"name": "Batu Caves", "location": (3.265154613796736, 101.68024844550233)},
    "J&T": {"name": "Kajang", "location": (2.9441205329488325, 101.7901521759029)},
    "DHL": {"name": "Sungai Buloh", "location": (3.2127230893650065, 101.57467295692778)}
}

CustomerData = {
    "Ravi": {
        "Origin": {"name": "Rawang", "location": (3.3615395462207878, 101.56318183511695)},
        "Destination": {"name": "Bukit Jelutong", "location": (3.1000170516638885, 101.53071480907951)},
        "color": '#194350'
        # "DirectDistance": {"Text": '23 Km': "Value": 23000}
        # "route": {'Hub': name, 'name': Hubs['name'], 'HubCoordinates': Hubs['location'],'DistanceTravelled': dist, 'FinalValue': [normDistance, normReview, FinalVal, rank, reconmended]}
        # prev_route: {}
        # "RouteRank": [{"name": J&T, "DistanceTravelled": 233}, {...}, {...}, {...}, {...}]
    },
    "Wang Koii": {
        "Origin": {"name": "Subang Jaya", "location": (3.049398375759954, 101.58546611160301)},
        "Destination": {"name": "Puncak Alam", "location": (3.227994355250716, 101.42730357605375)},
        "color": '#99154e'
    },
    "Azizul": {
        "Origin": {"name": "Ampang", "location": (3.141855957281073, 101.76158583424586)},
        "Destination": {"name": "Cyberjaya ", "location": (2.9188704151716256, 101.65251821655471)},
        "color": '#0a1931'
    }
}

Articles = {
    "City-Link-Express": {
        "file": "./Articles/City-Link-Express.txt"
        # "news": str
        # "filteredNews": list of words
        # "wordFrequency": dict of words, count
        # "wordCategoryCount" dict of category, list of words --> {"positive": [" ", ""], "negative": ["", "", ] ....}
    },
    "DHL": {
        "file": "./Articles/DHL.txt"
    },
    "Pos-Laju": {
        "file": "./Articles/Pos-Laju.txt"
    },
    "J&T": {
        "file": "./Articles/J&T.txt"
    },
    "GDEX": {
        "file": "./Articles/GDEX.txt"
    }
}

RankedSentiments = None

stopwords = [
    "a", "about", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along",
    "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "aren't", "around", "as", "at", "back", "be",
    "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below",
    "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "can't", "cannot",
    "cant", "co", "computer", "con", "could", "couldn't", "couldnt", "cry", "de", "describe", "detail", "did", "didn't",
    "do", "does", "doesn't", "doing", "don't", "done", "down", "due", "during", "e", "each", "eg", "eight", "either",
    "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything",
    "everywhere", "except", "few", "fifteen", "fifty", "fill", "find", "fire", "first", "five", "for", "former",
    "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "hadn't",
    "has", "hasn't", "hasnt", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "hence", "her", "here",
    "here's", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "how's",
    "however", "hundred", "i", "i'd", "i'll", "i'm", "i've", "ie", "if", "in", "inc", "indeed", "interest", "into",
    "is",
    "isn't", "it", "it's", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "let's", "ltd",
    "made",
    "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much",
    "must",
    "mustn't", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody",
    "none",
    "noone", "nor", "not", "nothing", "now", "nowhere", "o", "of", "off", "often", "on", "once", "one", "only", "onto",
    "or",
    "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "s", "same", "said", "see", "seem", "seemed", "seeming", "seems", "serious",
    "several",
    "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "show", "side", "since", "sincere", "six",
    "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such",
    "system", "take", "ten", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "thence",
    "there", "there's", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "they'd",
    "they'll",
    "they're", "they've", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
    "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until",
    "up",
    "upon", "us", "very", "via", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "well", "were", "weren't",
    "what",
    "what's", "whatever", "when", "when's", "whence", "whenever", "where", "where's", "whereafter", "whereas",
    "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "who's", "whoever", "whole",
    "whom", "whose", "why", "why's", "will", "with", "within", "without", "won't", "would", "wouldn't", "yet", "you",
    "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
]
