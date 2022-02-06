from .models import Application
def getSiteVisited(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Site visited"):
            count += 1

    return count

def getInstalled(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Installed"):
            count += 1

    return count

def getApplicationtypes(customers):
    Changamwe, Jomvu, Kisauni, Nyali, Likoni, Mvita, Msambweni, Lunga, Matuga, Kinango, Kilifi_North, Kilifi_South, Kaloleni, Rabai, Ganze, Malindi, Magarini, Garsen, Galole, Bura, Lamu_East, Lamu_West, Taveta, Wundanyi, Mwatate, Voi = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in customers:
        if(i.constituency is not None):
            Changamwe += i.constituency.count("Changamwe")
            Jomvu += i.constituency.count("Jomvu")
            Kisauni += i.constituency.count("Kisauni")
            Nyali += i.constituency.count("Nyali")
            Likoni += i.constituency.count("Likoni")
            Mvita += i.constituency.count("Mvita")
            Msambweni += i.constituency.count("Msambweni")
            Lunga += i.constituency.count("Lunga Lunga")
            Matuga += i.constituency.count("Matuga")
            Kinango += i.constituency.count("Kinango")
            Kilifi_North += i.constituency.count("Kilifi North")
            Kilifi_South += i.constituency.count("Kilifi South")
            Kaloleni += i.constituency.count("Kaloleni")
            Rabai += i.constituency.count("Rabai")
            Ganze += i.constituency.count("Ganze")
            Malindi += i.constituency.count("Malindi")
            Magarini += i.constituency.count("Magarini")
            Garsen += i.constituency.count("Garsen")
            Galole += i.constituency.count("Galole")
            Bura += i.constituency.count("Bura")
            Lamu_East += i.constituency.count("Lamu East")
            Lamu_West += i.constituency.count("Lamu West")
            Taveta += i.constituency.count("Taveta")
            Wundanyi += i.constituency.count("Wundanyi")
            Mwatate += i.constituency.count("Mwatate")
            Voi += i.constituency.count("Voi")

    context = {'Changamwe':Changamwe, 'Jomvu':Jomvu, 'Kisauni':Kisauni, 'Nyali':Nyali, 'Likoni':Likoni, 'Mvita':Mvita, 'Msambweni':Msambweni, 'Lunga':Lunga, 'Matuga':Matuga, 'Kinango':Kinango, 'Kilifi_North':Kilifi_North, 'Kilifi_South':Kilifi_South, 'Kaloleni':Kaloleni, 'Rabai':Rabai, 'Ganze':Ganze, 'Malindi':Malindi, 'Magarini':Magarini, 'Garsen':Garsen, 'Galole':Galole, 'Bura':Bura, 'Lamu_East':Lamu_East, 'Lamu_West':Lamu_West, 'Taveta':Taveta, 'Wundanyi':Wundanyi, 'Mwatate':Mwatate, 'Voi':Voi}

    return context

def Merge(dict1, dict2, dict3):
    dict2.update(dict1)
    dict2.update(dict3)

    return(dict2)

def getApplicationconst():

    tnew = Application.objects.filter(app_type__contains="New" ).count()
    tt = Application.objects.filter(app_type__contains="Temporary" ).count()
    tr = Application.objects.filter(app_type__contains="Routing" ).count()
    tga = Application.objects.filter(app_type__contains="Group Application" ).count()
    tal = Application.objects.filter(app_type__contains="Additional load" ).count()
    tms = Application.objects.filter(app_type__contains="Meter Seperation" ).count()
    return {'tnew':tnew, 'tt':tt, 'tr':tr, 'tga':tga, 'tal':tal, 'tms':tms}

def getApplicationAppliances(appliances):
    bulb, socket, cooker, oven, wheater, spm, tpm, airc, furnace, other = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in appliances:
        bulb += i.appliance.count("Light Bulb")
        socket += i.appliance.count("Socket")
        cooker += i.appliance.count("Cooker")
        oven += i.appliance.count("Water Heater")
        wheater += i.appliance.count("Oven")
        spm += i.appliance.count("Single Phase Motor")
        tpm += i.appliance.count("Three Phase Motor")
        airc += i.appliance.count("Air Conditioner")
        furnace += i.appliance.count("Furnace")
        other += i.appliance.count("Other")
    return {'bulb':bulb, 'socket':socket, 'cooker':cooker, 'oven':oven, 'wheater':wheater, 'spm':spm, 'tpm':tpm, 'airc':airc, 'furnace':furnace, 'other':other}