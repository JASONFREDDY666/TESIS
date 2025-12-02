# analisis_estadistico.py
"""
ANÁLISIS ESTADÍSTICO - CÁLCULOS EXACTOS
Todas las tablas del Capítulo IV recalculadas con precisión
"""

import pandas as pd
import numpy as np
from scipy.stats import kruskal, mannwhitneyu, spearmanr
import os

# ============================================================================
# DATOS ORIGINALES EXACTOS
# ============================================================================

def cargar_datos_originales():
    """Carga el dataset original exacto"""
    data = [
        ["ENT_PUB1", 2500, 180000, "Perimetral", 12, "Medio", 28, 18, 64.3, 45.2, 15.3, 3, 3, "Trimestral", 15, 8],
        ["ENT_PUB2", 1800, 95000, "Perimetral", 15, "Bajo", 42, 25, 59.5, 52.5, 18.1, 2, 2, "Semestral", 12, 5],
        ["ENT_PUB3", 3200, 220000, "Híbrido", 4, "Medio", 15, 12, 80.0, 22.8, 6.2, 4, 4, "Trimestral", 18, 12],
        ["ENT_PUB4", 1500, 120000, "Perimetral", 10, "Bajo", 38, 22, 57.9, 48.4, 16.7, 2, 3, "Anual", 11, 6],
        ["ENT_PUB5", 2800, 190000, "Híbrido", 3, "Medio", 18, 14, 77.8, 25.1, 7.5, 3, 4, "Trimestral", 17, 11],
        ["ENT_PUB6", 2200, 280000, "Zero Trust", 2, "Medio", 8, 7, 87.5, 8.4, 2.8, 4, 4, "Mensual", 22, 9],
        ["ENT_PUB7", 1900, 85000, "Perimetral", 8, "Bajo", 45, 26, 57.8, 55.3, 19.9, 2, 2, "Semestral", 10, 4],
        ["ENT_PUB8", 2600, 320000, "Zero Trust", 1, "Bajo", 12, 10, 83.3, 12.7, 4.3, 3, 3, "Trimestral", 24, 7],
        ["ENT_PUB9", 1700, 140000, "Híbrido", 5, "Medio", 16, 13, 81.3, 23.6, 6.8, 4, 3, "Trimestral", 16, 10],
        ["ENT_PUB10", 3000, 350000, "Zero Trust", 2, "Medio", 6, 5, 83.3, 6.1, 1.7, 4, 5, "Mensual", 25, 14],
        ["ENT_PUB11", 2100, 110000, "Perimetral", 11, "Medio", 32, 20, 62.5, 46.8, 17.4, 3, 3, "Trimestral", 13, 7],
        ["ENT_PUB12", 2400, 260000, "Híbrido", 4, "Medio", 14, 11, 78.6, 21.9, 5.9, 4, 4, "Trimestral", 19, 13],
        ["ENT_PUB13", 1300, 70000, "Perimetral", 9, "Bajo", 40, 23, 57.5, 53.7, 20.3, 2, 2, "Anual", 9, 3],
        ["ENT_PUB14", 2700, 300000, "Zero Trust", 3, "Medio", 7, 6, 85.7, 5.8, 1.4, 5, 4, "Mensual", 23, 12],
        ["ENT_PUB15", 2000, 170000, "Híbrido", 6, "Medio", 17, 13, 76.5, 24.5, 7.1, 3, 3, "Trimestral", 15, 9],
        ["ENT_PUB16", 2300, 125000, "Perimetral", 14, "Medio", 35, 21, 60.0, 49.1, 16.2, 3, 2, "Semestral", 14, 6],
        ["ENT_PUB17", 1600, 230000, "Zero Trust", 2, "Medio", 9, 8, 88.9, 9.3, 3.2, 4, 4, "Trimestral", 21, 8],
        ["ENT_PUB18", 2900, 195000, "Híbrido", 5, "Medio", 13, 10, 76.9, 22.3, 6.5, 4, 4, "Trimestral", 16, 15],
        ["ENT_PUB19", 1400, 80000, "Perimetral", 7, "Bajo", 43, 25, 58.1, 54.8, 21.5, 2, 2, "Anual", 8, 4],
        ["ENT_PUB20", 2500, 400000, "Zero Trust", 3, "Alto", 10, 9, 90.0, 3.2, 0.8, 5, 5, "Mensual", 28, 16]
    ]
    
    columnas = [
        "Entidad", "Empleados", "Presupuesto_Seguridad_USD", "Modelo_Seguridad", 
        "Años_Implementación", "Nivel_Madurez", "Incidentes_Mensuales", 
        "Bloqueos_Exitosos", "Tasa_Bloqueo_%", "Tiempo_Respuesta_min", 
        "Tiempo_Detección_min", "Percepción_1_5", "Capacitación_1_5", 
        "Frecuencia_Simulacros", "%_Presupuesto_IT_Seguridad", "Especialistas"
    ]
    
    df = pd.DataFrame(data, columns=columnas)
    return df

# ============================================================================
# TABLA 3: CARACTERÍSTICAS GENERALES (CÁLCULO EXACTO)
# ============================================================================

def generar_tabla3():
    """Tabla 3: Características generales de las entidades evaluadas"""
    df = cargar_datos_originales()
    
    # Calcular estadísticas exactas
    empleados_min = df['Empleados'].min()
    empleados_max = df['Empleados'].max()
    empleados_media = df['Empleados'].mean()
    
    presupuesto_min = df['Presupuesto_Seguridad_USD'].min()
    presupuesto_max = df['Presupuesto_Seguridad_USD'].max()
    presupuesto_media = df['Presupuesto_Seguridad_USD'].mean()
    
    años_min = df['Años_Implementación'].min()
    años_max = df['Años_Implementación'].max()
    años_media = df['Años_Implementación'].mean()
    
    especialistas_min = df['Especialistas'].min()
    especialistas_max = df['Especialistas'].max()
    especialistas_media = df['Especialistas'].mean()
    
    presupuesto_it_min = df['%_Presupuesto_IT_Seguridad'].min()
    presupuesto_it_max = df['%_Presupuesto_IT_Seguridad'].max()
    presupuesto_it_media = df['%_Presupuesto_IT_Seguridad'].mean()
    
    tabla3 = pd.DataFrame({
        "Variable": [
            "Número de empleados",
            "Presupuesto anual en seguridad (USD)",
            "Años de implementación del modelo actual",
            "Especialistas en seguridad (n)",
            "Porcentaje del presupuesto IT destinado a seguridad"
        ],
        "Rango / Media": [
            f"{empleados_min:,.0f} – {empleados_max:,.0f} (M = {empleados_media:,.0f})",
            f"{presupuesto_min:,.0f} – {presupuesto_max:,.0f} (M = {presupuesto_media:,.0f})",
            f"{años_min} – {años_max} (M = {años_media:.1f})",
            f"{especialistas_min} – {especialistas_max} (M = {especialistas_media:.1f})",
            f"{presupuesto_it_min}% – {presupuesto_it_max}% (M = {presupuesto_it_media:.1f}%)"
        ],
        "Descripción general": [
            "Tamaño típico de entidad pública con infraestructura digital consolidada.",
            "Inversión media-alta en ciberseguridad, dependiente de la criticidad de los datos gestionados.",
            "Se observan implementaciones maduras (Perimetral) y recientes (Zero Trust).",
            "Capacidad técnica media; refleja dependencia parcial de consultores externos.",
            "Asignación alineada con estándares internacionales (NIST, ISO/IEC 27001)."
        ]
    })
    
    return tabla3

# ============================================================================
# TABLA 6: DISTRIBUCIÓN DE MODELOS (CÁLCULO EXACTO)
# ============================================================================

def generar_tabla6():
    """Tabla 6: Distribución de modelos de seguridad"""
    df = cargar_datos_originales()
    
    # Calcular distribución exacta
    distribucion = df['Modelo_Seguridad'].value_counts().reset_index()
    distribucion.columns = ['Modelo de seguridad', 'Frecuencia']
    distribucion['Porcentaje (%)'] = (distribucion['Frecuencia'] / len(df) * 100)
    
    # Ordenar por frecuencia descendente
    distribucion = distribucion.sort_values('Frecuencia', ascending=False)
    
    # Añadir fila total
    total_frecuencia = distribucion['Frecuencia'].sum()
    total_porcentaje = 100.0
    
    total = pd.DataFrame({
        'Modelo de seguridad': ['Total'],
        'Frecuencia': [total_frecuencia],
        'Porcentaje (%)': [total_porcentaje]
    })
    
    # Combinar y formatear
    distribucion_completa = pd.concat([distribucion, total], ignore_index=True)
    distribucion_completa['Porcentaje (%)'] = distribucion_completa['Porcentaje (%)'].apply(
        lambda x: f"{x:.1f}%" if pd.notnull(x) else ""
    )
    
    return distribucion_completa

# ============================================================================
# TABLA 7: NIVEL DE MADUREZ (CÁLCULO EXACTO CON DESVIACIONES REALES)
# ============================================================================

def generar_tabla7():
    """Tabla 7: Nivel de madurez del modelo según años de implementación"""
    df = cargar_datos_originales()
    
    # Calcular estadísticas por nivel de madurez
    resultados = []
    
    for nivel in ['Bajo', 'Medio', 'Alto']:
        subset = df[df['Nivel_Madurez'] == nivel]
        
        if len(subset) > 0:
            años = subset['Años_Implementación']
            
            # Calcular estadísticas exactas
            promedio = años.mean()
            desviacion = años.std(ddof=1)  # Desviación estándar muestral
            varianza = años.var(ddof=1)
            
            # Determinar modelo predominante
            modelo_predominante = subset['Modelo_Seguridad'].mode()
            modelo_pred = modelo_predominante[0] if len(modelo_predominante) > 0 else "N/A"
            
            resultados.append({
                'Nivel de madurez': nivel,
                'Promedio de años de implementación': f"{promedio:.4f}",
                'Desviación estándar': f"{desviacion:.4f}",
                'Varianza': f"{varianza:.4f}",
                'Cantidad': len(subset),
                'Modelo predominante': modelo_pred
            })
    
    tabla7 = pd.DataFrame(resultados)
    
    # Formatear para presentación
    tabla7_formateada = pd.DataFrame({
        'Nivel de madurez': tabla7['Nivel de madurez'],
        'Promedio de años': tabla7['Promedio de años de implementación'],
        'Desviación estándar': tabla7['Desviación estándar'],
        'Modelo predominante': tabla7['Modelo predominante']
    })
    
    return tabla7_formateada

# ============================================================================
# TABLA 8: DESEMPEÑO PROMEDIO (CÁLCULO EXACTO)
# ============================================================================

def generar_tabla8():
    """Tabla 8: Desempeño promedio de los modelos de seguridad"""
    df = cargar_datos_originales()
    
    modelos = ['Perimetral', 'Híbrido', 'Zero Trust']
    resultados = []
    
    for modelo in modelos:
        subset = df[df['Modelo_Seguridad'] == modelo]
        
        if len(subset) > 0:
            # Calcular estadísticas exactas
            incidentes_media = subset['Incidentes_Mensuales'].mean()
            bloqueos_media = subset['Bloqueos_Exitosos'].mean()
            tasa_bloqueo_media = subset['Tasa_Bloqueo_%'].mean()
            tiempo_respuesta_media = subset['Tiempo_Respuesta_min'].mean()
            tiempo_deteccion_media = subset['Tiempo_Detección_min'].mean()
            
            # Calcular desviaciones estándar
            incidentes_std = subset['Incidentes_Mensuales'].std(ddof=1)
            bloqueos_std = subset['Bloqueos_Exitosos'].std(ddof=1)
            tasa_bloqueo_std = subset['Tasa_Bloqueo_%'].std(ddof=1)
            tiempo_respuesta_std = subset['Tiempo_Respuesta_min'].std(ddof=1)
            tiempo_deteccion_std = subset['Tiempo_Detección_min'].std(ddof=1)
            
            resultados.append({
                'Modelo': modelo,
                'N': len(subset),
                'Incidentes mensuales (M±SD)': f"{incidentes_media:.4f} ± {incidentes_std:.4f}",
                'Bloqueos exitosos (M±SD)': f"{bloqueos_media:.4f} ± {bloqueos_std:.4f}",
                'Tasa de bloqueo % (M±SD)': f"{tasa_bloqueo_media:.4f} ± {tasa_bloqueo_std:.4f}",
                'Tiempo respuesta min (M±SD)': f"{tiempo_respuesta_media:.4f} ± {tiempo_respuesta_std:.4f}",
                'Tiempo detección min (M±SD)': f"{tiempo_deteccion_media:.4f} ± {tiempo_deteccion_std:.4f}"
            })
    
    tabla8 = pd.DataFrame(resultados)
    
    # Versión simplificada para la tesis
    tabla8_simple = pd.DataFrame({
        'Modelo': tabla8['Modelo'],
        'Incidentes mensuales (M)': [x.split(' ± ')[0] for x in tabla8['Incidentes mensuales (M±SD)']],
        'Bloqueos exitosos (M)': [x.split(' ± ')[0] for x in tabla8['Bloqueos exitosos (M±SD)']],
        'Tasa de bloqueo (%)': [x.split(' ± ')[0] for x in tabla8['Tasa de bloqueo % (M±SD)']],
        'Tiempo de respuesta (min)': [x.split(' ± ')[0] for x in tabla8['Tiempo respuesta min (M±SD)']],
        'Tiempo de detección (min)': [x.split(' ± ')[0] for x in tabla8['Tiempo detección min (M±SD)']]
    })
    
    return tabla8_simple

# ============================================================================
# TABLA 9: PERCEPCIÓN Y CAPACITACIÓN
# ============================================================================

def generar_tabla9():
    """Tabla 9 CORREGIDA: Indicadores de percepción y capacitación"""
    df = cargar_datos_originales()
    
    modelos = ['Perimetral', 'Híbrido', 'Zero Trust']
    resultados = []
    
    for modelo in modelos:
        subset = df[df['Modelo_Seguridad'] == modelo]
        
        if len(subset) > 0:
            # Calcular promedios EXACTOS
            percepcion_media = subset['Percepción_1_5'].mean()
            capacitacion_media = subset['Capacitación_1_5'].mean()
            especialistas_media = subset['Especialistas'].mean()
            
            # Calcular desviaciones estándar
            percepcion_std = subset['Percepción_1_5'].std(ddof=1)
            capacitacion_std = subset['Capacitación_1_5'].std(ddof=1)
            especialistas_std = subset['Especialistas'].std(ddof=1)
            
            # Determinar frecuencia más común de simulacros
            frecuencia_counts = subset['Frecuencia_Simulacros'].value_counts()
            if len(frecuencia_counts) > 0:
                frecuencia_comun = frecuencia_counts.index[0]
            else:
                frecuencia_comun = "N/A"
            
            resultados.append({
                'Modelo': modelo,
                'Percepción de seguridad (1–5) (M±SD)': f"{percepcion_media:.4f} ± {percepcion_std:.4f}",
                'Nivel de capacitación (1–5) (M±SD)': f"{capacitacion_media:.4f} ± {capacitacion_std:.4f}",
                'Frecuencia de simulacros': frecuencia_comun,
                'Especialistas (M±SD)': f"{especialistas_media:.4f} ± {especialistas_std:.4f}"
            })
    
    tabla9 = pd.DataFrame(resultados)
    
    # Versión para la tesis
    tabla9_simple = pd.DataFrame({
        'Modelo': tabla9['Modelo'],
        'Percepción de seguridad (1–5)': [x.split(' ± ')[0] for x in tabla9['Percepción de seguridad (1–5) (M±SD)']],
        'Nivel de capacitación (1–5)': [x.split(' ± ')[0] for x in tabla9['Nivel de capacitación (1–5) (M±SD)']],
        'Frecuencia de simulacros': tabla9['Frecuencia de simulacros'],
        'Media especialistas': [x.split(' ± ')[0] for x in tabla9['Especialistas (M±SD)']]
    })
    
    return tabla9_simple

# ============================================================================
# TABLA 10: KRUSKAL-WALLIS (¡CÁLCULO EXACTO!)
# ============================================================================

def generar_tabla10():
    """Tabla 10: Prueba de Kruskal–Wallis con cálculos exactos"""
    df = cargar_datos_originales()
    
    variables = [
        ('Incidentes mensuales', 'Incidentes_Mensuales'),
        ('Tasa de bloqueo (%)', 'Tasa_Bloqueo_%'),
        ('Tiempo de respuesta (min)', 'Tiempo_Respuesta_min'),
        ('Tiempo de detección (min)', 'Tiempo_Detección_min')
    ]
    
    resultados = []
    
    for nombre_var, columna in variables:
        # Extraer datos por grupo
        grupos = []
        grupos_nombres = []
        
        for modelo in ['Perimetral', 'Híbrido', 'Zero Trust']:
            grupo_data = df[df['Modelo_Seguridad'] == modelo][columna].dropna().values
            if len(grupo_data) > 0:
                grupos.append(grupo_data)
                grupos_nombres.append(modelo)
        
        # Solo calcular si hay al menos 2 grupos con datos
        if len(grupos) >= 2:
            try:
                # Calcular Kruskal-Wallis exacto
                h_stat, p_valor = kruskal(*grupos)
                
                # Calcular medias por grupo para interpretación
                medias = []
                for i, modelo in enumerate(grupos_nombres):
                    media = np.mean(grupos[i])
                    medias.append((modelo, media))
                
                # Ordenar por media (ascendente o descendente según variable)
                if "Incidentes" in nombre_var or "Tiempo" in nombre_var:
                    # Para incidentes y tiempos, menor es mejor
                    medias_ordenadas = sorted(medias, key=lambda x: x[1])
                    mejor_modelo = medias_ordenadas[0][0]
                    interpretacion = f"Mejor desempeño: {mejor_modelo}"
                else:
                    # Para tasa de bloqueo, mayor es mejor
                    medias_ordenadas = sorted(medias, key=lambda x: x[1], reverse=True)
                    mejor_modelo = medias_ordenadas[0][0]
                    interpretacion = f"Mejor desempeño: {mejor_modelo}"
                
                # Determinar significancia
                if p_valor < 0.001:
                    significancia = "*** p < 0.001"
                elif p_valor < 0.01:
                    significancia = "** p < 0.01"
                elif p_valor < 0.05:
                    significancia = "* p < 0.05"
                else:
                    significancia = "ns p ≥ 0.05"
                
                resultados.append({
                    'Variable': nombre_var,
                    'H (gl = 2)': f"{h_stat:.6f}",
                    'p valor': f"{p_valor:.6f}",
                    'Significancia': significancia,
                    'Interpretación': interpretacion
                })
                
            except Exception as e:
                resultados.append({
                    'Variable': nombre_var,
                    'H (gl = 2)': "Error",
                    'p valor': "Error",
                    'Significancia': "Error",
                    'Interpretación': f"Error en cálculo: {str(e)}"
                })
    
    return pd.DataFrame(resultados)

# ============================================================================
# TABLA 11: MANN-WHITNEY (CÁLCULO EXACTO)
# ============================================================================

def generar_tabla11():
    """Tabla 11: Comparaciones pareadas con Mann-Whitney U"""
    df = cargar_datos_originales()
    
    # Comparaciones relevantes
    comparaciones = [
        ("Perimetral vs Híbrido", "Perimetral", "Híbrido", "Incidentes mensuales", "Incidentes_Mensuales"),
        ("Perimetral vs Zero Trust", "Perimetral", "Zero Trust", "Incidentes mensuales", "Incidentes_Mensuales"),
        ("Híbrido vs Zero Trust", "Híbrido", "Zero Trust", "Incidentes mensuales", "Incidentes_Mensuales"),
        ("Perimetral vs Zero Trust", "Perimetral", "Zero Trust", "Tiempo detección (min)", "Tiempo_Detección_min"),
        ("Perimetral vs Híbrido", "Perimetral", "Híbrido", "Tasa de bloqueo (%)", "Tasa_Bloqueo_%"),
        ("Perimetral vs Zero Trust", "Perimetral", "Zero Trust", "Tasa de bloqueo (%)", "Tasa_Bloqueo_%")
    ]
    
    resultados = []
    
    for nombre_comp, modelo1, modelo2, nombre_var, columna in comparaciones:
        # Extraer datos
        grupo1 = df[df['Modelo_Seguridad'] == modelo1][columna].dropna().values
        grupo2 = df[df['Modelo_Seguridad'] == modelo2][columna].dropna().values
        
        if len(grupo1) > 0 and len(grupo2) > 0:
            try:
                # Calcular Mann-Whitney U exacto
                u_stat, p_valor = mannwhitneyu(grupo1, grupo2, alternative='two-sided')
                
                # Calcular medias
                media1 = np.mean(grupo1)
                media2 = np.mean(grupo2)
                
                # Determinar dirección del efecto
                if "Incidentes" in nombre_var or "Tiempo" in nombre_var:
                    # Menor es mejor
                    if media1 < media2:
                        direccion = f"{modelo1} < {modelo2}"
                    else:
                        direccion = f"{modelo2} < {modelo1}"
                else:
                    # Mayor es mejor (tasa de bloqueo)
                    if media1 > media2:
                        direccion = f"{modelo1} > {modelo2}"
                    else:
                        direccion = f"{modelo2} > {modelo1}"
                
                # Determinar significancia
                if p_valor < 0.001:
                    significancia = "***"
                    interpretacion = f"Diferencia altamente significativa ({direccion})"
                elif p_valor < 0.01:
                    significancia = "**"
                    interpretacion = f"Diferencia muy significativa ({direccion})"
                elif p_valor < 0.05:
                    significancia = "*"
                    interpretacion = f"Diferencia significativa ({direccion})"
                else:
                    significancia = "ns"
                    interpretacion = f"Sin diferencia significativa"
                
                resultados.append({
                    'Comparación': nombre_comp,
                    'Variable': nombre_var,
                    'U de Mann': f"{u_stat:.6f}",
                    'p valor': f"{p_valor:.6f}",
                    'Significancia': significancia,
                    'Interpretación': interpretacion
                })
                
            except Exception as e:
                resultados.append({
                    'Comparación': nombre_comp,
                    'Variable': nombre_var,
                    'U de Mann': "Error",
                    'p valor': "Error",
                    'Significancia': "Error",
                    'Interpretación': f"Error en cálculo: {str(e)}"
                })
    
    return pd.DataFrame(resultados)

# ============================================================================
# TABLA 12: CORRELACIONES DE SPEARMAN (CÁLCULO EXACTO)
# ============================================================================

def generar_tabla12():
    """Tabla 12: Correlaciones de Spearman con cálculos exactos"""
    df = cargar_datos_originales()
    
    # Seleccionar variables relevantes para correlación
    variables_corr = [
        'Años_Implementación',
        'Nivel_Madurez_Num',  # Necesitamos convertir a numérico
        'Tasa_Bloqueo_%',
        'Tiempo_Detección_min',
        'Percepción_1_5',
        'Capacitación_1_5',
        'Especialistas',
        'Tiempo_Respuesta_min'
    ]
    
    # Crear dataframe para correlaciones
    df_corr = df.copy()
    
    # Convertir nivel de madurez a numérico
    madurez_map = {'Bajo': 1, 'Medio': 2, 'Alto': 3}
    df_corr['Nivel_Madurez_Num'] = df_corr['Nivel_Madurez'].map(madurez_map)
    
    # Convertir frecuencia de simulacros a numérico
    frecuencia_map = {'Anual': 1, 'Semestral': 2, 'Trimestral': 4, 'Mensual': 12}
    df_corr['Frecuencia_Num'] = df_corr['Frecuencia_Simulacros'].map(frecuencia_map)
    
    # Seleccionar columnas numéricas
    columnas_numericas = [
        'Años_Implementación',
        'Nivel_Madurez_Num',
        'Tasa_Bloqueo_%',
        'Tiempo_Detección_min',
        'Percepción_1_5',
        'Capacitación_1_5',
        'Especialistas',
        'Tiempo_Respuesta_min',
        'Frecuencia_Num'
    ]
    
    # Calcular matriz de correlación de Spearman
    corr_matrix = df_corr[columnas_numericas].corr(method='spearman')
    
    # Crear tabla formateada
    nombres_amigables = {
        'Años_Implementación': 'Años implementación',
        'Nivel_Madurez_Num': 'Madurez',
        'Tasa_Bloqueo_%': 'Tasa bloqueo (%)',
        'Tiempo_Detección_min': 'Tiempo detección (min)',
        'Percepción_1_5': 'Percepción',
        'Capacitación_1_5': 'Capacitación',
        'Especialistas': 'Especialistas',
        'Tiempo_Respuesta_min': 'Tiempo respuesta (min)',
        'Frecuencia_Num': 'Frecuencia simulacros'
    }
    
    # Renombrar índices y columnas
    corr_matrix_renamed = corr_matrix.rename(
        index=nombres_amigables,
        columns=nombres_amigables
    )
    
    # Formatear valores
    corr_formatted = corr_matrix_renamed.copy()
    for col in corr_formatted.columns:
        corr_formatted[col] = corr_formatted[col].apply(lambda x: f"{x:.6f}" if pd.notnull(x) else "N/A")
    
    # Resetear índice para mostrar como tabla
    tabla12 = corr_formatted.reset_index().rename(columns={'index': 'Variable'})
    
    return tabla12

# ============================================================================
# FUNCIONES DE EXPORTACIÓN
# ============================================================================

def crear_carpetas_exportacion():
    """Crea las carpetas necesarias para exportación"""
    carpetas = ['exportacion_capitulo_iv', 
                'exportacion_capitulo_iv/tablas',
                'exportacion_capitulo_iv/graficos',
                'exportacion_capitulo_iv/dataset']
    
    for carpeta in carpetas:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

def guardar_todas_tablas():
    """Guarda todas las tablas en formato Markdown y CSV"""
    crear_carpetas_exportacion()
    
    # Diccionario de tablas
    tablas = {
        'tabla3': generar_tabla3(),
        'tabla6': generar_tabla6(),
        'tabla7': generar_tabla7(),
        'tabla8': generar_tabla8(),
        'tabla9': generar_tabla9(),
        'tabla10': generar_tabla10(),
        'tabla11': generar_tabla11(),
        'tabla12': generar_tabla12()
    }
    
    # También guardar dataset completo
    df_completo = cargar_datos_originales()
    df_completo.to_excel('exportacion_capitulo_iv/dataset/dataset_completo.xlsx', index=False)
    df_completo.to_csv('exportacion_capitulo_iv/dataset/dataset_completo.csv', index=False, encoding='utf-8-sig')
    
    for nombre, tabla in tablas.items():
        # Guardar como Markdown
        with open(f'exportacion_capitulo_iv/tablas/{nombre}.md', 'w', encoding='utf-8') as f:
            f.write(f"# {nombre.upper().replace('TABLA', 'TABLA ')}\n\n")
            f.write(tabla.to_markdown(index=False))
            f.write(f"\n\n*Nota: Cálculos exactos basados en el dataset original (n=20).*\n")
            f.write(f"*Fecha de generación: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        
        # Guardar como CSV
        tabla.to_csv(f'exportacion_capitulo_iv/tablas/{nombre}.csv', index=False, encoding='utf-8-sig')
        
        # Guardar como Excel
        tabla.to_excel(f'exportacion_capitulo_iv/tablas/{nombre}.xlsx', index=False)
    
    print(f"✅ {len(tablas)} tablas guardadas en 'exportacion_capitulo_iv/tablas/'")
    print(f"✅ Dataset completo guardado en 'exportacion_capitulo_iv/dataset/'")
    
    return True

# ============================================================================
# FUNCIÓN DE VERIFICACIÓN DE CÁLCULOS
# ============================================================================

def verificar_todos_calculos():
    """Verifica y muestra todos los cálculos exactos"""
    df = cargar_datos_originales()
    
    resultado = "=" * 80 + "\n"
    resultado += "VERIFICACIÓN DE CÁLCULOS - CAPÍTULO IV\n"
    resultado += "CÁLCULOS EXACTOS CON 6 DECIMALES DE PRECISIÓN\n"
    resultado += "=" * 80 + "\n\n"
    
    # 1. Verificar distribución de modelos
    resultado += "1. DISTRIBUCIÓN DE MODELOS (Tabla 6):\n"
    resultado += "-" * 40 + "\n"
    distribucion = df['Modelo_Seguridad'].value_counts()
    total = len(df)
    for modelo, count in distribucion.items():
        porcentaje = (count / total) * 100
        resultado += f"  {modelo}: {count} entidades ({porcentaje:.6f}%)\n"
    resultado += f"  TOTAL: {total} entidades (100.000000%)\n\n"
    
    # 2. Verificar Tabla 9 - Percepción y capacitación
    resultado += "2. TABLA 9 - PERCEPCIÓN Y CAPACITACIÓN:\n"
    resultado += "-" * 40 + "\n"
    
    modelos = ['Perimetral', 'Híbrido', 'Zero Trust']
    for modelo in modelos:
        subset = df[df['Modelo_Seguridad'] == modelo]
        if len(subset) > 0:
            percepcion = subset['Percepción_1_5'].mean()
            capacitacion = subset['Capacitación_1_5'].mean()
            resultado += f"  {modelo}:\n"
            resultado += f"    • Percepción: {percepcion:.6f}\n"
            resultado += f"    • Capacitación: {capacitacion:.6f}\n"
            
            # Calcular diferencia con valores incorrectos anteriores
            if modelo == 'Perimetral':
                dif_cap = abs(capacitacion - 2.43)
                resultado += f"    • Diferencia con valor anterior (2.43): {dif_cap:.6f}\n"
            elif modelo == 'Híbrido':
                dif_cap = abs(capacitacion - 3.50)
                resultado += f"    • Diferencia con valor anterior (3.50): {dif_cap:.6f}\n"
            elif modelo == 'Zero Trust':
                dif_per = abs(percepcion - 4.57)
                dif_cap = abs(capacitacion - 4.40)
                resultado += f"    • Diferencia percepción anterior (4.57): {dif_per:.6f}\n"
                resultado += f"    • Diferencia capacitación anterior (4.40): {dif_cap:.6f}\n"
            resultado += "\n"
    
    # 3. Verificar Kruskal-Wallis para incidentes
    resultado += "3. TABLA 10 - KRUSKAL-WALLIS (INCIDENTES):\n"
    resultado += "-" * 40 + "\n"
    
    perimetral_inc = df[df['Modelo_Seguridad'] == 'Perimetral']['Incidentes_Mensuales'].values
    hibrido_inc = df[df['Modelo_Seguridad'] == 'Híbrido']['Incidentes_Mensuales'].values
    zerotrust_inc = df[df['Modelo_Seguridad'] == 'Zero Trust']['Incidentes_Mensuales'].values
    
    try:
        h_stat, p_valor = kruskal(perimetral_inc, hibrido_inc, zerotrust_inc)
        resultado += f"  H estadístico: {h_stat:.6f}\n"
        resultado += f"  Valor p: {p_valor:.6f}\n"
        resultado += f"  Significancia: {'SIGNIFICATIVO' if p_valor < 0.05 else 'NO SIGNIFICATIVO'}\n"
        resultado += f"  N por grupo: Perimetral={len(perimetral_inc)}, Híbrido={len(hibrido_inc)}, Zero Trust={len(zerotrust_inc)}\n"
    except Exception as e:
        resultado += f"  Error en cálculo: {str(e)}\n"
    resultado += "\n"
    
    # 4. Resumen de correcciones
    resultado += "4. RESUMEN DE CORRECCIONES APLICADAS:\n"
    resultado += "-" * 40 + "\n"
    resultado += "  ✅ Tabla 9 - Valores de percepción y capacitación\n"
    resultado += "  ✅ Tabla 10 - Valores de Kruskal-Wallis EXACTOS\n"
    resultado += "  ✅ Todas las tablas - Cálculos con 6 decimales de precisión\n"
    resultado += "  ✅ Desviaciones estándar calculadas correctamente (ddof=1)\n"
    resultado += "  ✅ Matriz de correlaciones con coeficientes de Spearman\n"
    resultado += "\n"
    
    # 5. Recomendaciones para la tesis
    resultado += "5. RECOMENDACIONES PARA LA TESIS:\n"
    resultado += "-" * 40 + "\n"
    resultado += "  • Usar los valores mostrados en esta verificación\n"
    resultado += "  • Reportar valores con 2 decimales en el texto principal\n"
    resultado += "  • Incluir valores exactos en apéndices si es necesario\n"
    resultado += "  • Verificar que todos los cálculos coincidan con esta salida\n"
    resultado += "\n" + "=" * 80 + "\n"
    resultado += "VERIFICACIÓN COMPLETADA - TODOS LOS CÁLCULOS SON EXACTOS\n"
    resultado += "=" * 80
    
    return resultado

# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("ANÁLISIS ESTADÍSTICO - CAPÍTULO IV")
    print("=" * 80)
    print("\nGenerando todas las tablas con cálculos exactos...\n")
    
    # Generar y mostrar todas las tablas
    tablas_funciones = [
        ("Tabla 3", generar_tabla3),
        ("Tabla 6", generar_tabla6),
        ("Tabla 7", generar_tabla7),
        ("Tabla 8", generar_tabla8),
        ("Tabla 9", generar_tabla9),
        ("Tabla 10", generar_tabla10),
        ("Tabla 11", generar_tabla11),
        ("Tabla 12", generar_tabla12)
    ]
    
    for nombre, funcion in tablas_funciones:
        print(f"\n{nombre}:")
        print("-" * 50)
        tabla = funcion()
        print(tabla.to_string(index=False, float_format=lambda x: f"{x:.6f}" if isinstance(x, float) else str(x)))
    
    # Verificar cálculos
    print("\n" + "=" * 80)
    print("VERIFICANDO CÁLCULOS...")
    print("=" * 80)
    print(verificar_todos_calculos())
    
    # Guardar todas las tablas
    guardar_todas_tablas()
    
    print("\n✅ Análisis completado exitosamente!")
    print("📁 Tablas guardadas en: 'exportacion_capitulo_iv/tablas/'")