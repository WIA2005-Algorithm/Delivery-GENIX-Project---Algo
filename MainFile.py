from HubsLocator import HubDeliveryMap
from RawData import CourierCompanies, CustomerData, Articles
from Sentimental_Analysis import ReadFile


def HubLocation(hub):
    return CourierCompanies[hub]['location']


def CPLocation(customer):
    return CustomerData[customer]['Origin']['location'], CustomerData[customer]['Destination']['location']


# myMap1 = HubDeliveryMap(CourierCompanies=CourierCompanies, CustomerData=CustomerData)
# myMap1.MarkDirectDistance()
# myMap1.MarkLeastDistantPath()
# print(myMap1)

# Sentimental Analysis
ReadFile()



