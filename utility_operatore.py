import tkinter as tk
from tkinter import ttk
import math

# Palette colori
BG_COLOR = "#A0A0A0"
FRAME_COLOR = "#A0A0A0"
PRIMARY_COLOR = "#000000"
BUTTON_COLOR = "#4BA485"
BUTTON_TEXT = "#ffffff"
TITLE_COLOR = "#000000"
ERROR_COLOR = "#d32f2f"
RESULT_COLOR = "#000000"
FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI", 22, "bold")
SUBTITLE_FONT = ("Segoe UI", 14, "bold")
FOOTER_FONT = ("Segoe UI", 12, "italic")

class UtilityOperatoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility Operatore")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.configure(bg=BG_COLOR)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=BG_COLOR)
        style.configure('Main.TFrame', background=FRAME_COLOR, relief="flat", borderwidth=1)
        style.configure('Menu.TFrame', background=BG_COLOR)
        style.configure('TLabel', background=BG_COLOR, font=FONT)
        style.configure('Title.TLabel', background=BG_COLOR, foreground=TITLE_COLOR, font=TITLE_FONT)
        style.configure('Subtitle.TLabel', background=BG_COLOR, foreground=PRIMARY_COLOR, font=SUBTITLE_FONT)
        style.configure('Result.TLabel', background=BG_COLOR, foreground=RESULT_COLOR, font=FONT)
        style.configure('Error.TLabel', background=BG_COLOR, foreground=ERROR_COLOR, font=FONT)
        style.configure('Footer.TLabel', background=BG_COLOR, font=FOOTER_FONT)
        style.configure('TButton', font=FONT, padding=6, background=BUTTON_COLOR, foreground=BUTTON_TEXT)
        style.map('TButton', background=[('active', "#459A7D")], foreground=[('active', BUTTON_TEXT)])

        # Titolo
        ttk.Label(root, text="Utility Operatore", style='Title.TLabel').pack(pady=(18, 2))
        ttk.Label(root, text="Scegli un'opzione:", style='Subtitle.TLabel').pack(pady=(0, 10))

        # Frame principale
        main_frame = ttk.Frame(root, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=18, pady=10)

        # Menu laterale
        menu_frame = ttk.Frame(main_frame, style='Menu.TFrame')
        menu_frame.pack(side='left', fill='y', padx=(0, 25), pady=0)

        # Area dinamica
        self.dynamic_frame = ttk.Frame(main_frame, style='Main.TFrame')
        self.dynamic_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.options = [
            ("Ottieni velocità di taglio vt (m/min)", self.vt_ui),
            ("Ottieni avanzamento al tagliente fz (mm/giro)", self.av_ui),
            ("Calcola n giri S (giri/min)", self.ss_ui),
            ("Calcola avanzamento F (mm/giro)", self.calc_av_ui),
            ("Ricava tutti i parametri", self.calc_tutto_ui),
            ("Calcolo distanza del golfare di riferimento", self.calc_golf_ui),
            ("Tolleranze dimensionali ISO", self.tolleranze_ui),
        ]
        for i, (text, func) in enumerate(self.options):
            ttk.Button(menu_frame, text=text, command=func, width=39, style='TButton').pack(pady=6)

        # Footer
        ttk.Label(root, text="Nuovo Pignone (V1.0)", style='Footer.TLabel').pack(side='bottom', pady=8)

        # Mostra la prima opzione di default
        self.vt_ui()

    def clear_dynamic(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def show_error(self, msg):
        self.error_label.config(text=msg)

    def clear_error(self):
        self.error_label.config(text="")

    def vt_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ottieni velocità di taglio", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        ttk.Label(form, text="Diametro utensile (mm):", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        diam_entry = ttk.Entry(form, font=FONT)
        diam_entry.grid(row=0, column=1, pady=6, padx=4)
        ttk.Label(form, text="Giri S:", style='TLabel').grid(row=1, column=0, sticky='e', pady=6, padx=4)
        giri_entry = ttk.Entry(form, font=FONT)
        giri_entry.grid(row=1, column=1, pady=6, padx=4)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                diam = float(diam_entry.get())
                giri = float(giri_entry.get())
                ris = giri * (diam * math.pi) / 1000
                result_label.config(text=f"vt = {ris:.2f} m/min")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ottieni avanzamento al tagliente", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        ttk.Label(form, text="Avanzamento F:", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        f_entry = ttk.Entry(form, font=FONT)
        f_entry.grid(row=0, column=1, pady=6, padx=4)
        ttk.Label(form, text="Giri S:", style='TLabel').grid(row=1, column=0, sticky='e', pady=6, padx=4)
        s_entry = ttk.Entry(form, font=FONT)
        s_entry.grid(row=1, column=1, pady=6, padx=4)
        ttk.Label(form, text="Numero dei taglienti:", style='TLabel').grid(row=2, column=0, sticky='e', pady=6, padx=4)
        t_entry = ttk.Entry(form, font=FONT)
        t_entry.insert(0, "1")
        t_entry.grid(row=2, column=1, pady=6, padx=4)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                f = float(f_entry.get())
                s = float(s_entry.get())
                t = float(t_entry.get())
                ris = (f / s) / t
                result_label.config(text=f"fz = {ris:.3f} mm/giro per tagliente")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def ss_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola n giri S", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        ttk.Label(form, text="Diametro (mm):", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        diam_entry = ttk.Entry(form, font=FONT)
        diam_entry.grid(row=0, column=1, pady=6, padx=4)
        ttk.Label(form, text="Velocità di taglio vt (m/min):", style='TLabel').grid(row=1, column=0, sticky='e', pady=6, padx=4)
        vt_entry = ttk.Entry(form, font=FONT)
        vt_entry.grid(row=1, column=1, pady=6, padx=4)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                diam = float(diam_entry.get())
                vt = float(vt_entry.get())
                ris = vt * 1000 / (diam * math.pi)
                result_label.config(text=f"S = {ris:.2f} giri/min")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def calc_av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola avanzamento F", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        ttk.Label(form, text="Giri (S):", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        giri_entry = ttk.Entry(form, font=FONT)
        giri_entry.grid(row=0, column=1, pady=6, padx=4)
        ttk.Label(form, text="Avanzamento mm/giro:", style='TLabel').grid(row=1, column=0, sticky='e', pady=6, padx=4)
        av_entry = ttk.Entry(form, font=FONT)
        av_entry.grid(row=1, column=1, pady=6, padx=4)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                giri = float(giri_entry.get())
                av = float(av_entry.get())
                ris = giri * av
                result_label.config(text=f"F = {ris:.2f}")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def calc_tutto_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ricava tutti i parametri", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        labels = [
            "Velocità di taglio desiderata (vt, m/min):",
            "Avanzamento a tagliente desiderato (fz, mm/giro):",
            "Numero dei taglienti:",
            "Diametro (mm):"
        ]
        entries = []
        for i, text in enumerate(labels):
            ttk.Label(form, text=text, style='TLabel').grid(row=i, column=0, sticky='e', pady=6, padx=4)
            e = ttk.Entry(form, font=FONT)
            e.grid(row=i, column=1, pady=6, padx=4)
            entries.append(e)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                vt = float(entries[0].get())
                fz = float(entries[1].get())
                tagl = float(entries[2].get())
                diam = float(entries[3].get())
                s = vt * 1000 / (diam * math.pi)
                f = fz * tagl * s
                result_label.config(text=f"Giri S: {s:.2f}\nAvanzamento F: {f:.2f}")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def calc_golf_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcolo distanza golfare", style='Subtitle.TLabel').pack(pady=8)
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        ttk.Label(form, text="Diametro (mm):", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        diam_entry = ttk.Entry(form, font=FONT)
        diam_entry.grid(row=0, column=1, pady=6, padx=4)
        ttk.Label(form, text="Gradi:", style='TLabel').grid(row=1, column=0, sticky='e', pady=6, padx=4)
        gradi_entry = ttk.Entry(form, font=FONT)
        gradi_entry.grid(row=1, column=1, pady=6, padx=4)
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        def calcola():
            self.clear_error()
            try:
                diam = float(diam_entry.get())
                gradi = float(gradi_entry.get())
                ris = diam * math.pi / 360 * gradi
                result_label.config(text=f"Distanza dal golfare: {ris:.1f} mm")
            except Exception:
                self.show_error("Inserisci tutti i valori correttamente.")
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola, style='TButton').pack(pady=8)

    def tolleranze_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Tolleranze dimensionali ISO", style='Subtitle.TLabel').pack(pady=8)
        
        # Dizionario delle deviazioni fondamentali ISO (in micrometri)
        # Per i fori (maiuscole): deviazione INFERIORE
        # Per gli alberi (minuscole): deviazione SUPERIORE
        self.tolleranze_data = {
            # Fori (maiuscole) - deviazione INFERIORE
            'A': {3: 270, 6: 280, 10: 290, 18: 300, 30: 310, 50: 330, 80: 360, 120: 400, 180: 460, 250: 520, 315: 580, 400: 660, 500: 760},
            'B': {3: 140, 6: 150, 10: 160, 18: 170, 30: 180, 50: 200, 80: 230, 120: 270, 180: 330, 250: 390, 315: 450, 400: 530, 500: 630},
            'C': {3: 60, 6: 70, 10: 80, 18: 90, 30: 100, 50: 120, 80: 150, 120: 190, 180: 250, 250: 310, 315: 370, 400: 450, 500: 550},
            'D': {3: 20, 6: 30, 10: 40, 18: 50, 30: 60, 50: 80, 80: 110, 120: 150, 180: 210, 250: 270, 315: 330, 400: 410, 500: 510},
            'E': {3: 14, 6: 20, 10: 25, 18: 32, 30: 40, 50: 50, 80: 63, 120: 80, 180: 100, 250: 125, 315: 160, 400: 200, 500: 250},
            'F': {3: 6, 6: 10, 10: 13, 18: 16, 30: 20, 50: 25, 80: 32, 120: 40, 180: 50, 250: 63, 315: 80, 400: 100, 500: 125},
            'G': {3: 2, 6: 4, 10: 5, 18: 6, 30: 7, 50: 9, 80: 10, 120: 12, 180: 14, 250: 16, 315: 18, 400: 20, 500: 25},
            'H': {3: 0, 6: 0, 10: 0, 18: 0, 30: 0, 50: 0, 80: 0, 120: 0, 180: 0, 250: 0, 315: 0, 400: 0, 500: 0},
            # Alberi (minuscole) - deviazione SUPERIORE (negative per essere sotto il nominale)
            'a': {3: -270, 6: -280, 10: -290, 18: -300, 30: -310, 50: -330, 80: -360, 120: -400, 180: -460, 250: -520, 315: -580, 400: -660, 500: -760},
            'b': {3: -140, 6: -150, 10: -160, 18: -170, 30: -180, 50: -200, 80: -230, 120: -270, 180: -330, 250: -390, 315: -450, 400: -530, 500: -630},
            'c': {3: -60, 6: -70, 10: -80, 18: -90, 30: -100, 50: -120, 80: -150, 120: -190, 180: -250, 250: -310, 315: -370, 400: -450, 500: -550},
            'd': {3: -20, 6: -30, 10: -40, 18: -50, 30: -60, 50: -80, 80: -110, 120: -150, 180: -210, 250: -270, 315: -330, 400: -410, 500: -510},
            'e': {3: -14, 6: -20, 10: -25, 18: -32, 30: -40, 50: -50, 80: -63, 120: -80, 180: -100, 250: -125, 315: -160, 400: -200, 500: -250},
            'f': {3: -6, 6: -10, 10: -13, 18: -16, 30: -20, 50: -25, 80: -32, 120: -40, 180: -50, 250: -63, 315: -80, 400: -100, 500: -125},
            'g': {3: -2, 6: -4, 10: -5, 18: -6, 30: -7, 50: -9, 80: -10, 120: -12, 180: -14, 250: -16, 315: -18, 400: -20, 500: -25},
            'h': {3: 0, 6: 0, 10: 0, 18: 0, 30: 0, 50: 0, 80: 0, 120: 0, 180: 0, 250: 0, 315: 0, 400: 0, 500: 0},
        }
        
        # Classi di tolleranza IT (in micrometri) - Valori corretti ISO 286
        self.it_grades = {
            1: {3: 0.8, 6: 1, 10: 1.2, 18: 1.5, 30: 1.5, 50: 2, 80: 2.5, 120: 3, 180: 4, 250: 5, 315: 6, 400: 7, 500: 8},
            2: {3: 1.2, 6: 1.5, 10: 1.8, 18: 2.2, 30: 2.2, 50: 3, 80: 3.5, 120: 4, 180: 5, 250: 6, 315: 7, 400: 8, 500: 9},
            3: {3: 2, 6: 2.5, 10: 3, 18: 3.5, 30: 3.5, 50: 4, 80: 5, 120: 6, 180: 7, 250: 8, 315: 9, 400: 10, 500: 11},
            4: {3: 3, 6: 4, 10: 5, 18: 6, 30: 6, 50: 7, 80: 8, 120: 10, 180: 12, 250: 14, 315: 16, 400: 18, 500: 20},
            5: {3: 4, 6: 5, 10: 6, 18: 8, 30: 8, 50: 9, 80: 11, 120: 13, 180: 15, 250: 17, 315: 19, 400: 21, 500: 23},
            6: {3: 6, 6: 8, 10: 9, 18: 11, 30: 11, 50: 13, 80: 16, 120: 19, 180: 22, 250: 25, 315: 28, 400: 31, 500: 34},
            7: {3: 10, 6: 12, 10: 15, 18: 18, 30: 21, 50: 25, 80: 30, 120: 35, 180: 40, 250: 46, 315: 52, 400: 57, 500: 63},
            8: {3: 14, 6: 18, 10: 22, 18: 27, 30: 33, 50: 39, 80: 46, 120: 54, 180: 63, 250: 72, 315: 81, 400: 89, 500: 97},
            9: {3: 25, 6: 30, 10: 36, 18: 43, 30: 52, 50: 62, 80: 74, 120: 87, 180: 100, 250: 115, 315: 130, 400: 140, 500: 155},
            10: {3: 40, 6: 48, 10: 58, 18: 70, 30: 84, 50: 100, 80: 120, 120: 140, 180: 160, 250: 185, 315: 210, 400: 230, 500: 250},
            11: {3: 60, 6: 75, 10: 90, 18: 110, 30: 130, 50: 160, 80: 190, 120: 220, 180: 250, 250: 290, 315: 320, 400: 360, 500: 400},
            12: {3: 100, 6: 120, 10: 150, 18: 180, 30: 210, 50: 250, 80: 300, 120: 350, 180: 400, 250: 460, 315: 520, 400: 570, 500: 630}
        }
        
        # Form
        form = ttk.Frame(self.dynamic_frame, style='Main.TFrame')
        form.pack(pady=16)
        
        # Campo diametro
        ttk.Label(form, text="Diametro nominale (mm):", style='TLabel').grid(row=0, column=0, sticky='e', pady=6, padx=4)
        diam_entry = ttk.Entry(form, font=FONT, width=12)
        diam_entry.grid(row=0, column=1, pady=6, padx=4)
        
        # Frame per selezione tipo
        tipo_frame = ttk.Frame(form, style='Main.TFrame')
        tipo_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Variabile per il tipo (foro/albero)
        self.tipo_var = tk.StringVar(value="foro")
        
        ttk.Radiobutton(tipo_frame, text="Foro (maiuscole)", variable=self.tipo_var, value="foro").pack(side='left', padx=10)
        ttk.Radiobutton(tipo_frame, text="Albero (minuscole)", variable=self.tipo_var, value="albero").pack(side='left', padx=10)
        
        # Frame per selezione tolleranza
        toll_frame = ttk.Frame(form, style='Main.TFrame')
        toll_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Label(toll_frame, text="Lettera:", style='TLabel').grid(row=0, column=0, pady=6, padx=4)
        
        # Combobox per lettera
        self.lettera_combo = ttk.Combobox(toll_frame, font=FONT, width=8, state="readonly")
        self.lettera_combo.grid(row=0, column=1, pady=6, padx=4)
        
        ttk.Label(toll_frame, text="Classe IT:", style='TLabel').grid(row=0, column=2, pady=6, padx=4)
        
        # Combobox per numero
        self.numero_combo = ttk.Combobox(toll_frame, font=FONT, width=8, state="readonly", 
                                        values=list(range(1, 13)))
        self.numero_combo.grid(row=0, column=3, pady=6, padx=4)
        
        # Funzione per aggiornare le lettere in base al tipo
        def aggiorna_lettere():
            if self.tipo_var.get() == "foro":
                lettere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            else:
                lettere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            self.lettera_combo['values'] = lettere
            if lettere:
                self.lettera_combo.current(7)  # Default H o h
        
        # Inizializza le lettere
        aggiorna_lettere()
        self.numero_combo.current(6)  # Default IT7
        
        # Collega il cambio tipo all'aggiornamento delle lettere
        self.tipo_var.trace('w', lambda *args: aggiorna_lettere())
        
        # Label per risultati
        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel', justify='left')
        result_label.pack(pady=10)
        
        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()
        
        def calcola_tolleranza():
            self.clear_error()
            try:
                diam_nominale = float(diam_entry.get())
                lettera = self.lettera_combo.get()
                it_class = int(self.numero_combo.get())
                
                if not lettera:
                    self.show_error("Seleziona una lettera di tolleranza.")
                    return
                
                # Trova il range di diametro appropriato
                range_diam = None
                for limite in sorted(self.tolleranze_data[lettera].keys()):
                    if diam_nominale <= limite:
                        range_diam = limite
                        break
                
                if range_diam is None:
                    self.show_error("Diametro fuori dai range supportati (max 500mm).")
                    return
                
                # Ottieni deviazione fondamentale e tolleranza IT
                deviazione_fond = self.tolleranze_data[lettera][range_diam]
                tolleranza_it = self.it_grades[it_class][range_diam]
                
                # Calcola i limiti secondo le norme ISO
                if lettera.isupper():  # Foro
                    # Per i fori: deviazione inferiore è quella fondamentale
                    # deviazione superiore = deviazione inferiore + IT
                    dev_inf = deviazione_fond  # deviazione inferiore
                    dev_sup = deviazione_fond + tolleranza_it  # deviazione superiore
                else:  # Albero
                    # Per gli alberi: deviazione superiore è quella fondamentale
                    # deviazione inferiore = deviazione superiore - IT
                    dev_sup = deviazione_fond  # deviazione superiore
                    dev_inf = deviazione_fond - tolleranza_it  # deviazione inferiore
                
                # Calcola le dimensioni reali
                dim_min = diam_nominale + dev_inf/1000
                dim_max = diam_nominale + dev_sup/1000
                
                tipo_text = "FORO" if lettera.isupper() else "ALBERO"
                result_text = f"""Tolleranza: Ø{diam_nominale:.0f} {lettera}{it_class} ({tipo_text})

Deviazione superiore: +{dev_sup/1000:.3f} mm ({dev_sup:+.0f} μm)
Deviazione inferiore: +{dev_inf/1000:.3f} mm ({dev_inf:+.0f} μm)
Tolleranza IT{it_class}: {tolleranza_it:.0f} μm

Dimensione massima: {dim_max:.3f} mm
Dimensione minima: {dim_min:.3f} mm"""
                
                result_label.config(text=result_text)
                
            except ValueError:
                self.show_error("Inserisci un diametro valido.")
            except Exception as e:
                self.show_error(f"Errore nel calcolo: {str(e)}")
        
        ttk.Button(self.dynamic_frame, text="Calcola Tolleranza", command=calcola_tolleranza, style='TButton').pack(pady=8)


def main():
    root = tk.Tk()
    app = UtilityOperatoreApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
