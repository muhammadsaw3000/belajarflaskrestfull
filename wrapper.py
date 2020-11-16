import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor
from config import config

class PostgresWrapper:
    """def __init__(self, **args):
        self.user = args.get('user', 'kkrvyufhvntpah')
        self.password = args.get('password', '83d46de592730061458eac590e598bfb2154050aaeec5ce3a669ad730f388da2')
        self.port = args.get('port', 5432)
        self.dbname = args.get('dbname', 'd4smfhtc7ekqsk')
        self.host = args.get('host', 'ec2-54-157-88-70.compute-1.amazonaws.com')
        self.connection = None"""
        
    def connect(self):
        params = config()
        pg_conn = psycopg2.connect(**params)
        """pg_conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=self.dbname,
            host=self.host
        )"""
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
    
    def get_countries(self):
        query = 'SELECT * FROM public."SALARY" LIMIT 2;'
        print(self.get_json_response(query))
        
#dbconn = PostgresWrapper()
#dbconn.connect()
#dbconn.get_countries()