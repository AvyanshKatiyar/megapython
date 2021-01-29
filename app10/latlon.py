import pandas
import geopy
import certifi
import ssl
from geopy.geocoders import ArcGIS
from soup import center_func

def latlon_func():
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx

    nom=ArcGIS()


    #n=nom.geocode("3995 23rd St, San Francisco, CA 94114")
    #this bit to create the html table
    data=pandas.read_csv("Sample.csv")

    if "Address" in data.columns:
        ad_col="Address"
    elif "address" in data.columns:
        ad_col="address"
    else:
        print("no")

    data["Coordinates"]=data[ad_col].apply(nom.geocode)
    data["Latitude"]=data["Coordinates"].apply(lambda x: x.latitude if x != None else None)
    data["Longitude"]=data["Coordinates"].apply(lambda x: x.longitude if x != None else None)
    data.drop("Coordinates",1, inplace=True)
    data.drop("Unnamed: 0",1, inplace=True)
    data.to_csv("edited.csv")
    data.to_html("templates/edited.html")

    center_func()


    print(data)

    #print(n.latitude)

