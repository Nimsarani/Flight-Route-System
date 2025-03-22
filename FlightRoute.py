import sys

countryList = ["SL","UK", "US", "Japan", "Singapore", "Australia"]

# country Validation
def countryValidation(country):
    return country > 0 and country <= len(countryList)

def countryMenu():
    print("\n------------------------------------------------------\n")
    print("*    -->         Flight Route Company         <---     *\n")
    print("*--------- Select your destination Countries  ---------*\n")
    print("\n 1.SL \n 2.UK\n 3.US\n 4.Japan \n 5.Singapore \n 6.Australia  \n")
    print("\n------------------------------------------------------\n")
    
    while True:
        temp_first_country = int(input("Enter the Starting country index from the list: "))
        if countryValidation(temp_first_country):
            first_country = countryList[temp_first_country - 1]
            print("You Selected Your starting country as "+first_country)
            print("\n------------------------------------------------------\n")
            break
        else:
            print("Invalid country. Please select from the provided list.")

    while True:
        temp_second_country = int(input("Enter the Destination country index from the list: "))
        if countryValidation(temp_second_country):
            if countryList[temp_second_country - 1] != first_country:
                second_country = countryList[temp_second_country - 1]
                print("You Selected Your destination country as "+second_country)
                print("\n------------------------------------------------------\n")
                break
            else:
                print("Destination country cannot be the same as the starting country.")
        else:
            print("Invalid country. Please select from the provided list.")

    print("Hello Customer! You have selected to travel from", first_country, "to", second_country)
    print("\n------------------------------------------------------\n")
    print("\n Waiting for Loading Country Data...")
    print("\n------------------------------------------------------\n")
    
    # calling main menu
    mainMenu(first_country, second_country)

def mainMenu(first_country, second_country):
    while True:
        print("-----------------------------------------------------------------------")
        print("     ---------->          Flight Route Company          <------------- ")
        print("-----------------------------------------------------------------------\n")
        print("01. Display All possible airline routes between two given countries with durations.")
        print("02. Display least time airline route between two given countries.")
        print("03. Exit")
        print("\n----------------------------------------------------------------------\n")
        
        choice = int(input("Enter your Choice Number: "))
        if choice == 1:
            routeDetails(first_country, second_country)
        elif choice == 2:
            least_country(first_country, second_country)
        elif choice == 3:
            print("Thank you for using our service!")
            sys.exit()
        else:
            print("Invalid Choice..")

def routeDetails(first_country, second_country):
    print("\n_______________________________________________________________________________________________\n")
    print("*             ------>         Flight Route Company         <-------        *\n")
    print("_________________________________________________________________________________________________\n")
    print(f"Starting Country: {first_country}                       Destination Country: {second_country}\n")
    print("_______________________________________________________________________________________________\n")
    
    found_data = False
    
    for routes in maps:
        if routes["Route"]["First Country"] == first_country and routes["Route"]["Second Country"] == second_country:
            duration = routes["duration"]
            middle_country = routes["Route"]["Middle Country"]
            print(f"Route: {first_country} -> {middle_country} -> {second_country}                         Expected Duration: {duration}\n")
            found_data = True
    
    if not found_data:
        print(" There are no routes between " + first_country + " to "+ second_country)
        print("\n back to main menu to click ( M )")
        
    
    print("\n__________________________________________________________________________\n")
    
    choice = str(input("Do you want to Move Main Menu / Country Menu or Go Exit.? M / C / E   :")).upper()
    if choice == "M":
        print("\n_______________ You Selected to go to the Main menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        mainMenu(first_country, second_country)
    elif choice == "C":
        print("\n_______________ You Selected to go to the Country menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        countryMenu()
    elif choice == "E":
        print("Thank you for using our service!")
        sys.exit()
    else:
        print("Invalid Choice..")
            

def least_country(first_country, second_country):
    print("\n--------------------------------------------------------------------------\n")
    print("*             ------>         Flight Route Company         <-------        *\n")
    print("_________________________________________________________________________________________________\n")
    print(f"Starting Country: {first_country}                       Destination Country: {second_country}\n")
    
    temp_duration = float('inf')
    least_route = ""
    
    for routes in maps:
        if routes["Route"]["First Country"] == first_country and routes["Route"]["Second Country"] == second_country:
            duration = float(routes["duration"].split()[0])
            if duration < temp_duration:
                temp_duration = duration
                least_route = routes["Route"]["Middle Country"]
    
    print("______________________________________________________________________________________________________________\n")
    if temp_duration == float('inf'):
        print("There are no routes between " + first_country + " to "+ second_country)
    else:
        print(f"Route: {first_country} -> {least_route} -> {second_country}                           Expected Duration: {temp_duration} Hrs\n")
    
    print("_______________________________________________________________________________________________________________\n")
    
    while True:
        try:
            choice = str(input("Do you want to Move Main Menu / Country Menu or Go Exit.? M / C / E   :")).upper()
            if choice in ( "M", "C", "E"):
                break
            else:
                print("Invalid Choice, Please Enter M / C or E ..")
        except ValueError:
            print("Invalid Choice, Please Enter M / C or E ..")

    if choice == "M":
        print("\n_______________ You Selected to go to the Main menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        mainMenu(first_country, second_country)
    elif choice == "C":
        print("\n_______________ You Selected to go to the Country menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        countryMenu()
    elif choice == "E":
        print("Thank you for using our service!")
        sys.exit()
    else:
        print("Invalid Choice..")

maps = [
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "UK"
        },
        "duration" : "11.45 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "UK",
            "Second Country" : "US"
        },
        "duration" : "19.45 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "JAPAN",
            "Second Country" : "US"
        },
        "duration" : "24 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore -> Japan",
            "Second Country" : "US"
        },
        "duration" : "24 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Japan"
        },
        "duration" : "8 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore",
            "Second Country" : "Japan"
        },
        "duration" : "8 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Singapore"
        },
        "duration" : "4 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "9.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore",
            "Second Country" : "Australia"
        },
        "duration" : "11.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore -> Japan",
            "Second Country" : "Australia"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Japan",
            "Second Country" : "Australia"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "UK",
            "Middle Country" : "",
            "Second Country" : "US"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Japan",
            "Middle Country" : "",
            "Second Country" : "US"
        },
        "duration" : "16 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Japan",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "10 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "",
            "Second Country" : "Japan"
        },
        "duration" : "4 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "Japan",
            "Second Country" : "US"
        },
        "duration" : "20 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "7.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "Japan",
            "Second Country" : "Australia"
        },
        "duration" : "14 Hrs"
    },
]

# calling to the Program
countryMenu()
import sys

countryList = ["SL","UK", "US", "Japan", "Singapore", "Australia"]

# country Validation
def countryValidation(country):
    return country > 0 and country <= len(countryList)

def countryMenu():
    print("\n------------------------------------------------------\n")
    print("*    -->         Flight Route Company         <---     *\n")
    print("*--------- Select your destination Countries  ---------*\n")
    print("\n 1.SL \n 2.UK\n 3.US\n 4.Japan \n 5.Singapore \n 6.Australia  \n")
    print("\n------------------------------------------------------\n")
    
    while True:
        temp_first_country = int(input("Enter the Starting country index from the list: "))
        if countryValidation(temp_first_country):
            first_country = countryList[temp_first_country - 1]
            print("You Selected Your starting country as "+first_country)
            print("\n------------------------------------------------------\n")
            break
        else:
            print("Invalid country. Please select from the provided list.")

    while True:
        temp_second_country = int(input("Enter the Destination country index from the list: "))
        if countryValidation(temp_second_country):
            if countryList[temp_second_country - 1] != first_country:
                second_country = countryList[temp_second_country - 1]
                print("You Selected Your destination country as "+second_country)
                print("\n------------------------------------------------------\n")
                break
            else:
                print("Destination country cannot be the same as the starting country.")
        else:
            print("Invalid country. Please select from the provided list.")

    print("Hello Customer! You have selected to travel from", first_country, "to", second_country)
    print("\n------------------------------------------------------\n")
    print("\n Waiting for Loading Country Data...")
    print("\n------------------------------------------------------\n")
    
    # calling main menu
    mainMenu(first_country, second_country)

def mainMenu(first_country, second_country):
    while True:
        print("-----------------------------------------------------------------------")
        print("     ---------->          Flight Route Company          <------------- ")
        print("-----------------------------------------------------------------------\n")
        print("01. Display All possible airline routes between two given countries with durations.")
        print("02. Display least time airline route between two given countries.")
        print("03. Exit")
        print("\n----------------------------------------------------------------------\n")
        
        choice = int(input("Enter your Choice Number: "))
        if choice == 1:
            routeDetails(first_country, second_country)
        elif choice == 2:
            least_country(first_country, second_country)
        elif choice == 3:
            print("Thank you for using our service!")
            sys.exit()
        else:
            print("Invalid Choice..")

def routeDetails(first_country, second_country):
    print("\n_______________________________________________________________________________________________\n")
    print("*             ------>         Flight Route Company         <-------        *\n")
    print("_________________________________________________________________________________________________\n")
    print(f"Starting Country: {first_country}                       Destination Country: {second_country}\n")
    print("_______________________________________________________________________________________________\n")
    
    found_data = False
    
    for routes in maps:
        if routes["Route"]["First Country"] == first_country and routes["Route"]["Second Country"] == second_country:
            duration = routes["duration"]
            middle_country = routes["Route"]["Middle Country"]
            print(f"Route: {first_country} -> {middle_country} -> {second_country}                         Expected Duration: {duration}\n")
            found_data = True
    
    if not found_data:
        print(" There are no routes between " + first_country + " to "+ second_country)
        print("\n back to main menu to click ( M )")
        
    
    print("\n__________________________________________________________________________\n")
    
    choice = str(input("Do you want to Move Main Menu / Country Menu or Go Exit.? M / C / E   :")).upper()
    if choice == "M":
        print("\n_______________ You Selected to go to the Main menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        mainMenu(first_country, second_country)
    elif choice == "C":
        print("\n_______________ You Selected to go to the Country menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        countryMenu()
    elif choice == "E":
        print("Thank you for using our service!")
        sys.exit()
    else:
        print("Invalid Choice..")
            

def least_country(first_country, second_country):
    print("\n--------------------------------------------------------------------------\n")
    print("*             ------>         Flight Route Company         <-------        *\n")
    print("_________________________________________________________________________________________________\n")
    print(f"Starting Country: {first_country}                       Destination Country: {second_country}\n")
    
    temp_duration = float('inf')
    least_route = ""
    
    for routes in maps:
        if routes["Route"]["First Country"] == first_country and routes["Route"]["Second Country"] == second_country:
            duration = float(routes["duration"].split()[0])
            if duration < temp_duration:
                temp_duration = duration
                least_route = routes["Route"]["Middle Country"]
    
    print("______________________________________________________________________________________________________________\n")
    if temp_duration == float('inf'):
        print("There are no routes between " + first_country + " to "+ second_country)
    else:
        print(f"Route: {first_country} -> {least_route} -> {second_country}                           Expected Duration: {temp_duration} Hrs\n")
    
    print("_______________________________________________________________________________________________________________\n")
    
    while True:
        try:
            choice = str(input("Do you want to Move Main Menu / Country Menu or Go Exit.? M / C / E   :")).upper()
            if choice in ( "M", "C", "E"):
                break
            else:
                print("Invalid Choice, Please Enter M / C or E ..")
        except ValueError:
            print("Invalid Choice, Please Enter M / C or E ..")

    if choice == "M":
        print("\n_______________ You Selected to go to the Main menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        mainMenu(first_country, second_country)
    elif choice == "C":
        print("\n_______________ You Selected to go to the Country menu ___________________\n")
        print("\n__________________________________________________________________________\n")
        countryMenu()
    elif choice == "E":
        print("Thank you for using our service!")
        sys.exit()
    else:
        print("Invalid Choice..")

maps = [
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "UK"
        },
        "duration" : "11.45 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "UK",
            "Second Country" : "US"
        },
        "duration" : "19.45 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "JAPAN",
            "Second Country" : "US"
        },
        "duration" : "24 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore -> Japan",
            "Second Country" : "US"
        },
        "duration" : "24 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Japan"
        },
        "duration" : "8 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore",
            "Second Country" : "Japan"
        },
        "duration" : "8 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Singapore"
        },
        "duration" : "4 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "9.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore",
            "Second Country" : "Australia"
        },
        "duration" : "11.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Singapore -> Japan",
            "Second Country" : "Australia"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "SL",
            "Middle Country" : "Japan",
            "Second Country" : "Australia"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "UK",
            "Middle Country" : "",
            "Second Country" : "US"
        },
        "duration" : "18 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Japan",
            "Middle Country" : "",
            "Second Country" : "US"
        },
        "duration" : "16 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Japan",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "10 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "",
            "Second Country" : "Japan"
        },
        "duration" : "4 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "Japan",
            "Second Country" : "US"
        },
        "duration" : "20 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "",
            "Second Country" : "Australia"
        },
        "duration" : "7.25 Hrs"
    },
    {
        "Route" : {
            "First Country" : "Singapore",
            "Middle Country" : "Japan",
            "Second Country" : "Australia"
        },
        "duration" : "14 Hrs"
    },
]

# calling to the Program
countryMenu()
