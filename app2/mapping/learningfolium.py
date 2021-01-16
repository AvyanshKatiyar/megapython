import folium
import pandas
#creates map object at 80,-100 
map=folium.Map(location=[38.58,-99.09], zoom_start=6,tiles="Stamen Terrain")
#zoom at start


#ADDING MARKERS NEEDS LOCATIOP
#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Marker 1",icon=folium.Icon(color="green")))

#dir(folium.Map)
#use tiles = "Stamen Terrain" changes background
#or use feature groups to add features as children 
fg=folium.FeatureGroup(name="My map")

fg.add_child(folium.Marker(location=[38.2,-99.1], popup="Marker 1",icon=folium.Icon(color="green")))
#add multiple 
for coordinates in [[36.2,-99.1],[37.2,-97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Marker 1",icon=folium.Icon(color="lightred")))

map.add_child(fg)
map.save("Map1.html")

