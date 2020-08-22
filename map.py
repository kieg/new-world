import folium
from media import Media, Descriptions
import pandas as pd

# Settings
icon_size = 40

media = Media()
desc = Descriptions()

# data = pd.read_csv('F:/Users/Kie/Documents/Projects/new_world')

class Mapping:

    def create_map(self):
        m = folium.Map(
            location=[-11.5906166, 144.0332089],
            zoom_start=3
        )

        layer_fauna = folium.FeatureGroup(name='Fauna')
        layer_flora = folium.FeatureGroup(name='Flora')
        layer_ecosystem = folium.FeatureGroup(name='Ecosystem')
        layer_melt = folium.FeatureGroup(name='Melting Ice')


        folium.Marker(
            location=[-11.5906166, 144.0332089],
            popup=folium.Popup(desc.desc_turtle, max_width=200),
            icon=folium.features.CustomIcon(media.icon_url_turtle, icon_size)
        ).add_to(layer_fauna)

        folium.Marker(
            location=[30.4416033, -91.1814585],
            popup=folium.Popup(desc.desc_flood, max_width=200),
            icon=folium.features.CustomIcon(media.icon_url_flood, icon_size)
        ).add_to(layer_ecosystem)

        folium.Marker(
            location=[48.62305328822785, -113.76222200000001],
            popup=folium.Popup(desc.desc_glacier_sperry, max_width=200),
            icon=folium.features.CustomIcon(media.icon_url_glacier, icon_size)
        ).add_to(layer_melt)


        layer_fauna.add_to(m)
        layer_flora.add_to(m)
        layer_ecosystem.add_to(m)
        layer_melt.add_to(m)
        folium.LayerControl().add_to(m)

        return m

    def save_map(self, map):
        map.save('map.html')
