import smtplib

def sendMail(recipient, showId):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
     
    sender = 'comp3013.social.network@gmail.com'
    password = 'socialnetwork'
    subject = '[MALNotifier] A new anime was just announced'
    body = 'The new anime is ' + str(showId)
     
    body = "" + body + ""
     
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)
     
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
     
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)
     
    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()