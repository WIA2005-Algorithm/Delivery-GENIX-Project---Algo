from RawData import Articles
from RawData import CourierCompanies, CustomerData, Articles, Rank
import Sentimental_Analysis
from Sentimental_Analysis import AnalyseArticles, AnalyseWordsCategories, Conclusion
import numpy as np
import matplotlib.pyplot as plt


def plot2():
    a = []
    b = []
    c=[]

    for name,file in Articles.items():
        s= len(file['wordCategoryCount']['positive'])
        d = len(file['wordCategoryCount']['negative'])
        c.append(name)
        a.append(s)
        b.append(d)
    print(type(a[0]),"  ", a)
    print(type(b[0]),"  ", b)

    n_groups= 5
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, a, bar_width,
    alpha=opacity,
    color='b',
    label='positive')

    rects2 = plt.bar(index + bar_width, b, bar_width,
    alpha=opacity,
    color='g',
    label='negative')

    for bar in rects1:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .005, yval)

    for bar in rects2:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .005, yval)


    plt.ylabel('Word count')

    plt.xticks(index + bar_width, c)
    plt.legend()

    plt.tight_layout()
    plt.show()