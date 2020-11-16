import psycopg2
from config import config


def insert_salary(KODE_KANTOR,NAMA_KANTOR,ID_DOKUMEN,KETERANGAN,CENTANG,NAMA_BANK,NO_REKENING,ATAS_NAMA,NOM_TRANSFER,TGL_UBAH):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO public."SALARY"("KODE_KANTOR","NAMA_KANTOR","ID_DOKUMEN","KETERANGAN","CENTANG","NAMA_BANK","NO_REKENING","ATAS_NAMA","NOM_TRANSFER","TGL_UBAH")
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING "SALARY_ID";"""
    conn = None
    salary_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        print("ASHARI THE KAMPRETOS: "+sql)
        # execute the INSERT statement
        #cur.execute(sql, ("43A","DEPUTI DIREKTUR BIDANG PENGEMBANGAN TEKNOLOGI INFORMASI","20101400655367","PEMBAYARAN GAJI NASIONAL BULAN OKTOBER 2020.",5,"MANDIRI","0700009726915","AGTRIA PRILIKA HERNIATY",10302093,"14/10/2020 18:02:13"))
        cur.execute(sql, (KODE_KANTOR,NAMA_KANTOR,ID_DOKUMEN,KETERANGAN,CENTANG,NAMA_BANK,NO_REKENING,ATAS_NAMA,NOM_TRANSFER,TGL_UBAH))
        # get the generated id back
        salary_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return salary_id

#if __name__ == '__main__':
    #connect()

#if __name__ == '__main__':
    #insert_salary("43A","DEPUTI DIREKTUR BIDANG PENGEMBANGAN TEKNOLOGI INFORMASI","20101400655367","PEMBAYARAN GAJI NASIONAL BULAN OKTOBER 2020.",5,"MANDIRI","0700009726915","AGTRIA PRILIKA HERNIATY",10302093,"14/10/2020 18:02:13")