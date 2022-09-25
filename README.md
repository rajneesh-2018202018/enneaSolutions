# enneaSolutions

Hi, this projects has been implemented in django and sqlite. 
Capabilities of the project are as follows: 
1. Upload records using csv file : We can upload records to the db by sending a csv file. The endpoint exposed for it is: /inventory/upload . I have tested the functionality by creating a csv consisting of subset of sample inventory provided along with the project. 
Limitation: There were soem invalid date types provided in the file, which consisted of / / , which are not handled in the limited amout of time that I had. 
2. We can search based on a supplier name using inventory/inventory/?supplier="<supplier_name>" 
3. Created a new endpoint /inventory/unexpired to get all the records having exp > today's date. Also, made field supplier searchable, using endpoint /inventory/unexpired/?supplier="<supplier_name>"  
4. There were around 3000 records, so loading all the records in a single request was taking a lot of time, so implemented pagination for the same. Currently one page shows 10 records as of now. We can change this limit as per our requirement by changing  'PAGE_SIZE': 20 in submission/submission/settings.py
