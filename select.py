import psycopg2
from config import config

def get_salary():
    """ query data from the salary table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT "SALARY_ID", "KODE_KANTOR", "NAMA_KANTOR", "ID_DOKUMEN", "KETERANGAN", "CENTANG", "NAMA_BANK", "NO_REKENING", "ATAS_NAMA", "NOM_TRANSFER", "TGL_UBAH" FROM public."SALARY" ORDER BY "KODE_KANTOR"')
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchall()
        
        #row = cur.fetchone()
        #while row is not None:
            #print(row)
            #row = cur.fetchone()
        cur.close()
        print(row)
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return {"msg":"Data tidak ditemukan."}
        
#if __name__ == '__main__':
    #get_salary()