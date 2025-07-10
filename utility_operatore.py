import tkinter as tk
from tkinter import ttk
import math

# Palette colori
BG_COLOR = "#BABABA"
FRAME_COLOR = "#A0A0A0"
PRIMARY_COLOR = "#000000"
BUTTON_COLOR = "#4BA485"
BUTTON_TEXT = "#ffffff"
TITLE_COLOR = "#000000"
ERROR_COLOR = "#d32f2f"
RESULT_COLOR = "#000000"
FONT = ("Segoe UI", 14)
TITLE_FONT = ("Segoe UI", 25, "bold")
SUBTITLE_FONT = ("Segoe UI", 14, "bold")
FOOTER_FONT = ("Segoe UI", 12, "italic")

class UtilityOperatoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility Operatore")
        self.root.geometry("900x500")
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
        style.map('TButton', background=[('active', PRIMARY_COLOR)], foreground=[('active', BUTTON_TEXT)])

        # Titolo
        ttk.Label(root, text="Utility Operatore", style='Title.TLabel').pack(pady=(18, 2))
        ttk.Label(root, text="Scegli un'opzione:", style='Subtitle.TLabel').pack(pady=(0, 10))

        # Frame principale
        main_frame = ttk.Frame(root, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=18, pady=10)

        # Menu laterale
        menu_frame = ttk.Frame(main_frame, style='Menu.TFrame')
        menu_frame.pack(side='left', fill='y', padx=(0, 25), pady=10)

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
        ]
        for i, (text, func) in enumerate(self.options):
            ttk.Button(menu_frame, text=text, command=func, width=38, style='TButton').pack(pady=6)

        # Footer
        ttk.Label(root, text="Nuovo Pignone", style='Footer.TLabel').pack(side='bottom', pady=8)

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
        ttk.Label(self.dynamic_frame, text="Calcola velocità di taglio", style='Subtitle.TLabel').pack(pady=8)
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
        ttk.Label(self.dynamic_frame, text="Calcola avanzamento al tagliente", style='Subtitle.TLabel').pack(pady=8)
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


def main():
    root = tk.Tk()
    app = UtilityOperatoreApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
