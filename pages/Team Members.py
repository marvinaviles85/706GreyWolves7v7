import streamlit as st

# Page title and description
def team_members_page():
    st.header("Team Members")
    st.markdown("<h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>", unsafe_allow_html=True)
    
    team_members = [
        {"name": "Marvin Aviles", "position": "Founder", "photo": "Images/MarvinSr.PNG"},
        {"name": "Pam Aviles", "position": "Co-Founder/Team Trainer", "photo": "Images/Pam.jpg"},
        {"name": "Marvin Aviles Jr", "position": "Defensive Coordinator", "photo": "Images/MarvinJr.PNG"},
        # Add more team members here
    ]

    # Create a dynamic layout for team members
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(member["photo"], caption=member["name"], width=150)
        with col2:
            st.markdown(f"**Name:** {member['name']}")
            st.markdown(f"**Position:** {member['position']}")
            # Add more details if available
            # st.markdown(f"**Bio:** {member['bio']}")

# Example usage
if __name__ == "__main__":
    team_members_page()
