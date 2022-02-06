from .models import *

def getWaitingForQoute(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Waiting for Qoute"):
            count += 1

    return count


def getWaitingForSend(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Under Review"):
            count += 1

    return count

def getInstalled(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Installed"):
            count += 1

    return count

def getPaymentSettled(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Payment Settled"):
            count += 1

    return count

def getSiteVisited(applications):
    count = 0

    for application in applications:
        if(application.app_status == "Site visited"):
            count += 1

    return count

def getOnDesign(applications):
    count = 0

    for application in applications:
        if(application.app_status == "On Design"):
            count += 1

    return count