import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
sequels = pd.read_csv('streamLitData.csv')

# Sidebar filter
selected_movie_series = st.sidebar.selectbox('Filter by Movie Series', ['All'] + sequels['Movie Series'].unique().tolist())
filtered_sequels = sequels if selected_movie_series == 'All' else sequels[sequels['Movie Series'] == selected_movie_series]

# Line chart
fig = px.line(
    filtered_sequels,
    x='Year',
    y='IMDb Rating',
    color='Movie Series',
    title='Movie Series IMDb Ratings Over Time',
    labels={'IMDb Rating': 'Rating', 'Year': 'Release Year'},
    hover_data={'Title': True, 
                'Movie Series': True, 
                'IMDb Rating': True, 
                'Year': True},
    line_shape='linear',
    markers=True  # Show markers
)

# Customize layout
fig.update_layout(
    xaxis_title='Release Year',
    yaxis_title='IMDb Rating',
    legend_title='Movie Series',
    font=dict(family='Arial', size=12),
)

# Streamlit UI
st.title('Movie Series From 1940-2020')
st.sidebar.markdown('### Movie Series Filter')
st.plotly_chart(fig)