import webbrowser
import folium

CourierCompanies = {
    "City-link Express": {"name": "Port Klang", "location": (3.0319924887507144, 101.37344116244806), "icon": 'red'},
    "Pos Laju": {"name": "Petaling Jaya", "location": (3.112924170027219, 101.63982650389863), "icon": 'blue'},
    "GDEX ": {"name": "Batu Caves", "location": (3.265154613796736, 101.68024844550233), "icon": 'black'},
    "J&T": {"name": "Kajang", "location": (2.9441205329488325, 101.7901521759029), "icon": 'darkblue'},
    "DHL": {"name": "Sungai Buloh", "location": (3.2127230893650065, 101.57467295692778), "icon": 'purple'}
}

CustomerData = {
    "Customer A": {
        "Origin": {"name": "Rawang", "location": (3.3615395462207878, 101.56318183511695)},
        "Destination": {"name": "Bukit Jelutong", "location": (3.1000170516638885, 101.53071480907951)}
    },
    "Customer B": {
        "Origin": {"name": "Subang Jaya", "location": (3.049398375759954, 101.58546611160301)},
        "Destination": {"name": "Puncak Alam", "location": (3.227994355250716, 101.42730357605375)}
    },
    "Customer C": {
        "Origin": {"name": "Ampang", "location": (3.141855957281073, 101.76158583424586)},
        "Destination": {"name": "Cyberjaya ", "location": (2.9188704151716256, 101.65251821655471)}
    }
}


def auto_open_Map(path):
    html_page = f'{path}'
    myMap.save(html_page)
    webbrowser.open(html_page, new=2)


DEFAULT_LDN_COORDINATES = (3.1390, 101.6869)
myMap = folium.Map(location=DEFAULT_LDN_COORDINATES, zoom_start=11)
