from HubsLocator import HubDeliveryMap
from RawData import CourierCompanies, CustomerData
from Sentimental_Analysis import AnalyseArticles
from Matplot import plotBarGraphs

print("""
 *** WELCOME TO HUBS DELIVERY SERVICE APPLICATION ***
        The best customer service in town
""")


# Sentimental Analysis
AnalyseArticles()
plotBarGraphs()
