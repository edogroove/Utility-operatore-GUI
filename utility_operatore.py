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
        style.configure('Main.TFrame', background=FRAME_COLOR)
        style.configure('Menu.TFrame', background=BG_COLOR)
        style.configure('TLabel', background=BG_COLOR, font=FONT)
        style.configure('Title.TLabel', background=BG_COLOR, foreground=TITLE_COLOR, font=TITLE_FONT)
        style.configure('Subtitle.TLabel', background=BG_COLOR, foreground=PRIMARY_COLOR, font=SUBTITLE_FONT)
        style.configure('Result.TLabel', background=BG_COLOR, foreground=RESULT_COLOR, font=FONT)
        style.configure('Error.TLabel', background=BG_COLOR, foreground=ERROR_COLOR, font=FONT)
        style.configure('Footer.TLabel', background=BG_COLOR, font=FOOTER_FONT)
        style.configure('TButton', font=FONT, padding=6, background=BUTTON_COLOR, foreground=BUTTON_TEXT)

        ttk.Label(root, text="Utility Operatore", style='Title.TLabel').pack(pady=(18, 2))
        ttk.Label(root, text="Scegli un'opzione:", style='Subtitle.TLabel').pack(pady=(0, 10))

        main_frame = ttk.Frame(root, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=18, pady=10)

        menu_frame = ttk.Frame(main_frame, style='Menu.TFrame')
        menu_frame.pack(side='left', fill='y', padx=(0, 25))

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

        for text, func in self.options:
            ttk.Button(menu_frame, text=text, command=func, width=39).pack(pady=6)

        ttk.Label(root, text="(V1.1)", style='Footer.TLabel').pack(side='bottom', pady=8)

        self.vt_ui()

    # ---------- UTIL ----------

    def clear_dynamic(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def show_error(self, msg):
        self.error_label.config(text=msg)

    def clear_error(self):
        self.error_label.config(text="")

    # 👉 bind invio su più entry
    def bind_enter(self, entries, func):
        for e in entries:
            e.bind("<Return>", lambda event: func())

    # ---------- UI ----------

    def vt_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ottieni velocità di taglio", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        ttk.Label(form, text="Diametro utensile (mm):").grid(row=0, column=0, sticky='e')
        diam_entry = ttk.Entry(form, font=FONT)
        diam_entry.grid(row=0, column=1)

        ttk.Label(form, text="Giri (S):").grid(row=1, column=0, sticky='e')
        giri_entry = ttk.Entry(form, font=FONT)
        giri_entry.grid(row=1, column=1)

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
            except:
                self.show_error("Inserisci tutti i valori correttamente.")

        self.bind_enter([diam_entry, giri_entry], calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)

    def av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ottieni avanzamento al tagliente", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        f_entry = ttk.Entry(form, font=FONT)
        s_entry = ttk.Entry(form, font=FONT)
        t_entry = ttk.Entry(form, font=FONT)

        ttk.Label(form, text="Avanzamento (F):").grid(row=0, column=0)
        f_entry.grid(row=0, column=1)

        ttk.Label(form, text="Giri (S):").grid(row=1, column=0)
        s_entry.grid(row=1, column=1)

        ttk.Label(form, text="Numero taglienti:").grid(row=2, column=0)
        t_entry.grid(row=2, column=1)
        t_entry.insert(0, "1")

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
                result_label.config(text=f"fz = {ris:.3f}")
            except:
                self.show_error("Inserisci tutti i valori correttamente.")

        self.bind_enter([f_entry, s_entry, t_entry], calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)

    def ss_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola giri S", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        diam_entry = ttk.Entry(form, font=FONT)
        vt_entry = ttk.Entry(form, font=FONT)

        ttk.Label(form, text="Diametro (mm):").grid(row=0, column=0)
        diam_entry.grid(row=0, column=1)

        ttk.Label(form, text="Vt (m/min):").grid(row=1, column=0)
        vt_entry.grid(row=1, column=1)

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
                result_label.config(text=f"S = {ris:.2f}")
            except:
                self.show_error("Inserisci tutti i valori correttamente.")

        self.bind_enter([diam_entry, vt_entry], calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)

    def calc_av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola avanzamento F", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        giri_entry = ttk.Entry(form, font=FONT)
        av_entry = ttk.Entry(form, font=FONT)

        ttk.Label(form, text="Giri (S):").grid(row=0, column=0)
        giri_entry.grid(row=0, column=1)

        ttk.Label(form, text="Avanzamento (mm/giro):").grid(row=1, column=0)
        av_entry.grid(row=1, column=1)

        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)

        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()

        def calcola():
            self.clear_error()
            try:
                ris = float(giri_entry.get()) * float(av_entry.get())
                result_label.config(text=f"F = {ris:.2f}")
            except:
                self.show_error("Inserisci tutti i valori correttamente.")

        self.bind_enter([giri_entry, av_entry], calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)

    def calc_tutto_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ricava tutti i parametri", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        entries = [ttk.Entry(form, font=FONT) for _ in range(4)]

        labels = ["Velocità di taglio vt:", "Avanzamento al tagliente fz:", "Numero taglienti:", "Diametro:"]

        for i, (lab, ent) in enumerate(zip(labels, entries)):
            ttk.Label(form, text=lab).grid(row=i, column=0)
            ent.grid(row=i, column=1)

        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)

        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()

        def calcola():
            self.clear_error()
            try:
                vt, fz, tagl, diam = [float(e.get()) for e in entries]
                s = vt * 1000 / (diam * math.pi)
                f = fz * tagl * s
                result_label.config(text=f"S = {s:.2f}\nF = {f:.2f}")
            except:
                self.show_error("Errore input.")

        self.bind_enter(entries, calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)

    def calc_golf_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcolo golfare", style='Subtitle.TLabel').pack(pady=8)

        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=16)

        diam_entry = ttk.Entry(form, font=FONT)
        gradi_entry = ttk.Entry(form, font=FONT)

        ttk.Label(form, text="Diametro:").grid(row=0, column=0)
        diam_entry.grid(row=0, column=1)

        ttk.Label(form, text="Gradi:").grid(row=1, column=0)
        gradi_entry.grid(row=1, column=1)

        result_label = ttk.Label(self.dynamic_frame, text="", style='Result.TLabel')
        result_label.pack(pady=10)

        self.error_label = ttk.Label(self.dynamic_frame, text="", style='Error.TLabel')
        self.error_label.pack()

        def calcola():
            self.clear_error()
            try:
                ris = float(diam_entry.get()) * math.pi / 360 * float(gradi_entry.get())
                result_label.config(text=f"Distanza: {ris:.1f} mm")
            except:
                self.show_error("Errore input.")

        self.bind_enter([diam_entry, gradi_entry], calcola)
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=8)


def main():
    root = tk.Tk()
    UtilityOperatoreApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
