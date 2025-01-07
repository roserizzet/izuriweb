import streamlit as st



st.title("Contact Us")
st.write("Feel free to reach out to us!")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you for reaching out!")

# Footer
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
