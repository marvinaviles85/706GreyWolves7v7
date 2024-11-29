import streamlit as st

# Dropdown menu for pages selection
# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"],
    key="upcoming_matches_selectbox"
)

# Page title and description
# Navigation Logic
def home_page():
    st.write("Welcome to the Home Page")

def team_members_page():
    st.write("Team Members Page")

def upcoming_matches_page():
    st.write("Upcoming Matches Page")

def sponsorship_and_donation_page():
    st.write("Sponsorship and Donation Page")

def registration_page():
    st.write("Registration Page")

def contact_us_page():
    st.title("Contact Us")

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
    st.write("Welcome to the Home Page")
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

def upcoming_matches_page():
    st.header("Upcoming Matches")
    
    matches = [
        {"date": "2025-01-18", "opponent": "Team Takeover Classic", "location": "Columbia, SC"},
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

# Example usage
if __name__ == "__main__":
    upcoming_matches_page()
