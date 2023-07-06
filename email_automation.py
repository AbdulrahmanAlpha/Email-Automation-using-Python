import smtplib
import email.message
import os
import schedule
import time

def send_email():
    # Create a message object
    msg = email.message.Message()
    msg['Subject'] = 'Hello World'
    msg['From'] = 'sender@example.com'
    msg['To'] = 'recipient@example.com'
    msg.set_payload('This is a test email.')

    # Add an attachment to the message
    attachment_path = 'attachment.txt'
    with open(attachment_path, 'rb') as f:
        attachment_data = f.read()
    attachment = email.mime.application.MIMEApplication(attachment_data, _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
    msg.attach(attachment)

    # Send the email message
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sender@example.com', 'password')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print('Failed to send email:', str(e))

# Schedule the email sending
schedule.every().day.at('09:00').do(send_email)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)