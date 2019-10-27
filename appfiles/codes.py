def butActivities():
    highBuy = {
        'departure':'Agege',
        'destination':'Ikeja',
    },{
        'departure':'Oshodi',
        'destination':'Ikeja',
    },{
        'departure':'Agege',
        'destination':'Marina',
    },{
        'departure':'Obalande',
        'destination':'Ikeja',
    }

    #Innitialize the routeToAssign variable and none
    routeToAssign = None
    # if one row if found
    if len(highBuy) == 1: 
        routeToAssign = {
            'route': highBuy.departure + '-' + highBuy.destination,
            'qtySold': highBuy.count()
        }
    #check if there multiple rows found
    else:
    #Loop through each row from DB
        for data in highBuy:
            routeToAssign = {
                'route': data.departure + '-' + data.destination,
                'qtySold': data.count()
            }

    return len(highBuy)

print(butActivities())