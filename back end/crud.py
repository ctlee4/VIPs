import mysql.connector
import flask
from mysql.connector import Error
from flask import jsonify, request 

import creds #local file
from sqlhelper import create_connection, execute_query, execute_read_query


#create a conneciton to MySQL db
myCreds = creds.Creds() #this is a constructor. tells python how to create an object 
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

#set up application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create tables
query = '''
create table if not exists member (
    id int unsigned auto_increment not null primary key,
    name varchar(25) not null,
    details varchar(255),
    title varchar(25) not null, 
    level enum('bronze','silver','gold')
);
create table if not exists event (
    id int unsigned auto_increment not null primary key,
    name varchar(25) not null,
    capacity int(5) unsigned not null,
    level enum('bronze','silver','gold') not null,
    date date not null
);
create table if not exists registration (
    id int unsigned auto_increment not null primary key,
    event_id int unsigned,
    member_id int unsigned,
    foreign key (event_id) references event(id),
    foreign key (member_id) references member(id)
);
'''

#execute_query(conn,query)


@app.route('/', methods=['GET'])
def home():
    return "<h>Home Page</h>"


#####################################################
#                                                   #
#               All Create Functions                #
#                                                   #
#####################################################

#Calvin - Edited function to add a new member to the Member table in the database
@app.route('/member',methods=["POST"])
def add_member():
    request_data = request.get_json()

    newName = request_data['name']
    newDetails = request_data['details']
    newTitle = request_data['title']
    newLevel = request_data['level']

    query = "INSERT INTO member (name, details, title, level) VALUES (%s, %s, %s, %s)"
    execute_query(conn, query, (newName, newDetails, newTitle, newLevel))
    return jsonify({'message': 'Member added successfully'})


@app.route('/event',methods=["POST"])
def add_event():
     


@app.route('/registration',methods=["POST"])
def add_registration():
    '''
    RULES:
    member cannot register for the same event twice
    members of the same (or higher) level may attend the event
    member can register if event is not yet at capacity
    '''
    pass 


#####################################################
#                                                   #
#                All Read Functions                 #
#                                                   #
#####################################################

@app.route('/members',methods=["GET"])
def read_members():
    pass 

@app.route('/events',methods=["GET"])
def read_events():
    pass 

@app.route('/registrations',methods=["GET"])
def read_registration():
    '''
    RULES:
    query will show the registered members for one event
    '''
    pass 


#####################################################
#                                                   #
#               All Update Functions                #
#                                                   #
#####################################################

@app.route('/member',methods=["PATCH"])
def update_member():
    pass 

@app.route('/',methods=["PATCH"])
def update_member():
    pass 

@app.route('/registration',methods=["PATCH"])
def update_registration():
    pass 


#####################################################
#                                                   #
#               All Delete Functions                #
#                                                   #
#####################################################

@app.route('/member',methods=["DELETE"])
def delete_member():
    pass 

@app.route('/event',methods=["DELETE"])
def delete_event():
    pass 

@app.route('/registration',methods=["DELETE"])
def delete_registration():
    pass 