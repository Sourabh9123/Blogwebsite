
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart







def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Change to the appropriate port (e.g., 465 for SSL/TLS)
    
    # Create a secure connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    
    try:
        # Login to the SMTP server
        server.login(sender_email, sender_password)
        
        # Create a message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject 

        # Add body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: Unable to send email.")
        print(e)
    finally:
        # Close the connection to the SMTP server
        server.quit()



