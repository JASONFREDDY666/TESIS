Descripción
Sistema completo para análisis estadístico de modelos de seguridad informática (Perimetral, Híbrido, Zero Trust) en 20 entidades públicas. Genera automáticamente todas las tablas y gráficos necesarios para el Capítulo IV: Resultados y Discusión de tesis.

✅ Características principales
8 tablas estadísticas con cálculos exactos (6 decimales de precisión)

8 gráficos profesionales listos para publicación (300 DPI)

Interfaz gráfica intuitiva con Tkinter

Cálculos verificados y corregidos (Tabla 9 y 10 corregidas)

Exportación automática en múltiples formatos (PNG, PDF, CSV, Excel)

Función de verificación de cálculos exactos

Dataset original de 20 entidades públicas

🚀 Instalación rápida
Requisitos previos
Python 3.8 o superior

Git instalado

Pasos de instalación
bash
# 1. Clonar el repositorio
git clone https://github.com/JASONFREDDY666/TESIS.git
cd TESIS

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la aplicación
python main.py
Instalación con scripts incluidos
bash
# Windows
install.bat

# Linux/Mac
chmod +x install.sh
./install.sh
📋 Tablas generadas (8 tablas completas)
Tabla	Nombre	Descripción
3	Características generales	Estadísticas descriptivas de las 20 entidades
6	Distribución de modelos	Frecuencia y porcentaje por modelo de seguridad
7	Nivel de madurez	Relación entre años de implementación y madurez
8	Desempeño promedio	Métricas técnicas por modelo (incidentes, bloqueos, tiempos)
9	Percepción y capacitación	VALORES CORREGIDOS - Indicadores organizacionales
10	Kruskal-Wallis	Prueba estadística no paramétrica - CÁLCULOS EXACTOS
11	Mann-Whitney	Comparaciones pareadas entre modelos
12	Correlaciones	Matriz de correlaciones de Spearman
📈 Gráficos incluidos (8 gráficos profesionales)
📉 Incidentes mensuales - Distribución por modelo (boxplot + barras)

📊 Tasa de bloqueo - Comparativa de efectividad (barras + violín)

⏱️ Tiempos de respuesta - Respuesta vs detección (comparativa completa)

👤 Percepción y capacitación - ¡GRÁFICO CORREGIDO! (barras agrupadas + líneas)

📈 Nivel de madurez - Relación con años de implementación (scatter + barras)

👥 Especialistas por modelo - Distribución y relación con presupuesto

📊 Mapa de correlaciones - Heatmap de correlaciones de Spearman

📦 Boxplot completo - Comparación de todas las métricas por modelo

🖥️ Uso detallado
Interfaz gráfica (recomendado)
bash
python main.py
La interfaz gráfica permite:

Generar las 8 tablas estadísticas individualmente

Visualizar los 8 gráficos con zoom y navegación

Exportar resultados en múltiples formatos

Verificar cálculos exactos con 6 decimales

Explorar el dataset completo

Línea de comandos
bash
# Generar análisis estadístico completo
python analisis_estadistico.py

# Generar todos los gráficos
python graficos_completos.py

# Ver dataset completo
python -c "from datos import cargar_datos_originales; df = cargar_datos_originales(); print(df.to_string())"

# Prueba rápida del sistema
python test.py
📁 Estructura del proyecto
text
TESIS/
├── 📦 CÓDIGO FUENTE
│   ├── main.py                    # Interfaz gráfica principal
│   ├── analisis_estadistico.py    # Análisis estadístico (8 tablas)
│   ├── datos.py                   # Dataset original (20 entidades)
│   ├── graficos_completos.py      # Generación de 8 gráficos
│   ├── visualizacion.py           # Funciones de visualización
│   ├── interfaz_principal.py      # Componentes de interfaz
│   └── test.py                    # Script de prueba
│
├── 📄 CONFIGURACIÓN
│   ├── requirements.txt           # Dependencias de Python
│   ├── .gitignore                 # Archivos excluidos de Git
│   ├── install.bat                # Instalador para Windows
│   └── install.sh                 # Instalador para Linux/Mac
│
└── 📚 DOCUMENTACIÓN
    └── README.md                  # Este archivo
🔧 Tecnologías utilizadas
Python 3.11 - Lenguaje principal

Pandas & NumPy - Análisis y manipulación de datos

Matplotlib & Seaborn - Visualización y gráficos

SciPy - Estadística y pruebas no paramétricas

Tkinter - Interfaz gráfica de usuario

OpenPyXL - Exportación a Excel

🎯 Características técnicas destacadas
✅ Cálculos exactos
Todos los valores con 6 decimales de precisión

Tabla 9 completamente corregida (valores anteriores incorrectos)

Tabla 10 con cálculos exactos de Kruskal-Wallis

Desviaciones estándar calculadas correctamente (ddof=1)

📊 Gráficos profesionales
300 DPI - Calidad de publicación

Formato vectorial (PDF) y raster (PNG)

Paletas de colores profesionales

Anotaciones y etiquetas claras

🖥️ Interfaz avanzada
Navegación por pestañas

Tooltips informativos

Exportación individual y masiva

Verificación de cálculos integrada

📊 Dataset original
El análisis se basa en 20 entidades públicas con las siguientes variables:

Variable	Descripción	Rango
Empleados	Número de empleados	1,300 - 3,200
Presupuesto seguridad	USD anual	$70,000 - $400,000
Años implementación	Antigüedad del modelo	1 - 15 años
Modelo seguridad	Perimetral, Híbrido, Zero Trust	3 categorías
Nivel madurez	Bajo, Medio, Alto	3 niveles
Incidentes mensuales	Número promedio	6 - 45
Tasa bloqueo	Porcentaje de éxito	57.5% - 90.0%
Tiempo respuesta	Minutos promedio	3.2 - 55.3 min
Tiempo detección	Minutos promedio	0.8 - 21.5 min
Percepción	Escala 1-5	2.0 - 5.0
Capacitación	Escala 1-5	2.0 - 5.0
Especialistas	Número de personas	3 - 16
🛠️ Funcionalidades de exportación
Formatos soportados:
📋 Tablas: Markdown, CSV, Excel

📊 Gráficos: PNG (300 DPI), PDF (vectorial)

📁 Dataset: Excel, CSV

Exportación con un clic:
bash
# Desde la interfaz gráfica: Botón "📥 EXPORTAR TODO"
# Se crea la carpeta: exportacion_capitulo_iv/
🔍 Verificación de cálculos
El sistema incluye función de verificación que muestra:

Valores exactos con 6 decimales

Diferencias con valores incorrectos anteriores

Significancia estadística exacta
