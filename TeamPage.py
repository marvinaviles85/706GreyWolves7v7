import streamlit as st
from streamlit_option_menu import option_menu

custom_css = """
<style>
    .centered-title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: white;
    }
    .team-member img, .photo-gallery img {
        width: 200px; /* Set a Consistent Width */
        height: auto; /* Maintain aspect ratio */
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
        height: 3000px;
        border: none;
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add the image to the sidebar
st.sidebar.image(".venv/Scripts/Images/706gw_no_bg.png", use_column_width=True)

# Define the sidebar menu
with st.sidebar:
    page = option_menu(
        "",
        ["Home", "Team Members", "Upcoming Matches", "Photos", "Registration", "Contact Us"],
        icons=["house", "people", "calendar", "images", "clipboard", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Page title and description

# Home section
if page == "Home":
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7</h1>", unsafe_allow_html=True)
    st.write("Welcome to the home of the 706 Grey Wolves! Explore our team members, schedule, and photos.")
    #st.write("Welcome to the home page!")
    st.image(".venv/Scripts/Images/706gw_no_bg.png", use_column_width=True)

# Team members section
elif page == "Team Members":
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>", unsafe_allow_html=True)
    team_members = [
        {"name": "Marvin Aviles", "position": "Founder", "photo": ".venv/Scripts/Images/MarvinSr.PNG"},
        {"name": "Pam Aviles", "position": "Co-Founder/Team Trainer", "photo": ".venv/Scripts/Images/Pam.jpg"},
        {"name": "Marvin Aviles Jr", "position": "Defensive Coordinator", "photo": ".venv/Scripts/Images/MarvinJr.PNG"},
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

# Photo Collage section
elif page == "Photos":
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 2024</h1>", unsafe_allow_html=True)

    # Create a 3-column layout
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(".venv/Scripts/706GWImages/AllStars.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/BJ.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/GetOutTheWay.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/MikeWeathers.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/TheBoys.jpg", use_column_width=True)

    with col2:
        st.image(".venv/Scripts/706GWImages/Bjorkman.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/Dylan.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/HunterHeadTop.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/MoneyInTheBank.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/TooStrong.jpg", use_column_width=True)

    with col3:
        st.image(".venv/Scripts/706GWImages/FirstTeamImage.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/Flash.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/Isaac.jpg", use_column_width=True)
        st.image(".venv/Scripts/706GWImages/PB12.jpg", use_column_width=True)

elif page == "Registration":
    st.header("Register Now")
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSexO7RZIemrzcf0Y2pBDd1d7k8ehU7EqAJcwPVcXiW1ryCUjw/viewform?embedded=true" width="800" height="2400" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div> 
    """, unsafe_allow_html=True)

elif page == "Contact Us":
    st.header("Contact Us")
    st.image(".venv/Scripts/Images/706gw_no_bg.png", use_column_width=True)
    st.write("Email us at 706greywovles7v7@gmail.com")
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
