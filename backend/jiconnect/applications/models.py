from django.db import models
from django.db.models.deletion import DO_NOTHING


class Customer(models.Model):
    COUNTIES = [
        ("Mombasa","Mombasa"),
        ("Kwale","Kwale"),
        ("Kilifi","Kilifi"),
        ("Tana River","Tana River"),
        ("Taita Taveta","Taita Taveta")
    ]
    WARDS = [
        ( "CHAANI","CHAANI"),
        ( "MIRITINI","MIRITINI"),
        ( "AIRPORT","AIRPORT"),
        ( "PORT REITZ","PORT REITZ"),
        ( "KIPEVU","KIPEVU"),
        ( "JOMVU KUU","JOMVU KUU"),
        ( "MAGONGO","MAGONGO"),
        ( "MIKINDANI","MIKINDANI"),
        ( "SHANZU","SHANZU"),
        ( "MWAKIRUNGE","MWAKIRUNGE"),
        ( "MJAMBERE","MJAMBERE"),
        ( "MAGOGONI","MAGOGONI"),
        ( "JUNDA","JUNDA"),
        ( "MTOPANGA","MTOPANGA"),
        ( "BAMBURI","BAMBURI"),
        ( "MKOMANI","MKOMANI"),
        ( "KONGOWEA","KONGOWEA"),
        ( "KADZANDANI","KADZANDANI"),
        ( "ZIWA LA NG'OMBE","ZIWA LA NG'OMBE"),
        ( "FRERE TOWN","FRERE TOWN"),
        ( "MTONGWE","MTONGWE"),
        ( "TIMBWANI","TIMBWANI"),
        ( "BOFU","BOFU"),
        ( "LIKONI","LIKONI"),
        ( "SHIKA ADABU","SHIKA ADABU"),
        ( "MJI WA KALE/ MAKADARA","MJI WA KALE/ MAKADARA"),
        ( "TUDOR","TUDOR"),
        ( "TONONOKA","TONONOKA"),
        ( "SHIMANZI/ GANJONI","SHIMANZI/ GANJONI"),
        ( "MAJENGO","MAJENGO"),
        ( "RAMISI","RAMISI"),
        ( "GOMBATO BONGWE","GOMBATO BONGWE"),
        ( "UKUNDA","UKUNDA"),
        ( "KINONDO","KINONDO"),
        ( "PONGWE KIDIMU/KIGWEDE","PONGWE KIDIMU/KIGWEDE"),
        ( "VANGA","VANGA"),
        ( "MWERENI","MWERENI"),
        ( "DZOMBO","DZOMBO"),
        ( "KUBO SOUTH","KUBO SOUTH"),
        ( "MKONGANI","MKONGANI"),
        ( "TSIMBA GOLINI","TSIMBA GOLINI"),
        ( "TIWI","TIWI"),
        ( "WAA","WAA"),
        ( "MACKINON ROAD","MACKINON ROAD"),
        ( "NDAVAYA","NDAVAYA"),
        ( "PUMA","PUMA"),
        ( "KINANGO","KINANGO"),
        ( "KASEMENI","KASEMENI"),
        ( "MWAVUMBO","MWAVUMBO"),
        ( "CHENGONI/SAMBURU","CHENGONI/SAMBURU"),
        ( "MATSANGONI","MATSANGONI"),
        ( "MNARANI","MNARANI"),
        ( "SOKONI","SOKONI"),
        ( "TEZO","TEZO"),
        ( "KIBARANI","KIBARANI"),
        ( "WATAMU","WATAMU"),
        ( "DABASO","DABASO"),
        ( "JUNJU","JUNJU"),
        ( "SHIMO LA TEWA","SHIMO LA TEWA"),
        ( "MTEPENI","MTEPENI"),
        ( "CHASIMBA","CHASIMBA"),
        ( "MWARAKAYA","MWARAKAYA"),
        ( "KAYAFUNGO","KAYAFUNGO"),
        ( "MARIAKANI","MARIAKANI"),
        ( "MWANAMWINGA","MWANAMWINGA"),
        ( "KALOLENI","KALOLENI"),
        ( "JIBANA/KAMBE/RIBE","JIBANA/KAMBE/RIBE"),
        ( "MAZERASRABAI/KISURUTINI","MAZERASRABAI/KISURUTINI"),
        ( "MWAWESA","MWAWESA"),
        ( "RURUMA","RURUMA"),
        ( "SOKOKE","SOKOKE"),
        ( "BAMBA","BAMBA"),
        ( "JARIBUNI","JARIBUNI"),
        ( "DUNGICHA/ GANZE","DUNGICHA/ GANZE"),
        ( "JILORE","JILORE"),
        ( "GANDA","GANDA"),
        ( "KAKUYUNI","KAKUYUNI"),
        ( "SHELLA","SHELLA"),
        ( "MALINDI TOWN","MALINDI TOWN"),
        ( "ADU","ADU"),
        ( "MARAFA","MARAFA"),
        ( "SABAKI","SABAKI"),
        ( "MAGARINI","MAGARINI"),
        ( "GONGONI","GONGONI"),
        ( "GARASHI","GARASHI"),
        ( "GARSEN NORTH","GARSEN NORTH"),
        ( "GARSEN WEST","GARSEN WEST"),
        ( "GARSEN CENTRAL","GARSEN CENTRAL"),
        ( "KIPINI EAST","KIPINI EAST"),
        ( "GARSEN SOUTH","GARSEN SOUTH"),
        ( "KIPINI WEST","KIPINI WEST"),
        ( "CHEWANI","CHEWANI"),
        ( "KINAKOMBA","KINAKOMBA"),
        ( "MAKINDUNI","MAKINDUNI"),
        ( "WAYU","WAYU"),
        ( "BANGALE","BANGALE"),
        ( "CHEWELE","CHEWELE"),
        ( "HIRIMAN","HIRIMAN"),
        ( "MADOGO","MADOGO"),
        ( "SALA","SALA"),
        ( "KIUNGA","KIUNGA"),
        ( "BASUBA","BASUBA"),
        ( "FAZA","FAZA"),
        ( "MKOMANI","MKOMANI"),
        ( "SHELLA","SHELLA"),
        ( "WITU","WITU"),
        ( "HINDI","HINDI"),
        ( "HONGWE","HONGWE"),
        ( "BAHARI","BAHARI"),
        ( "MKUNUMBI","MKUNUMBI"),
        ( "MATA","MATA"),
        ( "MAHOO","MAHOO"),
        ( "MBOGHONI","MBOGHONI"),
        ( "CHALA","CHALA"),
        ( "BOMANI","BOMANI"),
        ( "MWANDA/MGANGE","MWANDA/MGANGE"),
        ( "KISHUSHE/WUMINGU","KISHUSHE/WUMINGU"),
        ( "WERUGHA","WERUGHA"),
        ( "WUNDANYI/MBALE","WUNDANYI/MBALE"),
        ( "CHAWIA","CHAWIA"),
        ( "BURA","BURA"),
        ( "WUSI/KISHAMBA","WUSI/KISHAMBA"),
        ( "RONGE","RONGE"),
        ( "MWATATE","MWATATE"),
        ( "NGOLIA","NGOLIA"),
        ( "KASIGAU","KASIGAU"),
        ( "MARUNGU","MARUNGU"),
        ( "SAGALA","SAGALA"),
        ( "MBOLOLO","MBOLOLO"),
        ( "KALOLENI","KALOLENI"),
    ]
    CONSTITUENCIES = [
        ( "Changamwe","Changamwe"),
        ( "Jomvu","Jomvu"),
        ( "Kisauni","Kisauni"),
        ( "Nyali","Nyali"),
        ( "Likoni","Likoni"),
        ( "Mvita","Mvita"),
        ( "Msambweni","Msambweni"),
        ( "Lunga Lunga","Lunga Lunga"),
        ( "Matuga","Matuga"),
        ( "Kinango","Kinango"),
        ( "Kilifi North","Kilifi North"),
        ( "Kilifi South","Kilifi South"),
        ( "Kaloleni","Kaloleni"),
        ( "Rabai","Rabai"),
        ( "Ganze","Ganze"),
        ( "Malindi","Malindi"),
        ( "Magarini","Magarini"),
        ( "Garsen","Garsen"),
        ( "Galole","Galole"),
        ( "Bura","Bura"),
        ( "Lamu East","Lamu East"),
        ( "Lamu West","Lamu West"),
        ( "Taveta","Taveta"),
        ( "Wundanyi","Wundanyi"),
        ( "Mwatate","Mwatate"),
        ( "Voi","Voi")

    ]
    customer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    id_type = models.CharField(max_length=200, null=True, blank=True)
    id_number = models.CharField(max_length=200, null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=True,  choices=COUNTIES)
    po_box = models.CharField(max_length=200, null=True, blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    constituency = models.CharField(max_length=200, null=True, choices=CONSTITUENCIES)
    ward = models.CharField(max_length=200, null=True, choices=WARDS)
    lr_number = models.CharField(max_length=200, null=True, blank=True)
    estate_village = models.CharField(max_length=200, null=True, blank=True)
    area_code = models.CharField(max_length=200, null=True, blank=True)
    ccp = models.CharField(max_length=200, null=True, blank=True) #customer contract person
    voltage = models.CharField(max_length=200, null=True, blank=True)
    connect_type = models.CharField(max_length=200, null=True, blank=True)
    amd = models.CharField(max_length=200, null=True, blank=True) #authorised max demand
    id_document = models.TextField(null=True, blank=True) 
    pin_certificate = models.TextField(null=True, blank=True) 
    title_deed = models.TextField(null=True, blank=True) 
    wiring_certificate = models.TextField(null=True, blank=True) 
    site_plan = models.TextField(null=True, blank=True) 
    
    
    def __str__(self):
        return str(self.customer_id)




class Application(models.Model):
    PLAN = (
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
        
    )
    AGREESTATUS = (
        ('YES I AGREE', 'YES I AGREE'),
        ('NO I DO NOT AGREE', 'NO I DO NOT AGREE'),
        
    )

    APPTYPE = (
        ('NEW', 'NEW'),
        ('TEMPORARY', 'TEMPORARY'),
        ('ROUTING', 'ROUTING'),
        ('ADDITIONAL LOAD', 'ADDITIONAL LOAD'),
        ('GROUP APPLICATION', 'GROUP APPLICATION'),
        ('METER SEPERATION', 'METER SEPERATION'),
        
    )

    APPSTATUS = (
        ('Under Review', 'Under Review'),
        ('Waiting for Qoute', 'Waiting for Qoute'),
        ('Waiting for Payment', 'Waiting for Payment'),
        ('On Design', 'On Design'),
        ('Site Visited', 'Site Visited'),
        ('Payment Settled', 'Payment Settled'),
        ('Installed', 'Installed'),
        
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    plan = models.CharField(max_length=200, null=True, blank=True, choices=PLAN) 
    app_type = models.CharField(max_length=200, null=True, blank=True, choices=APPTYPE) 
    location = models.CharField(max_length=200, null=True, blank=True) #location cordinates
    app_status = models.CharField(max_length=200, default="Under Review", null=True, blank=True) #application status
    ref_number = models.CharField(max_length=200, null=True, blank=True) 
    site_info = models.TextField(null=True, blank=True) 
    agree_supply = models.CharField(max_length=200, null=True, blank=True, choices=AGREESTATUS)
    agree_wayleave = models.CharField(max_length=200, null=True, blank=True, choices=AGREESTATUS)
    qoutation = models.TextField(null=True, blank=True) 
    appcontrol = models.CharField(max_length=200, default="busdevclerk", null=True, blank=True) #To note what has been done to the application
    install_note = models.TextField(null=True, blank=True) #Engineer intallation note
    proposal = models.TextField(null=True, blank=True) 
    maplatlon = models.CharField(max_length=400, null=True, blank=True) #The map coordinates
    payment = models.TextField(null=True, blank=True) 
    date_created = models.DateField(auto_now_add=True)
    #Appliances
    numapps = models.CharField(max_length=3, default="0", null=True, blank=True) #num apps
    
    def __str__(self):
        return self.id


class Appliances(models.Model):
    application = models.ForeignKey(Application, null=True, on_delete=models.SET_NULL)
    appliance = models.CharField(max_length=200, blank=True) 
    consumption = models.CharField(max_length=100, blank=True)
    qty = models.CharField(max_length=100, blank=True) 
    total = models.CharField(max_length=100, blank=True) 


class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200, null=True,blank=True)
    jobs_done = models.IntegerField(default=0)
    role = models.CharField(max_length=150, default="busdevclerk")
