import flet as ft
from UI.view import View
from model.model import Model


'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None



    # POPOLA DROPDOWN
    # TODO
    """chi chiama il popola dropdown?"""
    def popola_musei(self):
        listamusei= self._model.get_musei()
        for museo in listamusei:
            self._view.scelta_museo.options.append(ft.dropdown.Option(museo))

    def popola_epoche(self):
        lista_epoche= self._model.get_epoche()
        for epoca in lista_epoche:
            self._view.scelta_epoca.options.append(ft.dropdown.Option(epoca))

    # CALLBACKS DROPDOWN
    # TODO
    """punto in cui devi scrivere i
     metodi che gestiscono cosa succede quando l'utente sceglie un valore dai menu a tendina."""
    def trovArtefatto(self, e):
        self.museo_selezionato= self._view.scelta_museo.value
        self.epoca_selezionata= self._view.scelta_epoca.value
        listArtefattiFiltrati = self._model.get_artefatti_filtrati(self.museo_selezionato,
                                                    self.epoca_selezionata)
        for artefatto in listArtefattiFiltrati:
            self._view.artefatti_scelti.controls.append(ft.Text(artefatto))
        self._view.page.update()
        if listArtefattiFiltrati== []:
            self._view.alert.show_alert("non esiste")


    # AZIONE: MOSTRA ARTEFATTI
    # TODO

