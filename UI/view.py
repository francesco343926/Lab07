import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self.scelta_museo= ft.Dropdown(label="Museo", options=[], width=200)
        self.scelta_epoca = ft.Dropdown(label="Epoca", options=[], width=200)
        self.controller.popola_musei()
        self.controller.popola_epoche()
        """Per popolare il menu a tendina tramite DropDown, occorre 
        aggiungere alla sua lista options oggetti di tipo ft.dropdown.Option. Ad esempio:
        self._view.elemento_dropdown.options.append(ft.dropdown.Option("Scelta 1"))`"""

        # Sezione 3: Artefatti
        # TODO
        self.pulsante_Artefatti= ft.ElevatedButton(text="Mostra Artefatti",
                                                   on_click= self.controller.trovArtefatto)
        self.artefatti_scelti = ft.ListView(auto_scroll=True)
        """Se nessun artefatto soddisfa i 
        criteri di filtraggio indicati, il sistema risponderà con un alert."""

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(controls=[self.scelta_museo, self.scelta_epoca], alignment= ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            # TODO
            ft.Row(controls= [self.pulsante_Artefatti], alignment= ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[self.artefatti_scelti], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider()

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
