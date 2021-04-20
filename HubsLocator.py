from MainRawData import *
from geopy.distance import geodesic

# Example Using geopy
# newport_ri = (41.49008, -71.312796)
# cleveland_oh = (41.499498, -81.695391)
# print(geodesic(newport_ri, cleveland_oh).miles)


def addHubMarkers():
    for Hub, detail in CourierCompanies.items():
        folium.Marker(
            location=detail["location"],
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{detail['name']} - {Hub}</div>",
            tooltip=f"HUB - {Hub}",
            icon=folium.Icon(icon='truck', prefix='fa', color=detail['icon'])
        ).add_to(myMap)


def CustomerParcel(customer, data, Position='Origin'):
    folium.Marker(
        location=data[Position]['location'],
        popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{customer} - {data[Position]['name']}<br>({Position}) </div>",
        tooltip=f"{Position} - {customer}",
        icon=folium.Icon(icon='user', prefix='fa', color=data['icon'])
    ).add_to(myMap)


def minimumCoordinates(origin):
    best = 1000
    Coordinates = origin
    for hubs in CourierCompanies.values():
        curr = geodesic(origin, hubs['location']).kilometers
        if curr < best:
            best = curr
            Coordinates = hubs['location']
    return Coordinates


def function():
    xoxox = [34, 345, 5, 56]


# Type out the code to mark the origin and destination similar to above code with different icon
def addCustomerMarkers():
    for customer, data in CustomerData.items():
        CustomerParcel(customer, data)
        CustomerParcel(customer, data, 'Destination')
        folium.PolyLine(
            [data['Origin']['location'], minimumCoordinates(data['Origin']['location']), data['Destination']['location']],
            color=data['icon'],
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{data['Origin']['name']} to {data['Destination']['name']}<br>({geodesic(data['Origin']['location'], data['Destination']['location']).kilometers:.2f} Km) </div>",
            tooltip=f"{customer}",
            weight=6
        ).add_to(myMap)


# NOT SURE OF THIS
# def Door_to_Door_Distance():
#     for customer, data in CustomerData.items():
#         print(customer, f"--> Distance from {data['Origin']['name']} to {data['Destination']['name']} is", geodesic(data['Origin']['location'], data['Destination']['location']).kilometers, "Km")


addHubMarkers()
addCustomerMarkers()
auto_open_Map('HubsLocator.html')
