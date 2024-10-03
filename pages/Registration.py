import streamlit as st
import webbrowser

# Dropdown menu for pages selection
# Add the image and navigation bar to the top of the page
st.markdown("""
<div class="top-bar">
    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Logo">
    <div id="dropdown-container"></div>
</div>
""", unsafe_allow_html=True)

# Dropdown menu for pages selection
# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"],
    key="registration_selectbox"
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
    # Payment Section
    # Payment Method Section
    st.header("Payment Method")
    payment_method = st.selectbox("Choose your payment method", ["Venmo", "CashApp", "Credit Card"])

    if payment_method == "Venmo":
        st.write("To complete your donation via Venmo, please [click here](https://venmo.com/code?user_id=3985557692613789993).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("Venmo Transaction ID")
    elif payment_method == "CashApp":
        st.write("To complete your donation via CashApp, please [click here](https://cash.app/$MarvinAviles85).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("CashApp Transaction ID")
    elif payment_method == "Credit Card":
        st.write("To complete your donation via Credit Card, please [click here](https://buy.stripe.com/cN2044cqYfAwd9e000).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("Credit Card Transaction ID")

# Run the page function if this file is executed
if __name__ == "__main__":
    registration_page()
