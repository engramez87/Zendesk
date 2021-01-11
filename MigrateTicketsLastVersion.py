""" This script allows the user to migrate multiy json files with limit to 100 tickets in each file.
    the results of this script will be written to listOfIds.txt file inside the script directory
"""
import json
import sys
import os
import requests
import time 


API_ENDPOINT = "https://betpointgroup.zendesk.com/api/v2/imports/tickets/create_many.json"
headers = {
    'Content-Type': 'application/json'
     # 'Authorization': 'Basic cmFtZXouYWxkd2loZUBpbW92by5jb20ubXQ6UEBzc3cwcmQxNDAzODg='
}
user = 'it@betpointgroup.com'
pwd = '5%e8DIqTu$Wm!!'

def writeIdsToFile(listOdIds,listOfErrors,total,status,message,link):
    """ Write the log file ("listOfIds.txt") for import tickets results.
    Parameters
    ----------
    listOdIds: list
        The imported tickets Ids
    listOfErrors: list
        The imported tickets errors description
    total: number
        The total number of imported tickets includeing the one that has an error
    status: str
        The status of the job task to import tickets  
    message: str
        The date and time is import happened    
    link: str
        Job status URL
    """
    f = open("listOfIds.txt", "a+")
    f.write("*********************The imported tickets are*****************")
    f.write("the job status URl is: " + str(link)+"\n")
    f.write("the status is: " + str(status)+"\n")
    f.write("the total number of tickets imported are: " + str(total)+"\n")
    f.write("the date and time is :" + str(message)+"\n")
    f.write("the ids are:\n")
    f.write(str(listOdIds)+"\n")
    f.write("the errors are:\n")
    f.write(str(listOfErrors)+"\n")
    f.write("****************************************************************")
    f.close()


def loopInsidePath(path): 
    """ This func will loop inside tha path that includes the json files to import to Zendesk instance.
    Parameters
    ----------
    path: str
        the path that includes the
    """
    files = []
    with os.scandir(path) as entries:
        for entry in entries:
            files.append(entry.name)
    return files

def createManyTickets(filesList,pathToFile): 
    """ This func request creat many tickets API to import to Zendesk instance.
    Parameters
    ----------
    filesList: list
        The list of json files that includes the tickets 
    pathToFile: str
        The dir that includes the files
    """
    link = []            

    for item in filesList:
        json_file = open(pathToFile+"/"+item, 'r')
        data = json.load(json_file)
        mm = json.dumps(data, indent=4, sort_keys=True)
        response = requests.post(url=API_ENDPOINT, headers=headers, data=mm, auth=(user, pwd))
        if (response.status_code == 200 or response.status_code == 201):
            r = response.json()
            link.append(r['job_status']['url'])
            print ("the bulk tickets imported\n")
            time.sleep(140)
    return link
        
def jopStatusResponse(jobUrl): #
    """ This func will return the job_Status for each request 
    Parameters
    ----------
    jobUrl: list
        The url of job status
    """
    ids = []
    errors = []
    for link in jobUrl:
        response1 = requests.get(url=link, headers=headers, auth=(user, pwd))
        r1 = response1.json()
        total = r1['job_status']['total']
        status = r1['job_status']['status']
        message = r1['job_status']['message']
        results = r1['job_status']['results']

        for index in range(len(results)):
            if("id" in results[index]):
                ids.append(results[index]["id"])
            else:
                errors.append(results[index]["details"]+" index is "+str(results[index]["index"]))
        print("****************************************")
        writeIdsToFile(ids,errors,total,status,message,jobUrl)
        time.sleep(5)
#*************************************************
if __name__ == "__main__":
    file_name = input('Path name: ')
    fileslist1 = loopInsidePath(file_name)
    links = createManyTickets(fileslist1,file_name)
    jopStatusResponse(links)
    


