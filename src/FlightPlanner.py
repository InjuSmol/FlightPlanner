from Airport import Airport
from PyTPS import PyTPS
from WeightedGraph import WeightedGraph
import readline
from AppendStopTransaction import AppendStopTransaction
import json

tps = PyTPS()
airport_graph = WeightedGraph()
stops = []


def display_airports():
    print("\n\nAIRPORTS YOU CAN TRAVEL TO AND FROM:\n")
    codes = []
    airport_graph.get_keys(codes)
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


def display_current_trip():
    text = ""
    text += "Current Trip Stops: \n"
    for i in range(len(stops)):
        text += "\t" + str(i + 1) + ". " + stops[i] + "\n"
    text += "\nCurrent Trip Legs: \n"
    leg_num = 1
    trip_distance = 0.0
    for i in range(len(stops)):
        leg_distance = 0.0

        if leg_num < len(stops):
            text += "\t" + str(i + 1) + '. '

            last_stop = stops[leg_num - 1]

            next_stop = stops[leg_num]

            route = []
            airport_graph.find_path(route, last_stop, next_stop)

            if len(route) < 2:
                text += "No Route Found from " + last_stop + " to " + next_stop + "\n"
            else:
                for i in range(len(route) - 1):
                    a1 = airport_graph.get_node_data(route[i])
                    a2 = airport_graph.get_node_data(route[i + 1])
                    distance = Airport.calculate_distance(a1, a2)
                    leg_distance += distance
                    if i == 0:
                        text += a1.get_code()
                    text += "-" + a2.get_code()
                text += " (Leg Distance: " + str(leg_distance) + " miles)\n"

            leg_num += 1
            trip_distance += leg_distance
    text += "Total Trip Distance: " + str(trip_distance) + " miles\n\n"
    print(text)


def display_menu():
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
        if airport_graph.node_exists(entry):
            neighbors = []
            airport_graph.get_neighbors(neighbors, entry)

            # MAKE SURE IT IS NOT THE SAME AIRPORT CODE AS THE PREVIOUS STOP
            if len(stops) > 0:
                last_stop = stops[-1]
                if last_stop == entry:
                    print("DUPLICATE STOP ERROR - NO STOP ADDED")
                else:
                    transaction = AppendStopTransaction(stops, entry)
                    tps.add_transaction(transaction)
            else:
                transaction = AppendStopTransaction(stops, entry)
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


def init_all_airports():
    with open('../data/Flights.json', 'r') as file:
        airport_data = json.load(file)
        for airportJSON in airport_data['airports']:
            new_airport = Airport(airportJSON['code'], airportJSON['latitudeDegrees'], airportJSON['latitudeMinutes'], airportJSON['longitudeDegrees'], airportJSON['longitudeMinutes'])
            airport_graph.add_node(airportJSON['code'], new_airport)

        for edgeJSON in airport_data['edges']:
            init_edge(edgeJSON[0], edgeJSON[1])


def init_edge(node1, node2):
    a1 = airport_graph.get_node_data(node1)
    a2 = airport_graph.get_node_data(node2)
    distance = Airport.calculate_distance(a1, a2)
    airport_graph.add_edge(node1, node2, distance)
    airport_graph.add_edge(node2, node1, distance)


init_all_airports()

keepGoing = True
while keepGoing:
    display_airports()
    display_current_trip()
    display_menu()
    keepGoing = process_user_input()
