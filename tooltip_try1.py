import numpy as np
import pandas as pd
import time
import streamlit as st
import pydeck as pdk

use_lat = 34.51073
use_lon = -97.4247

st_yr_2019_df = pd.read_csv("Data/st_yr_2019.csv")
#st_yr_2019_df.shape
#st_yr_2019_df.columns
#time.sleep(10)

st.title('Visualizing the EPA Toxic Releases Inventory (TRI) v2')

view = pdk.data_utils.compute_view(st_yr_2019_df[["Longitude", "Latitude"]])
view.pitch = 75
view.bearing = 60

column_layer = pdk.Layer(
    "ColumnLayer",
    data=st_yr_2019_df,
    get_position=['Longitude', 'Latitude'],
    get_elevation='WATER_TOTAL_RELEASE',
    elevation_scale=100,
    radius=5000,
    pickable=True,
    auto_highlight=True)

#    tooltip = {
#                "html": "<b>Value:</b> try typing a whole lot     of stuff and see if that will help this show up {tooltip_fld} somewhere on the map and then keep typing <br/>",
#                "style": {
#                    "backgroundColor": "steelblue",
#                    "color": "white"}
#            },

m2_deck = pdk.Deck(
#    column_layer,
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view
    )

st.pydeck_chart(m2_deck)

#    tooltip = {
#                "html": "<b>Value:</b> try typing a whole lot     of stuff and see if that will help this show up {tooltip_fld} somewhere on the map and then keep typing <br/>",
#                "style": {
#                    "backgroundColor": "steelblue",
#                    "color": "white"}
#            },
#    initial_view_state={
#        "latitude": use_lat,
#        "longitude": use_lon,
#        "zoom": 3,
#        "pitch": 20
#    },
