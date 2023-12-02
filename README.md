# Flask_REST_API_MySQL
This project is a Flask REST Web API attached to a MySQL relational database that can perform CRUD operations to the database.  
  
# URLs:
Index URL: http://localhost:5000/  
Create / Post: http://localhost:5000/create/name  
Read / Get: http://localhost:5000/read/id  
Update / Put: http://localhost:5000//update/id/name   
Delete: http://localhost:5000/delete/id  
  
# MySQL:
I start by creating a database (database.sql file) and table within MySQL.  This will house my data from the API.  
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/mysql.png" width="70%">
  
# Index:
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/index.png" width="70%">
  
# Create Functionality:  
Add an entry named Layla which is automatically appended to the end of the list of entries with the correct ascending id.  
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/create.png" width="70%">

# Read Functionality:  
Read "id" 2.  
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/read.png" width="70%">
  
# Update Functionality:  
Update "id" 2 to Shelby.  
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/update.png" width="70%">

# Delete Functionality:  
Delete "id" 2.  Once an entry is removed, all of the remaining entries become updated with the correct ascending id.  
<img src="https://github.com/david125tran/Flask_REST_API_MySQL/blob/main/images/delete.png" width="70%">
