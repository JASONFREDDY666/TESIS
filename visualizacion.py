# visualizacion.py
"""
Módulo para generar visualizaciones del análisis
Modificado para retornar figuras en lugar de mostrarlas
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datos import cargar_datos_originales

# Configuración de estilo
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def generar_grafico_cajas_incidentes():
    """Genera gráfico de cajas para incidentes mensuales y retorna la figura"""
    df = cargar_datos_originales()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Crear gráfico de cajas
    boxplot = sns.boxplot(
        x='Modelo_Seguridad', 
        y='Incidentes_Mensuales', 
        data=df,
        order=['Perimetral', 'Híbrido', 'Zero Trust'],
        ax=ax
    )
    
    # Añadir puntos individuales
    sns.stripplot(
        x='Modelo_Seguridad', 
        y='Incidentes_Mensuales', 
        data=df,
        color='black',
        alpha=0.5,
        jitter=True,
        order=['Perimetral', 'Híbrido', 'Zero Trust'],
        ax=ax
    )
    
    # Personalizar
    ax.set_title('Distribución de Incidentes Mensuales por Modelo de Seguridad', 
              fontsize=14, fontweight='bold')
    ax.set_xlabel('Modelo de Seguridad', fontsize=12)
    ax.set_ylabel('Incidentes Mensuales', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Añadir anotaciones
    modelos = df['Modelo_Seguridad'].unique()
    for i, modelo in enumerate(['Perimetral', 'Híbrido', 'Zero Trust']):
        media = df[df['Modelo_Seguridad'] == modelo]['Incidentes_Mensuales'].mean()
        ax.text(i, df['Incidentes_Mensuales'].max() * 1.05, 
                f'Media: {media:.1f}', 
                ha='center', fontsize=10)
    
    plt.tight_layout()
    return fig

def generar_grafico_tasa_bloqueo():
    """Genera gráfico de barras para tasa de bloqueo y retorna la figura"""
    df = cargar_datos_originales()
    
    # Calcular promedios por modelo
    promedios = df.groupby('Modelo_Seguridad')['Tasa_Bloqueo_%'].mean().reset_index()
    promedios = promedios.sort_values('Tasa_Bloqueo_%', ascending=False)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Crear gráfico de barras
    bars = ax.bar(promedios['Modelo_Seguridad'], promedios['Tasa_Bloqueo_%'], 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    
    # Añadir valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=11)
    
    ax.set_title('Tasa de Bloqueo Promedio por Modelo de Seguridad', 
              fontsize=14, fontweight='bold')
    ax.set_xlabel('Modelo de Seguridad', fontsize=12)
    ax.set_ylabel('Tasa de Bloqueo (%)', fontsize=12)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

def generar_grafico_tiempos_respuesta():
    """Genera gráfico para tiempos de respuesta y detección y retorna la figura"""
    df = cargar_datos_originales()
    
    # Calcular promedios
    tiempos = df.groupby('Modelo_Seguridad')[['Tiempo_Respuesta_min', 'Tiempo_Detección_min']].mean()
    tiempos = tiempos.reset_index()
    tiempos_melted = tiempos.melt(id_vars='Modelo_Seguridad', 
                                   value_vars=['Tiempo_Respuesta_min', 'Tiempo_Detección_min'],
                                   var_name='Tipo', 
                                   value_name='Minutos')
    
    # Traducir nombres
    tiempos_melted['Tipo'] = tiempos_melted['Tipo'].map({
        'Tiempo_Respuesta_min': 'Tiempo de Respuesta',
        'Tiempo_Detección_min': 'Tiempo de Detección'
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Gráfico de barras agrupadas
    sns.barplot(x='Modelo_Seguridad', y='Minutos', hue='Tipo', 
                data=tiempos_melted, palette='Set2', ax=ax)
    
    ax.set_title('Tiempos de Respuesta y Detección por Modelo de Seguridad', 
              fontsize=14, fontweight='bold')
    ax.set_xlabel('Modelo de Seguridad', fontsize=12)
    ax.set_ylabel('Minutos', fontsize=12)
    ax.legend(title='Tipo de Tiempo')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

def generar_grafico_percepcion_capacitacion():
    """Genera gráfico para percepción y capacitación y retorna la figura"""
    df = cargar_datos_originales()
    
    # Calcular promedios
    percep_capac = df.groupby('Modelo_Seguridad')[['Percepción_1_5', 'Capacitación_1_5']].mean()
    percep_capac = percep_capac.reset_index()
    percep_melted = percep_capac.melt(id_vars='Modelo_Seguridad', 
                                        value_vars=['Percepción_1_5', 'Capacitación_1_5'],
                                        var_name='Indicador', 
                                        value_name='Puntuación')
    
    # Traducir nombres
    percep_melted['Indicador'] = percep_melted['Indicador'].map({
        'Percepción_1_5': 'Percepción de Seguridad',
        'Capacitación_1_5': 'Nivel de Capacitación'
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(percep_capac['Modelo_Seguridad']))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, percep_capac['Percepción_1_5'], width, 
                    label='Percepción', color='#95E1D3')
    rects2 = ax.bar(x + width/2, percep_capac['Capacitación_1_5'], width, 
                    label='Capacitación', color='#F38181')
    
    ax.set_ylabel('Puntuación (1-5)', fontsize=12)
    ax.set_title('Percepción y Capacitación por Modelo de Seguridad', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(percep_capac['Modelo_Seguridad'])
    ax.legend()
    ax.set_ylim(0, 5)
    
    # Añadir valores en las barras
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10)
    
    autolabel(rects1)
    autolabel(rects2)
    
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig

def generar_visualizaciones():
    """Genera todas las visualizaciones y las guarda en archivos"""
    import os
    
    # Crear directorio de gráficos si no existe
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
    
    # Generar todos los gráficos
    figuras = [
        (generar_grafico_cajas_incidentes, 'incidentes_por_modelo'),
        (generar_grafico_tasa_bloqueo, 'tasa_bloqueo'),
        (generar_grafico_tiempos_respuesta, 'tiempos_respuesta'),
        (generar_grafico_percepcion_capacitacion, 'percepcion_capacitacion')
    ]
    
    for funcion, nombre in figuras:
        fig = funcion()
        fig.savefig(f'graficos/{nombre}.png', dpi=300, bbox_inches='tight')
        fig.savefig(f'graficos/{nombre}.pdf', bbox_inches='tight')
        plt.close(fig)
    
    print("✅ Todas las visualizaciones han sido generadas en la carpeta 'graficos/'")