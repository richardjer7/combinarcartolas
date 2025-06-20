# 🧾 Combinador de Cartolas BancoEstado (CuentaRUT)

Este script en Python permite **unir múltiples cartolas descargadas desde BancoEstado** en un solo archivo consolidado en formato CSV.

Es ideal para quienes desean revisar su historial de movimientos fácilmente, sin tener que abrir una por una las decenas (o cientos) de cartolas que entrega el banco.

---

## 📂 Requisitos

- Python 3.7 o superior
- Las cartolas deben estar en **formato Excel (.xlsx)** y ubicadas en una carpeta, por ejemplo: `C:\cartolas`

---

## 📦 Instalación de dependencias

Este script usa las siguientes librerías:

- `pandas`
- `glob`
- `os`
- `re`

Instala `pandas` si no lo tienes:

```bash
pip install pandas
```

---

## 🚀 ¿Cómo ejecutar?

1. Descarga tus cartolas desde BancoEstado (formato Excel).
2. Coloca todos los archivos `.xlsx` en la carpeta `C:\cartolas`.
3. Abre una terminal o consola.
4. Ejecuta el script en Python:

```bash
python combinador_cartolas.py
```

Al finalizar, el script creará un archivo llamado:

```
cartolas_combinadas.csv
```

que contiene todos los movimientos en una sola tabla, lista para analizar con Excel, Python, Power BI u otra herramienta.

---

## 📌 ¿Qué hace el script?

- Lee cada archivo Excel individual.
- Extrae los movimientos desde la cartola, saltando las cabeceras fijas.
- Reconoce y transforma las fechas escritas con meses en español.
- Limpia montos de abonos, cargos y saldo.
- Añade una columna indicando de qué archivo proviene cada movimiento.
- Une todo en un solo archivo `.csv`.

---

## 🧪 Archivos de ejemplo

Incluye un par de cartolas ficticias para que puedas probar el script sin necesidad de tus propias cartolas.

---

## 🇨🇱 ¿Por qué esto es útil?

En Chile, BancoEstado puede entregar hasta 100 cartolas por año, sin un resumen consolidado. Esta herramienta te permite recuperar el control de tu historial financiero en minutos.

---

## 📬 Contacto

Si tienes sugerencias o quieres mejorar el script, ¡bienvenido a contribuir!
https://www.linkedin.com/in/richardcastroi/
richard.castro@mat.uc.cl
