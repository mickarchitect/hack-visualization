import pandas as pd
import time
import streamlit as st
import plotly.graph_objects as go

st.write("# Testing Sankey Diagrams")
st.write("## Try to emulate this [EPA Diagram](https://www.epa.gov/trinationalanalysis/introduction-2019-tri-national-analysis-0)")

opacity = 0.4

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = 'black', width = 0.5),
        label = ["A1", "A2", "B1", "B2", "C1", "C2"],
        color = "blue"
    ),
    link = dict(
        source = [0, 1, 0, 2, 3, 3],
        target = [2, 3, 3, 4, 4, 5],
        value = [8, 4, 2, 8, 4, 2]
    ))])

fig.update_layout(hovermode='x', title_text="Basic Sankey Diagram", font_size=10)
#fig.show()
st.write(fig)
