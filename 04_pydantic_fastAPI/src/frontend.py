import pandas as pd
import requests
import streamlit as st

def layout_page():
    url = "http://127.0.0.1:8000/movie"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        print(df.head())
    else:
        print(f"Något gick fel. Statuskod: {response.status_code}")


    st.title("Movie Database")
    selected_genre = st.selectbox("Select a genre", options=list(df['genre'].unique()) + ["All"])
    if selected_genre == "All":
        df = df
    else:
        df = requests.get(url).json()

    filtered_df = 

    year_range = st.slider("Select year range", min_value=df['year'].min(), max_value=df['year'].max(), value=(df['year'].min(), df['year'].max()), step=1)

    if selected_genre and selected_genre != "All":
        df = df[df['genre'] == selected_genre]

    if year_range:
        df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]      

    with st.container(border=True):
        st.subheader(f"Movies in genre: {selected_genre}")
        st.bar_chart(df.head(5), x='title', y='rating')

    st.dataframe(df)

if __name__ == "__main__":
    layout_page()