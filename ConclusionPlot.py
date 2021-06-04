from RawData import Articles
import matplotlib.pyplot as plt
import pandas as pd


def plotBar(axis, dictList, index, con):
    green, red = '#206a5d', '#f05454'
    txt = pd.DataFrame(dictList, index=index)
    txt.plot.bar(ax=axis, rot=0)
    [axis.text(v - 0.18, i + 0.5, str(i), color='black', fontweight='bold', horizontalalignment='left') for v, i in
     enumerate(dictList["Positive"])]
    [axis.text(v + 0.18, i + 0.5, str(i), color='black', fontweight='bold', horizontalalignment='right') for v, i in
     enumerate(dictList["Negative"])]
    [axis.text(i, -5, con[i], color=green if con[i] == 'POSITIVE' else red, horizontalalignment='center',
               fontweight='heavy') for i in range(5)]
    axis.set_axisbelow(True)
    axis.yaxis.grid(color='red')


def initializeFigure(dic, index):
    figure, axis = plt.subplots(figsize=(10, 10))
    con = ["POSITIVE" if p >= n else "NEGATIVE" for p, n in zip(dic['Positive'], dic['Negative'])]
    plt.title(f"Article Analysis")
    plt.ylabel(f"Word Count")
    plt.subplots_adjust(bottom=0.112, top=0.952)
    plotBar(axis, dic, index, con)


def PlotSentimentConclusion():
    WordsCategoryLength = {
        "Positive": [],
        "Negative": []
    }
    HubsIndex = Articles.keys()
    for file in Articles.values():
        WordsCategoryLength["Positive"].append(len(file['wordCategoryCount']['positive']))
        WordsCategoryLength["Negative"].append(len(file['wordCategoryCount']['negative']))
    initializeFigure(WordsCategoryLength, HubsIndex)
    plt.show()
