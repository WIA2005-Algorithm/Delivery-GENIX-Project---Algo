import webbrowser
import folium
from folium import plugins
from geopy.distance import geodesic


class HubDeliveryMap:
    def __init__(self, CourierCompanies, CustomerData):
        self.myMap = plugins.DualMap(location=(3.1390, 101.6869), zoom_start=11)
        self.CourierCompanies = CourierCompanies
        self.CustomerData = CustomerData

    def addMarker(self, location, popupText, hoverText, Icon, iconColour):
        folium.Marker(
            location=location,
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{popupText}</div>",
            tooltip=hoverText,
            icon=folium.Icon(icon=Icon, prefix='fa', color=iconColour)
        ).add_to(self.myMap)

    def addHub(self):
        for Hub, detail in self.CourierCompanies.items():
            self.addMarker(detail["location"], f"{detail['name']} - {Hub}", f"HUB - {Hub}", 'truck', detail['icon'])
        self.addCustomer()

    def addCustomer(self):
        for customer, data in self.CustomerData.items():
            self.addMarker(data['Origin']['location'], f"{customer} - {data['Origin']['name']}<br>(Origin) ",
                           f"Origin - {customer}", 'user', data['icon'])
            self.addMarker(data['Destination']['location'],
                           f"{customer} - {data['Destination']['name']}<br>(Destination) ",
                           f"Destination - {customer}", 'user', data['icon'])

    def minimumFromOrigin(self, origin):
        best = 1000
        Coordinates = origin
        for hubs in self.CourierCompanies.values():
            curr = geodesic(origin, hubs['location']).kilometers
            if curr < best:
                best = curr
                Coordinates = hubs['location']
        return Coordinates

    def minimumFromDistance(self, origin, destination):
        best = 1000
        coordinates = origin
        for hubs in self.CourierCompanies.values():
            curr = geodesic(origin, hubs['location']).kilometers + geodesic(destination, hubs['location']).kilometers
            if curr < best:
                best = curr
                coordinates = hubs['location']
        return coordinates

    def addPolyLines(self, Map):
        m1 = True if Map == self.myMap.m1 else False
        for customer, data in self.CustomerData.items():
            if m1:
                coordinates = self.minimumFromOrigin(data['Origin']['location'])
            else:
                coordinates = self.minimumFromDistance(data['Origin']['location'], data['Destination']['location'])
            folium.PolyLine(
                [data['Origin']['location'], coordinates,
                 data['Destination']['location']],
                color=data['icon'],
                popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{data['Origin']['name']} to {data['Destination']['name']}<br>({geodesic(data['Origin']['location'], data['Destination']['location']).kilometers:.2f} Km) </div>",
                tooltip=f"{customer}",
                weight=4
            ).add_to(Map)

    def __str__(self):
        html_page = 'HubsLocator.html'
        self.myMap.save(html_page)
        webbrowser.open(html_page, new=2)
        return "Successfully Opened HubsLocator.html"




# NOT SURE OF THIS
# def Door_to_Door_Distance():
#     for customer, data in CustomerData.items():
#         print(customer, f"--> Distance from {data['Origin']['name']} to {data['Destination']['name']} is", geodesic(data['Origin']['location'], data['Destination']['location']).kilometers, "Km")


