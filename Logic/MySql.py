def Import_Connection_Details():
    with open('MysqlConnection.txt') as f:
        data = f.read()
        connectionDetails = json.loads(data)
    return connectionDetails