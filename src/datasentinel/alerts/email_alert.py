import os
import smtplib

from email.message import EmailMessage


class EmailSender:

    def __init__(self):

        self.sender = os.getenv("EMAIL_ADDRESS")
        self.password = os.getenv("EMAIL_PASSWORD")

    def send(

        self,

        receiver,

        subject,

        body,

        attachment=None,

    ):

        message = EmailMessage()

        message["From"] = self.sender
        message["To"] = receiver
        message["Subject"] = subject

        message.set_content(body)

        if attachment:

            with open(attachment, "rb") as file:

                message.add_attachment(

                    file.read(),

                    maintype="application",

                    subtype="pdf",

                    filename=os.path.basename(attachment),

                )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

            smtp.starttls()

            smtp.login(

                self.sender,

                self.password,

            )

            smtp.send_message(message)