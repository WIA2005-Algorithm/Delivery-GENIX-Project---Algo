from HubsLocator import HubDeliveryMap
from RawData import CourierCompanies, CustomerData
from Sentimental_Analysis import AnalyseArticles
from Matplot import plotBarGraphs

myMap1 = HubDeliveryMap(CourierCompanies=CourierCompanies, CustomerData=CustomerData)
myMap1.MarkDirectDistance()
myMap1.MarkLeastDistantPath()
print(myMap1)

# Sentimental Analysis
AnalyseArticles()
plotBarGraphs()
