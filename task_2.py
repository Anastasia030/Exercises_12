class AirTicket:
    """
    Flight class for each passenger
    """
    passenger_name = []
    _from = []
    to = []
    date_time = []
    flight = []
    seat = []
    _class = []
    gate = []

    def __init__(self, passengers, nmbr_pssngr):
        """
        Initialized with the necessary information about the passenger and his ticket
        :param passengers: str, Initialized with the necessary information about the passenger and his ticket
        :param nmbr_pssngr: int, ticket processing queue number
        """
        cell_size = [16, 4, 3, 16, 20, 4, 3, 4]
        passenger = passengers.strip().split(';')
        AirTicket.passenger_name.append(passenger[0] + ' ' * (cell_size[0] - len(passenger[0])))
        AirTicket._from.append(passenger[1] + ' ' * (cell_size[1] - len(passenger[1])))
        AirTicket.to.append(passenger[2] + ' ' * (cell_size[2] - len(passenger[2])))
        AirTicket.date_time.append(passenger[3] + ' ' * (cell_size[3] - len(passenger[3])))
        AirTicket.flight.append(passenger[4] + ' ' * (cell_size[4] - len(passenger[4])))
        AirTicket.seat.append(passenger[5] + ' ' * (cell_size[5] - len(passenger[5])))
        AirTicket._class.append(passenger[6] + ' ' * (cell_size[6] - len(passenger[6])))
        AirTicket.gate.append(passenger[7] + ' ' * (cell_size[7] - len(passenger[7])))
        self.number = nmbr_pssngr

    def __str__(self):
        """
        String representation of ticket information, in a readable format
        :return: str, containing information about the ticket
        """
        answer = f'|{AirTicket.passenger_name[self.number]}|{AirTicket._from[self.number]}|' \
                 f'{AirTicket.to[self.number]}|{AirTicket.date_time[self.number]}|{AirTicket.flight[self.number]}|' \
                 f'{AirTicket.seat[self.number]}|{AirTicket._class[self.number]}|{AirTicket.gate[self.number]}|'
        return answer


class Load:
    """
    A class that reads information from a file
    """
    data = []

    @staticmethod
    def write(file):
        """
        Statistical method for downloading data from a file
        :param file: a file containing information about all passengers
        """
        with open(file, 'r') as file_out:
            description = file_out.readline()
            nmbr_pssngr = 0
            for information in file_out:
                Load.data.append(AirTicket(information, nmbr_pssngr))
                nmbr_pssngr += 1
