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
        .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: None;
        flex-wrap: wrap;
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        z-index: 1000, /* Ensure it stays on top of other content */
    }
    .top-bar img {
        height: 50px;
    }
    .top-bar select {
        padding: 5px;
        font-size: 16px;
    }
    @media (max-width: 600px) {
        .top-bar {
            flex-direction: column;
            align-items: flex-start;
        }
        .top-bar img {
            margin-bottom: 10px;
        }
        .top-bar select {
            width: 100%;
        }
        body {
            padding-top: 70px;
        }
</style>
"""
st.set_page_config(layout="wide")

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add the image and navigation bar to the top of the page
st.markdown("""
<div class="top-bar">
    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Logo">
    <div id="dropdown-container"></div>
</div>
""", unsafe_allow_html=True)

# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donations", "Registration", "Contact Us"]
)
# Sponsorship and Donations section
#elif page == "Sponsorship and Donations":
# Title
st.title("Donate or Sponsor the Grey Wolves")

# Display the image using Streamlit's markdown function
st.markdown(image_html, unsafe_allow_html=True)

# Button to show impact information
if st.button("What impact will your donation have?"):
    st.sidebar.title("Impact of Your Donation")
    st.sidebar.write("""
    The 706 Grey Wolves (706 GW) is a dedicated travel 7v7 football team for youth aged 11-18. As we gear up for our second season with the Hands League, we are excited to announce our schedule from January 2025 to June 2025. Every Saturday, 706 GW will travel out of state for 7v7 tournaments, while also competing in local Augusta Hands League 7v7 tournaments. 706 GW thrives thanks to the generous support of our sponsors and the unwavering commitment of our volunteers. We invite you to join us in our mission to shape the leaders of tomorrow by supporting the 706 Grey Wolves.

    Sponsorship Levels
    - $100 Individual Donation: Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account.
    - $250 Donation: Your business name and logo will be prominently featured on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be included on a sponsor banner (provided by 706 GW) displayed every Saturday during multiple games.
    - $500 Business Donation: Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be featured on a sponsor banner (provided by 706 GW) showcased every Saturday during multiple games, and proudly displayed on players’ uniforms.

    Donation Information
    Your generous donation assists with the costs of: uniforms, softshell helmets, player equipment, tournament fees, player insurance, qualified family assistance, and medical supplies.
    """)

# Donation Section
st.header("Your donation")
donation_options = ["One-time donation", "$100", "$250", "$500", "$1000"]
donation_choice = st.radio("Choose your donation amount", donation_options)

if donation_choice == "One-time donation":
    donation_amount = st.number_input("Enter your donation amount", min_value=0.00, format="%.2f")
else:
    donation_amount = float(donation_choice.strip('$'))

st.write(f"Donation Amount: ${donation_amount:.2f}")

# Your Details Section
st.header("Your details")
email = st.text_input("Email*")
first_name = st.text_input("First name*")
last_name = st.text_input("Last name*")
country = st.selectbox("Country*", ["United States", "Canada", "United Kingdom", "Australia", "Other"])
state = st.selectbox("State*", ["Georgia", "California", "New York", "Texas", "Other"])
is_corporate = st.checkbox("This is a corporate/organization donation")

# Payment Method Section
st.header("Payment Method")
payment_method = st.selectbox("Choose your payment method", ["Venmo", "CashApp"])

if payment_method == "Venmo":
    st.write("To complete your donation via Venmo, please click here.")
    st.write("After completing the payment, please enter the transaction ID below.")
    transaction_id = st.text_input("Venmo Transaction ID")
elif payment_method == "CashApp":
    st.write("To complete your donation via CashApp, please click here.")
    st.write("After completing the payment, please enter the transaction ID below.")
    transaction_id = st.text_input("CashApp Transaction ID")

# Summary Section
st.header("Summary")
st.write(f"Donation: ${donation_amount:.2f}")
st.write(f"Payment Method: {payment_method}")

# Submit Button
if st.button("Submit"):
    if not transaction_id:
        st.error(f"Please enter the {payment_method} transaction ID to confirm your payment.")
    else:
        st.success("Thank you for your donation!")
        save_to_csv(email, first_name, last_name, country, state, is_corporate, donation_amount, payment_method, transaction_id)

#def save_to_csv(email, first_name, last_name, country, state, is_corporate, donation_amount, payment_method, transaction_id):
#    import pandas as pd
#    import os
#
#    # Create a DataFrame with the donation details
#    df = pd.DataFrame({
#        'Email': [email],
#        'First Name': [first_name],
#        'Last Name': [last_name],
#        'Country': [country],
#        'State': [state],
#        'Corporate Donation': [is_corporate],
#        'Donation Amount': [donation_amount],
#        'Payment Method': [payment_method],
#        'Transaction ID': [transaction_id]
#    })
#
#    # Save the DataFrame to a CSV file
#    csv_file = 'donations.csv'
#    if os.path.exists(csv_file):
#        df.to_csv(csv_file, mode='a', header=False, index=False)
#    else:
#        df.to_csv(csv_file, index=False)
#
#    # Upload the CSV file to GitHub
#    upload_to_github(csv_file)
#
#def upload_to_github(csv_file):
#    from github import Github
#
#    # Authenticate to GitHub
#    g = Github("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")
#
#    # Get the repository
#    repo = g.get_user().get_repo("706GreyWolves7v7")
#
#    # Read the CSV file content
#    with open(csv_file, 'r') as file:
#        content = file.read()
#
#    # Create or update the file in the repository
#    try:
#        contents = repo.get_contents(csv_file)
#        repo.update_file(contents.path, "Update donations", content, contents.sha)
#    except:
#        repo.create_file(csv_file, "Create donations file", content)