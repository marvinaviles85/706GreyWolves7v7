import streamlit as st

def media_page():
    # Title and description
    st.title("Welcome to Our Media Page!")
    st.write("Check out our latest videos and don't forget to subscribe!")

    # Embed latest YouTube video
    st.markdown("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/BB_D-3LKsNY?si=8GT4jiKph8E87Skl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

    # Embed YouTube playlist
#    st.markdown("""
#    <h2>Watch Our Playlist</h2>
#    <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=YOUR_PLAYLIST_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#    """, unsafe_allow_html=True)

    # Add subscribe button
    st.markdown("""
    <h2>Subscribe to Our Channel</h2>
    <a href="https://www.youtube.com/channel/@706GreyWolves7v7?sub_confirmation=1" target="_blank">
        <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/subscribe.jpg" alt="Subscribe to our channel">
    </a>
    """, unsafe_allow_html=True)


    # Social Media Icons (Optional)
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.youtube.com/@706GreyWolves7v7" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube" width="50" height="50">
        </a>
    </div>
    """, unsafe_allow_html=True)
