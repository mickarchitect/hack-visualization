import numpy as np
import pandas as pd
import time
import streamlit as st
import pydeck as pdk

# Example locations
ctr_of_us_lat = 31.51073
use_lat = 34.51073
ctr_of_us_lon = -96.4247
use_lon = -97.4247

# Need to validate TRI acronym
st.title('Visualizing the EPA Toxic Releases Inventory (TRI) v2')

def map(lat, lon, zoom) :
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 20,
        }))

# Phase 1 - Map and Totals

map(use_lat, use_lon, 3.1)
gl_tot_str = """
## Some Starting Facts
- Year: 2020
- Total Toxic Releases to:
    - Air: 
    - Water:
    - Land:

### But what is a Toxic Release
"""
st.markdown(gl_tot_str)
time.sleep(5)

gl_tri_str = """
The Toxics Release Inventory (TRI) tracks the management of over 650 toxic chemicals that pose a threat to human health and the environment. U.S. facilities in certain industry sectors that manufacture, process, or otherwise use these chemicals in amounts above established levels must report how each chemical is managed through recycling, energy recovery, treatment, and releases to the environment. A “release” of a chemical means that it is emitted to the air or water, or placed in some type of land disposal. The information submitted by facilities to the EPA and states is compiled annually as the Toxics Release Inventory or TRI, and is stored in a publicly accessible database in Envirofacts.
"""

st.markdown(gl_tri_str)
