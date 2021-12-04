import folium
import pandas

data = pandas.read_csv("archivos/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[40.482792,-3.697634], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("archivos/maps/Map1.html")