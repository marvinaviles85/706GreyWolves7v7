import streamlit as st

# Data structure to organize photos by tournament
tournament_photos = {
    "Rare Air": [
        {"caption": "Rare Air 1", "file": "706GWImages/RareAir.jpg"}
    ],
    "Shock Doctor": [
        {"caption": "Shock Doctor 1", "file": "706GWImages/ShockDoctor.png"}
    ],
    "TTO": [
        {"caption": "TTO 1", "file": "706GWImages/TTO.png"},
        {"caption": "TTO Gameday", "file": "706GWImages/TTOGamedayFlyer.jpg"}
    ],
    "The Boys": [
        {"caption": "The Boys", "file": "706GWImages/TheBoys.jpg"}
    ],
    "Too Strong": [
        {"caption": "Too Strong", "file": "706GWImages/TooStrong.jpg"}
    ],
    "Valley Center": [
        {"caption": "Valley Center", "file": "706GWImages/ValleyCenter.PNG"}
    ],
    "Venmo": [
        {"caption": "Venmo", "file": "706GWImages/Venmo.jpg"}
    ],
    "NXGN Regional Showcase": [
        {"caption": "NXGN Showcase", "file": "706GWImages/NXGNRegionalShowcase.jpg"}
    ]
}

# Main photo gallery page
def photo_gallery_page():
    st.title("Tournament Photo Gallery")
    
    # Display clickable tournament links
    st.header("Select a Tournament")
    for tournament in tournament_photos.keys():
        if st.button(tournament):  # Button to select tournament
            display_tournament_photos(tournament)

# Function to display photos for the selected tournament
def display_tournament_photos(tournament):
    st.header(f"Photos from {tournament}")
    photos = tournament_photos[tournament]

    # Create a dynamic layout for the selected tournament
    col1, col2, col3 = st.columns(3)
    for idx, photo in enumerate(photos):
        if idx % 3 == 0:
            with col1:
                st.image(photo["file"], caption=photo["caption"], use_column_width=True)
        elif idx % 3 == 1:
            with col2:
                st.image(photo["file"], caption=photo["caption"], use_column_width=True)
        else:
            with col3:
                st.image(photo["file"], caption=photo["caption"], use_column_width=True)

# Example usage
if __name__ == "__main__":
    photo_gallery_page()
