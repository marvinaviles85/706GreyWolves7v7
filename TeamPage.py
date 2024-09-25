import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import streamlit.components.v1 as components
import pandas as pd
import requests
import base64
import json
import os

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
#st.set_page_config(layout="wide")

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

st.markdown("""
<script>
    const dropdownContainer = document.getElementbyId('drowndown-container');
    const selectbox = document.querySelector('select[data-testid="stSelectbox"]');
    dropdownContainer.appendChild(selectbox);
</script>
""", unsafe_allow_html=True)
# Page title and description

# Home section
if page == "Home":
    st.markdown("<h1 class='title'>706 Grey Wolves 7v7</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='centered-text'>**Welcome to the home of the 706 Grey Wolves!**\n\nExplore our team members, schedule, and photos.</h1>", unsafe_allow_html=True)
    #st.write("Welcome to the home page!")
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.write("<h3 class='centered-text'>Registration is now open for age groups 11U to 18U! Spots are limited, so secure your place today!</h3>", unsafe_allow_html=True)

    # Add a scrolling image gallery
    images = [
        {'img': '706GWImages/AllStars.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/BJ.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/BJ and Alan.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/cody.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Dylan.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/FirstTeamImage.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Flash.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/GetOutTheWay.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/HunterHeadTop.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/Isaac.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/MikeWeathers.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/MoneyInTheBank.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/PB12.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/TheBoys.jpg', 'title': '', 'text': ''},
        {'img': '706GWImages/TooStrong.jpg', 'title': '', 'text': ''},
    ]

    carousel(images)
    st.header("Latest News")
    st.write("Stay tuned for the latest news and updates.")

     # Add sponsors section
    st.markdown("""
    <h1 class='centered-title'>Our Valued Sponsors</h1>
    <p class='subtext'>Click on the images to visit their websites</p>
""", unsafe_allow_html=True)
    sponsors_donors = [
        {"name": "", "position": "", "photo": "706GWImages/VetsValor.JPG"}
    ]
        
    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # First and third images in the first outer column
    with col1:
        st.markdown("""
            <div>
                <a href="https://www.vetvalor.com" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/VetValor.PNG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 100;">
                <a href="https://www.amsoil.com/?zo=408125" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/amsoil.png" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <a href="https://www.valleycenterrepair.com/" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/ValleyCenter.PNG" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

# Team members section
elif page == "Team Members":
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>", unsafe_allow_html=True)
    team_members = [
        {"name": "Marvin Aviles", "position": "Founder", "photo": "Images/MarvinSr.PNG"},
        {"name": "Pam Aviles", "position": "Co-Founder/Team Trainer", "photo": "Images/Pam.jpg"},
        {"name": "Marvin Aviles Jr", "position": "Defensive Coordinator", "photo": "Images/MarvinJr.PNG"},
        # Add more team members here
    ]

    # Create outer columns
    col1, col2 = st.columns(2)

    # First and third images in the first outer column
    with col1:
        st.image(team_members[0]["photo"], caption=team_members[0]["name"], width=200)
        st.write(f"Position: {team_members[0]['position']}")
        st.image(team_members[2]["photo"], caption=team_members[2]["name"], width=200)
        st.write(f"Position: {team_members[2]['position']}")

    # Second image in the second outer column
    with col2:
        st.image(team_members[1]["photo"], caption=team_members[1]["name"], width=200)
        st.write(f"Position: {team_members[1]['position']}")


# Schedule section
elif page == "Upcoming Matches":
    st.header("Upcoming Matches")
    matches = [
        {"date": "2025-01-01", "opponent": "TBD", "location": "TBD"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD"},
        # Add more matches here
    ]

    for match in matches:
        st.write(f"{match['date']} - vs {match['opponent']} ({match['location']})")

# Sponsorship and Donations section
elif page == "Sponsorship and Donations":
    # Page title
# HTML and CSS to position the image
    image_html = """
        <div style="position: absolute; top: 5px; right: 5px;">
            <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/FirstTeamImage.jpg" alt="Your Image" width="300">
        </div>
        """

    # Display the image using Streamlit's markdown function
    st.markdown(image_html, unsafe_allow_html=True)

    # JavaScript for side scroll action
    scroll_js = """
        <script>
        function showImpact() {
            var sidebar = document.getElementById("sidebar-content");
            sidebar.style.display = "block";
            sidebar.scrollIntoView({behavior: 'smooth'});
        }
        </script>
        """

    # Embed the JavaScript in Streamlit
    components.html(scroll_js)

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

    # Add a hidden div for the sidebar content
    st.sidebar.markdown('<div id="sidebar-content" style="display:none;"></div>', unsafe_allow_html=True)

    # Donation Section
    st.header("Your Sponsorship or Donation")
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

    # Submit Button
    if st.button("Submit"):
        if not transaction_id:
            st.error(f"Please enter the {payment_method} transaction ID to confirm your payment.")
        else:
            st.success("Thank you for your donation!")
            save_to_csv(email, first_name, last_name, country, state, is_corporate, donation_amount, payment_method,
                        transaction_id)


    def save_to_csv(email, first_name, last_name, country, state, is_corporate, donation_amount, payment_method,
                    transaction_id):
        # Create a DataFrame with the donation details
        df = pd.DataFrame({
            'Email': [email],
            'First Name': [first_name],
            'Last Name': [last_name],
            'Country': [country],
            'State': [state],
            'Corporate Donation': [is_corporate],
            'Donation Amount': [donation_amount],
            'Payment Method': [payment_method],
            'Transaction ID': [transaction_id]
        })

        # Save the DataFrame to a CSV file
        csv_file = 'donations.csv'
        if os.path.exists(csv_file):
            df.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_file, index=False)

        # Upload the CSV file to GitHub
        upload_to_github(csv_file)


    def upload_to_github(csv_file):
        # Authenticate to GitHub
        g = Github("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")

        # Get the repository
        repo = g.get_user().get_repo("706GreyWolves7v7")

        # Read the CSV file content
        with open(csv_file, 'r') as file:
            content = file.read()

        # Create or update the file in the repository
        try:
            contents = repo.get_contents(csv_file)
            repo.update_file(contents.path, "Update donations", content, contents.sha)
        except:
            repo.create_file(csv_file, "Create donations file", content)

# Registration Page
if page == "Registration":
    # Dictionary to store the count of registered players for each age group
    player_limits = {
        "11U": 20,
        "13U": 20,
        "15U": 20,
        "18U": 20
    }

# Dictionary to store the current count of registered players for each age group
    registered_players = {
        "11U": 0,
        "13U": 0,
        "15U": 0,
        "18U": 0
    }

# Dictionary to store assigned jersey numbers for each age group
    assigned_jersey_numbers = {
        "11U": set(),
        "13U": set(),
        "15U": set(),
        "18U": set()
    }

# Function to get available jersey numbers for a specific age group
def get_available_jersey_numbers(age_group):
    all_numbers = set(range(00, 100))  # Assuming jersey numbers range from 1 to 99
    return sorted(all_numbers - assigned_jersey_numbers[age_group])

# Registration Section
st.header("Player Registration")

# Player Details Section
st.header("Player Details")
first_name = st.text_input("First Name*")
last_name = st.text_input("Last Name*")
email = st.text_input("Email*")
phone = st.text_input("Phone Number*")
age_group = st.selectbox("Age Group*", ["11U", "13U", "15U", "18U"])
name_on_jersey = st.text_input("Name Requested on Jersey")

# Check if the age group has reached its player limit
if registered_players[age_group] >= player_limits[age_group]:
    st.error(f"Registration for {age_group} is full. Please select a different age group.")
else:
    jersey_number = st.selectbox("Jersey Number*", get_available_jersey_numbers(age_group))
    jersey_size = st.selectbox("Jersey Size*", ["Youth Small", "Youth Medium", "Youth Large", "Youth Extra Large", "Adult Small", "Adult Medium", "Adult Large", "Adult Extra Large"])
    shorts_size = st.selectbox("Shorts Size*", ["Youth Small", "Youth Medium", "Youth Large", "Youth Extra Large", "Adult Small", "Adult Medium", "Adult Large", "Adult Extra Large"])

    # Address Section
    st.header("Address")
    street = st.text_input("Street Address*")
    city = st.text_input("City*")
    zip_code = st.text_input("Zip Code*")
    country = st.selectbox("Country*", ["United States", "Other"])
    state = st.selectbox("State*", ["Georgia", "South Carolina", "Texas", "Other"])

    # Emergency Contact Section
    st.header("Emergency Contact")
    emergency_contact_name = st.text_input("Emergency Contact Name*")
    emergency_contact_phone = st.text_input("Emergency Contact Phone Number*")
    relationship = st.text_input("Relationship to Player*")

    # Payment Method Section
    st.header("Payment Method")
    payment_method = st.selectbox("Choose your payment method", ["Venmo", "CashApp"])

    if payment_method == "Venmo":
        st.write("To complete your payment via Venmo, please [click here](https://venmo.com/code?user_id=3985557692613789993).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("Venmo Transaction ID")
    elif payment_method == "CashApp":
        st.write("To complete your payment via CashApp, please [click here](https://cash.app/$MarvinAviles85).")
        st.write("After completing the payment, please enter the transaction ID below.")
        transaction_id = st.text_input("CashApp Transaction ID")

    # Summary Section
    st.header("Summary")
    st.write(f"Player Name: {first_name} {last_name}")
    st.write(f"Email: {email}")
    st.write(f"Phone Number: {phone}")
    st.write(f"Age Group: {age_group}")
    st.write(f"Name on Jersey: {name_on_jersey}")
    st.write(f"Jersey Number: {jersey_number}")
    st.write(f"Jersey Size: {jersey_size}")
    st.write(f"Shorts Size: {shorts_size}")
    st.write(f"Address: {street}, {city}, {state}, {country}, {zip_code}")
    st.write(f"Emergency Contact: {emergency_contact_name} ({relationship}) - {emergency_contact_phone}")
    st.write(f"Payment Method: {payment_method}")

    # Submit Button
    if st.button("Submit"):
        if not (first_name and last_name and email and phone and age_group and name_on_jersey and jersey_number and jersey_size and shorts_size and street and city and state and country and zip_code and emergency_contact_name and emergency_contact_phone and relationship and transaction_id):
            st.error("Please fill out all required fields.")
        else:
            # Update the assigned jersey numbers
            assigned_jersey_numbers[age_group].add(jersey_number)

            # Update the registered players count
            registered_players[age_group] += 1

            # Create a DataFrame
            data = {
                "First Name": [first_name],
                "Last Name": [last_name],
                "Email": [email],
                "Phone": [phone],
                "Age Group": [age_group],
                "Name on Jersey": [name_on_jersey],
                "Jersey Number": [jersey_number],
                "Jersey Size": [jersey_size],
                "Shorts Size": [shorts_size],
                "Country": [country],
                "State": [state],
                "Street": [street],
                "City": [city],
                "Zip Code": [zip_code],
                "Emergency Contact Name": [emergency_contact_name],
                "Emergency Contact Phone": [emergency_contact_phone],
                "Relationship": [relationship],
                "Payment Method": [payment_method],
                "Transaction ID": [transaction_id]
            }
            df = pd.DataFrame(data)

            # Save the DataFrame to a CSV file
            csv_file = 'registrations.csv'
            if os.path.exists(csv_file):
                df.to_csv(csv_file, mode='a', header=False, index=False)
            else:
                df.to_csv(csv_file, index=False)

            # Upload the CSV file to GitHub
            upload_to_github(csv_file)

            st.success("Thank you for registering!")

def upload_to_github(csv_file):
    # Read the CSV file content
    with open(csv_file, 'r') as file:
        content = file.read()

    # Encode the content to base64
    encoded_content = base64.b64encode(content.encode()).decode()

    # Prepare the request payload
    payload = {
        "message": "Update registrations",
        "content": encoded_content
    }

    # GitHub API URL for the file
    url = f"https://api.github.com/repos/marvinaviles85/706GreyWolves7v7/contents/{csv_file}"

    # GitHub token
    token = os.getenv("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")

    # Headers for the request
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Make the request to create or update the file
    response = requests.put(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print("File created successfully.")
    elif response.status_code == 200:
        print("File updated successfully.")
    else:
        print(f"Failed to upload file: {response.json()}")

if page == "Contact Us":
    st.header("Contact Us")
    st.image("Images/706gw_no_bg.png", use_column_width=True)
    st.write("Email us at 706greywovles7v7@gmail.com")
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
        """,
        unsafe_allow_html=True
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
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" height="50">
                </a>
                <a href="https://www.instagram.com/706greywolves" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" height="50">
                </a>
            </div>
        """, unsafe_allow_html=True)
