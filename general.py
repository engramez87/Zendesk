import json
import sys

# this script is to mapping old brands id with new on

def customCatogary():
    """ This fun is put the value of  the custom field with id:360000750113 in tags list inside the ticket.
    """
    inputFile = sys.argv[1]
    with open(inputFile, 'r',encoding='utf-8') as file:
        json_data = json.load(file)
        
    for item in range (len(json_data["tickets"])):
        ticketsItem= json_data["tickets"][item]
        customFieldsItems = ticketsItem["custom_fields"]
        for fieldItem in range (len(customFieldsItems)):
            customFieldsListItem = customFieldsItems[fieldItem]
            #print (customFieldsListItem["id"])
            if (customFieldsListItem["id"] ==360000750113):
                itemValue = customFieldsListItem["value"]
                ticketsItem["tags"].append(itemValue)        
    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    print ("it is done")
    
def closedMerge():
    """ This func to check if the value of custom filed id is: 360005454238 and the value is true, 
        in this case it adds "closed_by_merge_is_true" to tags list inside the ticket
    """
    inputFile = sys.argv[1]
    with open(inputFile, 'r',encoding='utf-8') as file:
        json_data = json.load(file)
        
    for item in range (len(json_data["tickets"])):
        ticketsItem= json_data["tickets"][item]
        customFieldsItems = ticketsItem["custom_fields"]
        for fieldItem in range (len(customFieldsItems)):
            customFieldsListItem = customFieldsItems[fieldItem]
            #print (customFieldsListItem["id"])
            if (customFieldsListItem["id"] ==360005454238 and customFieldsListItem["value"]==bool(1)):
                itemValue = "closed_by_merge_is_true"
                ticketsItem["tags"].append(itemValue)        
    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    print ("it is done")

def makeBrandSwap():
    """ This func to replace old brands Ids with the new ones from the new instance, 
        in others words to make the mapping.
    """
    inputFile = sys.argv[1]
    with open(inputFile, 'r',encoding='utf-8') as file:
     json_data = json.load(file)
     for item in json_data["tickets"]:
        if (item['brand_id'] ==360002855634):
            item['brand_id'] = 360001648357
        elif(item['brand_id'] ==360000404797):
            item['brand_id'] = 360001650398
        elif(item['brand_id'] ==360001004518):
            item['brand_id'] = 360001648457
        elif(item['brand_id'] ==360000675198):
            item['brand_id'] = 360001650438
        elif(item['brand_id'] ==360001391937):
            item['brand_id'] = 360001648477      
    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    
    print ("it is done")
    
def addCoomentsEmptyList():

    inputFile = sys.argv[1]
    with open(inputFile, 'r',encoding='utf-8') as file:
     json_data = json.load(file)
    for item in range (len(json_data["tickets"])):
        json_data["tickets"][item].update({"comments": []})
        
    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    
    print ("it is done")
    
def commentsInsert():
    """ This func is to add the comments inside the tickets if they are in seperated file.
        The key between tickets and comments is the ticket id.
    """
    inputFile = sys.argv[1]
    with open(inputFile, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    with open("commentLast.json", 'r', encoding='utf-8') as file:
        json_datac = json.load(file)
        
    for item in range(len(json_data["tickets"])):
        for itemComments in range(len(json_datac["comments"])):
            if (json_data["tickets"][item]["id"]== json_datac["comments"][itemComments]["ticket_id"]):
                json_data["tickets"][item]["comments"].append(json_datac["comments"][itemComments])
                #print( json_data["tickets"][item]["comments"])

    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    print ("it is done")


def removeRest():
    """ Remove other group of fileds that denied to make import.
    """
    inputFile = sys.argv[1]
    with open(inputFile, 'r',encoding='utf-8') as file:
        json_data = json.load(file)
        
    for item in range (len(json_data["tickets"])):
        ticketsItem= json_data["tickets"][item]
        if (ticketsItem["requester_id"]!=None):
            del ticketsItem["requester_id"]
        if (ticketsItem["submitter_id"]!=None):
            del ticketsItem["submitter_id"]
        if (ticketsItem["assignee_id"]!=None):
            del ticketsItem["assignee_id"]
        if(ticketsItem["group_id"]!=None ):
            del ticketsItem["group_id"]
        if(ticketsItem["submitter_email"]!= None):
            del ticketsItem["submitter_email"]
        if (ticketsItem["satisfaction_rating"]!= None):
            del ticketsItem["satisfaction_rating"]
        if (ticketsItem["assignee_email"]!= None):
            del ticketsItem["assignee_email"]
            
        customFieldsItems = ticketsItem["comments"]
        for fieldItem in range (len(customFieldsItems)):
            customFieldsListItem = customFieldsItems[fieldItem]
            #print (customFieldsListItem["author_id"])
            if (customFieldsListItem["author_id"] !=None):
                del customFieldsListItem["author_id"] 
  
    with open(inputFile, 'w',encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
    print ("it is done")


    
if __name__ == "__main__":
    customCatogary()
    closedMerge()
    makeBrandSwap()
    addCoomentsEmptyList()
    commentsInsert()
    removeRest()