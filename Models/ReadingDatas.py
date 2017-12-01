from ast import literal_eval

class ReadingData:
    class Constants:
        prox_sensor = "ProximitySensor"
        temperature = "TemperatureSensor"

    def __init__(self, datas):
        cleanned_datas = self.__clean_data(datas)
        self.__prox_sensor = cleanned_datas.get(self.Constants.prox_sensor, None)
        self.__temperature = cleanned_datas.get(self.Constants.temperature, None)

    def __clean_data(self, datas):
        clean_data = literal_eval(datas)
        return clean_data

    def get_proximity_data(self):
        return self.__prox_sensor

    def get_temperature_data(self):
        return self.__temperature
