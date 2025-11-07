from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        listartefattifiltrati = []
        musei = self._museo_dao.get_musei()
        id=0
        for Museo in musei:
            if Museo.nome == museo:
                id = Museo.id
        artefatti = self._artefatto_dao.get_artefatti()
        filtrati = []
        if museo=="Nessun filtro" and epoca=="Nessun filtro":
            return artefatti
        elif museo=="Nessun filtro":
            for artefatto in artefatti:
                if artefatto.epoca==epoca:
                    filtrati.append(artefatto)
            return filtrati
        elif epoca=="Nessun filtro":
            for artefatto in artefatti:
                if artefatto.id_museo== id-14:
                    filtrati.append(artefatto)
            return filtrati
        else:
            for artefatto in artefatti:
                if artefatto.id_museo== id-14 and artefatto.epoca==epoca:
                    filtrati.append(artefatto)
            return filtrati


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        artefatti = self._artefatto_dao.get_artefatti()
        listartefatti = []
        for artefatto in artefatti:
            epoca = artefatto.epoca
            listartefatti.append(epoca)
        ordinata = sorted(listartefatti)
        ordinata.append("Nessun filtro")
        return ordinata

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        musei = self._museo_dao.get_musei()
        listanomimusei= []
        for museo in musei:
            nome= museo.nome
            listanomimusei.append(nome)
        ordinata = sorted(listanomimusei)
        ordinata.append("Nessun filtro")
        return ordinata
