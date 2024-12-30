import streamlit as st

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"],
    key="upcoming_matches_selectbox"
)

# Navigation Logic
def home_page():
    st.write("Welcome to the Home Page")

def team_members_page():
    st.write("Team Members Page")

def upcoming_matches_page():
    st.header("Upcoming Matches")
    
    matches = [
        {"date": "01/18-19/2025", "opponent": "Team Takeover Classic", "location": "Columbia, SC", "image_url": "https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/TTO.png"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD", "image_url": "https://example.com/image2.jpg"},
        # Add more matches here
    ]

    st.markdown("<style>.match-card { padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }</style>", unsafe_allow_html=True)

    for match in matches:
        st.image(match["image_url"], caption=f"{match['opponent']} on {match['date']} at {match['location']}")
        st.markdown(f"""
        <div class="match-card">
            <strong>Date:</strong> {match['date']}<br>
            <strong>Opponent:</strong> {match['opponent']}<br>
            <strong>Location:</strong> {match['location']}
        </div>
        """, unsafe_allow_html=True)
        st.write("---")

def sponsorship_and_donation_page():
    st.write("Sponsorship and Donation Page")

def registration_page():
    st.write("Registration Page")

def contact_us_page():
    st.title("Contact Us")

# Page title and description
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

# Example usage
if __name__ == "__main__":
    upcoming_matches_page()
