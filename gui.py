import tkinter as tk
from tkinter import ttk
from epimodeler import EpiModeler

class EpiModelerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EpiModeler")

        self.beta = tk.DoubleVar(value=0.3)
        self.gamma = tk.DoubleVar(value=0.1)
        self.S0 = tk.DoubleVar(value=0.99)
        self.I0 = tk.DoubleVar(value=0.01)
        self.R0 = tk.DoubleVar(value=0.0)
        self.days = tk.IntVar(value=160)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Beta:").grid(column=0, row=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.beta).grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(self.root, text="Gamma:").grid(column=0, row=1, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.gamma).grid(column=1, row=1, padx=5, pady=5)

        ttk.Label(self.root, text="Initial S:").grid(column=0, row=2, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.S0).grid(column=1, row=2, padx=5, pady=5)

        ttk.Label(self.root, text="Initial I:").grid(column=0, row=3, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.I0).grid(column=1, row=3, padx=5, pady=5)

        ttk.Label(self.root, text="Initial R:").grid(column=0, row=4, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.R0).grid(column=1, row=4, padx=5, pady=5)

        ttk.Label(self.root, text="Days:").grid(column=0, row=5, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.days).grid(column=1, row=5, padx=5, pady=5)

        ttk.Button(self.root, text="Run Simulation", command=self.run_simulation).grid(column=0, row=6, columnspan=2, padx=5, pady=5)

    def run_simulation(self):
        model = EpiModeler(beta=self.beta.get(), gamma=self.gamma.get(), S0=self.S0.get(), I0=self.I0.get(), R0=self.R0.get(), days=self.days.get())
        results = model.run()
        print(results)  # Replace with actual visualization code later

if __name__ == "__main__":
    root = tk.Tk()
    app = EpiModelerGUI(root)
    root.mainloop()
