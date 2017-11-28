class ProximityAlarm:

    def __init__(self, status, alarm_handler):
        self.__status = status
        self.__alarm_handler = alarm_handler
        self.__activate_alarm()

    def __activate_alarm(self):
        self.__alarm_handler(self.__status)



