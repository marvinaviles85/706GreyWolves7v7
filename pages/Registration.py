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
    st.markdown("<h2 class='section-title'>Payment Information</h2>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-content'>Please send your registration payment to our Venmo or CashApp account:</div>",
        unsafe_allow_html=True)

    # Create columns for QR codes and buttons
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div>
                <a href="https://venmo.com/code?user_id=3985557692613789993" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/Venmo.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://cash.app/$MarvinAviles85" target="_blank">
                    <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/CashApp.jpg" width="200">
                </a>
            </div>
        """, unsafe_allow_html=True)

    # Additional registration information
    st.markdown("""
    <h2 class='section-title'>Additional Information</h2>
    <div class='section-content'>
        <p>Please ensure that all fields in the registration form are filled out accurately. Once you have completed the form and submitted your payment, you will receive a confirmation email with further details.</p>
        <p>If you have any questions or need assistance, please contact us at <a href="mailto:support@706greywolves.com">support@706greywolves.com</a>.</p>
    </div>
    """, unsafe_allow_html=True)

# Run the page function if this file is executed
if __name__ == "__main__":
    registration_page()
