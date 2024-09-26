import streamlit as st


# Registration Page
def registration_page():
    st.title("Registration")

    # Create outer columns
    col1, col2, col3 = st.columns(3)

    # Center the logo in the middle column
    with col2:
        st.image("Images/706gw_no_bg.png", width=200)
        
    st.markdown("<h1 class='centered-title'>Register Now</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSexO7RZIemrzcf0Y2pBDd1d7k8ehU7EqAJcwPVcXiW1ryCUjw/viewform?embedded=true" width="640" height="2665" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div> 
    """, unsafe_allow_html=True)

    # Venmo and CashApp Information


# Run the page function if this file is executed
if __name__ == "__main__":
    registration_page()
