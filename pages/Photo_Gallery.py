import os
import streamlit as st

# Function to load images dynamically from a folder
def load_images_from_folder(folder_path):
    image_files = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for valid image file extensions
            image_files.append({"caption": file_name, "file": os.path.join(folder_path, file_name)})
    return image_files

# Function to display photos for the selected tournament
def display_tournament_photos(folder_path, tournament_name):
    st.header(f"Photos from {tournament_name}")
    photos = load_images_from_folder(folder_path)

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

# Main photo gallery page
def photo_gallery_page():
    st.title("Tournament Photo Gallery")

    # Dictionary linking tournament names to their respective folder paths
    tournament_folders = {
        #"Rare Air": "706GWImages/RareAir",
        "Hands League": "706GWImages/Hands League 4-19/",
        #"TTO": "706GWImages/TTO",
        #"The Boys": "706GWImages/The Boys",
        #"Too Strong": "706GWImages/Too Strong",
        #"Valley Center": "706GWImages/Valley Center",
        #"Venmo": "706GWImages/Venmo",
        #"NXGN Regional Showcase": "706GWImages/NXGN Regional Showcase"
    }

    # Sidebar to select a tournament
    st.sidebar.title("Select a Tournament")
    selected_tournament = st.sidebar.selectbox("Choose a tournament:", list(tournament_folders.keys()))

    if selected_tournament:
        folder_path = tournament_folders[selected_tournament]
        display_tournament_photos(folder_path, selected_tournament)

# Example usage
if __name__ == "__main__":
    photo_gallery_page()
