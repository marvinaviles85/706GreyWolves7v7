import streamlit as st
import pandas as pd
import os
import webbrowser


# Dropdown menu for pages selection
# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Team Members", "Upcoming Matches", "Sponsorship and Donation", "Registration", "Contact Us"],
    key="sponsorship_and_donation_selectbox"
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
    
def update_csv(new_data):
    # Path to your CSV file
    csv_file_path = "sponsorships.csv"

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        # Create the CSV file with headers if it doesn't exist
        df = pd.DataFrame(columns=new_data.keys())
        df.to_csv(csv_file_path, index=False)

    # Read the existing CSV file
    df = pd.read_csv(csv_file_path)

    # Append the new data using concat
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated CSV file
    df.to_csv(csv_file_path, index=False)
# Sponsorship and Donations section
def sponsorship_and_donation_page():
    # Title
    st.title("Donate or Sponsor the Grey Wolves")

    # Display the image using Streamlit's markdown function
    #image_html = """
    #<img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Grey Wolves Logo" style="width:100%;height:auto;">
    #"""
    #st.markdown(image_html, unsafe_allow_html=True)

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
        Your generous donation assists with the costs of: uniforms, softshell helmets, player equipment, tournament fees, player travel expenses, and more.
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
    country = st.selectbox("Country*", ["United States", "Canada", "Other"])
    state = st.selectbox("State*", ["Georgia", "California", "New York", "Texas", "Other"])
    is_corporate = st.checkbox("This is a corporate/organization donation")

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

    #st.header("Complete Your Payment")
    #if st.button("Pay Now"):
    #    webbrowser.open("https://buy.stripe.com/cN2044cqYfAwd9e000")

    # Summary Section
    st.header("Summary")
    st.write(f"Donation: ${donation_amount:.2f}")
    st.write(f"Payment Method: {payment_method}")

    # Submit Button
    if st.button("Submit"):
        if not transaction_id:
            st.error(f"Please enter the {payment_method} transaction ID to confirm your payment.")
        else:
            # Update the CSV file
            new_data = {
                "Email": email,
                "First Name": first_name,
                "Last Name": last_name,
                "Country": country,
                "State": state,
                "Corporate Donation": is_corporate,
                "Donation Amount": donation_amount,
                "Payment Method": payment_method,
                "Transaction ID": transaction_id
            }
            update_csv(new_data)
            st.success("Thank you for your donation!")

# Run the page function if this file is executed
if __name__ == "__main__":
    sponsorship_and_donation_page()
