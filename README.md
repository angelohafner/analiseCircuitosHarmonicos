
# Impedance Calculation and Harmonic Analysis

This project contains Python code to calculate the impedances of various circuit elements (resistor, inductor, capacitor) and their parallel combination. It also includes functions to plot impedance and harmonic voltage/current analysis for a given set of frequencies.

## Project Files

1. **main.py**: The main script to run impedance calculations and harmonic analysis for a range of frequencies. This file also generates plots for impedance and harmonic analysis.
   
   - Example usage:
     ```python
     frequencias = np.arange(60, 601, 60)
     impedancia_transformador, impedancia_filtro, impedancia_paralelo = calcular_impedancias(frequencias)
     plotar_impedancias(frequencias, impedancia_transformador, impedancia_filtro, impedancia_paralelo)
     ```

2. **calculo_impedancias.py**: Contains functions to calculate impedances for a transformer and an RLC filter at different frequencies, as well as plot the results.

   - Functions:
     - `calcular_impedancias(frequencias)`: Calculates impedances of the transformer, RLC filter, and their parallel combination.
     - `plotar_impedancias(frequencias, impedancia_transformador, impedancia_filtro, impedancia_paralelo)`: Plots the magnitude and phase of the impedances over the frequency range.
     - `plotar_tensao_corrente_harmonicas(frequencias, tensoes_harmonicas, correntes_harmonicas)`: Plots the harmonic voltages and currents.

3. **impedancia.py**: Defines the `Impedancia` class with methods to compute the total impedance for different components (R, L, C) and for parallel combinations.

   - Class `Impedancia`:
     - `impedancia_resistor()`: Calculates the impedance of a resistor.
     - `impedancia_indutor()`: Calculates the impedance of an inductor.
     - `impedancia_capacitor()`: Calculates the impedance of a capacitor.
     - `impedancia_total()`: Computes the total impedance (R, L, C in series).
     - `associar_paralelo(impedancias)`: Computes the parallel combination of impedances.

## Usage

To run the project, ensure all the files are in the same directory. You can execute the `main.py` script, which will perform impedance calculations for a range of harmonic frequencies and generate the respective plots.

```bash
python main.py
```

### Dependencies

- NumPy
- Plotly

Install the required libraries using pip:

```bash
pip install numpy plotly
```

## Results

- **Impedance vs Frequency**: Plots showing the magnitude and angle of the impedance for each component (transformer, RLC filter) and their parallel combination over the frequency range.
- **Harmonic Voltages and Currents**: Bar plots showing the magnitude of the harmonic voltages and currents for a set of frequencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to [Gustavo](https://github.com/gustavo) for the idea and initial implementation.
