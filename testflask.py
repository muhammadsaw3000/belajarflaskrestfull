from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from insert import insert_salary
from selectsalary import *
#from wrapper import *

app = Flask(__name__)
api = Api(app)
CORS(app)
SALARY = {}
PENDUDUK = {}
SALARY_ID = None
PENDUDUK_ID = None

class ContohResource(Resource):
    def get(self):
        #response = { "msg":"Hallo dunia, ini app restfull pertamaku"}
        #return SALARY
        
        #INI HANYA TEST SAJA
        if request.form["INVOKE"] == "KN_PENDUDUK":
            dbconn = PostgresWrapper()
            VALUE = request.form["VALUE"]
            FIELD = request.form["FIELD"]
            return dbconn.select_penduduk(FIELD, VALUE).replace('\"','"',10000)
        elif request.form["INVOKE"] == "SALARY":
            dbconn = PostgresWrapper()
            VALUE = request.form["VALUE"]
            FIELD = request.form["FIELD"]
            return dbconn.select_salary(FIELD, VALUE).replace('\"','"',10000)
    
    def post(self):
        if request.form["INVOKE"] == "SALARY":
            KODE_KANTOR = request.form["KODE_KANTOR"]
            NAMA_KANTOR = request.form["NAMA_KANTOR"]
            ID_DOKUMEN = request.form["ID_DOKUMEN"]
            KETERANGAN = request.form["KETERANGAN"]
            CENTANG = request.form["CENTANG"]
            NAMA_BANK = request.form["NAMA_BANK"]
            NO_REKENING = request.form["NO_REKENING"]
            ATAS_NAMA = request.form["ATAS_NAMA"]
            NOM_TRANSFER = request.form["NOM_TRANSFER"]
            TGL_UBAH = request.form["TGL_UBAH"]

            SALARY_ID = insert_salary(KODE_KANTOR,NAMA_KANTOR,ID_DOKUMEN,KETERANGAN,CENTANG,NAMA_BANK,NO_REKENING,ATAS_NAMA,NOM_TRANSFER,TGL_UBAH)
            print(SALARY_ID)
            
            response = {"msg":"Data berhasil disimpan. SALARY_ID: "+str(SALARY_ID)}
            return response
        elif request.form["INVOKE"] == "KN_PENDUDUK":
            NIK = request.form["NIK"]
            NO_KARTU_KELUARGA = request.form["NO_KARTU_KELUARGA"]
            NAMA_LENGKAP = request.form["NAMA_LENGKAP"]
            JENIS_KELAMIN = request.form["JENIS_KELAMIN"]
            TEMPAT_LAHIR = request.form["TEMPAT_LAHIR"]
            TGL_LAHIR = request.form["TGL_LAHIR"]
            NAMA_IBU_KANDUNG = request.form["NAMA_IBU_KANDUNG"]
            NAMA_AYAH_KANDUNG = request.form["NAMA_AYAH_KANDUNG"]
            GOLONGAN_DARAH = request.form["GOLONGAN_DARAH"]
            AGAMA = request.form["AGAMA"]
            STATUS_KAWIN = request.form["STATUS_KAWIN"]
            STATUS_HUB_KELUARGA = request.form["STATUS_HUB_KELUARGA"]
            PENDIDIKAN_AKHIR = request.form["PENDIDIKAN_AKHIR"]
            JENIS_PEKERJAAN = request.form["JENIS_PEKERJAAN"]
            KODE_PROPINSI = request.form["KODE_PROPINSI"]
            NAMA_PROPINSI = request.form["NAMA_PROPINSI"]
            KODE_KABUPATEN = request.form["KODE_KABUPATEN"]
            NAMA_KABUPATEN = request.form["NAMA_KABUPATEN"]
            KODE_KECAMATAN = request.form["KODE_KECAMATAN"]
            NAMA_KECAMATAN = request.form["NAMA_KECAMATAN"]
            KODE_KELURAHAN = request.form["KODE_KELURAHAN"]
            NAMA_KELURAHAN = request.form["NAMA_KELURAHAN"]
            ALAMAT = request.form["ALAMAT"]
            RT = request.form["RT"]
            RW = request.form["RW"]
            DUSUN = request.form["DUSUN"]
            KODE_POS = request.form["KODE_POS"]
            TGL_KAWIN = request.form["TGL_KAWIN"]
            EKTP_STATUS = request.form["EKTP_STATUS"]
            EKTP_LOCAL_ID = request.form["EKTP_LOCAL_ID"]
            EKTP_CREATED = request.form["EKTP_CREATED"]
            AKTAKWN = request.form["AKTAKWN"]
            NOAKTACERAI = request.form["NOAKTACERAI"]
            NOAKTAKWN = request.form["NOAKTAKWN"]
            TANGGALCERAI = request.form["TANGGALCERAI"]
            AKTALAHIR = request.form["AKTALAHIR"]
            NOAKTALAHIR = request.form["NOAKTALAHIR"]
            LAST_SYNC = request.form["LAST_SYNC"]

            PENDUDUK_ID = insert_kn_penduduk(NIK,NO_KARTU_KELUARGA,NAMA_LENGKAP,JENIS_KELAMIN,TEMPAT_LAHIR,TGL_LAHIR,NAMA_IBU_KANDUNG,NAMA_AYAH_KANDUNG,GOLONGAN_DARAH,AGAMA,STATUS_KAWIN,STATUS_HUB_KELUARGA,PENDIDIKAN_AKHIR,JENIS_PEKERJAAN,KODE_PROPINSI,NAMA_PROPINSI,KODE_KABUPATEN,NAMA_KABUPATEN,KODE_KECAMATAN,NAMA_KECAMATAN,KODE_KELURAHAN,NAMA_KELURAHAN,ALAMAT,RT,RW,DUSUN,KODE_POS,TGL_KAWIN,EKTP_STATUS,EKTP_LOCAL_ID,EKTP_CREATED,AKTAKWN,NOAKTACERAI,NOAKTAKWN,TANGGALCERAI,AKTALAHIR,NOAKTALAHIR,LAST_SYNC)
            print(PENDUDUK_ID)

            response = {"msg":"Data berhasil disimpan. PENDUDUK_ID: "+str(PENDUDUK_ID)}
            return response
    
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])
    
if __name__ == "__main__":
    app.run(debug=True, port=5005)
    #app.run()