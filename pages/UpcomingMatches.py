import streamlit as st

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"]
)

# Navigation Logic
if page == "Home":
    home_page()
elif page == "Team Members":
    team_members_page()
elif page == "Upcoming Matches":
    upcoming_matches_page()
elif page == "Sponsorship and Donation":
    sponsorship_and_donation_page()
elif page == "Registration":
    registration_page()
elif page == "Contact Us":
    contact_us_page()

def home_page():
    st.write("Welcome to the Home Page")

def team_members_page():
    st.header("Team Members")
    # Add content for Team Members page

def upcoming_matches_page():
    st.header("Upcoming Matches")
    
    matches = [
        {"date": "2025-01-01", "opponent": "TBD", "location": "TBD"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD"},
        # Add more matches here
    ]

    st.markdown("<style>.match-card { padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }</style>", unsafe_allow_html=True)

    for match in matches:
        st.markdown(f"""
        <div class="match-card">
            <strong>Date:</strong> {match['date']}<br>
            <strong>Opponent:</strong> {match['opponent']}<br>
            <strong>Location:</strong> {match['location']}
        </div>
        """, unsafe_allow_html=True)

def sponsorship_and_donation_page():
    st.header("Sponsorship and Donation")
    # Add content for Sponsorship and Donation page

def registration_page():
    st.header("Registration")
    # Add content for Registration page

def contact_us_page():
    st.header("Contact Us")
    # Add content for Contact Us page

# Example usage
if __name__ == "__main__":
    if page == "Home":
        home_page()
    elif page == "Team Members":
        team_members_page()
    elif page == "Upcoming Matches":
        upcoming_matches_page()
    elif page == "Sponsorship and Donation":
        sponsorship_and_donation_page()
    elif page == "Registration":
        registration_page()
    elif page == "Contact Us":
        contact_us_page()
