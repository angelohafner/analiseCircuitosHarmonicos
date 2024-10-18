import numpy as np
import plotly.graph_objects as go
from impedancia import Impedancia  # Certifique-se de que o arquivo impedancia.py está no mesmo diretório


# Função para calcular as impedâncias
def calcular_impedancias(frequencias):
    # Criar os objetos para o transformador e o filtro RLC (independente da frequência)
    transformador = Impedancia(R=3.28e-3, L=3.21e-3)  # Trafo: R=3.28mOhms, L=3.21mH
    filtro_RLC = Impedancia(R=1.27, L=34.3e-3, C=8.54e-6)  # Filtro RLC: R=1.27Ohms, L=34.3mH, C=8.54uF

    # Listas para armazenar os resultados
    impedancia_transformador = []
    impedancia_filtro = []
    impedancia_paralelo = []

    # Loop sobre as frequências para calcular as impedâncias
    for f in frequencias:
        # Atualizar a frequência nos objetos de impedância
        transformador.atualizar_frequencia(f)
        filtro_RLC.atualizar_frequencia(f)

        # Calculando as impedâncias totais
        Z_transformador = transformador.impedancia_total()
        Z_filtro = filtro_RLC.impedancia_total()

        # Impedância equivalente em paralelo
        Z_paralelo = Impedancia.associar_paralelo([Z_transformador, Z_filtro])

        # Armazenando as impedâncias na forma complexa
        impedancia_transformador.append(Z_transformador)
        impedancia_filtro.append(Z_filtro)
        impedancia_paralelo.append(Z_paralelo)

    return impedancia_transformador, impedancia_filtro, impedancia_paralelo



def plotar_impedancias(frequencias, impedancia_transformador, impedancia_filtro, impedancia_paralelo):
    """
    Plota os módulos e ângulos das impedâncias recebidas na forma complexa.

    Args:
    frequencias (np.array): Array de frequências.
    impedancia_transformador (list or np.array): Impedância complexa do transformador.
    impedancia_filtro (list or np.array): Impedância complexa do filtro RLC.
    impedancia_paralelo (list or np.array): Impedância complexa equivalente (paralelo do transformador e filtro).
    """

    # Calcular módulos
    modulo_transformador = np.abs(impedancia_transformador)
    modulo_filtro = np.abs(impedancia_filtro)
    modulo_paralelo = np.abs(impedancia_paralelo)

    # Calcular ângulos (em graus)
    angulo_transformador = np.angle(impedancia_transformador, deg=True)
    angulo_filtro = np.angle(impedancia_filtro, deg=True)
    angulo_paralelo = np.angle(impedancia_paralelo, deg=True)

    # Gráfico do módulo das impedâncias
    fig_modulo = go.Figure()

    # Módulo da impedância do transformador
    fig_modulo.add_trace(go.Scatter(x=frequencias, y=modulo_transformador, mode='lines', name='Transformador'))

    # Módulo da impedância do filtro
    fig_modulo.add_trace(go.Scatter(x=frequencias, y=modulo_filtro, mode='lines', name='Filtro RLC'))

    # Módulo da impedância equivalente (paralelo)
    fig_modulo.add_trace(
        go.Scatter(x=frequencias, y=modulo_paralelo, mode='lines', name='Paralelo Transformador + Filtro'))

    # Configurações do gráfico de módulo
    fig_modulo.update_layout(
        title="Módulo das Impedâncias vs Frequência",
        xaxis_title="Frequência (Hz)",
        yaxis_title="Módulo da Impedância (Ohms)",
        yaxis_type="log",  # Escala logarítmica no eixo Y
        template="plotly"
    )

    # Gráfico do ângulo das impedâncias
    fig_angulo = go.Figure()

    # Ângulo da impedância do transformador
    fig_angulo.add_trace(go.Scatter(x=frequencias, y=angulo_transformador, mode='lines', name='Transformador'))

    # Ângulo da impedância do filtro
    fig_angulo.add_trace(go.Scatter(x=frequencias, y=angulo_filtro, mode='lines', name='Filtro RLC'))

    # Ângulo da impedância equivalente (paralelo)
    fig_angulo.add_trace(
        go.Scatter(x=frequencias, y=angulo_paralelo, mode='lines', name='Paralelo Transformador + Filtro'))

    # Configurações do gráfico de ângulo
    fig_angulo.update_layout(
        title="Ângulo das Impedâncias vs Frequência",
        xaxis_title="Frequência (Hz)",
        yaxis_title="Ângulo da Impedância (Graus)",
        template="plotly"
    )

    # Exibir os gráficos
    fig_modulo.show()
    fig_angulo.show()


def plotar_tensao_corrente_harmonicas(frequencias, tensoes_harmonicas, correntes_harmonicas):
    """
    Função para plotar o módulo das tensões e correntes harmônicas como gráficos de barras
    em função da frequência.

    Args:
        frequencias (np.array): Array de frequências harmônicas.
        tensoes_harmonicas (np.array): Array de tensões harmônicas (complexas).
        correntes_harmonicas (np.array): Array de correntes harmônicas (complexas).
    """
    # Calcular os módulos (magnitudes) das tensões e correntes
    modulo_tensoes = np.abs(tensoes_harmonicas)
    modulo_correntes = np.abs(correntes_harmonicas)

    # Criar a figura Plotly
    fig = go.Figure()

    # Adicionar o trace das tensões como barras
    fig.add_trace(go.Bar(x=frequencias, y=modulo_tensoes, name='Tensão (V)'))

    # Adicionar o trace das correntes como barras
    fig.add_trace(go.Bar(x=frequencias, y=modulo_correntes, name='Corrente (A)'))

    # Configurar layout com apenas um eixo Y (primário)
    fig.update_layout(
        title="Tensões e Correntes Harmônicas vs Frequência (Gráfico de Barras)",
        xaxis_title="Frequência (Hz)",
        yaxis_title="Magnitude (V/A)",  # Um único eixo Y para ambos
        yaxis_type="linear",  # Escala logarítmica no eixo Y
        template="plotly",
        barmode='group'  # Exibe as barras lado a lado
    )

    # Exibir o gráfico
    fig.show()