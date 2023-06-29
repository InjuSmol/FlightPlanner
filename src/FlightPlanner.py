from Airport import Airport
from pyTPS import pyTPS
from WeightedGraph import WeightedGraph
import readline
from AppendStop_Transaction import AppendStop_Transaction
import json

tps = pyTPS()
airportGraph = WeightedGraph()
stops = []

def displayAirports():
    print("\n\nAIRPORTS YOU CAN TRAVEL TO AND FROM:\n")
    codes = []
    airportGraph.getKeys(codes)
    text = ""
    for i in range(len(codes)):
        if (i % 10) == 0:
            text += "\t"
        text += codes[i]
        if i < (len(codes) - 1):
            text += ", "
        if (i % 10) == 9:
            text += "\n"
    text += "\n\n"
    print(text)

def displayCurrentTrip():
    text = ""
    text += "Current Trip Stops: \n"
    for i in range(len(stops)):
        text += "\t" + str(i + 1) + ". " + stops[i] + "\n"
    text += "\nCurrent Trip Legs: \n"
    legNum = 1
    tripDistance = 0.0
    for i in range(len(stops)):
        legDistance = 0.0

        if legNum < len(stops):
            text += "\t" + str(i + 1) + '. '

            lastStop = stops[legNum - 1]

            nextStop = stops[legNum]

            route = []
            airportGraph.findPath(route, lastStop, nextStop)

            if len(route) < 2:
                text += "No Route Found from " + lastStop + " to " + nextStop + "\n"
            else:
                for i in range(len(route) - 1):
                    a1 = airportGraph.getNodeData(route[i])
                    a2 = airportGraph.getNodeData(route[i + 1])
                    distance = Airport.calculateDistance(a1, a2)
                    legDistance += distance
                    if i == 0:
                        text += a1.getCode()
                    text += "-" + a2.getCode()
                text += " (Leg Distance: " + str(legDistance) + " miles)\n"

            legNum += 1
            tripDistance += legDistance
    text += "Total Trip Distance: " + str(tripDistance) + " miles\n\n"
    print(text)

def displayMenu():
    text = "ENTER A SELECTION\n"
    text += "S) Add a Stop to your Trip\n"
    text += "U) Undo\n"
    text += "R) Redo\n"
    text += "E) Empty Trip\n"
    text += "Q) Quit\n"
    print(text)

def process_user_input():
    # GET THE USER SELECTION
    entry = input()

    if entry == "S":
        print("\nEnter the Airport Code: ")
        entry = input()
        if airportGraph.node_exists(entry):
            neighbors = []
            airportGraph.get_neighbors(neighbors, entry)

            # MAKE SURE IT IS NOT THE SAME AIRPORT CODE AS THE PREVIOUS STOP
            if len(stops) > 0:
                last_stop = stops[-1]
                if last_stop == entry:
                    print("DUPLICATE STOP ERROR - NO STOP ADDED")
                else:
                    transaction = AppendStop_Transaction(stops, entry)
                    tps.add_transaction(transaction)
            else:
                transaction = AppendStop_Transaction(stops, entry)
                tps.add_transaction(transaction)
        else:
            print("INVALID AIRPORT CODE ERROR - NO STOP ADDED")
    elif entry == "U":
        tps.undo_transaction()
    elif entry == "R":
        tps.do_transaction()
    elif entry == "E":
        tps.clear_all_transactions()
    elif entry == "Q":
        return False
    return True

# def getUserInput(prompt):
#     answer = input(prompt)
#     return answer
#
# def processUserInput():
#     choice = getUserInput("-")
#     if choice == "S":
#         enteredCode = getUserInput("\nEnter the Airport Code: ")
#         if airportGraph.nodeExists(enteredCode):
#             neighbors = []
#             airportGraph.getNeighbors(neighbors, enteredCode)
#
#             if len(stops) > 0:
#                 lastStop = stops[-1]
#                 if lastStop == enteredCode:
#                     print("DUPLICATE STOP ERROR - NO STOP ADDED")
#                 else:
#                     transaction = AppendStop_Transaction(stops, enteredCode)
#                     tps.addTransaction(transaction)
#             else:
#                 transaction = AppendStop_Transaction(stops, enteredCode)
#                 tps.addTransaction(transaction)
#         else:
#             print("INVALID AIRPORT CODE ERROR - NO STOP ADDED")
#     elif choice == "U":
#         tps.undoTransaction()
#     elif choice == "R":
#         tps.doTransaction()
#     elif choice == "E":
#         tps.clearAllTransactions()
#     elif choice == "Q":
#         return False
#     return True

def initAllAirports():
    with open('../data/Flights.json', 'r') as file:
        airportData = json.load(file)
        for airportJSON in airportData['airports']:
            newAirport = Airport(airportJSON['code'], airportJSON['latitudeDegrees'], airportJSON['latitudeMinutes'], airportJSON['longitudeDegrees'], airportJSON['longitudeMinutes'])
            airportGraph.addNode(airportJSON['code'], newAirport)

        for edgeJSON in airportData['edges']:
            initEdge(edgeJSON[0], edgeJSON[1])

def initEdge(node1, node2):
    a1 = airportGraph.getNodeData(node1)
    a2 = airportGraph.getNodeData(node2)
    distance = Airport.calculateDistance(a1, a2)
    airportGraph.addEdge(node1, node2, distance)
    airportGraph.addEdge(node2, node1, distance)

initAllAirports()

keepGoing = True
while keepGoing:
    displayAirports()
    displayCurrentTrip()
    displayMenu()
    keepGoing = process_user_input()
