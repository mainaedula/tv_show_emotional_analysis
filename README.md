# README.md

### Streamlit link: https://mainaedula-tv-show-emotional-analysis-home-lceg8c.streamlit.app/

## Introduction

Most of us consume some form of entertainment every single day. But what factors drive the choices we make around entertainment? And specifically how do our emotions play a role in this process? This data from Magid embarks on a comprehensive analysis of the emotional landscape of TV entertainment, specifically by compiling numerous TV shows from top networks and streaming services. Some of the information gathered on these shows include subgenre categorization, emotional dimensions, proximity to other shows, and intention for watching.

These insights can be used to better understand why we watch what we watch. What shows do we watch when certain emotions are present? Or do we only end up watching things that are recommemded by others? While for the everyday consumer this exercise is merely an interesting introspective opportunity, for entertainment companies this is a powerful tool. They can leverage this data to better understand consumer behavior, which will drive their marketing strategies and recommendation algorithms to ultimately increase revenue.


## Data design

Overall, this data set was pretty clean from the start. It consisted of various separate tables/csv files but the ones of interest for this project were identified and extracted separately. An inner join was performed as well to combine the data in 2 separate tables. Data from some of the columns had to be aggregated because it applied for the same show across various dates, but then these values were renamed for a clean presentation.

## Future work:

This app is only an introductory analysis. In the future, it would be interesting to generate a custom recommendation engine based on the shows a customer already watches. Ideally, we would combine the emotional metrics, subgenres, intention, and proximity metrics to recommend a similar show to the customer. In addition, it would be interesting to create customer profiles/personas based on these factors if the data patterns are strong enough.
