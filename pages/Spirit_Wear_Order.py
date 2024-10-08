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
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Spirit Wear Order" "Contact Us"],
    key="spirit_wear_order_selectbox"
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
    
def spirit_wear_order_page():
    st.write("Spirit Wear Order")
    
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
elif page == "Spirit Wear Order":
    spirit_wear_order_page()
elif page == "Contact Us":
    contact_us_page()

# Registration Page
def spirit_wear_order_page():
    st.markdown("""
    <iframe id="JotFormIFrame-242764337730156" title="Product Order Form" onload="window.parent.scrollTo(0,0)" allowtransparency="true" allow="geolocation; microphone; camera; fullscreen" src="https://form.jotform.com/242764337730156" frameborder="0" style="min-width:100%;height:2700px;border:none;overflow:auto;" scrolling="yes"></iframe>
    <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script>
    <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-242764337730156']", "https://form.jotform.com/")</script>
    """, unsafe_allow_html=True)
    

    # Venmo and CashApp Information
    # Payment Section
    # Payment Method Section
    #st.header("Payment Method")
    #payment_method = st.selectbox("Choose your payment method", ["Venmo", "CashApp", "Credit Card"])

   # if payment_method == "Venmo":
    #    st.write("To complete your donation via Venmo, please [click here](https://venmo.com/code?user_id=3985557692613789993).")
     #   st.write("After completing the payment, please enter the transaction ID below.")
      #  transaction_id = st.text_input("Venmo Transaction ID")
    #elif payment_method == "CashApp":
     #   st.write("To complete your donation via CashApp, please [click here](https://cash.app/$MarvinAviles85).")
      #  st.write("After completing the payment, please enter the transaction ID below.")
       # transaction_id = st.text_input("CashApp Transaction ID")
    #elif payment_method == "Credit Card":
     #   st.write("To complete your donation via Credit Card, please [click here](https://buy.stripe.com/cN2044cqYfAwd9e000).")
      #  st.write("After completing the payment, please enter the transaction ID below.")
       # transaction_id = st.text_input("Credit Card Transaction ID")

# Run the page function if this file is executed
if __name__ == "__main__":
    registration_page()
