# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:

#         SendEmail(
#             tracker.get_slot("email"),
#             tracker.get_slot("subject"),
#             tracker.get_slot("message")
#         )
#         dispatcher.utter_message(
#             "Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email")))
#         return []


# def SendEmail(toaddr, subject, message):
#     fromaddr = 'shahcharmi144@gmail.com'
#     # instance of MIMEMultipart
#     msg = MIMEMultipart()

#     # storing the senders email address
#     msg['From'] = fromaddr

#     # storing the receivers email address
#     msg['To'] = toaddr

#     # storing the subject
#     msg['Subject'] = subject

#     # string to store the body of the mail
#     body = message

#     # attach the body with the msg instance
#     msg.attach(MIMEText(body, 'plain'))

#     # open the file to be sent
#     # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
#     # attachment = open(filename, "rb")
#     #
#     # # instance of MIMEBase and named as p
#     # p = MIMEBase('application', 'octet-stream')
#     #
#     # # To change the payload into encoded form
#     # p.set_payload((attachment).read())
#     #
#     # # encode into base64
#     # encoders.encode_base64(p)
#     #
#     # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#     #
#     # # attach the instance 'p' to instance 'msg'
#     # msg.attach(p)

#     # creates SMTP session
#     s = smtplib.SMTP('smtp.gmail.com', 587)

#     # start TLS for security
#     s.starttls()

#     # Authentication
#     try:
#         s.login(fromaddr, "djxqzzzfthcuckqp")

#         # Converts the Multipart msg into a string
#         text = msg.as_string()

#         # sending the mail
#         s.sendmail(fromaddr, toaddr, text)
#     except Exception as e:
#         print("An Error occured while sending email.", str(e))
#     finally:
#         # terminating the session
#         s.quit()

# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# Importing required modules
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib

# Creating new class to send emails.


class ActionEmail(Action):

    def name(self) -> Text:

        # Name of the action
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Getting the data stored in the
        # slots and storing them in variables.
        user_name = tracker.get_slot("name")
        email_id = tracker.get_slot("email")

        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Making connection secured
        s.starttls()
        try:
            s.login("shahcharmi144@gmail.com", "djxqzzzfthcuckqp")

        # Message to be sent
            message = "Hello {} , This is a demo message".format(user_name)

        # Sending the mail
            s.sendmail("shahcharmi144@gmail.com", email_id, message)

        except Exception as e:
            print("An Error occured while sending email.", str(e))
        finally:
            # terminating the session
            s.quit()

        # Authentication

        # Closing the connection

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []
