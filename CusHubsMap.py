import webbrowser

import API_KEY
import Algorithms
import gmplot
import requests
from RawData import CourierCompanies, CustomerData


class PreProcess:
    def __init__(self):
        self.API_KEY = API_KEY.API_KEY
        self.DirectionsAPI = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        self.PreProcessDirectDistance()
        self.PreProcessCustomerDeliveryHubs()

    # Common Function to Calculate Distance between 2 or 3 Locations
    def CalculateDistance(self, origin, destination):
        request = f"origins={','.join(map(str, origin))}&destinations={','.join(map(str, destination))}&key={self.API_KEY}"
        return requests.get(self.DirectionsAPI + request).json()['rows'][0]['elements'][0]['distance']

    # Function to calculate the best hub among the given hubs to transfer package between given locations
    def CalculateBestHub(self, origin, Destination):
        HubRanks = Algorithms.QuickSortAlgo([{'Hub': name, 'name': Hubs['name'], 'HubCoordinates': Hubs['location'],
                                              'DistanceTravelled': float(
                                                  (self.CalculateDistance(origin, Hubs['location'])['value']) + (
                                                      self.CalculateDistance(Hubs['location'], Destination)[
                                                          'value'])) / 1000} for
                                             name, Hubs in CourierCompanies.items()],
                                            key=lambda x: x["DistanceTravelled"])
        for i in range(len(HubRanks)):
            HubRanks[i]['Recommended'] = '\u2705' if i == 0 else '\u274C'
        return HubRanks[0], HubRanks

    # Function to Calculate Distance between Customer Origin & Customer Destination
    def PreProcessDirectDistance(self):
        for name, customer in CustomerData.items():
            customer['DirectDistance'] = self.CalculateDistance(customer["Origin"]["location"],
                                                                customer["Destination"]["location"])

    # Function to Calculate Hubs each Customers will transfer there package from
    def PreProcessCustomerDeliveryHubs(self):
        for name, customer in CustomerData.items():
            customer['route'], customer['RouteRank'] = self.CalculateBestHub(customer["Origin"]["location"],
                                                                             customer["Destination"]["location"])


class HubDeliveryMap:
    def __init__(self, Permission=True):
        self.API_KEY = "AIzaSyCvn0ce0DhkRist0XmM4llOrwc6moS9ePc"
        self.info_box_template = """
        <dl>
        <div style="text-align:center;font-size: 16px;margin-bottom: 10px;color: red;"> <b>{Type}</b> </div>
        <span><b>Name: </b> {name}</span>
        <br>
        <span><b>Location: </b> {location}</span>
        <div style="text-align:center;font-size: 14px;margin-top: 8px;color: red;"> <b>{AddContent}</b> </div>
        </dl>
        """
        self.HubIconURL = 'https://i.postimg.cc/63S7TpWH/location-pin.png'
        self.CusIconURL = 'http://image.flaticon.com/icons/svg/252/252025.svg'
        self.Permission = Permission
        self.Map = gmplot.GoogleMapPlotter(3.1390, 101.6869, 13, apikey=self.API_KEY, title="Hub Delivery Service")
        self.HTML_PAGE = ('MAP_P1' if Permission else 'MAP_P2') + '.html'
        self.addHubMarker()
        self.addCustomerMarker()

    # Common Function to add Marker for respective locations given
    def addMarker(self, coordinates, MarkerName, MarkerLocation, ICON=None, Type='Customer', AContent=''):
        self.Map.marker(coordinates[0], coordinates[1], title=f"{MarkerName} - {MarkerLocation}",
                        info_window=self.info_box_template.format(Type=Type, name=MarkerName, location=MarkerLocation,
                                                                  AddContent=AContent),
                        IconURL=(ICON or self.CusIconURL))

    def addHubMarker(self):
        for name, Hubs in CourierCompanies.items():
            self.addMarker(Hubs['location'], name, Hubs['name'], self.HubIconURL, 'Delivery Hub')

    def addCustomerMarker(self):
        for name, customer in CustomerData.items():
            content = f"Direct Distance: {customer['DirectDistance']['text']}" if self.Permission else f"Passing through - {customer['route']['Hub']} <br> Total Distance: {customer['route']['DistanceTravelled']} Km"
            self.addMarker(customer["Origin"]["location"], name + " (Origin)", customer['Origin']['name'],
                           AContent=content)
            self.addMarker(customer["Destination"]["location"], name + " (Destination)",
                           customer['Destination']['name'], AContent=content)

    def PlotRoute(self, origin, destination, color, WayPoint=None):
        if WayPoint is None:
            WayPoint = []
        self.Map.directions(origin, destination, strokeColor=color, waypoints=WayPoint)

    def MarkLeastDistantPath(self):
        for name, customer in CustomerData.items():
            self.PlotRoute(customer["Origin"]["location"], customer["Destination"]["location"], customer['color'])

    def MarkRoutesHubs(self):
        for name, customer in CustomerData.items():
            self.PlotRoute(customer["Origin"]["location"], customer
            ["Destination"]["location"], customer['color'],
                           WayPoint=[customer['route']['HubCoordinates']])

    def __str__(self):
        self.Map.draw(self.HTML_PAGE)
        webbrowser.open(self.HTML_PAGE, new=1)
        return "\nSuccessfully Opened Page In Web Browser\n"
