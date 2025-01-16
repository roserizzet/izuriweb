import streamlit as st
#important to receive data from contact from to company email
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#DB Configuration
import sqlite3
from sqlite3 import Error

# Function to connect to SQLite
def connect_to_db():
    try:
        # Create a local SQLite database file
        connection = sqlite3.connect("izuri.db")  # Database file will be created in the app directory
        return connection
    except Error as e:
        st.error(f"Error connecting to SQLite: {e}")
        return None

# Function to initialize the database
def initialize_db():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Create a table if it doesn't exist
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS contact_form (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    category TEXT NOT NULL,
                    message TEXT NOT NULL,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            connection.commit()
        except Error as e:
            st.error(f"Error initializing database: {e}")
        finally:
            connection.close()

# Function to store form data in SQLite
def store_form_data(name, email, category, message):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO contact_form (name, email, category, message)
                VALUES (?, ?, ?, ?)
                """,
                (name, email, category, message)
            )
            connection.commit()
            st.success("Thank you for reaching out! Your message has been stored.")
        except Error as e:
            st.error(f"Error storing data: {e}")
        finally:
            connection.close()

# Function to fetch data from SQLite and send it via email(Maybe Important when company grows)
# def send_data_via_email():
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT * FROM contact_form")
#             rows = cursor.fetchall()

#             # Format the data as a string
#             email_content = "Here are the submitted entries:\n\n"
#             for row in rows:
#                 email_content += f"ID: {row[0]}\n"
#                 email_content += f"Name: {row[1]}\n"
#                 email_content += f"Email: {row[2]}\n"
#                 email_content += f"Category: {row[3]}\n"
#                 email_content += f"Message: {row[4]}\n"
#                 email_content += f"Submitted At: {row[5]}\n\n"

#             # Send the email
#             send_email("Submitted Data from Contact Form", email_content)

#         except Error as e:
#             st.error(f"Error fetching data: {e}")
#         finally:
#             connection.close()

# # Function to send an email
# def send_email(subject, body):
#     sender_email = "your_email@gmail.com"  # Replace with your email
#     sender_password = "your_password"  # Replace with your email password or app password
#     recipient_email = "zuricollc@gmail.com"

#     try:
#         # Create the email
#         msg = MIMEMultipart()
#         msg["From"] = sender_email
#         msg["To"] = recipient_email
#         msg["Subject"] = subject

#         # Attach the body content
#         msg.attach(MIMEText(body, "plain"))

#         # Connect to Gmail's SMTP server
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.send_message(msg)
#             st.success("Data sent to your email successfully!")

#     except Exception as e:
#         st.error(f"Error sending email: {e}")

# Initialize the database
initialize_db()


# Contact Forms
st.title("Contact Us")
#st.write("Feel free to reach out to us!")

# Get the category from session state
if "category" not in st.session_state or st.session_state["category"] == "-- Select --":
    category = st.selectbox(
        "Choose category of Service needed",
        ["-- Select --", "IT Consultation and Development", "Export Services", "All"]
    )
else:
    category = st.session_state["category"]

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if category == "-- Select --":
            st.warning("Please select a category.")
        else:
            store_form_data(name, email, category, message)

# Footer
st.markdown("---")

#View stored Data in DB(Maybe important in future)
# View stored data
# def view_data():
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT * FROM contact_form")
#             rows = cursor.fetchall()
#             st.write("Submitted Data:")
#             for row in rows:
#                 st.write(row)
#         except Error as e:
#             st.error(f"Error fetching data: {e}")
#         finally:
#             connection.close()

# # Call the function to display data
# view_data()



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
