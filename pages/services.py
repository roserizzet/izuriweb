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

st.title("Our Services")
service = st.selectbox(
    "Choose a category",
    ["-- Select --", "IT Consultation and Development", "Export Services", "All"]
)
if service == "IT Consultation and Development":
    st.subheader("IT Consultation and Development")
    # Adding a row of images
    col1, col2 = st.columns(2)
    with col1:
        st.image("website.jpg", caption="Web Development")
    with col2:
        st.image("hydroponics.jpg", caption="Smart Agriculture")
    
    #st.image("https://via.placeholder.com/400", caption="IT Consultation")
    st.write("- Website Development")
    st.write("- Cloud Migration and Database Management")
    st.write("- Marketing")
    st.write("- Smart Agriculture and Drone Consultation")
elif service == "Export Services":
    st.subheader("Export Services")
    # Adding a row of images
    col1, col2 = st.columns(2)
    with col1:
        st.image("export.jpg", caption="Export Services")
    with col2:
        st.image("export2.jpg", caption="Packaging")
    
    #st.image("https://via.placeholder.com/400", caption="Export Services")
    st.write("- Home Appliances")
    st.write("- USED: Cars/Bicycles/Spare-parts")
    st.write("**We export worldwide!**")
footer()