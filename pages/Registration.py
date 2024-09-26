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

# Registration Page
def registration_page():
    st.title("Registration")

    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # Center the logo in the middle column
    with col2:
        st.image("Images/706gw_no_bg.png", width=200)
        
    st.markdown("<h1 class='centered-title'>Register Now</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSexO7RZIemrzcf0Y2pBDd1d7k8ehU7EqAJcwPVcXiW1ryCUjw/viewform?embedded=true" width="640" height="2665" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div> 
    """, unsafe_allow_html=True)

    # Venmo and CashApp Information


# Run the page function if this file is executed
if __name__ == "__main__":
    registration_page()
