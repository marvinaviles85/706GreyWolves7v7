import streamlit as st

# Page title and description
def photo_gallery_page():
    st.title("Explore Our Gallery")
    #st.markdown("<h1 class='centered-title'>Explore Our Gallery</h1>", unsafe_allow_html=True)

    photos = [
        {"caption": " ", "file": "706GWImages/FSG_Sign.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_13U.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_13U_CHamps.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_13U_Champs_2.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_13U_Coaches.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_at_FSG_1.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_Coachs_FSG_Champs.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_FSG_Team_Champs.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_FSG_Trophy.JPG"},
        {"caption": " ", "file": "706GWImages/NFZ_Prayer_3.JPG"},
        # Add more photos here
    ]

    # Create a dynamic layout for the photo gallery
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
