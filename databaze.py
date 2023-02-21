import sqlite3
from sqlite3 import Error as SQLError


class Databaze:

    cur = None

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except SQLError as err:
            print(f"Error: '{err}'")
        return conn

    def create_table_in_db(self, cur):
        create_cmd = "CREATE TABLE IF NOT EXISTS uzivatele (" \
                        "jmeno TEXT, " \
                        "prijmeni TEXT, " \
                        "stari_osoby INTEGER, " \
                        "tel_cislo TEXT);"
        cur.execute(create_cmd)

    def read_sql(self, cur):
        cur.execute("SELECT * FROM uzivatele;")
        for u in cur.fetchall():
            print(f"{u[0]}\t", f"{u[1]}\t", f"{u[2]}\t", f"{u[3]}\t")

    def search_sql(self, cur, jmeno, prijmeni):
        cur.execute(f"SELECT * FROM uzivatele WHERE jmeno = \"{jmeno}\" AND prijmeni = \"{prijmeni}\";")
        for u in cur.fetchall():
            print(f"{u[0]}\t", f"{u[1]}\t", f"{u[2]}\t", f"{u[3]}\t")

    def insert_sql(self, cur, jmeno, prijmeni, stari_osoby, tel_cislo):
        insrt_cmd = "INSERT INTO uzivatele (jmeno, prijmeni, stari_osoby, tel_cislo) VALUES(?, ?, ?, ?);"
        insrt_data = (jmeno, prijmeni, stari_osoby, tel_cislo)
        cur.execute(insrt_cmd, insrt_data)

    def main(self):
        database = "evidence_uzivatelu.db"
        conn = self.create_connection(database)
        if conn is not None:
            self.cur = conn.cursor()
            self.create_table_in_db(self.cur)
        else:
            print("Chyba spojení s databází!\n" + SQLError)
