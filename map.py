import geopandas as gpd
import folium
from branca.colormap import LinearColormap

def createDiscreteMap(dataframe, columnName, mapName, values = [], labels = [], colors = []):
    lambert = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.X, dataframe.Y), crs="EPSG:3949")
    wgs84 = lambert.to_crs(epsg=4326)
    new_map = folium.Map(zoom_start = 13, tiles = 'cartodb.positron')
    coord_list = [[point.xy[1][0], point.xy[0][0]] for point in wgs84.geometry]
    i = 0
    for coordinates in coord_list:
        j = 0
        for val in values:
            if wgs84[columnName][i] == val:
                new_map.add_child(
                    folium.CircleMarker(
                        location=coordinates,
                        radius=2,
                        weight=5,
                        popup=labels[j],
                        color=colors[j]
                    )
                )
                break;
            else:
                j = j + 1 
        i = i + 1

    new_map.fit_bounds(new_map.get_bounds())
    new_map.save(mapName + '.html')


def createContinuousMap(dataframe, columnName, mapName, minVal, maxVal, colors = []):
    colormap = LinearColormap(colors=colors, vmin=minVal, vmax=maxVal)
    lambert = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.X, dataframe.Y), crs="EPSG:3949")
    wgs84 = lambert.to_crs(epsg=4326)
    new_map = folium.Map(zoom_start = 13, tiles = 'cartodb.positron')
    coord_list = [[point.xy[1][0], point.xy[0][0]] for point in wgs84.geometry]
    i = 0
    for coordinates in coord_list:
        new_map.add_child(
            folium.CircleMarker(
                location=coordinates,
                radius=2,
                weight=5,
                popup=wgs84[columnName].iloc[i],
                color=colormap(wgs84[columnName].iloc[i])
            )
        )
        i = i + 1

    new_map.add_child(colormap)
    new_map.fit_bounds(new_map.get_bounds())
    new_map.save(mapName + '.html')