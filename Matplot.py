import collections
from matplotlib.widgets import Slider
from RawData import Articles
import matplotlib.pyplot as plt
import pandas as pd

default_count = 40


def plotBar(axis, doc, top_count=default_count):
    txt = pd.DataFrame(collections.Counter(doc).most_common(top_count), columns=['words', 'occurrence']).sort_values(
        by="occurrence")
    txt.plot.barh(x='words', y='occurrence', ax=axis, color="red")
    [axis.text(v + 0.2, i - 0.2, str(v), color='black', fontweight='bold') for i, v in enumerate(txt['occurrence'])]


def initializeFigure(doc, name):
    figure, axis = plt.subplots(figsize=(10, 10))
    plt.title(f"Word Frequency Count - {name}")
    plt.ylabel(f"Words - Top {default_count} ")
    plt.subplots_adjust(bottom=0.112, top=0.952)
    axis_position = plt.axes([0.2, 0.03, 0.65, 0.03], facecolor='White')
    slider_positions = Slider(axis_position, 'Top Words', 10, 90, default_count, valstep=10)
    plotBar(axis, doc)
    return figure, axis, slider_positions


def plotBarGraphs():
    for name, file in Articles.items():
        text = file["wordFrequency"]
        fig, ax, slider_position = initializeFigure(text, name)

        def update(val):
            ax.clear()
            plotBar(ax, text, int(slider_position.val))

        slider_position.on_changed(update)
        plt.show()
