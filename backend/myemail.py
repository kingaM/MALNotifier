import smtplib

def sendMail(recipient, showtitle, airdate, description, url):
    SMTP_SERVER = 'smtp.mail.yahoo.com'
    SMTP_PORT = 587
     
    sender = 'malnotifier.fbhackathon@yahoo.co.uk'
    password = 'FBHackathon1'
    subject = '[MALNotifier] A new anime was just announced'
     
    body = createBody(showtitle, airdate, description, url)
     
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


def createBody(showTitile, airdate, description, url):
  return """The new show that came out is <b>""" + showTitile + """</b>. It's air date is """ + airdate + """. <br><br>
      <b>A short description:</b><br>
      """ + description + """
      <br><br>For more information see: <a href=\"http://anidb.net/perl-bin/animedb.pl?show=anime&aid=
      """ + str(url) + "\">AniDB</a>"
