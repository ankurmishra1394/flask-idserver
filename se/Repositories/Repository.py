from flask import Flask
from app.connection import connection
import psycopg2.extras
class Repository():

    def fetchDetailsWithoutJoin(self, tableName, params=None):
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fields = ', '.join(params.keys())
        values = ', '.join(['%%(%s)s' % x for x in params])
        if params:
            query = 'SELECT * FROM %s WHERE (%s)=(%s)' %(tableName, fields, values)
        else:
            query = 'SELECT * FROM %s ' %(tableName)
        cursor.execute(query, params)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def fetchDetailsWithJoin(self, fromTableName, withTableName, joinOn=None, params=None):
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fields = ', '.join(joinOn.keys())
        values = ', '.join(joinOn.values())
        fieldsMatch = ', '.join(params.keys())
        valuesMatch = ', '.join(['%%(%s)s' % x for x in params])
        if params:
            query = "SELECT %s.*, %s.* FROM %s LEFT OUTER JOIN %s ON (%s) = (%s) WHERE (%s)=(%s)" %(fromTableName, withTableName, fromTableName, withTableName, fields, values, fieldsMatch, valuesMatch)
        else:
            query = "SELECT %s.*, %s.* FROM %s LEFT OUTER JOIN %s ON (%s) = (%s)" %(fromTableName, withTableName, fromTableName, withTableName, fields, values)
        joinOn.update(params)
        cursor.execute(query, joinOn)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def store(self, tableName, params=None):
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fields = ', '.join(params.keys())
        values = ', '.join(['%%(%s)s' % x for x in params])
        query = 'INSERT INTO %s (%s) VALUES (%s) RETURNING id;' % (tableName, fields, values)
        cursor.execute(query, params)
        connection.commit()
        return self.bind_column_name_with_data(cursor.fetchall())

    def update(self, tableName, updateParams=None, searchParams=None):
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        updateFields = ', '.join(updateParams.keys())
        updateValues = ', '.join(['%%(%s)s' % x for x in updateParams])
        searchFields = ', '.join(searchParams.keys())
        searchValues = ', '.join(['%%(%s)s' % x for x in searchParams])
        query = 'UPDATE %s SET (%s)=(%s) WHERE (%s)=(%s);' % (tableName, updateFields, updateValues, searchFields, searchValues)
        updateParams.update(searchParams)
        cursor.execute(query, updateParams)
        connection.commit()
        return cursor.rowcount

    def bind_column_name_with_data(self,  data):
        result = []
        if len(data) == 1:
            return dict(data[0])
        for row in data:
            result.append(dict(row))
        return result