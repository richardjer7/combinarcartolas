
import pandas as pd
import glob
import os
import re

# Diccionario para traducir meses en español
meses_es = {
    'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Ago': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12'
}

def procesar_cartola(path_archivo):
    xls = pd.ExcelFile(path_archivo)
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    df_filtrado = df.iloc[10:].reset_index(drop=True)
    columnas = df_filtrado.iloc[7]
    df_mov = df_filtrado.iloc[8:].copy()
    df_mov.columns = columnas
    df_mov = df_mov.reset_index(drop=True)

    # Extraer año desde el nombre del archivo
    nombre_archivo = os.path.basename(path_archivo)
    match = re.search(r'Cartola CuentaRUT (\d{4})\d{4}', nombre_archivo)
    anio_cartola = match.group(1) if match else '2025'

    # Armar fecha real con el año extraído
    df_mov['Fecha_str'] = df_mov['Fecha'].astype(str)
    for mes_es, mes_num in meses_es.items():
        df_mov['Fecha_str'] = df_mov['Fecha_str'].str.replace(mes_es, mes_num, regex=False)
    df_mov['Fecha'] = pd.to_datetime(df_mov['Fecha_str'] + f'/{anio_cartola}', format='%d/%m/%Y', errors='coerce')

    # Limpieza numérica
    df_mov['Abonos'] = pd.to_numeric(df_mov['Abonos'], errors='coerce')
    df_mov['Cargos'] = pd.to_numeric(df_mov['Cargos'], errors='coerce')
    df_mov['Saldo'] = df_mov['Saldo'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    df_mov['Saldo'] = pd.to_numeric(df_mov['Saldo'], errors='coerce')

    df_mov['Fuente'] = nombre_archivo
    return df_mov

# Leer todos los archivos .xlsx (excepto los temporales ~)
archivos = [f for f in glob.glob(r"C:\cartolas\*.xlsx") if not os.path.basename(f).startswith('~$')]
print(f"Se encontraron {len(archivos)} archivos para procesar.")

# Procesar y combinar
dfs = [procesar_cartola(f) for f in archivos]
df_total = pd.concat(dfs, ignore_index=True)

# Exportar resultado
df_total.to_csv("cartolas_combinadas.csv", index=False)
print("Cartolas combinadas guardadas en 'cartolas_combinadas.csv'")
