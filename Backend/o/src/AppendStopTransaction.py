from PyTPSTransaction import PyTPSTransaction


class AppendStopTransaction(PyTPSTransaction):
    def __init__(self, init_stops, init_code):
        super()
        self.code = init_code
        self.trip_stops = init_stops

    def do_transaction(self):
        self.trip_stops.append(self.code)

    def undo_transaction(self):
        self.trip_stops.pop()

    def to_string(self):
        return "Appending Stop"
