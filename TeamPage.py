import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import streamlit.components.v1 as components
import webbrowser

from pages.TeamMembers import team_members_page
from pages.UpcomingMatches import upcoming_matches_page
from pages.SponsorshipandDonation import sponsorship_and_donation_page
from pages.Registration import registration_page
#from pages.Spirit_Wear_Order import spirit_wear_order_page
#from pages.Media import media_page
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
        background-color: None;
        border-radius: 10px;
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
        @import url('style.css');
        }
</style>
"""
st.set_page_config(
    page_title="706 Grey Wolves",
    page_icon="Images/706gw_no_bg.png",
    initial_sidebar_state="collapsed")

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
    """,
        unsafe_allow_html=True,
    )

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
        padding-top: 60px; /* Adjust this value based on the height of your fixed top bar */
    }
    </style>
    """, unsafe_allow_html=True)

st.image("Images/gwlogonobg.jpg", caption= " ")

# Custom CSS to change the dropdown menu colors
st.markdown(
    """
    <style>
    /* Change the background color of the dropdown menu */
    div[data-baseweb="select"] > div {
        background-color: black;
    }
    /* Change the text color of the dropdown menu */
    div[data-baseweb="select"] > div > div {
        color: white;
    }
    /* Change the background color of the dropdown options */
    div[role="listbox"] ul {
        background-color: black;
    }
    /* Change the text color of the dropdown options */
    div[role="listbox"] li {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add JavaScript to ensure the menu stays fixed
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"]
)

#st.markdown("""
#<script>
#    const dropdownContainer = document.getElementbyId('drowndown-container');
#    const selectbox = document.querySelector('select[data-testid="stSelectbox"]');
#    dropdownContainer.appendChild(selectbox);
#</script>
#""", unsafe_allow_html=True)
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
elif page == "Registration":
    registration_page()
#elif page == "Spirit Wear Order":
#    spirit_wear_order_page()
#elif page == "Media":
#    media_page()
elif page == "Contact Us":
    contact_us_page()

# Home section
if page == "Home":
    #st.markdown("<h1 class='title'>706 Grey Wolves 7v7</h1>", unsafe_allow_html=True)
    #st.markdown("<h1 class='centered-text'>**Welcome to the home of the 706 Grey Wolves!**\n\nExplore our team members, schedule, and photos.</h1>", unsafe_allow_html=True)
    #st.write("Welcome to the home page!")
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.write("<h3 class='centered-text'>Registration is now open for age groups 13U to 18U! Spots are limited, so secure your place today!</h3>", unsafe_allow_html=True)

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
        {'img': '706GWImages/TooStrong.jpg', 'title': '', 'text': ''},
    ]

    carousel(images)
    st.markdown("""
    <h1 class='centered-title'>Latest News</h1>
    <p class='subtext'>#MEETUSONTHE50</p>
""", unsafe_allow_html=True)
    #st.header("Latest News")
    #st.write("Stay tuned for the latest news and updates.")
    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # First and third images in the first outer column
    with col1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.facebook.com/profile.php?id=61567362084142" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/HandsLeagueLogo.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.facebook.com/photo/?fbid=122181338096177637&set=pb.61555329136562.-2207520000" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/NXGNRegionalShowcase.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.facebook.com/events/2695524287283994/?acontext=%7B%22event_action_history%22%3A[]%7D" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/Slim Chickens Fundraiser.jpg" width="3000">
                </a>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.community-fundraiser.com/fundraiser/events/promotions/3b124f16-c59e-8fce-d33a-6cdb6c068a0d/en/landing?fbclid=IwY2xjawGFzIFleHRuA2FlbQIxMAABHcumqDHUx1rDBMe2JT637Scofx9xE0WgF2MSsvasnZ8oE9t1Fyd_Blvjgg_aem_z4sVpeIcqWkNyH9UDGTbIw" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/PandaExpressFundraiser.jpg" width="3000">
                </a>
            </div>
        """, unsafe_allow_html=True)
    st.title("Join Our Shoe Drive Fundraiser!")
    st.write("""
We're kicking off a shoe drive fundraiser and we need your help! Donate your unwanted, gently worn shoes, cleats, boots, and more. The team earns money for every pound of shoes we collect. Our goal is to gather 100 bags of shoes, with each bag holding 25 pairs.

**Important Guidelines:**
- No holes in the shoes
- No flip-flops
- No ice skates or roller blades

Your contributions will make a huge difference. Let's make this fundraiser a step in the right direction!

For details, [e-mail me](mailto:706greywolves7v7@gmail.com)
""")


 # Add sponsors section
    st.markdown("""
    <h1 class='centered-title'>Our Valued Sponsors</h1>
    <p class='subtext'>Click on the images to visit their websites</p>
""", unsafe_allow_html=True)
    sponsors_donors = [
        {"name": "", "position": "", "photo": "706GWImages/VetsValor.JPG"}
    ]
        
    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # First and third images in the first outer column
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

    with col3:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <a href="https://www.valleycenterrepair.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/ValleyCenter.PNG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
