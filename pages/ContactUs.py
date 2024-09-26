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
    #st.write("Welcome to the Home Page")
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

def contact_us_page():
    st.title("Contact Us")

    st.image("Images/706gw_no_bg.png", use_column_width=True, caption="706 Grey Wolves Logo")
    st.write("Email us at 706greywolves7v7@gmail.com")
    
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
        """, unsafe_allow_html=True
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
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" height="50" alt="Facebook">
            </a>
            <a href="https://www.instagram.com/706greywolves" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" height="50" alt="Instagram">
            </a>
        </div>
        """, unsafe_allow_html=True
    )
