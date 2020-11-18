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
SALARY_ID = None

class ContohResource(Resource):
    def get(self):
        #response = { "msg":"Hallo dunia, ini app restfull pertamaku"}
        #return SALARY
        
        #INI HANYA TEST SAJA
        if request.form["INVOKE"] != "SALARY":
            return "INVOKE ANDA ADALAH: "+request.form["INVOKE"]
        else:
            dbconn = PostgresWrapper()
            VALUE = request.form["VALUE"]
            FIELD = request.form["FIELD"]
            return dbconn.select_salary(FIELD, VALUE).replace('\"','"',10000)
    
    def post(self):
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
        
        SALARY["KODE_KANTOR"] = KODE_KANTOR
        SALARY["NAMA_KANTOR"] = NAMA_KANTOR
        SALARY["ID_DOKUMEN"] = ID_DOKUMEN
        SALARY["KETERANGAN"] = KETERANGAN
        SALARY["CENTANG"] = CENTANG
        SALARY["NAMA_BANK"] = NAMA_BANK
        SALARY["NO_REKENING"] = NO_REKENING
        SALARY["ATAS_NAMA"] = ATAS_NAMA
        SALARY["NOM_TRANSFER"] = NOM_TRANSFER
        SALARY["TGL_UBAH"] = TGL_UBAH
        
        response = {"msg":"Data berhasil disimpan. SALARY_ID: "+str(SALARY_ID)}
        return response
    
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])
    
if __name__ == "__main__":
    app.run(debug=True, port=5005)
    #app.run()