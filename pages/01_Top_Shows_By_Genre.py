import streamlit as st
from vega_datasets import data
import altair as alt
import pandas as pd

st.title('Top Shows By Genre')

st.write('The data groups the shows into 1 of 3 main genres: Comedy, Drama, or Unscripted')

st.write('Here are the most favorited shows in each genre. Does yours make the list?')

tv = pd.read_csv('tv_content.csv', encoding="utf-16", sep='\t')



col1, col2, col3 = st.columns(3)

with col1:

    st.subheader('Comedy ' + '😂')

    tv_comedy = tv.loc[(tv['Genre'] == 'Comedy')]

    top5_comedy = tv_comedy.groupby('Show Name')['Favorited'].mean()

    st.write(top5_comedy.sort_values(ascending=False))
   
with col2:

    st.subheader('Drama ' + '😧')

    tv_drama = tv.loc[(tv['Genre'] == 'Drama')]

    top5_drama = tv_drama.groupby('Show Name')['Favorited'].mean()

    st.write(top5_drama.sort_values(ascending=False))
  
with col3:
    
    st.subheader('Unscripted ' + '😶')

    tv_unscripted = tv.loc[(tv['Genre'] == 'Unscripted')]

    top5_uns = tv_unscripted.groupby('Show Name')['Favorited'].mean()

    st.write(top5_uns.sort_values(ascending=False))