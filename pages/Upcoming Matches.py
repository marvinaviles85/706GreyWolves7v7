import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import streamlit.components.v1 as components

custom_css = """
<style>
    .centered-title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: white;
    }
    .team-member img, .photo-gallery img {
        width: 100%; /* Set a Consistent Width */
        height: 100%; /* Maintain aspect ratio */
        object-fit: contain;
    }
     .carousel-title {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-size: 1.5em;
        color: white;
    }
    .carousel-text {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-size: 1em;
        color: white;
    }
    .iframe-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .iframe-container iframe {
        width: 100%;
        border: none;
    }
        .section-content {
        font-family: 'Arial', sans-serif;
        font-size: 1.2em;
        color: white;
        margin-bottom: 20px;
    }
    .sponsor-level {
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        color: white;
        margin-top: 10px;
    }
    .sponsor-details {
        font-family: 'Arial', sans-serif;
        font-size: 1em;
        color: white;
        margin-bottom: 10px;
    }
    .donate-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius:12px;
    }
    .venmo-inf {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2em;
        color: #333;
        margin-top: 20px;
    }
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .title {
        text-align: center;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 50px;
        text-shadow: 2px 2px 0 #000000, 4px 4px 0 #000000;
    }
    .centered-text {
        text-align: center;
    }
     #sponsors {
        text-align: center;
        padding: 20px;
    }
    .sponsor-logos {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
    }
    .sponsor-logos a img {
        max-width: 150px;
        transition: transform 0.3s;
    }
    .sponsor-logos a img:hover {
        transform: scale(1.1);
    }
    @media (max-width: 768px) {
            .stMarkdown div {
                text-align: center;
            }
            .stMarkdown img {
                width: 100% !important;
                height: auto !important;
            }
        }
    .centered-title {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: white; /* Change this color to match your theme */
            padding: 20px;
            border-bottom: 2px solid white; /* Optional: Add a bottom border */
        }
        .subtext {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: white; /* Change this color to match your theme */
            font-size: 14px; /* Smaller font size */
        }
        .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: None;
        flex-wrap: wrap;
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        z-index: 1000, /* Ensure it stays on top of other content */
    }
    .top-bar img {
        height: 50px;
    }
    .top-bar select {
        padding: 5px;
        font-size: 16px;
    }
    @media (max-width: 600px) {
        .top-bar {
            flex-direction: column;
            align-items: flex-start;
        }
        .top-bar img {
            margin-bottom: 10px;
        }
        .top-bar select {
            width: 100%;
        }
        body {
            padding-top: 70px;
        }
</style>
"""
st.set_page_config(layout="wide")

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add the image and navigation bar to the top of the page
st.markdown("""
<div class="top-bar">
    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Logo">
    <div id="dropdown-container"></div>
</div>
""", unsafe_allow_html=True)

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donations", "Registration", "Contact Us"]
)
# Schedule section
#elif page == "Upcoming Matches":
st.header("Upcoming Matches")
    matches = [
        {"date": "2025-01-01", "opponent": "TBD", "location": "TBD"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD"},
        # Add more matches here
    ]

    for match in matches:
        st.write(f"{match['date']} - vs {match['opponent']} ({match['location']})")