import streamlit as st
from vega_datasets import data
import altair as alt
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tk

st.title('Subgenres of each genre')

st.write('Each of those 3 genres have been further subcategorized into 44 total subgenres')

st.write('Below is a breakdown of the most favorited subgenres:')

df = pd.read_csv('tv_content.csv', encoding="utf-16", sep='\t')

bar = alt.Chart(df).mark_bar(color='#03cffc').encode(
    y = alt.Y("Genre Taxonomy:N", sort = '-x'),
    x = 'mean(Favorited):Q',
).facet(
    column='Genre:N'
).resolve_scale(
    y='independent'
)

st.altair_chart(bar, use_container_width=True)

shows = df['Show Name'].unique()

st.subheader('Which genres does your favorite show belong to?')

shows_selected = st.selectbox('Select a show', shows)
mask_shows = df['Show Name'].isin([shows_selected])

data = df[mask_shows]

genre = data.iloc[0][2]
subgenre = data.iloc[0][3]

st.write('Genre: ' + genre)
st.write(' Subgenre: ' + subgenre)



