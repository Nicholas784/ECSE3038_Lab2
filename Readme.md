# **ECSE3038 LAB 2**  

### **This repo was created as part of a laboratory excersise that is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.**  

# **The three routes used and their operation is as follows:**  

## /profile

1. A user is allowed to create ONE profile consisting of Username, Role and Favorite color. 
2. A POST request allows the user to create a profile. The information provided is stored within a global variable in the script. Date and time is updated by the server with each request.
3. The user is also allowed to make changes to the profile using a PATCH request consisting of a JSON body with any combination of the three attributes. Date and time are also updated by the server to show when the last update was made.
4. A GET request returns a singular JSON object. Initial dummy values are set and are returned after a GET request if the user hasn't yet created a profile. 

## /data

1. An initial GET request returns an empty array. After data has been added using the POST request, it returns the posted object in the array. 
2. A POST request allows the user to add new tank information to an array for which an ID number is automatically assigned. ID numbers are increments of 1 for each new addition. 

## /data/:id

1. The user can send a PATCH request to change the parts of one of the tanks after it has been posted. The requester can make a JSON body with any combination of the attributes and update them as necessary. The "id" attribute cannot be edited. 
2. The user can make a DELETE request to delete any previously POSTed object, providing the id number of the object they wish to delete. 

#### **Note: A test file was used to test the server inside of a terminal window. The main file was tested and appears to work. A web browser can also be used to see the data that was added by the test file using the corresponding route. Test data is provided in this test file and can be used by anyone interested in seeing if the server works. A separate terminal must be used to run the test file.** 





