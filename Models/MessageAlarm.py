from twilio.rest import Client
from Models.OpenJson import OpenJson

class MessageAlarm():
    class Constants:
        env_file = 'Env/env'
        message = "Alert! There is someone near your house"
        account_sid = "account_sid"
        auth_token = "auth_token"
        twilio_phone = "twilio_phone"
        phone = "+525560785905"

    def __init__(self):
        env_var = OpenJson.opening(self.Constants.env_file)
        if env_var is None: return
        account_sid = env_var.get(self.Constants.account_sid, None)
        auth_token = env_var.get(self.Constants.auth_token, None)
        self.__twilio_phone = env_var.get(self.Constants.twilio_phone, None)
        self.__client = Client(account_sid, auth_token)

    def send_message(self):
        self.__client.messages.create(to = self.Constants.phone, from_= self.__twilio_phone, body = self.Constants.message)
