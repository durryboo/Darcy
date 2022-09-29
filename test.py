methods = {"Roundabout"    :{"H":0.5, "M":0.75, "L":0.9},
           "Stop Signs"    :{"H":0.2, "M":0.3,  "L":0.4},
           "Traffic Lights":{"H":0.9, "M":0.75, "L":0.2}}

def get_input_cpm():
    values = input("Please input FOUR new CPM values seperated by ',': ").split(',')
    if len(values) != 4:
        print("Must input FOUR numbers")
    if not all(a.isnumeric() for a in values):
        print("Inputs must be numbers")
        return get_input_cpm()
    values = [int(x) for x in values]
    return values

def get_input_costs():
    values = input("Enter construction costs for Roundabout, Stop Signs and Traffic Lights respectively (separated by ','): ").split(',')
    if len(values) != 3:
        print("Must input THREE numbers")
        return get_input_costs()
    if not all(a.isnumeric() for a in values):
        print("Inputs must be numbers")
        return get_input_costs()
    values = [int(x) for x in values]
    return values

def traffic_control(road1cpm, road2cpm, road3cpm, road4cpm):
    cpm = sum(list(locals().values()))
    #Extension 6
    costs = get_input_costs()
    costs = {"Roundabout":costs[0], "Stop Signs":costs[1], "Traffic Lights":costs[2]}
    #Extension 5
    if road1cpm + road3cpm >= 2 * (road2cpm + road4cpm):
        methods["Roundabout"] = {"H":0.6, "M":0.85, "L":1.0}
    if cpm >= 20:
        throughput = "H"
    elif cpm < 10:
        throughput = "L"
    else:
        throughput = "M"
    print("For {} CPM:".format(cpm))
    for method in methods:
        efficiency = methods[method][throughput]
        print("Efficiency score of {} traffic control method is {}".format(method, efficiency))
        #Extension 6 cont.
        cpm_method = cpm * efficiency
        cpm_per_dollar = cpm_method / costs[method]
        print("CPM per dollar value is: {:.4f}".format(cpm_per_dollar))
        
    #Extension 1
    val = input("Would you like to try new CPM values? Please type YES if so. ")
    if val == "YES":
        r1, r2, r3, r4 = get_input_cpm()
        traffic_control(r1, r2, r3, r4)
        
    
    
    