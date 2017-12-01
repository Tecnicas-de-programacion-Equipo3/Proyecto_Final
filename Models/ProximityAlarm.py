from Models.MessageAlarm import MessageAlarm

class ProximityAlarm:

    def __init__(self, status, datas):
        self.__status = status
        self.__data = datas

    def there_is_someone(self):
        if self.__status and self.__data == "True":
            alarm_alert = MessageAlarm()
            alarm_alert.send_message()




