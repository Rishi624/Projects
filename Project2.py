# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port):
#     # Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         # Connect to the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(from_email, from_password)

#         # Send the email
#         server.sendmail(from_email, to_email, msg.as_string())
#         print(f"Email sent to {to_email}")

#     except Exception as e:
#         print(f"Failed to send email: {e}")

#     finally:
#         server.quit()

# # Example usage
# subject = "Test Email"
# body = "This is a test email."
# to_email = "ggowni@student.gitam.edu"
# from_email = "waste4159@gmail.com"
# from_password = "ufkz izzt wwkz ircd"
# smtp_server = "smtp.gmail.com"
# smtp_port = 587

# # Send a controlled number of emails
# num_emails = 100  # You can change this number
# for _ in range(num_emails):
#     send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port)





import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(server, subject, body, to_email, from_email):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Example usage
subject = "Test Email"
body = "This is a test email."
to_email = "lboggara@student.gitam.edu"
from_email = "waste4159@gmail.com"
from_password = "jupe umix nfqa xkcp"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Send a controlled number of emails
num_emails = 100  # You can change this number

try:
    # Connect to the SMTP server once
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_password)

    # Send multiple emails using the same connection
    for _ in range(num_emails):
        send_email(server, subject, body, to_email, from_email)

except Exception as e:
    print(f"Failed to connect to SMTP server: {e}")

finally:
    # Quit the server connection
    server.quit()