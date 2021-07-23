import base64
from email.mime.text import MIMEText


RECIPIENT = "skyler@skyler.cc"

def sendMessage(message, name, email):
    letter = createLetter(RECIPIENT, RECIPIENT, createBody(message, name, email))


def createBody(message, name, email):
    return \
        "---BEGIN MESSAGE FROM {}---\n".format(name)\
        + message\
        + "---END MESSAGE FROM {}---\n".format(name) \
        + "This message was sent from the contact form at skyler.cc/contact.\n\nRespond to this email or email {}".format(email)


def createLetter(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message['reply-to']
    return {'raw': base64.urlsafe_b64encode(message.as_string())}



