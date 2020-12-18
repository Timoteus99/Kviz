import csv
import sqlite3
import random



class Vprasanje:
    vprasanje = ""
    nepravi_odg = []
    pravi_odg = ""
    vsi_odg = []
    def poglej_vprasanje(_self, id_vprasanja):
        vprasanje = preberi_sql_table(id_vprasanja)
        _self.vprasanje = vprasanje[1]
        _self.pravi_odg = vprasanje[2]
        _self.nepravi_odg = vprasanje[3].split("/")
    def izpis_moznih_odg(_self):
        random.shuffle(_self.vsi_odg)
        if len(_self.vsi_odg) > 3:
            print(_self.vsi_odg)
        else:
            print("________")
    def poglej_resitev(_self, odgovor):
        if odgovor == _self.pravi_odg:
            return True
    def __init__(_self, id_vprasanja):
        _self.vprasanje = id_vprasanja
        _self.poglej_vprasanje(id_vprasanja)
    def igraj(_self):
        print(_self.vprasanje)
        _self.vsi_odg = _self.nepravi_odg
        _self.vsi_odg.append(_self.pravi_odg)
        _self.izpis_moznih_odg()
#        print(_self.pravi_odg, _self.nepravi_odg)
        odgovor = input("Vnesi odgovor: ")
        return odgovor == _self.pravi_odg

def seznam_nakljucnih_st(n):
    seznam = []
    while len(seznam) < n:
        cifra = random.randint(1, 100)
        if cifra not in seznam:
            seznam.append(cifra)
    return seznam

def preberi_sql_table(id):
    record = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")
        sqlite_select_query = f"SELECT * from vprasanja where id = ?"
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
#           print("The SQLite connection is closed")
        return record

class Igra:
    def __init__(_self, st_vprasanj):
        _self.tocke = 0
        seznam_vpr = seznam_nakljucnih_st(15)
        for vpr_id in seznam_vpr:
            vpr = Vprasanje(vpr_id)
            if vpr.igraj() == True:
                print("Bravo, svaka čast.")
                _self.tocke += 1
            else:
                print("Nimaš za burek.")
        print("Dobil/a si",_self.tocke, "točk od 15.")
        
igra = Igra(15)
    

    