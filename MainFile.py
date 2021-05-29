import time

from CusHubsMap import HubDeliveryMap, PreProcess
from RawData import CourierCompanies, CustomerData
# from Sentimental_Analysis import AnalyseArticles
from Matplot import plotBarGraphs


def Continue():
    input("Please Enter Key to Continue....")


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
H2 = HubDeliveryMap(False)
time.sleep(1)
print("""
*** Now Let's Mark a Direct Distance between the Customer Origin & Destination Locations ***\n
""")
H.MarkLeastDistantPath()
time.sleep(1)
for cus, detail in CustomerData.items():
    print(f"Customer {cus} :->  {detail['Origin']['name']} <-> {detail['Destination']['name']} :> Distance = {detail['DirectDistance']} Km")

time.sleep(1)
print("""
Alright, Time for Some Visuals... Let's Goo
Hint: Click on the symbols to view more details
""")
Continue()
print(H)
Continue()
print("""
*** Welcome Back, Let's Continue***
Oki, Time to decide the best hub out there...hihi
""")
H2.MarkRoutesHubs()
for cus, detail in CustomerData.items():
    print(f"According to the analytics :> Customer {cus} :->  {detail['Origin']['name']} <-> {detail['Destination']['name']} will use {detail['route']['Hub']} covering a total route distances of {detail['route']['DistanceTravelled']} Km")

time.sleep(1)
print("""
*** Let's Have a Look at it on the Map ***
""")
Continue()
print(H2)
Continue()

# Sentimental Analysis
# AnalyseArticles()
# plotBarGraphs()
