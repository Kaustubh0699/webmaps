import folium
import pandas
data = pandas.read_csv("Volcanoes_USA.txt")
lon =list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
location = list(data["LOCATION"])
status = list(data["STATUS"])
elev = list(data["ELEV"])

def color_decider(elev):
    if(elev < 2000):
        return "green"
    elif(elev >=2000 and elev <=2500):
        return "orange"
    else:
        return "red"



map = folium.Map(location=[34.55,78.98],zoom_start=6,tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes_USA")
for i in range(1,len(lon)):
    details = str(name[i]) + " ," +str(location[i]) + "\n" + str(status[i])
    fgv.add_child(folium.CircleMarker(location=[lat[i],lon[i]],radius=6,popup=details,fill_color=color_decider(elev[i]),color = "grey",fill_opacity =0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data = open("world.json","r",encoding="utf-8-sig").read(),
                            style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                                                      else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")