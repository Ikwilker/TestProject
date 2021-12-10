import requests
import credentials

#Generates Important Session information.
loginPayload = {"email":credentials.Username,"password": credentials.Password}
s = requests.Session()
r = s.post(url="https://logicinfo.atlassian.net/jsd-login/v1/authentication/authenticate", json=loginPayload)

#ID's 6/Closed 10403/Waiting for logic 10404/Waiting for customer
IdList = (10404, 10403, 6)
#Testing Payloads to not spam API with too many requests while debugging.
ticketPayload = {"options":{"portalWebFragments":{"portalPage":"MY_REQUESTS"},"allReqFilter":{"selectedPage":1,"filter":"","reporter":"all","status":"open"}},"models":["portalWebFragments","xsrfToken","allReqFilter","requestsColumnSettings"]}
exPayload = {"options":{"allReqFilter":{"selectedPage":1,"filter":"","reporter":"all","status":"","statusFilter":{"statusPortalId":"83","statusInfo":[{"statusId":"10404"}]}}},"models":["allReqFilter","xsrfToken"]}

#Loops through known ID's for TicketTypes and Amounts. Print Tickets and their Type. 
for i in range(len(IdList)):
    currentID = IdList[i]
    idPayload = {"options":{"allReqFilter":{"selectedPage":1,"filter":"","reporter":"all","status":"","statusFilter":{"statusPortalId":"83","statusInfo":[{"statusId":str(currentID)}]}}},"models":["allReqFilter","xsrfToken"]}
    ticket = s.post(url="https://logicinfo.atlassian.net/rest/servicedesk/1/customer/models", json=idPayload)
    jsonTicket = ticket.json()

#    ticketType = jsonTicket["allReqFilter"]["requestList"][1]["status"]
    if currentID == 6:
        ticketType = "Closed"
    elif currentID == 10403:
        ticketType = "Waiting for Logic"
    elif currentID == 10404:
        ticketType = "Waiting for Customer"
    totalTickets = jsonTicket["allReqFilter"]["totalResults"]
    print(f"{totalTickets} ticket(s) are {ticketType}")

#Extra debugging things. Same as above, Don't want to spam API's

#ticket = s.post(url="https://logicinfo.atlassian.net/rest/servicedesk/1/customer/models", json=exPayload)
#jsonTicket = ticket.json()
#totalTickets = jsonTicket["allReqFilter"]["totalResults"]
#print(jsonTicket["allReqFilter"]["requestList"][1]["status"])