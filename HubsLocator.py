import webbrowser
import folium
from geopy.distance import geodesic


class HubDeliveryMap:
    def __init__(self, CourierCompanies, CustomerData):
        self.myMap = folium.Map(location=(3.1390, 101.6869), zoom_start=11)
        self.CourierCompanies = CourierCompanies
        self.CustomerData = CustomerData
        # Add Hub Markers
        self.addHub()
        # Add Customer Markers (Origin & Destination)
        self.addCustomer()

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

    def addCustomer(self):
        for customer, data in self.CustomerData.items():
            self.addMarker(data['Origin']['location'], f"{customer} - {data['Origin']['name']}<br>(Origin) ",
                           f"Origin - {customer}", 'user', data['icon'])
            self.addMarker(data['Destination']['location'],
                           f"{customer} - {data['Destination']['name']}<br>(Destination) ",
                           f"Destination - {customer}", 'user', data['icon'])

    def MarkDirectDistance(self):
        for customer, data in self.CustomerData.items():
            data['directDistance'] = geodesic(data['Origin']['location'], data['Destination']['location'])
            folium.PolyLine(
                locations=[data['Origin']['location'], data['Destination']['location']],
                color=data['icon'],
                popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{data['Origin']['name']} to {data['Destination']['name']}<br>({data['directDistance'].kilometers:.2f} Km) </div>",
                tooltip=f"{customer}",
                weight=4
            ).add_to(self.myMap)

    def __str__(self):
        html_page = 'HubsLocator.html'
        self.myMap.save(html_page)
        webbrowser.open(html_page, new=2)
        return "Successfully Opened HubsLocator.html"
