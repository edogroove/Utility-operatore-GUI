import tkinter as tk
from tkinter import ttk
import math

class UtilityOperatoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility Operatore v1.3")
        self.root.geometry("900x500")
        self.root.resizable(True, True)
        style = ttk.Style()
        style.theme_use('clam')

        # Titolo
        ttk.Label(root, text="Utility Operatore v1.3", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(root, text="Scegli un'opzione:", font=("Arial", 12)).pack(pady=5)

        # Frame principale
        main_frame = ttk.Frame(root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Menu laterale
        menu_frame = ttk.Frame(main_frame)
        menu_frame.pack(side='left', fill='y', padx=(0, 15))

        # Area dinamica
        self.dynamic_frame = ttk.Frame(main_frame)
        self.dynamic_frame.pack(side='left', fill='both', expand=True)

        self.options = [
            ("1. Ottieni velocità di taglio vt (m/min)", self.vt_ui),
            ("2. Ottieni avanzamento al tagliente fz (mm/giro)", self.av_ui),
            ("3. Calcola n giri S (giri/min)", self.ss_ui),
            ("4. Calcola avanzamento F (mm/giro)", self.calc_av_ui),
            ("5. Ricava tutti i parametri", self.calc_tutto_ui),
            ("6. Calcolo distanza del golfare di riferimento", self.calc_golf_ui),
        ]
        for i, (text, func) in enumerate(self.options):
            ttk.Button(menu_frame, text=text, command=func, width=32).pack(pady=3)

        # Footer
        ttk.Label(root, text="By Edoardo Nanni", font=("Arial", 9, "italic")).pack(side='bottom', pady=5)

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
        ttk.Label(self.dynamic_frame, text="Calcola velocità di taglio vt", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        ttk.Label(form, text="Diametro (mm):").grid(row=0, column=0, sticky='e', pady=3)
        diam_entry = ttk.Entry(form)
        diam_entry.grid(row=0, column=1, pady=3)
        ttk.Label(form, text="Giri S:").grid(row=1, column=0, sticky='e', pady=3)
        giri_entry = ttk.Entry(form)
        giri_entry.grid(row=1, column=1, pady=3)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)

    def av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola avanzamento al tagliente fz", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        ttk.Label(form, text="Avanzamento F:").grid(row=0, column=0, sticky='e', pady=3)
        f_entry = ttk.Entry(form)
        f_entry.grid(row=0, column=1, pady=3)
        ttk.Label(form, text="Giri S:").grid(row=1, column=0, sticky='e', pady=3)
        s_entry = ttk.Entry(form)
        s_entry.grid(row=1, column=1, pady=3)
        ttk.Label(form, text="Numero dei taglienti:").grid(row=2, column=0, sticky='e', pady=3)
        t_entry = ttk.Entry(form)
        t_entry.grid(row=2, column=1, pady=3)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)

    def ss_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola n giri S", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        ttk.Label(form, text="Diametro (mm):").grid(row=0, column=0, sticky='e', pady=3)
        diam_entry = ttk.Entry(form)
        diam_entry.grid(row=0, column=1, pady=3)
        ttk.Label(form, text="Velocità di taglio vt (m/min):").grid(row=1, column=0, sticky='e', pady=3)
        vt_entry = ttk.Entry(form)
        vt_entry.grid(row=1, column=1, pady=3)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)

    def calc_av_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcola avanzamento F", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        ttk.Label(form, text="Giri (S):").grid(row=0, column=0, sticky='e', pady=3)
        giri_entry = ttk.Entry(form)
        giri_entry.grid(row=0, column=1, pady=3)
        ttk.Label(form, text="Avanzamento mm/giro:").grid(row=1, column=0, sticky='e', pady=3)
        av_entry = ttk.Entry(form)
        av_entry.grid(row=1, column=1, pady=3)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)

    def calc_tutto_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Ricava tutti i parametri", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        labels = [
            "Velocità di taglio desiderata (vt, m/min):",
            "Avanzamento a tagliente desiderato (fz, mm/giro):",
            "Numero dei taglienti:",
            "Diametro (mm):"
        ]
        entries = []
        for i, text in enumerate(labels):
            ttk.Label(form, text=text).grid(row=i, column=0, sticky='e', pady=3)
            e = ttk.Entry(form)
            e.grid(row=i, column=1, pady=3)
            entries.append(e)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)

    def calc_golf_ui(self):
        self.clear_dynamic()
        ttk.Label(self.dynamic_frame, text="Calcolo distanza golfare", font=("Arial", 13, "bold")).pack(pady=5)
        form = ttk.Frame(self.dynamic_frame)
        form.pack(pady=10)
        ttk.Label(form, text="Diametro (mm):").grid(row=0, column=0, sticky='e', pady=3)
        diam_entry = ttk.Entry(form)
        diam_entry.grid(row=0, column=1, pady=3)
        ttk.Label(form, text="Gradi:").grid(row=1, column=0, sticky='e', pady=3)
        gradi_entry = ttk.Entry(form)
        gradi_entry.grid(row=1, column=1, pady=3)
        result_label = ttk.Label(self.dynamic_frame, text="", font=("Arial", 11))
        result_label.pack(pady=8)
        self.error_label = ttk.Label(self.dynamic_frame, text="", foreground="red")
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
        ttk.Button(self.dynamic_frame, text="Calcola", command=calcola).pack(pady=5)


def main():
    root = tk.Tk()
    app = UtilityOperatoreApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
