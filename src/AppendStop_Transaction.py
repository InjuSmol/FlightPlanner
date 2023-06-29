from PyTPSTransaction import pyTPS_Transaction

class AppendStop_Transaction(pyTPS_Transaction):
    def __init__(self, initStops, initCode):
        super().__init__()
        self.code = initCode
        self.tripStops = initStops

    def doTransaction(self):
        self.tripStops.append(self.code)

    def undoTransaction(self):
        self.tripStops.pop()

    def toString(self):
        return "Appending Stop"
