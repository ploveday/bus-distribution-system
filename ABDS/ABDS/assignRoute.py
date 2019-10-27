


location = {"agege":10, 
            "Alimosho": 80, 
            "Bariga": 30, 
            "Ojota": 30,
            "Oshodi": 120,
            "Egbeda": 95,
            "Obalende": 45,
            "Ojo": 25,
            "Mile2":45,
            "Magodo":20
            }

def assignRoute(location):
    from math import ceil
    busCapacity = 20
    for key, value in location.items():
        deploy = ceil(value / busCapacity)
        location[key] = deploy
    deploying = location
    return deploying


if __name__ == "__main__":
    assignRoute(    location = {"agege":10, 
                "Alimosho": 80, 
                "Bariga": 30, 
                "Ojota": 30,
                "Oshodi": 120,
                "Egbeda": 95,
                "Obalende": 45,
                "Ojo": 25,
                "Mile2":45,
                "Magodo":20
                })