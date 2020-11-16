import psycopg2
from config import config

row = {}
row_return = {}

def select_salary():
    """ query data from the salary table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = 'SELECT "SALARY_ID", "KODE_KANTOR", "NAMA_KANTOR", "ID_DOKUMEN", "KETERANGAN", "CENTANG", "NAMA_BANK", "NO_REKENING", "ATAS_NAMA", "NOM_TRANSFER", "TGL_UBAH" FROM public."SALARY" ORDER BY "KODE_KANTOR"'
        cur.execute(sql)
        print(sql)
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchall()
        
        for x in range(len(row)):
            row_return[x]["SALARY_ID"] = row["SALARY_ID"]
            row_return[x]["KODE_KANTOR"] = row["KODE_KANTOR"]
            row_return[x]["NAMA_KANTOR"] = row["NAMA_KANTOR"]
            row_return[x]["ID_DOKUMEN"] = row["ID_DOKUMEN"]
            row_return[x]["KETERANGAN"] = row["KETERANGAN"]
            row_return[x]["CENTANG"] = row["CENTANG"]
            row_return[x]["NAMA_BANK"] = row["NAMA_BANK"]
            row_return[x]["NO_REKENING"] = row["NO_REKENING"]
            row_return[x]["ATAS_NAMA"] = row["ATAS_NAMA"]
            row_return[x]["NOM_TRANSFER"] = row["NOM_TRANSFER"]
            row_return[x]["TGL_UBAH"] = row["TGL_UBAH"]
        
        #row = cur.fetchone()
        #while row is not None:
            #print(row)
            #row = cur.fetchone()
        cur.close()
        #print(row)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return row_return
        
#if __name__ == '__main__':
    #select_salary()