from db import DBConnection as mydb
class Mahasiswa:
    def __init__(self):
        self.__id=None
        self.__Nim=None
        self.__nama=None
        self.__prodi=None
        self.__Kelas=None
        self.__Tanggal_Lahir=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def Nim(self):
        return self.__Nim
        
    @Nim.setter
    def Nim(self, value):
        self.__Nim = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def Kelas(self):
        return self.__Kelas
        
    @Kelas.setter
    def Kelas(self, value):
        self.__Kelas = value
    @property
    def Tanggal_Lahir(self):
        return self.__Tanggal_Lahir
        
    @Tanggal_Lahir.setter
    def Tanggal_Lahir(self, value):
        self.__Tanggal_Lahir = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__Nim,self.__nama,self.__prodi,self.__Kelas,self.__Tanggal_Lahir)
        sql="INSERT INTO Mahasiswa (Nim,nama,prodi,Kelas,Tanggal_Lahir) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__Nim,self.__nama,self.__prodi,self.__Kelas,self.__Tanggal_Lahir, id)
        sql="UPDATE mahasiswa SET Nim = %s,nama = %s,prodi = %s,Kelas = %s,Tanggal_Lahir = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByKELAS(self, Kelas):
        self.conn = mydb()
        val = (self.__Nim,self.__nama,self.__prodi,self.__Tanggal_Lahir, Kelas)
        sql="UPDATE mahasiswa SET Nim = %s,nama = %s,prodi = %s,Tanggal_Lahir = %s WHERE Kelas=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByKELAS(self, Kelas):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE Kelas='" + str(Kelas) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__Nim = self.result[1]
        self.__nama = self.result[2]
        self.__prodi = self.result[3]
        self.__Kelas = self.result[4]
        self.__Tanggal_Lahir = self.result[5]
        self.conn.disconnect
        return self.result
    def getByKELAS(self, Kelas):
        a=str(Kelas)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE Kelas='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__Nim = self.result[1]
           self.__nama = self.result[2]
           self.__prodi = self.result[3]
           self.__Kelas = self.result[4]
           self.__Tanggal_Lahir = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__Nim = ''
           self.__nama = ''
           self.__prodi = ''
           self.__Kelas = ''
           self.__Tanggal_Lahir = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result