import geopandas as gpd
import folium
from branca.colormap import LinearColormap
import plotly.express as px

def createDiscreteMap(dataframe, columnName, values = [], colors = []):
    lambert = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.X, dataframe.Y), crs="EPSG:3949")
    wgs84 = lambert.to_crs(epsg=4326)
    wgs84[columnName] = wgs84[columnName].astype(str)
    fig = px.scatter_map(wgs84,
                         lat=wgs84.geometry.y,
                         lon=wgs84.geometry.x,
                         color=columnName,
                         color_discrete_map={str(val): colors[i] for i, val in enumerate(values)},
                         size_max=15,
                         zoom=10)
    fig.show() 


def createContinuousMap(dataframe, columnName, colors = []):
    lambert = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.X, dataframe.Y), crs="EPSG:3949")
    wgs84 = lambert.to_crs(epsg=4326)
    wgs84[columnName] = wgs84[columnName].astype(float)
    fig = px.scatter_map(wgs84,
                         lat=wgs84.geometry.y,
                         lon=wgs84.geometry.x,
                         color=columnName,
                         color_continuous_scale=colors,
                         size_max=15,
                         zoom=10)    
    fig.show()