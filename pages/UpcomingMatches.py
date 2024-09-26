import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

# Inject custom CSS and JavaScript
st.markdown("""
    <style>
        [data-testid='stSidebarNav'] {
            display: none;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sidebar = document.querySelector("[data-testid='stSidebarNav']");
            if (sidebar) {
                sidebar.style.display = 'none';
            }
        });
    </script>
    """, unsafe_allow_html=True)

def upcoming_matches_page():
    st.header("Upcoming Matches")
    
    matches = [
        {"date": "2025-01-01", "opponent": "TBD", "location": "TBD"},
        {"date": "2025-02-01", "opponent": "TBD", "location": "TBD"},
        # Add more matches here
    ]

    st.markdown("<style>.match-card { padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }</style>", unsafe_allow_html=True)

    for match in matches:
        st.markdown(f"""
        <div class="match-card">
            <strong>Date:</strong> {match['date']}<br>
            <strong>Opponent:</strong> {match['opponent']}<br>
            <strong>Location:</strong> {match['location']}
        </div>
        """, unsafe_allow_html=True)

# Example usage
if __name__ == "__main__":
    upcoming_matches_page()
