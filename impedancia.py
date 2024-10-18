import numpy as np

# Frequências de 60Hz a 3000Hz
frequencias = np.linspace(60, 3000, 500)


# Definindo a classe Impedancia
class Impedancia:
    def __init__(self, R=None, L=None, C=None, f=60):
        self.R = R  # Resistência
        self.L = L  # Indutância
        self.C = C  # Capacitância
        self.f = f  # Frequência em Hertz

    def atualizar_frequencia(self, f):
        """Atualiza a frequência do objeto."""
        self.f = f

    # Método para calcular a impedância de um resistor
    def impedancia_resistor(self):
        if self.R is None:
            return 0
        return self.R

    # Método para calcular a impedância de um indutor
    def impedancia_indutor(self):
        if self.L is None:
            return 0
        w = 2 * np.pi * self.f  # Frequência angular
        return 1j * w * self.L

    # Método para calcular a impedância de um capacitor
    def impedancia_capacitor(self):
        if self.C is None:
            return 0
        w = 2 * np.pi * self.f
        return 1 / (1j * w * self.C)

    # Método para calcular a impedância total da instância atual (série R, L, C)
    def impedancia_total(self):
        Z_R = self.impedancia_resistor()
        Z_L = self.impedancia_indutor()
        Z_C = self.impedancia_capacitor()
        return Z_R + Z_L + Z_C

    # Método para associar impedâncias em paralelo
    @staticmethod
    def associar_paralelo(impedancias):
        inv_impedancias = [1 / Z for Z in impedancias if Z != 0]
        return 1 / sum(inv_impedancias)


