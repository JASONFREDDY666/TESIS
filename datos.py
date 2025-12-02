# datos.py
"""
Módulo que contiene los datos originales del estudio
20 entidades públicas con métricas de seguridad
"""

import pandas as pd

def cargar_datos_originales():
    """Carga y retorna el dataset original del estudio"""
    
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

def obtener_resumen_datos():
    """Retorna un resumen estadístico básico del dataset"""
    df = cargar_datos_originales()
    
    resumen = {
        'total_entidades': len(df),
        'modelos': df['Modelo_Seguridad'].value_counts().to_dict(),
        'niveles_madurez': df['Nivel_Madurez'].value_counts().to_dict(),
        'rango_empleados': f"{df['Empleados'].min():,} - {df['Empleados'].max():,}",
        'presupuesto_promedio': f"${df['Presupuesto_Seguridad_USD'].mean():,.0f} USD",
        'años_implementacion_promedio': f"{df['Años_Implementación'].mean():.1f} años"
    }
    
    return resumen