import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ivana Carolina'
email['to'] = 'carollolivei7@gmail.com'
email['subject'] = 'test Python'

email.set_content('I am a Python developer !')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ivana.carolina00@gmail.com', 'carol2001')
    smtp.send_message(email)
    print('email send')