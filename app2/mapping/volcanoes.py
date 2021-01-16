import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
print(data)
lat=list(data["LAT"])
lon=list(data["LON"])
elevation=list(data["ELEV"])

#using zip to iterate through equal length lists 
# for i,j in zip([1,2,3],[4,5,6]):
#print(i,j)

#creates map object at 80,-100 
map=folium.Map(location=[38.58,-99.09], zoom_start=4,tiles="Stamen Terrain")
#zoom at start
#use tiles = "Stamen Terrain" changes background
fgv=folium.FeatureGroup(name="Volcanoes")
def returncolor(a):
    if a <1000:
        return "green"
    elif 1000<= a< 3000:
        return "orange"
    else:
        return "red"

fgp=folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat,lon, elevation):
 
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",
    fill_color= returncolor(el),color="grey",fill_opacity=0.7))

#add

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(), 
style_function = lambda x: {"fillColor":"green" if  x['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <=x['properties']['POP2005']<20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)

#after adding feature layer
#detects differenct festure groups
map.add_child(folium.LayerControl())

map.save("volc.html")
print(type(el))
#print(data.columns)
#print(data) 