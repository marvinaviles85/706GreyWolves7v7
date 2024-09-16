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
</style>
"""
st.set_page_config(layout="wide")

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add the image to the sidebar
st.sidebar.image("Images/706gw_no_bg.png", use_column_width=True)

# Define the sidebar menu
with st.sidebar:
    page = option_menu(
        "",
        ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donations", "Registration", "Contact Us"],
        icons=["house", "people", "calendar", "star", "clipboard", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

    # Add a clickable phone number at the bottom
    st.markdown("---")  # Add a horizontal line for separation
    st.markdown("""
        <div style="text-align: center;">
            <a href="tel:+15207053812" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #4CAF50;
                border: none;
                border-radius: 5px;
                text-decoration: none;
            ">
                1-520-705-3812
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
# Page title and description

# Home section
if page == "Home":
    st.markdown("<h1 class='title'>706 Grey Wolves 7v7</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='centered-text'>**Welcome to the home of the 706 Grey Wolves!**\n\nExplore our team members, schedule, and photos.</h1>", unsafe_allow_html=True)
    #st.write("Welcome to the home page!")
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.write("<h3 class='centered-text'>Registration is now open for age groups 11U to 18U! Spots are limited, so secure your place today!</h3>", unsafe_allow_html=True)

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
    st.header("Latest News")
    st.write("Stay tuned for the latest news and updates.")

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
            <div>
                <a href="https://www.vetvalor.com" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/c92681657cdceb02bb28d0dd767d8069d3d0427c/706GWImages/VetsValor.JPG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://www.amsoil.com/?zo=408125" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/amsoil.png" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://www.valleycenterrepair.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/ValleyCenter.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

# Team members section
elif page == "Team Members":
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>", unsafe_allow_html=True)
    team_members = [
        {"name": "Marvin Aviles", "position": "Founder", "photo": "Images/MarvinSr.PNG"},
        {"name": "Pam Aviles", "position": "Co-Founder/Team Trainer", "photo": "Images/Pam.jpg"},
        {"name": "Marvin Aviles Jr", "position": "Defensive Coordinator", "photo": "Images/MarvinJr.PNG"},
        # Add more team members here
    ]

    # Create outer columns
    col1, col2 = st.columns(2)

    # First and third images in the first outer column
    with col1:
        st.image(team_members[0]["photo"], caption=team_members[0]["name"], width=200)
        st.write(f"Position: {team_members[0]['position']}")
        st.image(team_members[2]["photo"], caption=team_members[2]["name"], width=200)
        st.write(f"Position: {team_members[2]['position']}")

    # Second image in the second outer column
    with col2:
        st.image(team_members[1]["photo"], caption=team_members[1]["name"], width=200)
        st.write(f"Position: {team_members[1]['position']}")


# Schedule section
elif page == "Upcoming Matches":
    st.header("Upcoming Matches")
    matches = [
        {"date": "2025-01-01", "opponent": "TBD", "location": "TBD"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD"},
        # Add more matches here
    ]

    for match in matches:
        st.write(f"{match['date']} - vs {match['opponent']} ({match['location']})")

# Sponsorship and Donations section
elif page == "Sponsorship and Donations":
    # Page title
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("Images/706gw_no_bg.png", use_column_width=True)

    # Centered Title
    st.markdown("<h1 class='centered-title'>Sponsorship and Donations</h1>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-content'>The 706 Grey Wolves (706 GW) is a travel 7v7 football team for youth ages 11-18. 706 GW is about to embark on its second season with the Hands League. From January 2025 to June 2025, the 706 GW will travel out of state every Saturday for 7v7 tournaments, as well as compete in the local Augusta Hands League 7v7 tournaments. 706 GW is proudly funded by sponsors and operated solely by dedicated volunteers.</div>",
        unsafe_allow_html=True)

    # Sponsorship Levels
    st.markdown("<h2 style='text-align: center;' class='section-title'>Sponsorship Levels</h2>", unsafe_allow_html=True)

    sponsorship_levels = [
        {"level": "$100 Individual Donation",
         "details": "Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account."},
        {"level": "$250 Donation",
         "details": "Your business name and logo will be prominently featured on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be included on a sponsor banner (provided by 706 GW) displayed every Saturday during multiple games."},
        {"level": "$500 Business Donation",
         "details": "Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be featured on a sponsor banner (provided by 706 GW) showcased every Saturday during multiple games, and proudly displayed on players’ uniforms."},
    ]

    for level in sponsorship_levels:
        st.markdown(f"<div class='sponsor-level'>{level['level']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='sponsor-details'>{level['details']}</div>", unsafe_allow_html=True)

    # Donation Information
    st.markdown("<h2 style='text-align: center;' class='section-title'>Donation Information</h2>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-content'>Your generous donation assists with the costs of: uniforms, softshell helmets, player equipment, tournament fees, player insurance, qualified family assistance, and medical supplies</div>",
        unsafe_allow_html=True)

    # Venmo and CashApp Information
    st.markdown("<h2 style='text-align: center;' class='section-title'>Payment Information</h2>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-content'>To make a donation, please send your payment to our Venmo or CashApp account:</div>",
        unsafe_allow_html=True)

    # Create columns for QR codes and buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div>
                <a href="https://venmo.com/code?user_id=3985557692613789993" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/Venmo.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://cash.app/$MarvinAviles85" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/CashApp.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
    # Add the GoFundMe widget
        gofundme_widget = '''
        <style>
            .gfm-embed {
                border: none !important;
                box-shadow: none !important;
            }
        </style>
        <div class="gfm-embed" data-url="https://www.gofundme.com/f/empower-706-grey-wolves-football-journey/widget/medium?sharesheet=dashboard&attribution_id=sl:100c727f-d2bf-44ed-bf04-dedbac75b8c1"></div>
        <script defer src="https://www.gofundme.com/static/js/embed.js"></script>
        '''
        components.html(gofundme_widget, height=300, width=300)

elif page == "Registration":
    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # First and third images in the first outer column
    with col2:
        st.image("Images/706gw_no_bg.png", width=200)
        
    st.markdown("<h1 class='centered-title'>Register Now</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSexO7RZIemrzcf0Y2pBDd1d7k8ehU7EqAJcwPVcXiW1ryCUjw/viewform?embedded=true" width="640" height="2665" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div> 
    """, unsafe_allow_html=True)

    # Venmo and CashApp Information
    st.markdown("<h2 class='section-title'>Payment Information</h2>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-content'>Please send your registration payment to our Venmo or CashApp account:</div>",
        unsafe_allow_html=True)

    # Create columns for QR codes and buttons
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div>
                <a href="https://venmo.com/code?user_id=3985557692613789993" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/Venmo.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://cash.app/$MarvinAviles85" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/CashApp.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

elif page == "Contact Us":
    st.header("Contact Us")
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.write("Email us at 706greywovles7v7@gmail.com")
    st.markdown("""
        <div style="text-align: center;">
            <a href="tel:+15207053812" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #4CAF50;
                border: none;
                border-radius: 5px;
                text-decoration: none;
            ">
                1-520-705-3812
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
            <style>
                .social-icons img {
                    margin-right: 20px;
                }
            </style>
            **Follow us on social media:**
            <div class="social-icons">
                <a href="https://www.facebook.com/706GreyWolves7v7" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" height="50">
                </a>
                <a href="https://www.instagram.com/706greywolves" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" height="50">
                </a>
            </div>
        """, unsafe_allow_html=True)
