import collections
import time

from ConclusionPlot import PlotSentimentConclusion
from CusHubsMap import HubDeliveryMap, PreProcess
from RawData import CourierCompanies, CustomerData, Articles
from Sentimental_Analysis import AnalyseArticles, AnalyseWordsCategories, Conclusion
from Matplot import plotBarGraphs

print("""
 \t\t\t*** WELCOME TO HUBS DELIVERY SERVICE APPLICATION ***
        \t\t\tThe best customer service in town

Our Mission is to provide the best possible hub service to choose from so your parcel reach faster & in good health.
Well, don't believe it?
Let me take you through our application... \nPlease wait...\nDrum roll in
""")
time.sleep(0.5)
print("3...")
time.sleep(0.5)
print("2...")
time.sleep(0.5)
print("1..")
time.sleep(0.5)
print("\nFirst of all let us analysis our customers & their requirements: \n")
c = 1
for cus, detail in CustomerData.items():
    print(
        f"Our Customer {c} {cus.upper()}, lives in {detail['Origin']['name']} & wants to deliver a parcel at {detail['Destination']['name']}")
    c += 1

time.sleep(1)
print("\nAvailable Hubs are: \n")
c = 1
for Hub, detail in CourierCompanies.items():
    print(f"Our Hub {c} - {Hub} is situated in {detail['name']}")
    c += 1
time.sleep(1)
print("""
*** Okay, this all looks pretty complex to actually render out a solution. Let me simplify for you ***
Let us mark customer's origin as well as destination locations on map.
We also will be marking Hub locations for future Use.
""")
print("Please wait while the resources load...APIs do take time sometime due to internet connection problems...")
PreProcess()
H = HubDeliveryMap()
print("""
*** Now Let's Mark a Direct Distance between the Customer Origin & Destination Locations ***\n
""")
H.MarkLeastDistantPath()
for cus, detail in CustomerData.items():
    print(
        f"Customer {cus} :->  {detail['Origin']['name']} <-> {detail['Destination']['name']} :> Distance = {detail['DirectDistance']} Km")

print("""
Alright, Time for Some Visuals... Let's Goo
Hint: Click on the symbols to view more details
""")
input("Press Enter to visualize it...")
print(H)
input("Press Enter to continue...")
print("""
*** Welcome Back, Let's Continue***
Oki, Time to decide the best hub out there...hihi
""")
for name, detail in CustomerData.items():
    print(f"Customer {name} has these available options:- \n")
    c = 1
    for hub in detail["RouteRank"]:
        print(f"Hub {hub['hub']} will take <{hub['DistanceTravelled']} Km> to transfer the parcel", "- BEST CHOICE" if c == 1 else "")
        c += 1
    print("")
H2 = HubDeliveryMap(False)
H2.MarkRoutesHubs()
for cus, detail in CustomerData.items():
    print(
        f"According to the analytics :> Customer {cus} :->  {detail['Origin']['name']} <-> {detail['Destination']['name']} will use {detail['route']['Hub']} covering a total route distances of {detail['route']['DistanceTravelled']} Km")

print("""
*** Let's Have a Look at it on the Map ***
""")
input("Press Enter to visualize it...")
print(H2)
AnalyseArticles()
AnalyseWordsCategories()
input("Press Enter to continue...")

print(""" 
Alright! Just to make sure, Making your parcel reach faster is not our only mission, We also ensure, your parcel reaches healthy & in good quality conditions
Let's look at companies, having the highest review rates
For an example, We took 3 articles from Internet about each company & collected the data to analyse it 
""")
print("Here's the frequency count for top 40 words in each article: - \n")
for name, file in Articles.items():
    print(name, " --> ", collections.Counter(file["wordFrequency"]).most_common(40))
input("\nPress Enter to Plot Visualisation of bar graphs: ")
plotBarGraphs()
input("\nPress Enter to Continue: ")
print("""
After analysing the words for its count, We rank them based on their positive & negative review
Here are the total results :-->
""")
c = 1
for name, rank in Conclusion().items():
    print(
        f"{name} has acquired a rank {c} among quality assurance with {'POSITIVE' if rank >= 0 else 'NEGATIVE'} review")
    c += 1
print("Enter to initialise concluding graph...")
PlotSentimentConclusion()

