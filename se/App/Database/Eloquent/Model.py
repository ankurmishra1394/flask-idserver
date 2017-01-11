from flask import Flask
from app.connection import connection
import psycopg2.extras

class Model():
    def __init__(self, modelPath, pivotTableName, searchByValue, searchForValue, foreignTableKey = 'id'):
        self.modelPath = modelPath
        self.pivotTableName = pivotTableName
        self.searchByValue = searchByValue
        self.searchForValue = searchForValue
        self.foreignTableKey = foreignTableKey
        self.cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def belongsTo():
        # Player Belongs to a team
        query = "SELECT * FROM %s(user_token) JOIN %s(users) ON %s.%s(user_token.user_id) = (%s)(users.id) WHERE %s(user_token.user_id)=%s" %(self.pivotTableName, self.modelPath().tableName, self.pivotTableName, self.searchForValue, self.searchForValue, self.searchByValue, self.id)
        self.cursor.execute(query)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def hasOne():
        #One Player has one team
        query = "SELECT * FROM %s(user_token) JOIN %s(users) ON %s.%s(user_token.user_id) = (%s)(users.id) WHERE %s(user_token.user_id)=%s" %(self.pivotTableName, self.modelPath().tableName, self.pivotTableName, self.searchForValue, self.searchForValue, self.searchByValue, self.id)
        self.cursor.execute(query)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def hasMany():
        #One Project has many developers
        query = "SELECT * FROM %s(user_token) RIGHT OUTER JOIN %s(users) ON %s.%s(user_token.user_id) = (%s)(users.id) WHERE %s(user_token.user_id)=%s" %(self.pivotTableName, self.modelPath().tableName, self.pivotTableName, self.searchForValue, self.searchForValue, self.searchByValue, self.id)
        self.cursor.execute(query)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def belongsToMany(self):
        # Many developers belongs to many projects
        query = "SELECT * FROM %s RIGHT OUTER JOIN %s ON %s.%s = (%s) WHERE %s=%s" %(self.pivotTableName, self.modelPath().tableName, self.pivotTableName, 
            self.searchForValue, self.searchForValue, self.searchByValue, self.id)
        query = "SELECT * FROM %s LEFT OUTER JOIN %s ON %s.%s = (%s) WHERE %s=%s" %(self.pivotTableName, self.modelPath().tableName, self.pivotTableName, 
            self.searchForValue, self.searchForValue, self.searchByValue, self.id)
        self.cursor.execute(query)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def bind_column_name_with_data(self,  data):
        result = []
        if len(data) == 1:
            return dict(data[0])
        for row in data:
            result.append(dict(row))
        return result
