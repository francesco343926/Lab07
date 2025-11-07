from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        self.database_connect = ConnessioneDB
    # TODO
    def get_artefatti(self):
        cnx = self.database_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT *
                FROM artefatto"""
        cursor.execute(query)
        result = []
        for riga in cursor:
            result.append(Artefatto(riga["id"],
                                riga["nome"], riga["tipologia"], riga["epoca"],
                                    riga["id_museo"]))
        cursor.close()
        cnx.close()
        return result
