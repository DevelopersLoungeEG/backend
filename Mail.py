from google.appengine.api import mail



message = AdminEmailMessage()
message.sender = 'marwanxreda9@gmail.com'
message.subject = 'TEST'
message.body = 'WE ARE Done!!!!!!'
message.check_initialized()
message.send()




# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
​
sg = sendgrid.SendGridClient("YOUR_SENDGRID_API_KEY")
message = sendgrid.Mail()
​
message.add_to("test@sendgrid.com")
message.set_from("you@youremail.com")
message.set_subject("Sending with SendGrid is Fun")
message.set_html("and easy to do anywhere, even with Python")
sg.send(message)
