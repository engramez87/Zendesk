This project has some scripts to prapare the json files for importing them in new Zendesk.

to prepare the files:
in case tickets and comments in seperated files »
1- apply General.py {"files_include_all_Tickets.json"}
    you hav to be sure that the comments files is: commentLast.json.

2- you have to apply json_splitter.py which is inside splitt-json direcor 
    the results will be many json files include between 1 and 100 tickets per file depend on your choise.

- apply MigrateTicketsLastVersion.py script
    


