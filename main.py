
import streamlit as st


# Load custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Footer
def footer():
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Email: <a href="mailto:zuricollc@gmail.com">zuricollc@gmail.com</a></p>
            <p>Instagram: <a href="https://instagram.com/zuricollc">@zuricollc</a></p>
            <p> **We export worldwide!**<p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Services", "Contact"])

# Load CSS
load_css()

# Add a placeholder home content (optional)
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src="static/izuri-logo.jpg" style="width: 50px; margin-right: 10px;">
        <h1 style="display: inline;">Welcome to IZURI INC</h1>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    This is IZURI Main Website! Please select a page from the sidebar to view our services.
    """
)
st.video("video.mp4")

footer()
