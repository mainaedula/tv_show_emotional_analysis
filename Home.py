import streamlit as st
from vega_datasets import data
import altair as alt
import pandas as pd

st.title('Emotional Analysis of TV shows ' + ":tv:")

st.write('This dataset from Magid is titled "Content Value, Engagement and Emotional Metrics for Television Programs and Networks".' )
st.write('It contains survey based data about how viewers interact with almost 3800+ TV shows including emotional metrics, intentionality of interaction, watch frequency, proximity to other shows, and more.')
st.write('Stakeholders in the media and entertainment industry can use this data to better understand their viewer engagement and inform decisions about content recommendations or product marketing. ')
st.write("For our purposes, let's look at some high level data about some of our favorite TV shows")


