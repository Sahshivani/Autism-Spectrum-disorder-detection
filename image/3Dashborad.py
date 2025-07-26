# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set title and section divider
st.title(":signal_strength: :blue[ Let's take a look at the statistics of last 5 years]")
st.write("---")

# Read the dataset from a CSV file
df = pd.read_csv("data_csv.csv")   

# ----- ASD Trait Filter -----
# Get unique ASD trait values and show a dropdown to select one
ASD_traits_data = df["ASD_traits"].unique().tolist()
select_date = st.selectbox("ASD traits ?", ASD_traits_data)

# Filter the dataframe based on selected ASD trait
df_up = df[df["ASD_traits"].isin(ASD_traits_data)]

# ----- Gender Multiselect Filter -----
# Get unique gender values and allow multi-selection
sub_opt = df_up["Sex"].unique().tolist()
select_sub = st.multiselect("Gender", sub_opt)

# Further filter data based on selected genders
df_up_sub = df_up[df_up["Sex"].isin(select_sub)]
st.write("---")

# ----- Jaundice Statistics -----
col1, col2 = st.columns(2)
with col1:
    st.subheader("Jaundice statistics")
    with st.expander("See the plot"):     
        # Plot bar chart with gender on x-axis and color-coded by jaundice status
        fig = px.bar(df_up_sub, x="Sex", color="Jaundice")
        fig.update_layout(height=500, width=200)
        st.write(fig)

# ----- Childhood Autism Rating Scale Statistics -----
with col2:
    st.subheader("Childhood Autism Rating Scale statistics")
    with st.expander("See the plot"):        
        # Bar chart by gender and color-coded by rating scale
        fig = px.bar(df_up_sub, x="Sex", color="Childhood Autism Rating Scale")
        fig.update_layout(height=500, width=200)
        st.write(fig)

st.write("---")

# ----- Family Member with ASD Statistics -----
col1, col2 = st.columns(2)
with col1:
    st.subheader("Family member with ASD statistics")
    with st.expander("See the plot"):     
        # Bar chart by gender and color-coded by whether they have family member with ASD
        fig = px.bar(df_up_sub, x="Sex", color="Family_mem_with_ASD")
        fig.update_layout(height=500, width=200)
        st.write(fig)

# ----- Social Responsiveness Scale Statistics -----
with col2:
    st.subheader("Social Responsiveness Scale statistics")
    with st.expander("See the plot"):        
        # Bar chart by gender and colored by social responsiveness scale
        fig = px.bar(df_up_sub, x="Sex", color="Social_Responsiveness_Scale")
        fig.update_layout(height=500, width=200)
        st.write(fig)
