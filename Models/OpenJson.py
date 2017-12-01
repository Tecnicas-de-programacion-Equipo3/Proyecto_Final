import json

class OpenJson:
    @staticmethod
    def opening(file):
        try:
            with open(file + '.json', r) as in_file:
                json_file = json.load(in_file)
        except Exception:
            return None
        return json_file
