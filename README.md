# :steam_locomotive: Train Database Management System

A Database designed to solve the problem of the data management in scheduling trains, selling tickets, managing trips, and trains supporting staff (personnel). This database can be adopted for different use cases related to other modes of transportation with few changes but the most closest one is the bus management system. 

## Problem Statement

The mismanagement of transportation services has the potential to induce damage which could range from minor economic inefficiencies to major tragedy. Therefore, the duty of those enabling decision makers within these systems must be to provide the aforementioned with every extent of relevant and considerable data in order to make appropriate determinations. Relational Database Management Systems (RDBMS) hold a particularly essential role in the logistics of multi-dimensional transport services, and their implementation must maintain a level of absolute integrity while undertaking the challenges of a system that thrives off of improve efficiency. Train Database Management system is an example of a transport service system whose proper attribution of subcomponents mean the difference between profitable day or national catastrophe. The work intends to address the extent of considerations which must be taken when designing and implementing a functional database around a simulated train system. Our group hold that in the context of an organization administering the logistics of a train service system, it is, to a great extent, requisite for a DBMS to simultaneously maintain the integrity of the data while enabling frequent and varied querying for decision-making.

## Use Cases

There are a variety of reasons as to why one might want to incorporate a database into the train system. Most use cases are similar, in that data contained in the system will be used to make a higher-level decision. Here are a few possible uses for our system:

+	Insert new train trips such that they do not conflict with other scheduled times
+	Track validity of passenger tickets
+	Analyze the popularity of locomotive transportation in different areas
+	Identify stations that have few visiting trains
+	Determine possible employee layoffs based off hours worked
+	Schedule workforce based on load placed on train system
+	Calculate train and station capacity

## Entity Relationship(ER) Diagram

<img width="789" alt="ER Diagram Image" src="https://i.imgur.com/F9fDmeP.png">

Figma Diagram Link: https://www.figma.com/file/ZRRgenXlwvHCWJBwiLe5V0/Train-System---ER-Diagram-(Copy)?node-id=0%3A1&t=P0VamMKyzHIq5dwq-1

## Relational Model

<img width="500" alt="Relational Model Image" src="https://i.imgur.com/Htb1y7m.png">

Relational Model Diagram Link: https://drive.google.com/file/d/122r9TxerxlKNg0tmUsMI62lb2sSeRPTB/view?usp=sharing

## Tech Stack

HTML, Python, JavaScript, Bootstrap 5, Django, and Azure PostgreSQL Server

## Group Members

McLain Barrett, Ayush Budhwani, Guillermo Clara, Hoan Ngo, James Pham, Joshua Tang, Freddy Velasco 

## Setup Project

## Prerequisites

- [Git](https://git-scm.com/downloads) version >= 2.37.0
- [Python](https://www.python.org/downloads/) version >= 3.10.8
- [Pip](https://pip.pypa.io/en/stable/installation/) version >= 22.3

## Instructions

1. Clone the project using command `git clone https://github.com/joshuahT/TrainSystem/ `
2. Change directory to navigate inside the trainsystem project: `cd trainsystem/`
3. Create a .env file inside the root of the project directory (TrainSystem) along with manage.py file with the following details: <br/><br/>
    .env 
    ```
    SECRET_KEY=<django-secret-key> 
    DB_NAME=<database-name> 
    USER_NAME=<database-username> 
    PASSWORD=<database-password> 
    HOST=<database-server-host-endpoint> 
    PORT=<database-server-exposed-port> 
    ```
    Fields: <br/>
    ```<django-secret-key>``` : django app generated secret key which will be used in settings.py file<br/>
    ```<database-name>``` : name of the database <br/>
    ```<database-username>```: username of the database <br/> 
    ```<database-password>```: password for the database user <br/> 
    ```<database-server-host-endpoint>```: host name where server is running (if running locally it should be localhost unless configured to something else during setup process of PgAdmin, else if running on cloud it there should be a field with database host name) <br/>
    ```<database-server-exposed-port>```: port on which the database is running (default is 5432 but it could be different based on the config) <br/> 

4. Run command `pip install -r requirements.txt` to install all the libraries used by this project
5. Run development server by using command `python manage.py runserver` and you can type in the url `http://localhost:8000` into your browser to view the website.

## References

[1]	Hector Garcia-Molina, Jeffrey D. Ullman and Jennifer Widom, Database Systems: The Complete Book, 2nd ed, Pearson, 2008 <br/>
[2]	“What is an Entity Relationship Diagram ?”. n.d. https://www.lucidchart.com/pages/er-diagrams.
