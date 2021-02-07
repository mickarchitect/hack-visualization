import numpy as np
import pandas as pd
import time
import streamlit as st
import pydeck as pdk
import plotly.graph_objects as go

def display_page_united_states() :
    st_yr_df = pd.read_csv("Data/st_yr_lat_lon_tt.csv")
    map3(st_yr_df, use_lat, use_lon, 3)
    return

def display_page_state_view() :
    st.markdown("## State View")
    return

def display_page_about() :
    st.markdown("## About")
    st.markdown("### About the App")
    st.markdown('- This app was created in response to the USA Facts Data Challenge and Visualization Challenge.')
    st.markdown('- The USA Facts mission is about making U.S. government data accessible and understandable.')
    st.markdown('- The Challenge was focused on Environmental data.')
    st.markdown('- One specific piece was on EPA Strategic Goals, and many of those goals were about toxic releases to the environment.')
    st.markdown('- After researching a lot of EPA data during the Data Challenge, I settled on the Toxics Release Inventory data for the Visualization Challenge.')
    st.markdown('### Excuses')
    st.markdown('- This app is not ready for use nor ready for presentation')
    st.markdown('- The exciting features still are not here at all - a state view with more detail, a time lapse for perspective')
    st.markdown('- And the features that are here are incomplete - no real colors, very surface level data validation, ...')
    st.markdown("### About the Data")
    st.markdown('- For TRI Data, there is an EZ Search and a fully Customizable Report Download.  The fully Customizable Report Download has a large amount of well organized information.  It should be the long term source for this data.')
    st.markdown("- However, for the short time frame of the Visualization Challenge, I used EZ Search - it has enough information to answer many questions.")
    st.markdown('### Acknowledgements')
    st.markdown('- Any issues with this application - the buck stops here - provide me some feedback - mickarchitect@gmail.com')
    st.markdown('- Thanks to Emily Ng for the suggestions of using the Streamlit tool and for using Sankey diagrams - the app would not have gotten off the ground without those suggestions!')
    st.markdown('- Thanks to USA Facts for the Challenges and special thanks to the hosts - Tanveer and Sasha at USA Facts.')
    return

def display_page_time_slice() :
    st.markdown("## Time Slice")
    return

def map3(df, lat, lon, zoom) :
    filter = df['REPORTING_YEAR'] == use_year
    use_df = df.loc[filter]
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=use_df,
        get_position=['Longitude', 'Latitude'],
        get_elevation='TOTAL_ON_OFF_SITE_RELEASE',
        elevation_scale=0.01,
        radius=10000,
        pickable=True,
        auto_highlight=True,
        )

    tooltip = {
        "html": "<b> {tooltip_fld} </b>",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }

    m2_deck = pdk.Deck(
        column_layer,
        width=3200,
        height=3200,
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 20,
        },
        tooltip=tooltip,
        map_provider='mapbox',
        map_style="mapbox://styles/mapbox/light-v9",
        # width and height do not appear to be working
        )
    st.pydeck_chart(m2_deck, use_container_width=False)

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
    years_df = pd.read_csv('Data/years.CSV')
    filter = years_df['REPORTING_YEAR'] == use_year
    yeartot = years_df.loc[filter]
    st.markdown("## Some Starting Facts")
    st.markdown("### Chosen Year: " + str(use_year) + " (all numbers below in pounds)")
    st.markdown("### Total On and Off Site Releases: " + "{:,}".format((int(yeartot['TOTAL_ON_OFF_SITE_RELEASE']))))
    st.markdown("### Total On Site Releases: " + "{:,}".format((int(yeartot['TOTAL_ON_SITE_RELEASE']))))
    st.markdown("### Total On Site Land Releases: " + "{:,}".format((int(yeartot['LAND_TOTAL_RELEASE']))))
    st.markdown("### Total On Site Water Releases: " + "{:,}".format((int(yeartot['WATER_TOTAL_RELEASE']))))
    st.markdown("### Total On Site Air Releases: " + "{:,}".format((int(yeartot['AIR_TOTAL_RELEASE']))))
    st.markdown("### Total Off Site Releases: " + "{:,}".format((int(yeartot['TOTAL_OFF_SITE_RELEASE']))))
    st.markdown("#### See What Is... for a more complete description")
    
def display_page_works() :
    st_yr_2019_df = pd.read_csv("Data/st_yr_2019.csv")
    map2(st_yr_2019_df, use_lat, use_lon, 3)
    return

def display_page_whatis() :
    st.markdown("## What is the Toxics Release Inventory (TRI) - Summary")
    st.markdown("""
- An EPA Program that tracks the management of certain toxic chemicals (see 'List-*' pages),
  - At U.S. Company "Facilities" in different industry sectors (see 'List-TRI-NAICS' page).
  - Each Facility Annually reports how much of each chemical is managed through recycling, energy recovery and treatment,
  - And how much is released to the environment.
  - See [EPA What is TRI Page](https://www.epa.gov/toxics-release-inventory-tri-program/what-toxics-release-inventory) for more.
                """)
    st.markdown("## Example - 2019 Totals and Dispositions")
    st.markdown("""
- From the [2019 TRI National Analysis](https://www.epa.gov/trinationalanalysis/introduction-2019-tri-national-analysis-0)
- Most of the Waste is managed - recycled, recovered or treated. The remainder (approximately 11% in 2019) is "Disposal or Other Releases".
                """)

# OTH_LANDF_TOT_REL  SURF_IMP_TOT_REL  OTH_DISP_TOT_REL OTHER_LAND_RELEASE  TOT_ALL_OTH_CATEGS


    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = 'black', width = 0.5),
            label = ["Total Waste Managed", "Recycling", "Energy Recovery", "Treatment",     # 0, 1, 2, 3
                     "Disposal or Other Releases", "On-Site", "Off-Site",                    # 4, 5, 6
                     "AIR", "WATER", "LAND", "Landfill-Surf",                                # 7, 8, 9, 10
                     "Other-Landfill", "Other-Land", "Other-Disposition", "Total-All-Not-Listed"],            # 11, 12, 13, 14
            color = "blue"
        ),
        link = dict(
            source = [0, 0, 0, 0, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6],
            target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            value = [15500,7700,3070, 2900, 2900, 430, 600, 200, 2160, 100, 80, 60, 40, 20]
        ))])

    fig.update_layout(hovermode='x', title_text="2019 Totals (units actually in B (not k))", font_size=16, 
                  height=600, width=800)
    st.write(fig)
    st.markdown("## This app focuses on 'Disposal or Other Releases'")
    return


def display_page_chem_pfa() :
    q = pd.read_csv("Data/chem_pfa.csv")
    chem_pfa_df = q.drop('Chemical Structure', axis=1)
    st.markdown('## Chemical (PFA) Listing')
    st.dataframe(chem_pfa_df, height=800)
    return

def display_page_chem_non_pfa() :
    q = pd.read_csv("Data/chem_non_pfa.csv")
    chem_non_pfa_df = q.drop('Chemical Structure', axis=1)
    st.markdown('## Chemical (Non-PFA) Listing')
    st.dataframe(chem_non_pfa_df, height=800)
    return

def display_page_tri_naics() :
    tri_naics_df = pd.read_csv("Data/TRI_Covered_NAICS_Codes.csv")
    st.markdown('## TRI Covered NAICS Codes Listing')
    st.dataframe(tri_naics_df, height=800, width=1000)
    return

######################################################################
# Main
#
# Later
#   State View, with Year Comparison Time Lapse
#   State View, with all facilities/releases instead of totals
#        Sankey diagrams at the bottom of this one for sure, think about others
#   Time Slice some of the larger incidents?
######################################################################

page = st.sidebar.radio('Select page:', ['Introduction', 
                                         'What is the Toxics Release Inventory', 
#                                         'It-Works-View', 
                                         'U.S. View', 
#                                         'State View', 
#                                         'Time Slice', 
                                         'List-Chemicals-PFA', 
                                         'List-Chem-Non-PFA', 
                                         'List-TRI-NAICS',
                                         'About this App'])

use_year = st.sidebar.selectbox('year (for U.S. View)', [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007,
                                         2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994])
# Example locations
ctr_of_us_lat = 31.51073
use_lat = 34.51073
ctr_of_us_lon = -96.4247
use_lon = -97.4247
#use_year = 2019

# Need to validate TRI acronym
st.title('Visualizing the EPA Toxics Release Inventory (TRI)')

if page == 'Introduction' :
    display_page_intro()
elif page == 'What is the Toxics Release Inventory' :
    display_page_whatis()
elif page == 'It-Works-View' :
    display_page_works()
elif page == 'U.S. View' :
    display_page_united_states()
elif page == 'State View' :
    display_page_state_view()
elif page == 'Time Slice' :
    display_page_time_slice()
elif page == 'List-Chemicals-PFA' :
    display_page_chem_pfa()
elif page == 'List-Chem-Non-PFA' :
    display_page_chem_non_pfa()
elif page == 'List-TRI-NAICS' :
    display_page_tri_naics()
elif page == 'About this App' :
    display_page_about()
