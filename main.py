import numpy as np
from calculo_impedancias import calcular_impedancias, plotar_impedancias, plotar_tensao_corrente_harmonicas

FREQ_FUND = 60
TENSAO_BASE = 34.5E3
POTENCIA_BASE = 60E6
IMPEDANCIA_BASE = TENSAO_BASE**2 / POTENCIA_BASE
CORRENTE_BASE = POTENCIA_BASE / (np.sqrt(3) * TENSAO_BASE)

# %% Para calcular as tensões em vários harmônicos
frequencias = np.arange(FREQ_FUND, 10 * FREQ_FUND + 1, FREQ_FUND)
impedancia_transformador, impedancia_filtro, impedancia_paralelo = calcular_impedancias(frequencias)
correntes_harmonicas = np.ones_like(frequencias, dtype=np.complex128)
tensoes_harmonicas = impedancia_paralelo * correntes_harmonicas

plotar_impedancias(frequencias, impedancia_transformador, impedancia_filtro, impedancia_paralelo)
plotar_tensao_corrente_harmonicas(frequencias, tensoes_harmonicas, correntes_harmonicas)

