from main import iata_code_list

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data = iata_code_list

    def give_name(self):
        for self.item in self.data:
            self.item = 'Testing'
