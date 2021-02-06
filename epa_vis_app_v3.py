import numpy as np
import pandas as pd
import time
import streamlit as st
import pydeck as pdk
import plotly.graph_objects as go


def map2(df, lat, lon, zoom) :
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=df,
        get_position=['Longitude', 'Latitude'],
        get_elevation='WATER_TOTAL_RELEASE',
        #elevation_scale=100,
        radius=5000,
        pickable=True,
        auto_highlight=True,
        )

    tooltip = {
        "html": "<b> {tooltip_fld} </b>",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }

    m2_deck = pdk.Deck(
        column_layer,
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 20,
        },
        tooltip=tooltip,
        map_provider='mapbox',
        map_style="mapbox://styles/mapbox/light-v9",
        )
    st.pydeck_chart(m2_deck)

def display_page_intro() :
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
    
def display_page_air() :
    gl_tri_str = """
    The Toxics Release Inventory (TRI) tracks the management of over 650 toxic chemicals that pose a threat to human health and the environment. U.S. facilities in certain industry sectors that manufacture, process, or otherwise use these chemicals in amounts above established levels must report how each chemical is managed through recycling, energy recovery, treatment, and releases to the environment. A release of a chemical means that it is emitted to the air or water, or placed in some type of land disposal. The information submitted by facilities to the EPA and states is compiled annually as the Toxics Release Inventory or TRI, and is stored in a publicly accessible database in Envirofacts.
    """

    st.markdown(gl_tri_str)
    st_yr_2019_df = pd.read_csv("Data/st_yr_2019.csv")
    #st_lat_lon = pd.read_csv("Data/state_lat_lon.csv")
    #st_yr_2019_lat_lon = st_yr_2019_df.merge(st_lat_lon, left_on='STATE_ABBR', 
    #                                         right_on='State_Abbr')
    #st.write(st_yr_2019_df.columns)
    #st.write(st_yr_2019_lat_lon.columns)
    #time.sleep(20)
    map2(st_yr_2019_df, use_lat, use_lon, 3)
    return

def display_page_whatis() :
    st.markdown("## Summary")
    st.markdown("""
- Tracks management of certain toxic chemicals
  - U.S. Company "Facilities" in different industry sectors
  - Annually report how much of each chemical is managed through recycling, energy recovery and treatment
  - And how much is released to the environment
  - [EPA What is TRI Page](https://www.epa.gov/toxics-release-inventory-tri-program/what-toxics-release-inventory)
                """)
    st.markdown("## Example - 2019 Totals and Dispositions")
    st.markdown("""
- From the [2019 TRI National Analysis](https://www.epa.gov/trinationalanalysis/introduction-2019-tri-national-analysis-0)
- Most of the Waste is managed - recycled, recovered or treated.
- The remaining is the amount "Disposal or Other Releases" - which this application focuses on.
- The Disposal or Other Releases flows On or Off Site.
- On Site flows to Land/Water/Air
- Off Site flows to various other sources
- The graph below shows these flows
                """)

    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = 'black', width = 0.5),
            label = ["Total Waste Managed", "Recycling", "Energy Recovery", "Treatment",     # 0, 1, 2, 3
                     "Disposal or Other Releases", "On-Site", "Off-Site",                    # 4, 5, 6
                     "AIR", "WATER", "LAND", "Landfill-Surf",                                # 7, 8, 9, 10
                     "Storage", "Underground Injection"],                                    # 11, 12
            color = "blue"
        ),
        link = dict(
            source = [0, 0, 0, 0, 4, 4, 5, 5, 5, 6, 6, 6],
            target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            value = [15500,7700,3070, 2900, 2900, 430, 600, 200, 2160, 100, 100, 100]
        ))])

    fig.update_layout(hovermode='x', title_text="2019 Totals", font_size=16, 
                  height=1000, width=1000)
    st.write(fig)
    st.markdown("## This app focuses on 'Disposal or Other Releases'")
    return

def display_page_chem_pfa() :
    q = pd.read_csv("Data/chem_pfa.csv")
    chem_pfa_df = q.drop('Chemical Structure', axis=1)
    st.markdown('## Chemical (PFA) Listing')
    st.write(chem_pfa_df)
    return

def display_page_chem_non_pfa() :
    q = pd.read_csv("Data/chem_non_pfa.csv")
    chem_non_pfa_df = q.drop('Chemical Structure', axis=1)
    st.markdown('## Chemical (Non-PFA) Listing')
    st.write(chem_non_pfa_df)
    return

def display_page_tri_naics() :
    tri_naics_df = pd.read_csv("Data/TRI_Covered_NAICS_Codes.csv")
    st.markdown('## TRI Covered NAICS Codes Listing')
    st.write(tri_naics_df)
    return

######################################################################
# Main
######################################################################

page = st.sidebar.radio('Select page:', ['Introduction', 
                                         'What is the toxic release inventory', 
                                         'Main-View', 
                                         'List-Chemicals-PFA', 
                                         'List-Chem-Non-PFA', 
                                         'List-TRI-NAICS'])
# later have a year choice
# later have a state choice - could do a lot more there

# Example locations
ctr_of_us_lat = 31.51073
use_lat = 34.51073
ctr_of_us_lon = -96.4247
use_lon = -97.4247

# Need to validate TRI acronym
st.title('Visualizing the EPA Toxics Release Inventory (TRI)')

if page == 'Introduction' :
    display_page_intro()
elif page == 'What is the toxic release inventory' :
    display_page_whatis()
elif page == 'Main-View' :
    display_page_air()
elif page == 'List-Chemicals-PFA' :
    display_page_chem_pfa()
elif page == 'List-Chem-Non-PFA' :
    display_page_chem_non_pfa()
elif page == 'List-TRI-NAICS' :
    display_page_tri_naics()
