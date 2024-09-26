import streamlit as st

# Sponsorship and Donations section
def sponsorship_and_donation_page():
    # Title
    st.title("Donate or Sponsor the Grey Wolves")

    # Display the image using Streamlit's markdown function
    image_html = """
    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Grey Wolves Logo" style="width:100%;height:auto;">
    """
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
    country = st.selectbox("Country*", ["United States", "Canada", "United Kingdom", "Australia", "Other"])
    state = st.selectbox("State*", ["Georgia", "California", "New York", "Texas", "Other"])
    is_corporate = st.checkbox("This is a corporate/organization donation")

    # Payment Method Section
    st.header("Payment Method")
    payment_method = st.selectbox("Choose your payment method", ["Venmo", "CashApp"])

    if payment_method == "Venmo":
        st.write("To complete your donation via Venmo, please [click here](https://venmo.com/code?user_id=3985557692613789993).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("Venmo Transaction ID")
    elif payment_method == "CashApp":
        st.write("To complete your donation via CashApp, please [click here](https://cash.app/$MarvinAviles85).")
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

# Run the page function if this file is executed
if __name__ == "__main__":
    sponsorship_and_donation_page()

#            save_to_csv(email, first_name, last_name, country, state, is_corporate, donation_amount, payment_method, transaction_id)

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