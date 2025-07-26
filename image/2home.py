# Import necessary libraries
import requests
import streamlit as st
from PIL import Image

# Configure Streamlit page
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Page title
st.title(":blue[Autism Spectrum Disorder]")
st.write("---")

# ---------- Section: What is Autism Spectrum Disorder ----------
with st.container():
    col1, col2 = st.columns([3, 2])  # Divide layout into two columns
    with col1:
        st.title("What is Autism Spectrum Disorder?")
        st.write("""
        Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. 
        People with ASD often have problems with social communication and interaction, and restricted or 
        repetitive behaviors or interests. People with ASD may also have different ways of learning, moving, 
        or paying attention.
        """)
    with col2:
        img1 = Image.open("image/asd_child.jpg")  # Load image
        st.image(img1, width=300)  # Display image

# ---------- Section: Causes of Autism Spectrum Disorder ----------
with st.container():
    col1, col2 = st.columns([4, 2])
    with col1:
        st.title("What Causes Autism Spectrum Disorder?")
        st.write("""
        The Autism Spectrum Disorder Foundation lists the following as possible causes of ASD:

        :blue[Genetics] : Research suggests that ASD can be caused by a combination of genetic and environmental factors.
        
        :blue[Environmental factors] : Exposure to toxins during pregnancy or after birth may increase ASD risk.
        
        :blue[Brain differences] : Structural differences in the brain have been observed in people with ASD.
        """)
    with col2:
        img1 = Image.open("image/causes-of-autism.png")
        st.image(img1, width=350, caption="Causes of ASD")

# ---------- Section: Symptoms of Autism Spectrum Disorder ----------
with st.container():
    col1, col2 = st.columns([4, 2])
    with col1:
        st.title("Symptoms of ASD:")
        st.write("""
        1. Avoids or does not keep eye contact
        2. Does not respond to name by 9 months of age
        3. Does not show facial expressions like happy, sad, angry, and surprised by 9 months
        4. Lines up toys and gets upset when order is changed
        5. Repeats words or phrases (echolalia)
        6. Plays with toys the same way every time
        7. Delayed language/movement/cognitive skills
        8. Hyperactivity or inattentiveness
        9. Unusual eating/sleeping habits or emotional reactions
        10. Epilepsy, GI issues, anxiety, lack or excess of fear, etc.
        """)
        st.write("[Learn More >](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders)")
    with col2:
        img = Image.open("image/autism.png")
        st.image(img, caption="Signs of ASD")
        img1 = Image.open("image/Strategies.jpeg")
        st.image(img1, caption="")

# ---------- Section: Relevant Statistics ----------
with st.container():
    left_column, right_column = st.columns([4, 2])
    with left_column:
        st.title("Relevent statistics ")
        st.write("""
            Estimates vary, but some studies suggest ASD affects 1-2 per 1000 children in India.

            • Prevalence: Between 1 in 500 to 1 in 166 children have ASD.

            • Rate in India: ~0.20% or over 2 million people.

            • Incidence extrapolation: ~11,914 new cases/year.

            • 4x more prevalent in boys than girls (US data).

            • Increasing 10–17% per year (US), expected to reach 4M cases in the next decade.
            """)
    with right_column:
        img = Image.open("image/autism-stats-1.jpg")
        st.image(img, width=350, caption="ASD statistics")
        img1 = Image.open("image/autism-stats-2.png")
        st.image(img1, width=350, caption="USA data over 18 years")

# ---------- Section: World Autism Awareness Day ----------
with st.container():
    st.title("World Autism Awareness Day")
    st.write(
        "WAAD 2024 will be observed with a virtual event on April 2nd. It will feature autistic voices globally, "
        "discussing how to shift the narrative around neurodiversity and support contributions of autistic individuals "
        "towards achieving Sustainable Development Goals."
    )

# Two columns to display awareness day images
c1, c2 = st.columns([5, 5])
im = Image.open("image/World.png")
c1.image(im, caption="")
im1 = Image.open("image/Worlds.png")
c2.image(im1, caption="")
