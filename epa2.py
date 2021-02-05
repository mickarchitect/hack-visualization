import numpy as np
import pandas as pd
import time
import streamlit as st
import pydeck as pdk

def map2(df, lat, lon, zoom) :
    column_layer = pdk.Layer(
        "ColumnLayer",
        id='map2_col_lyr',
        data=df,
        get_position=['Longitude', 'Latitude'],
        get_elevation='WATER_TOTAL_RELEASE',
        tooltip = {
                    "html": "<b>Value:</b> try typing a whole lot of stuff and see if that will help this show up {STATE_CODE} somewhere on the map and then keep typing <br/>",
                    "style": {
                        "backgroundColor": "steelblue",
                        "color": "white"}
                },
        auto_highlight=True,
        pickable=True,
        radius=5000)

    m2_deck = pdk.Deck(
    #st.write(pdk.Deck(
        column_layer,
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 20,
        }
        )
    st.pydeck_chart(m2_deck)

def map1(lat, lon, zoom) :
#    tot_col_lyr = pdk.Layer (
#            )

    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 20,
        }))

def display_page_intro() :
    map1(use_lat, use_lon, 3.1)
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
    
# Next: Isolate this and get help on tooltips, and interactivity

def display_page_air() :
    gl_tri_str = """
    The Toxics Release Inventory (TRI) tracks the management of over 650 toxic chemicals that pose a threat to human health and the environment. U.S. facilities in certain industry sectors that manufacture, process, or otherwise use these chemicals in amounts above established levels must report how each chemical is managed through recycling, energy recovery, treatment, and releases to the environment. A release of a chemical means that it is emitted to the air or water, or placed in some type of land disposal. The information submitted by facilities to the EPA and states is compiled annually as the Toxics Release Inventory or TRI, and is stored in a publicly accessible database in Envirofacts.
    """

    st.markdown(gl_tri_str)

    st_yr_2019_df = pd.read_csv("Data/st_yr_2019.csv")
#    rls_complt_raw = pd.read_csv("Data/releases_complete2.CSV")
#    use_columns = ['REPORTING_YEAR', 'STATE_ABBR', 'TOTAL_ON_OFF_SITE_RELEASE', 'WATER_TOTAL_RELEASE', 'LAND_TOTAL_RELEASE']
#    st_yr = rls_complt_raw[use_columns].groupby(['REPORTING_YEAR', 'STATE_ABBR'], as_index=False).sum()
#    
    st_lat_lon = pd.read_csv("Data/state_lat_lon.csv")
    st_yr_2019_lat_lon = st_yr_2019_df.merge(st_lat_lon, left_on='STATE_ABBR', right_on='State_Abbr')
    
    map2(st_yr_2019_lat_lon, use_lat, use_lon, 3)
    #st.write(st_yr_lat_lon.shape)
    return

def display_page_water() :
    st.markdown("# water stub for now")
    return

def display_page_land() :
    st.markdown("# land stub for now")
    return

def display_page_whatis() :
    st.markdown("### description stuff here")
    st.markdown("Sankey diagram here")
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

page = st.sidebar.radio('Select page:', ['Introduction-Totals', 'What-is-a-toxic-release', 'Air', 'Water', 'Land', 'Chemical-List-PFA', 'Chem-Non-PFA', 'TRI-NAICS'])
# later have a year choice
# later have a "totals" vs "occurrences" choice box(?), and use scatterplot for occurrences and column for totals

# Example locations
ctr_of_us_lat = 31.51073
use_lat = 34.51073
ctr_of_us_lon = -96.4247
use_lon = -97.4247

event_loop = True
ctr = 1
#while event_loop :

# Need to validate TRI acronym
st.title('Visualizing the EPA Toxic Releases Inventory (TRI) v2')

if page == 'Introduction-Totals' :
    display_page_intro()
elif page == 'What-is-a-toxic-release' :
    display_page_whatis()
elif page == 'Air' :
    display_page_air()
elif page == 'Water' :
    display_page_water()
elif page == 'Land' :
    display_page_land()
elif page == 'Chemical-List-PFA' :
    display_page_chem_pfa()
elif page == 'Chem-Non-PFA' :
    display_page_chem_non_pfa()
elif page == 'TRI-NAICS' :
    display_page_tri_naics()
