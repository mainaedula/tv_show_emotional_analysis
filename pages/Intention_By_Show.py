import streamlit as st
from vega_datasets import data
import altair as alt
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title('Why are you watching this?')

st.write('Was it recommended by friends? Are you trying to understand the memes online? Or do you only have it playing in the background and eventually see this...')

st.image('netflix.jpg.webp')

st.write('Magid has identified the most common reasons behind watching certain TV shows, both intentional and unintentional')

st.subheader('See why others are watching your favorite show too')

df = pd.read_csv('intention_by_show.csv', encoding="utf-16", sep='\t')
df = df.replace(to_replace=["Avg. Forgot Where", "Avg. Rarely Watch", "Avg. Nothing Better", "Avg. Social Media Share", "Avg. If Surfing", "Avg. Talk With Others", "Avg. Total Attention", "Avg. Binge On Air", "Avg. Binge Stream", "Avg. Watch In Background", "Avg. Because People Talk", "Avg. Social Media Like", "Avg. Read Online"],
           value=["Forgot Where", "Rarely Watch", "Nothing Better", "Social Media Share", "If Surfing", "Talk With Others", "Total Attention", "Binge On Air", "Binge Stream", "Watch In Background", "Because People Talk", "Social Media Like", "Read Online"])

#st.write(df.head())

shows = df['Show'].unique()

shows_selected = st.selectbox('Select a show', shows)
mask_shows = df['Show'].isin([shows_selected])


data = df[mask_shows]
#st.write(data)

word_data = df.set_index('Measure').to_dict()['Values']
#st.write(word_data)

stopword_set = set(["Avg. "])

wc = WordCloud(width=800, height=400, max_words=200, stopwords = stopword_set).generate_from_frequencies(word_data)


st.image(wc.to_array())

bar = alt.Chart(data).mark_bar(color='#03cffc').encode(
    y = alt.Y("Measure:N", title = "Intention", sort = '-x'),
    x= 'Values:Q',
    column='Show',
    tooltip = ['Measure', 'Values']
)

st.altair_chart(bar, use_container_width=True)



