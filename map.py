import folium
from media import Media, Descriptions, Layers
import pandas as pd

# Settings
icon_size = 40

media = Media()
desc = Descriptions()
layers = Layers()

data = pd.read_csv('F:/Users/Kie/Documents/Projects/new_world/db.csv', header=0)


class Mapping:

    def create_map(self):
        m = folium.Map(
            location=[27.9715098, -29.7763845],
            zoom_start=1.5
        )

        for index, row in data.iterrows():
            folium.Marker(
                location=[row['lat'], row['lon']],
                popup=folium.Popup(getattr(desc, row["text"]), max_width=200),
                icon=folium.features.CustomIcon(getattr(media, row['icon']), icon_size)
            ).add_to(getattr(layers, row['layer']))

        layers.layer_fauna.add_to(m)
        layers.layer_flora.add_to(m)
        layers.layer_ecosystem.add_to(m)
        layers.layer_melt.add_to(m)
        folium.LayerControl().add_to(m)

        return m

    def save_map(self, map):
        map.save('map.html')
