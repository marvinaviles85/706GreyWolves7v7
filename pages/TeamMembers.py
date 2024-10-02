import streamlit as st

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
if page == "Team Members":
    st.write("Welcome to the Team Members Page")
elif page == "Home":
    teampage_page()
elif page == "Upcoming Matches":
    upcoming_matches_page()
elif page == "Sponsorship and Donation":
    sponsorship_and_donation_page()
elif page == "Registration":
    registration_page()
elif page == "Contact Us":
    contact_us_page()

# Page title and description
def team_members_page():
    st.header("Team Members")
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>", unsafe_allow_html=True)
    
    team_members = [
        {"name": "Marvin Aviles", "position": "Founder", "photo": "Images/MarvinSr.PNG"},
        {"name": "Pam Aviles", "position": "Co-Founder/Team Trainer", "photo": "Images/Pam.jpg"},
        {"name": "Marvin Aviles Jr", "position": "Defensive Coordinator", "photo": "Images/MarvinJr.PNG"},
        # Add more team members here
    ]

    # Create a dynamic layout for team members
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(member["photo"], caption=member["name"], width=150)
        with col2:
            st.markdown(f"**Name:** {member['name']}")
            st.markdown(f"**Position:** {member['position']}")
            # Add more details if available
            # st.markdown(f"**Bio:** {member['bio']}")

# Example usage
if __name__ == "__main__":
    team_members_page()
