import webbrowser
import folium
from folium import plugins
from geopy.distance import geodesic


class HubDeliveryMap:
    def __init__(self, CourierCompanies, CustomerData):
        self.myMap = plugins.DualMap(location=(3.1390, 101.6869), zoom_start=11)
        self.CourierCompanies = CourierCompanies
        self.CustomerData = CustomerData
        self.addHub()
        self.addCustomer()

    def addMarker(self, location, popupText, hoverText, Icon, iconColour):
        folium.Marker(
            location=location,
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{popupText}</div>",
            tooltip=hoverText,
            icon=folium.Icon(icon=Icon, prefix='fa', color=iconColour)
        ).add_to(self.myMap)

    def addPolyLine(self, locations, color, popupText, hoverText, m):
        folium.PolyLine(
            locations=locations,
            color=color,
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{popupText} Km) </div>",
            tooltip=hoverText,
            weight=4
        ).add_to(m)

    def addHub(self):
        for Hub, detail in self.CourierCompanies.items():
            self.addMarker(detail["location"], f"{detail['name']} - {Hub}", f"HUB - {Hub}", 'truck', detail['icon'])

    def addCustomer(self):
        for customer, data in self.CustomerData.items():
            self.addMarker(data['Origin']['location'], f"{customer} - {data['Origin']['name']}<br>(Origin) ",
                           f"Origin - {customer}", 'user', data['icon'])
            self.addMarker(data['Destination']['location'],
                           f"{customer} - {data['Destination']['name']}<br>(Destination) ",
                           f"Destination - {customer}", 'user', data['icon'])

    def MarkDirectDistance(self):
        for customer, data in self.CustomerData.items():
            data['directDistance'] = geodesic(data['Origin']['location'], data['Destination']['location']).kilometers
            self.addPolyLine(
                [data['Origin']['location'], data['Destination']['location']],
                data['icon'], f"{data['Origin']['name']} to {data['Destination']['name']}<br>({data['directDistance']:.2f}",
                customer,
                self.myMap.m1
            )

    def CalculateLeastDistance(self, origin, destination):
        return min(
            [{'Hub': Hub, 'TotalHubDistance': geodesic(origin, detail['location'], destination).kilometers, 'HubCoordinates': detail['location']} for Hub, detail in self.CourierCompanies.items()],
            key=lambda d: d['TotalHubDistance']
        )

    def MarkLeastDistantPath(self):
        for customer, data in self.CustomerData.items():
            data['LeastHub'] = self.CalculateLeastDistance(data['Origin']['location'], data['Destination']['location'])
            self.addPolyLine(
                [data['Origin']['location'],  data['LeastHub']['HubCoordinates'], data['Destination']['location']],
                data['icon'],
                f"{data['Origin']['name']} to {data['Destination']['name']}<br> through {data['LeastHub']['Hub']} ({data['directDistance']:.2f}",
                customer,
                self.myMap.m2
            )

    def __str__(self):
        html_page = 'HubsLocator.html'
        self.myMap.save(html_page)
        webbrowser.open(html_page, new=2)
        return "Successfully Opened HubsLocator.html"
