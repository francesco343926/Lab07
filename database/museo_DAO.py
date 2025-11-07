from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
    # TODO

        self.database_connect = ConnessioneDB

    def get_musei(self):
        cnx = self.database_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT *
            FROM museo"""
        cursor.execute(query)
        result = []
        for riga in cursor:
            result.append(Museo(riga["id"],
                                riga["nome"], riga["tipologia"]))
        cursor.close()
        cnx.close()
        return result