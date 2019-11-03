road = {'north': 'green', 'east' : 'red'}

def streetlight(crossroad):
    for key in crossroad.keys():
        if crossroad[key] == 'green':
            crossroad[key] = 'yellow'
        elif crossroad[key] == 'yellow':
            crossroad[key] = 'red'
        elif crossroad[key] == 'red':
            crossroad[key] = 'green'
        assert 'red' in crossroad.values(), 'Neither light is in red!' + str(crossroad)

streetlight(road)
            
    
