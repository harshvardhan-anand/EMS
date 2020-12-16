# Team Number 27 - IVOTED

### Project Overview

Problem: To implement an online Election Management System to conduct the college council elections ensuring the anonymity of the voter to the admin.

Solution: A full-stack secure application (I-VOTED) for conduction of council election has been **implemented and deployed** and it can be accessed here: **https://harshvardhanpy.pythonanywhere.com/**

 - User Access = jinen@smit.smu.edu.in (psw - munnamunna)
 - Election Admin = admin@smit.smu.edu.in (psw - smitsmit) 

### Solution Description

The application is made in Python using the django framework. The application architechture is robust and contains all the necessary security features given in the problem statement.**No information of the voters is being stored in the database thus ensuring complete anonymity of the voters**. It consists of four views, three of which are i.e.- Election-Admin, Candidate and Voter. Apart from these, there is a fourth view which allows the application to be controlled by a Super-Admin who will possess the necessary rights to create and modify the election-admin. The implementation of super-admin gives the required flexibility to the application without compromising its security. Hence the app is fully scalable and can be modified easily to implement an election management system for any other scenario. The architecture design and other technical details are as follows.

### Architecture Diagram

<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/DataFlow.png">

### Technical Description

An overview of:
* Technologies Used - 
 1. Python 3.7 (Backend)
 2. Django 3.1 (Backend)
 3. SQLite (Database)
 3. JavaScript (FrontEnd)
 4. HTML (Frontend)
 5. CSS (Frontend)
 6. Bootstrap 4 (Frontend)

* Setup/Installations - 
-- To install Django<br>
1. Install Python
2. pip install django

* Instructions to run the submitted code - python manage.py runserver
<br>You can also view the EMS at: https://harshvardhanpy.pythonanywhere.com/

### Flow Diagram
The complete working of the app is represented in the following flow-chart
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Flowchart.png">
<br><br>

### Screenshots and Usage Instructions
Here you can see the complete flow of application and usage instructions

#### HomePage
This is the homepage of the application. As explained in the architecture we can access the application in three modes:<br>
* Admin 
* Voter (or Candidate) 
* SuperAdmin
We can access the login page for admin and voter from the links given on the homepage. The superadmin can be accessed by ammending "/admin" at the end of the homepage url. Lets first see the admin view.
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(1).png">
<br><br>

#### Admin View
This is an intelligent login system which will automatically detect whether the user is an admin or a voter. Use the login id and password given above to access the admin dashboard.
<br>
<img src='https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(22).png'>
<br><br>
The Election Admin will have the following rights:<br>
* Start Election
* Start Polling
* Stop Polling
* Stop Election
<br>
<img src='https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(2).png'>
<br><br>
As the Election admin clicks on <b>"Start Election"</b>, An email will be sent to all the students containing a **SECURE ONE-TIME login id and password** which can be used only for that particular election. All voters as well as candidates can register themselves using that secure credentials.

##### Note: You may not be able to send the emails because the free version of the hosting doesn't provide the feature to set the SMTP server. However that can be bypassed by the superuser. The screenshots provided here are of "localhost". 
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(3).png">
<br><br>
Once the email is sent to all the students, the <b>"Start Polling"</b> button will be activated. Generally a duration of 48 hrs (or as decided by authorities) will be given for candidates and voter to register themselves. Clicking on this button to start the polling process. 
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(4).png"
<br><br>

#### Candidate View
The candidate view can be accessed only when the poll has not yet started. To access the candidate view you need to click on "Vote/Register" button on the homepage and enter your ONE-TIME SECURE credentials before the polling begins. 
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(5).png">
<br><br>
On successful login, you should see this screen.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(23).png">
<br><br>
Click on register and you will be taken to the candidate registration page. You can register for the election from here.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(24).png">
<br><br>


#### Voter View
You can access the voter view when the polling has started.
On the homepage, if you click on the "Vote/Register" button, you will be directed to the smart login system where you can use your ONE-TIME SECURE credentials received through email to login.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(6).png">
<br><br>
You will be directed to the Election Portal where you can cast your vote.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(7).png">
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(8).png">
<br><br>
Once you cast your vote, you will be logged out and your credentials will expire so that you do not have any access to the application. This makes the application absolutely secure as there is no way one can gain access to the voting portal.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(9).png">
<br><br>
After the allocated time for polling is over, the Election admin can click the stop polling button (from admin dashboard). This will redirect to the results page.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(11).png">
<br><br>
If the Election Admin clicks on the "Stop Election" button, the election will be stopped and all the variables will be reset. The election can only be stopped once the results have been declared.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(12).png">
<br><br>



#### Super Admin View
Super Admin dashboard can be accessed at **https://harshvardhanpy.pythonanywhere.com/admin**
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(13).png">
<br><br>
Super Admin possess special priviledges and can access the profiles of voters, candidates and admins and can modify the election status.
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(15).png">
<br><br>
List of all Candidates
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(16).png">
<br><br>
Form to change the candidate
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(17).png">
<br><br>
Form to change the access level of users
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(18).png">
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(19).png">
<br><br>
Form to change the election status
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(20).png">
<br><br>
Form to change the voter profile
<br>
<img src="https://github.com/harshvardhan-anand/EMS/blob/master/IVote/Screenshots/Screenshot%20(21).png">
<br><br>
