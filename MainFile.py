import collections
import time
import RawData
from Algorithms import NormaliseDataRanking
from ConclusionPlot import PlotSentimentConclusion
from CusHubsMap import HubDeliveryMap, PreProcess
from RawData import CourierCompanies, CustomerData, Articles
from Sentimental_Analysis import AnalyseArticles, AnalyseWordsCategories, Conclusion
from Matplot import plotBarGraphs
from prettytable import PrettyTable


def PrettyPrint(FieldNames, iterableRows, keys):
    if len(FieldNames) != len(keys):
        return "Not Sufficient Keys to Operate"
    x = PrettyTable()
    x.field_names = FieldNames
    for row in iterableRows:
        x.add_row([key(row) for key in keys])
    return x


def PrintCustomer_Hubs():
    print("\nFirst of all let us analysis our customers & their requirements:")
    print(PrettyPrint(['Customer', 'Origin Location', 'Destination Location'], CustomerData.items(),
                      [lambda x: 'Customer ' + x[0], lambda x: x[1]['Origin']['name'],
                       lambda x: x[1]['Destination']['name']]))
    print("\nFollowing are the available Hubs: ")
    print(PrettyPrint(['Hub', 'Location'], CourierCompanies.items(), [lambda x: x[0], lambda x: x[1]['name']]))


def AddDirectDistanceMap():
    print("Please wait while the resources load...APIs do take time sometime due to internet connection problems...")
    PreProcess()
    H = HubDeliveryMap()
    print("\nFollowing is the customer direct distance:- ")
    H.MarkLeastDistantPath()
    print(PrettyPrint(['Customer', 'Origin', 'Destination', 'Distance (Meters)', 'Distance (KM)'],
                      CustomerData.items(),
                      [lambda x: 'Customer ' + x[0], lambda x: x[1]['Origin']['name'],
                       lambda x: x[1]['Destination']['name'], lambda x: str(x[1]['DirectDistance']['value']) + ' m',
                       lambda x: x[1]['DirectDistance']['text']]
                      ))
    print("""
    Alright, Time for Some Visuals... Let's Goo
    Hint: Click on the symbols to view more details
    """)
    input("Press enter to visualize it...")
    print(H)
    input("Press enter to continue...")


def AvailableOptions():
    for Customer, CusDetails in CustomerData.items():
        print(f"\nCustomer {Customer} has these available options:- ")
        print(PrettyPrint(['Hub', 'Distance through Hub', 'Recommended Choice'], CusDetails['RouteRank'],
                          [lambda x: x['Hub'], lambda x: str(x['DistanceTravelled']) + ' Km',
                           lambda x: x['Recommended']]))
    H2 = HubDeliveryMap(False)  # I am going to mark route through hub
    H2.MarkRoutesHubs()
    print("\nBelow are the recomended choices based on the distance:-")
    print(PrettyPrint(['Customer', 'Origin', 'Destination', 'Hub Recommended', 'Distance (Km)'],
                      CustomerData.items(),
                      [lambda x: 'Customer ' + x[0], lambda x: x[1]['Origin']['name'],
                       lambda x: x[1]['Destination']['name'], lambda x: x[1]['route']['Hub'],
                       lambda x: str(x[1]['route']['DistanceTravelled']) + ' Km']
                      ))
    print("""
    *** Let's Have a Look at it on the Map ***
    """)
    input("Press enter to visualize it...")
    print(H2)
    AnalyseArticles()
    AnalyseWordsCategories()
    input("Press enter to continue...")


def FrequencyAnalysis():
    print("\nHere's the frequency count for top 40 words in each article: - \n")
    for Name, file in Articles.items():
        print(f"Review Word Frequency for Hub {Name}")
        print(PrettyPrint(['word', 'Frequncy'], collections.Counter(file["wordFrequency"]).most_common(40),
                          [lambda x: x[0], lambda x: x[1]]))


def SentimentalPrint():
    print(
        "After analysing the words for its count, We rank them based on their positive & negative review.\nHere are the total results :-->")
    RawData.RankedSentiments = []
    for name, rank in Conclusion().items():
        RawData.RankedSentiments.append({'Hub': name, 'rank': rank[1], 'value': rank[0], 'Recommended': rank[2]})
    print(PrettyPrint(['Hub', 'Rank', 'Review', 'Recomended'],
                      RawData.RankedSentiments,
                      [lambda x: x['Hub'], lambda x: x['rank'], lambda x: 'POSITIVE' if x['value'] <= 0 else 'NEGATIVE',
                       lambda x: x['Recommended']]
                      ))
    print("Enter to initialise concluding graph...")
    PlotSentimentConclusion()
    input('Enter to continue..')


def FinalConclusion():
    print("Based on the distance Analysis & Sentimental Analysis,\nFollowing is the data otained:-")
    for customer, detail in CustomerData.items():
        print(f"Summary Table for Customer - {customer}")
        Final = NormaliseDataRanking(detail['RouteRank'], RawData.RankedSentiments, lambda x: x['Hub'],
                                     lambda x: x['DistanceTravelled'], lambda x: x['value'])
        detail['prev_route'], detail['route'] = detail['route'], Final[0]
        print(PrettyPrint(
            ['Hub', 'Distance Normalised', 'Reviews Normalised', 'Final Conclusion', 'Rank', 'Recomendation based'],
            Final,
            [lambda x: x['Hub'], lambda x: "{:.2f}".format(x['FinalDetails'][0]),
             lambda x: "{:.2f}".format(x['FinalDetails'][1]),
             lambda x: "{:.2f}".format(x['FinalDetails'][2]), lambda x: x['FinalDetails'][3],
             lambda x: x['FinalDetails'][4]]
        ))

    print("""
    Below is the Customer Summary Table to choose the best hub
    Distance is given weight 2, while reviews have been given 1
    """)
    print(PrettyPrint(
        ['Customer', 'Origin', 'Destination', 'Direct Distance', 'Hub (Distance Based)', 'Hub (Review Based)',
         'Hub (Final Recomendation)'],
        CustomerData.items(),
        [lambda x: 'Customer ' + x[0],
         lambda x: x[1]['Origin']['name'],
         lambda x: x[1]['Destination']['name'],
         lambda x: x[1]['DirectDistance']['text'],
         lambda x: x[1]['prev_route']['Hub'],
         lambda x: RawData.RankedSentiments[0]['Hub'],
         lambda x: x[1]['route']['Hub']]
    ))


print("""
 \t\t\t*** WELCOME TO HUBS DELIVERY SERVICE APPLICATION ***
        \t\t\tThe best customer service in town
Our Mission is to provide the best possible hub service to choose from so your parcel reach faster & in good health.
Well, don't believe it?
Let me take you through our application... \nPlease wait...\nDrum roll in 3..2..1
""")
PrintCustomer_Hubs()
time.sleep(1)
print("""
*** Okay, this all looks pretty complex to actually render out a solution. Let me simplify for you ***
Let us mark customer's origin as well as destination locations on map.
We also will be marking Hub locations for future Use.
""")
AddDirectDistanceMap()
print("""
\t\t Welcome Back, Let's Continue
Oki, Time to decide the best hub out there...hihi
""")
AvailableOptions()
print("""
Alright! Just to make sure, Making your parcel reach faster is not our only mission, We also ensure, your parcel reaches healthy & in good quality conditions
Let's look at companies, having the highest review rates
For an example, We took 3 articles from Internet about each company & collected the data to analyse it
""")
FrequencyAnalysis()
input("\nPress Enter to Plot Visualisation of bar graphs: ")
plotBarGraphs()
input("\nPress Enter to Continue: ")
SentimentalPrint()
FinalConclusion()
HNew = HubDeliveryMap(False)
HNew.MarkRoutesHubs()
print(HNew)
