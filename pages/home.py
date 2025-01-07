import streamlit as st

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

# Add logo with title
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src="logo.jpg"  style="width: 50px; margin-right: 10px;">
        <h1 style="display: inline;">IZURI INC</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
st.image("IMG_zurico.png", caption="IZURI: Excellence Delivered")
st.markdown("IZURI provides top-notch IT and export services.")

# Adding a row of images
col1, col2 = st.columns(2)
with col1:
    st.image("export1.jpg", caption="Export Services")
with col2:
    st.image("Consultation.jpg", caption="IT Consultation")
footer()

