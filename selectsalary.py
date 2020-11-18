import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor
from config import config

class PostgresWrapper:
    def connect(self):
        params = config()
        pg_conn = psycopg2.connect(**params)
        self.connection = pg_conn
        
    def get_json_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)
    
    @staticmethod
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res
    
    def get_json_response(self, query):
        cursor = self.get_json_cursor()
        response = self.execute_and_fetch(cursor, query)
        return json.dumps(response)
    
    def select_salary(self, field, kondisi):
        self.connect()
        #query = 'SELECT * FROM public."SALARY" LIMIT 2;'
        if kondisi!='':
            query = 'SELECT * FROM public."SALARY" WHERE "'+field+'"='+"'"+kondisi+"'"
        elif kondisi=="":
            query = 'SELECT * FROM public."SALARY"'
        #print(self.get_json_response(query))
        return self.get_json_response(query)
    
    def select_penduduk(self, field, kondisi):
        self.connect()
        if kondisi!='':
            query = 'SELECT * FROM public."KN_PENDUDUK" WHERE "'+field+'"='+"'"+kondisi+"'"
        elif kondisi=="":
            query = 'SELECT * FROM public."KN_PENDUDUK"'
        #print(self.get_json_response(query))
        return self.get_json_response(query)
        
#dbconn = PostgresWrapper()
#print(dbconn.select_salary())