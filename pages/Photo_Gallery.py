import streamlit as st

# Page title and description
def photo_gallery_page():
    st.title("Explore Our Gallery")
    #st.markdown("<h1 class='centered-title'>Explore Our Gallery</h1>", unsafe_allow_html=True)

    photos = [
        {"caption": " ", "file": "706GWImages/RareAir.jpg"},
        {"caption": " ", "file": "706GWImages/ShockDoctor.png"},
        {"caption": " ", "file": "706GWImages/TTO.png"},
        {"caption": " ", "file": "706GWImages/TTOGamedayFlyer.jpg"},
        {"caption": " ", "file": "706GWImages/TheBoys.jpg"},
        {"caption": " ", "file": "706GWImages/TooStrong.jpg"},
        {"caption": " ", "file": "706GWImages/ValleyCenter.PNG"},
        {"caption": " ", "file": "706GWImages/VelleyCenter.jpg"},
        {"caption": " ", "file": "706GWImages/Venmo.jpg"},
        {"caption": " ", "file": "706GWImages/NXGNRegionalShowcase.jpg"},
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
