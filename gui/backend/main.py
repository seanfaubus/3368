import flask
from flask import jsonify, request, redirect, url_for
from sql import create_connection
from sql import execute_read_query
from sql import execute_query
import creds
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(dir_path, "templates")

# setting up an application name
app = flask.Flask(__name__) # sets up the app
app.config["DEBUG"] = True # allow to show errors in browser


# read all planes in table
@app.route('/api/planes', methods=['GET'])
def api_read_planes():
    # this api reads all planes
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM planes"
    planes = execute_read_query(conn, sql)
    # returns plane data in json format
    return jsonify(planes)


# read selected plane from table
@app.route('/api/plane', methods=['GET'])
def api_read_plane():
    # collects data from user to read an entry
    if 'id' in request.args: # only if an id is provided as an arg, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: no id provided'
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM planes"
    plane = execute_read_query(conn, sql)
    results = []
    for p in plane:
        if p['id'] == id:
            results.append(p)
    # if no results to return, send message to try a new ID.
    if len(results) == 0:
        return "ID not found. Try a different ID."
    # returns plane data in json format
    return jsonify(results)


# delete a plane
@app.route('/api/plane', methods=['DELETE'])
def api_delete_plane():
    # collects data from user to delete an entry
    request_data = request.get_json()
    print(request_data)

    id_to_delete = request_data['id']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "DELETE FROM planes WHERE id = %s" % id_to_delete

    execute_query(conn, sql)
    return "delete was successful"


# add plane as post request
@app.route('/api/plane', methods=['POST'])
def add_plane():
    # collects plane data from user to add a new plane to the table
    request_data = request.get_json()
    newMake = request_data['make']
    newModel = request_data['model']
    newYear = request_data['year']
    newCapacity = request_data['capacity']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    create_statement = "INSERT INTO planes (make, model, year, capacity) VALUES ('%s', '%s', %s, %s)" % (newMake, newModel, newYear, newCapacity)
    execute_query(conn, create_statement)
    return "add request successful"


# UPDATE capacity of plane as PUT request
# Allows to update any number of attributes
@app.route('/api/plane', methods=['PUT'])
# User must provide the id of plane whose attributes to update
def update_plane():
    request_data = request.get_json()
    print(request_data)
    idToUpdate = request_data['id']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    cats = ['capacity', 'make', 'model', 'year']

    # TO UPDATE JUST ONE COLUMN, ENTER WHICHEVER COLUMN AND DESIRED VALUE FOR COLUMN.
    # NEED TO ADD INT IF VARIABLE IS CAPACITY ************
    if len(request_data) == 2:
        variable1 = ''
        variableToUpdate = ''
        for i in cats:
            if i in request_data.keys():
                variable1 = i
                variableToUpdate = request_data[i]
        update_query = "UPDATE planes SET %s = '%s' WHERE id = %s" % (variable1,variableToUpdate, idToUpdate)

    elif len(request_data) == 3:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE planes SET %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],variableToUpdate[0],
                                                                                 variables[1],variableToUpdate[1],
                                                                                 idToUpdate)

    elif len(request_data) == 4:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE planes SET %s = '%s', %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],
                                                                                            variableToUpdate[0],
                                                                                            variables[1],
                                                                                            variableToUpdate[1],
                                                                                            variables[-1],
                                                                                            variableToUpdate[-1],
                                                                                            idToUpdate)

    else:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE planes SET %s = '%s', %s = '%s', %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],
                                                                                            variableToUpdate[0],
                                                                                            variables[1],
                                                                                            variableToUpdate[1],
                                                                                            variables[2],
                                                                                            variableToUpdate[2],
                                                                                            variables[-1],
                                                                                            variableToUpdate[-1],
                                                                                            idToUpdate)

    execute_query(conn, update_query)
    return "Update request successful"


#############################################
# APIs for airport table

# read all airports in table
@app.route('/api/airports', methods=['GET'])
def api_read_airports():
    # this api reads all airports
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM airports"
    airports = execute_read_query(conn, sql)
    # returns airport data in json format
    return jsonify(airports)


# read selected airport from table
@app.route('/api/airport', methods=['GET'])
def api_read_airport():
    # collects data from user to read an entry
    if 'id' in request.args: # only if an id is provided as an arg, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: no id provided'
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM airports"
    airports = execute_read_query(conn, sql)
    results = []
    for airport in airports:
        if airport['id'] == id:
            results.append(airport)
    # if no results to return, send message to try a new ID.
    if len(results) == 0:
        return "ID not found. Try a different ID."
    # returns airport data in json format
    return jsonify(results)


# delete selected airport from table
@app.route('/api/airport', methods=['DELETE'])
def api_delete_airport():
    # collects data from user to delete an entry
    request_data = request.get_json()
    print(request_data)

    id_to_delete = request_data['id']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "DELETE FROM airports WHERE id = %s" % id_to_delete

    execute_query(conn, sql)
    return "delete was successful"


# add airport as post request
@app.route('/api/airport', methods=['POST'])
def add_airport():
    # collects airport data from user to add a new airport to the table
    request_data = request.get_json()
    newAirportcode = request_data['airportcode']
    newAirportname = request_data['airportname']
    newCountry = request_data['country']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    create_statement = "INSERT INTO airports (airportcode, airportname, country) VALUES ('%s', '%s', '%s')" % (newAirportcode, newAirportname, newCountry)
    execute_query(conn, create_statement)
    return "add request successful"


# UPDATE API of airport as PUT request
# Allows to update any number of attributes
@app.route('/api/airport', methods=['PUT'])
def update_airport():
    request_data = request.get_json()
    idToUpdate = request_data['id']      # Need to provide id of airport whose attributes to update
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    cats = ['airportcode', 'airportname', 'country']

    # TO UPDATE JUST ONE COLUMN, ENTER WHICHEVER COLUMN AND DESIRED VALUE FOR COLUMN.
    # USER MUST PROVDIE CORRECT DATA TYPE WHEN UPDATING VALUES
    if len(request_data) == 2:
        variable1 = ''
        variableToUpdate = ''
        for i in cats:
            if i in request_data.keys():
                variable1 = i
                variableToUpdate = request_data[i]
        update_query = "UPDATE airports SET %s = '%s' WHERE id = %s" % (variable1,variableToUpdate, idToUpdate)

    elif len(request_data) == 3:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE airports SET %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],variableToUpdate[0],
                                                                                 variables[1],variableToUpdate[1],
                                                                                 idToUpdate)

    elif len(request_data) == 4:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE airports SET %s = '%s', %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],
                                                                                            variableToUpdate[0],
                                                                                            variables[1],
                                                                                            variableToUpdate[1],
                                                                                            variables[-1],
                                                                                            variableToUpdate[-1],
                                                                                            idToUpdate)

    else:
        variables = []
        variableToUpdate = []
        for i in cats:
            if i in request_data.keys():
                variables.append(i)
                variableToUpdate.append(request_data[i])
        update_query = "UPDATE airports SET %s = '%s', %s = '%s', %s = '%s', %s = '%s' WHERE id = %s" % (variables[0],
                                                                                            variableToUpdate[0],
                                                                                            variables[1],
                                                                                            variableToUpdate[1],
                                                                                            variables[2],
                                                                                            variableToUpdate[2],
                                                                                            variables[-1],
                                                                                            variableToUpdate[-1],
                                                                                            idToUpdate)

    execute_query(conn, update_query)
    return "Update request successful"


#############################################
# APIs for flight table

# read all flights in table
@app.route('/api/flights', methods=['GET'])
def api_read_flights():
    # this api reads all flights
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM flights"
    flights = execute_read_query(conn, sql)
    # returns flight data in json format
    return jsonify(flights)


# read selected flight from table
@app.route('/api/flight', methods=['GET'])
def api_read_flight():
    # collects data from user to read an entry
    if 'id' in request.args: # only if an id is provided as an arg, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: no id provided'
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "SELECT * FROM flights"
    flights = execute_read_query(conn, sql)
    results = []
    for flight in flights:
        if flight['id'] == id:
            results.append(flight)
    # if no results to return, send message to try a new ID.
    if len(results) == 0:
        return "ID not found. Try a different ID."
    # returns flight data in json format
    return jsonify(results)


# delete selected flight from table
@app.route('/api/flight', methods=['DELETE'])
def api_delete_flight():
    # collects data from user to delete an entry

    request_data = request.get_json()
    print(request_data)

    id_to_delete = request_data['id']

    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    sql = "DELETE FROM flights WHERE id = %s" % id_to_delete

    execute_query(conn, sql)
    return "delete was successful"


# add airport as post request
@app.route('/api/flight', methods=['POST'])
def add_flight():
    # collects flight data from user to add a new flight to the table
    request_data = request.get_json()
    print(request_data)
    newAirportfromid = request_data['airportfromid']
    newAirporttoid = request_data['airporttoid']
    newdate = request_data['date']
    newPlaneid = request_data['planeid']
    # connects to database to run the SQL statement
    mycreds = creds.Creds()
    conn = create_connection(mycreds.conString, mycreds.userName, mycreds.password, mycreds.dbName)
    create_statement = "INSERT INTO flights (airportfromid, airporttoid, date, planeid) VALUES (%s, %s, '%s', %s)" % (newAirportfromid, newAirporttoid, newdate, newPlaneid)
    execute_query(conn, create_statement)
    return "add request successful"


authorizedusers = [
{
    'username': 'admin',
    'password': 'admin', # do not use cleartext passwords in tables
    'role': 'default',
    'token': '0',
    'admininfo': None
    }
]


# figure out how to get back to templates folder
# redirect to flights once flights APIs get made ************
@app.route('/login', methods=['GET'])
def login():

    username = request.headers['username']  # get header params (as dictionaries)
    pw = request.headers['password']
    for au in authorizedusers:
        if au['username'] == username and au['password'] == pw:
            return redirect(url_for('api_read_flights')) # displays flights info if login succeeds
    return 'Security Error'



app.run()
