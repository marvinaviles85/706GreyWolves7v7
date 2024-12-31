import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import streamlit.components.v1 as components
import webbrowser

from pages.TeamMembers import team_members_page
from pages.UpcomingMatches import upcoming_matches_page
from pages.SponsorshipandDonation import sponsorship_and_donation_page
from pages.ContactUs import contact_us_page

custom_css = """
<style>
    .centered-title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: white;
    }
    .team-member img, .photo-gallery img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }
    .carousel-title, .carousel-text {
        position: absolute;
        bottom: 20px;
        left: 20px;
        color: white;
    }
    .carousel-title {
        font-size: 1.5em;
    }
    .carousel-text {
        font-size: 1em;
    }
    .iframe-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 10px;
    }
    .iframe-container iframe {
        width: 100%;
        border: none;
    }
    .section-content, .sponsor-details, .venmo-inf {
        font-family: 'Arial', sans-serif;
        color: white;
    }
    .section-content {
        font-size: 1.2em;
        margin-bottom: 20px;
    }
    .sponsor-level {
        font-size: 1.5em;
        margin-top: 10px;
    }
    .sponsor-details {
        font-size: 1em;
        margin-bottom: 10px;
    }
    .donate-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        text-align: center;
        text-decoration: none;
    }
    .venmo-inf {
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
    .centered-title, .subtext {
        text-align: center;
        font-family: 'Arial', sans-serif;
        color: white;
    }
    .centered-title {
        padding: 20px;
        border-bottom: 2px solid white;
    }
    .subtext {
        font-size: 14px;
    }
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        flex-wrap: wrap;
        background-color: None;
        position: sticky;
        top: 0;
        z-index: 1000;
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
        @import url('style.css');
    }
</style>
"""

st.set_page_config(
    page_title="706 Grey Wolves",
    page_icon="Images/706gw_no_bg.png",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        [data-testid='stSidebarNav'] {
            display: none;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sidebar = document.querySelector("[data-testid='stSidebarNav']");
            if (sidebar) {
                sidebar.style.display = 'none';
            }
        });
    </script>
""", unsafe_allow_html=True)

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add the image and navigation bar to the top of the page
st.markdown("""
    <div class="top-bar" style="position: fixed; top: 0; width: 100%; background-color: black; z-index: 1000;">
        <div id="dropdown-container"></div>
    </div>
""", unsafe_allow_html=True)

# Add some padding to the top of the page content to avoid overlap with the fixed menu
st.markdown("""
    <style>
        body {
            padding-top: 60px;
        }
    </style>
""", unsafe_allow_html=True)

st.image("Images/gwlogonobg.jpg", caption=" ")

# Custom CSS to change the dropdown menu colors
st.markdown("""
    <style>
        div[data-baseweb="select"] > div {
            background-color: black;
        }
        div[data-baseweb="select"] > div > div {
            color: white;
        }
        div[role="listbox"] ul {
            background-color: black;
        }
        div[role="listbox"] li {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Add JavaScript to ensure the menu stays fixed
st.markdown("""
    <script>
        window.onscroll = function() {
            var topBar = document.querySelector('.top-bar');
            if (window.pageYOffset > 0) {
                topBar.style.position = 'fixed';
                topBar.style.top = '0';
                topBar.style.width = '100%';
                topBar.style.zIndex = '1000';
            } else {
                topBar.style.position = 'relative';
            }
        };
    </script>
""", unsafe_allow_html=True)

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Contact Us"]
)

# Page title and description
# Navigation Logic
if page == "Home":
    st.write(" ")
elif page == "Team Members":
    team_members_page()
elif page == "Upcoming Matches":
    upcoming_matches_page()
elif page == "Sponsorship and Donation":
    sponsorship_and_donation_page()
elif page == "Contact Us":
    contact_us_page()

# Home section
if page == "Home":
    st.markdown("<h1 class='centered-text'>**Welcome to the home of the 706 Grey Wolves!**\n\nExplore our team members, schedule, and photos. \n\n We are a 501(c)(3) Organization</h1>", unsafe_allow_html=True)
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.markdown("<h3 class='centered-text'>Registration is now open for age groups 13U to 18U! Spots are limited, so secure your place today!</h3>", unsafe_allow_html=True)
    
    # Add a scrolling image gallery
    images = [
        {'img': '706GWImages/AllStars.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/BJ.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/BJ and Alan.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/cody.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Dylan.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/FirstTeamImage.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Flash.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/GetOutTheWay.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/HunterHeadTop.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Isaac.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/MikeWeathers.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/MoneyInTheBank.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/PB12.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/TheBoys.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/TooStrong.jpg', 'title': '', 'text': ''}
    ]

    carousel(images)

    st.markdown("""
        <h1 class='centered-title'>Latest News</h1>
        <p class='subtext'>#MEETUSONTHE50</p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.facebook.com/profile.php?id=61567362084142" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/HandsLeagueLogo.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.facebook.com/photo/?fbid=122181338096177637&set=pb.61555329136562.-2207520000" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/NXGNRegionalShowcase.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <h1 class='centered-title'>Our Valued Sponsors</h1>
        <p class='subtext'>Click on the images to visit their websites</p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.carboncustomhomes.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/carbonhomes.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://vetvalor.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/VetValor.PNG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.amsoil.com/?zo=408125" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/amsoil.png" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://superior-athlete.com//" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/superiorathlete.png" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.valleycenterrepair.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/ValleyCenter.PNG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
