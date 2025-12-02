# graficos_completos.py
"""
GRÁFICOS COMPLETOS PARA CAPÍTULO IV
8 gráficos profesionales para la tesis
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from analisis_estadistico import cargar_datos_originales
import os

# Configuración de estilo profesional
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'

def generar_grafico_incidentes():
    """Gráfico 1: Distribución de incidentes mensuales"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de cajas
    sns.boxplot(x='Modelo_Seguridad', y='Incidentes_Mensuales', 
                data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                ax=axes[0])
    sns.stripplot(x='Modelo_Seguridad', y='Incidentes_Mensuales', 
                  data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                  color='black', alpha=0.5, jitter=True, ax=axes[0])
    axes[0].set_title('Distribución de Incidentes Mensuales por Modelo', fontweight='bold')
    axes[0].set_xlabel('Modelo de Seguridad')
    axes[0].set_ylabel('Incidentes Mensuales')
    
    # Gráfico de barras con promedios
    promedios = df.groupby('Modelo_Seguridad')['Incidentes_Mensuales'].mean()
    promedios = promedios.reindex(['Perimetral', 'Híbrido', 'Zero Trust'])
    
    bars = axes[1].bar(promedios.index, promedios.values, 
                       color=['#e74c3c', '#3498db', '#2ecc71'])
    axes[1].set_title('Promedio de Incidentes Mensuales por Modelo', fontweight='bold')
    axes[1].set_xlabel('Modelo de Seguridad')
    axes[1].set_ylabel('Incidentes Mensuales (Promedio)')
    
    # Añadir valores en las barras
    for bar in bars:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height:.2f}', ha='center', va='bottom')
    
    plt.tight_layout()
    return fig

def generar_grafico_tasa_bloqueo():
    """Gráfico 2: Tasa de bloqueo por modelo"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de barras
    promedios = df.groupby('Modelo_Seguridad')['Tasa_Bloqueo_%'].mean()
    promedios = promedios.reindex(['Perimetral', 'Híbrido', 'Zero Trust'])
    
    colors = ['#e74c3c', '#3498db', '#2ecc71']
    bars = axes[0].bar(promedios.index, promedios.values, color=colors)
    axes[0].set_title('Tasa de Bloqueo Promedio por Modelo', fontweight='bold')
    axes[0].set_xlabel('Modelo de Seguridad')
    axes[0].set_ylabel('Tasa de Bloqueo (%)')
    axes[0].set_ylim(0, 100)
    
    # Añadir valores
    for bar, color in zip(bars, colors):
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height:.2f}%', ha='center', va='bottom', 
                    fontweight='bold', color=color)
    
    # Gráfico de violín
    sns.violinplot(x='Modelo_Seguridad', y='Tasa_Bloqueo_%', 
                   data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                   ax=axes[1])
    axes[1].set_title('Distribución de Tasas de Bloqueo', fontweight='bold')
    axes[1].set_xlabel('Modelo de Seguridad')
    axes[1].set_ylabel('Tasa de Bloqueo (%)')
    
    plt.tight_layout()
    return fig

def generar_grafico_tiempos():
    """Gráfico 3: Tiempos de respuesta y detección"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Tiempo de respuesta - Boxplot
    sns.boxplot(x='Modelo_Seguridad', y='Tiempo_Respuesta_min', 
                data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                ax=axes[0, 0])
    axes[0, 0].set_title('Tiempo de Respuesta por Modelo', fontweight='bold')
    axes[0, 0].set_xlabel('Modelo de Seguridad')
    axes[0, 0].set_ylabel('Minutos')
    
    # Tiempo de detección - Boxplot
    sns.boxplot(x='Modelo_Seguridad', y='Tiempo_Detección_min', 
                data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                ax=axes[0, 1])
    axes[0, 1].set_title('Tiempo de Detección por Modelo', fontweight='bold')
    axes[0, 1].set_xlabel('Modelo de Seguridad')
    axes[0, 1].set_ylabel('Minutos')
    
    # Comparación de promedios
    tiempos_avg = df.groupby('Modelo_Seguridad')[['Tiempo_Respuesta_min', 'Tiempo_Detección_min']].mean()
    tiempos_avg = tiempos_avg.reindex(['Perimetral', 'Híbrido', 'Zero Trust'])
    
    x = np.arange(len(tiempos_avg.index))
    width = 0.35
    
    axes[1, 0].bar(x - width/2, tiempos_avg['Tiempo_Respuesta_min'], width, 
                   label='Respuesta', color='#e74c3c')
    axes[1, 0].bar(x + width/2, tiempos_avg['Tiempo_Detección_min'], width, 
                   label='Detección', color='#3498db')
    axes[1, 0].set_title('Promedios de Tiempos por Modelo', fontweight='bold')
    axes[1, 0].set_xlabel('Modelo de Seguridad')
    axes[1, 0].set_ylabel('Minutos')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(tiempos_avg.index)
    axes[1, 0].legend()
    
    # Gráfico de radar para comparación
    from matplotlib.patches import Circle
    from matplotlib.path import Path
    from matplotlib.spines import Spine
    from matplotlib.projections.polar import PolarAxes
    from matplotlib.projections import register_projection
    
    # Datos normalizados para radar
    modelos = ['Perimetral', 'Híbrido', 'Zero Trust']
    metricas = ['Respuesta', 'Detección']
    
    datos_radar = []
    for modelo in modelos:
        subset = df[df['Modelo_Seguridad'] == modelo]
        datos_radar.append([
            subset['Tiempo_Respuesta_min'].mean(),
            subset['Tiempo_Detección_min'].mean()
        ])
    
    # Normalizar (invertir porque menor es mejor)
    datos_radar = np.array(datos_radar)
    datos_normalizados = 1 - (datos_radar / datos_radar.max(axis=0))
    
    # Configurar radar
    angles = np.linspace(0, 2*np.pi, len(metricas), endpoint=False).tolist()
    angles += angles[:1]
    
    ax_radar = axes[1, 1]
    ax_radar = plt.subplot(224, projection='polar')
    
    for i, modelo in enumerate(modelos):
        values = datos_normalizados[i].tolist()
        values += values[:1]
        ax_radar.plot(angles, values, 'o-', linewidth=2, label=modelo)
        ax_radar.fill(angles, values, alpha=0.1)
    
    ax_radar.set_xticks(angles[:-1])
    ax_radar.set_xticklabels(metricas)
    ax_radar.set_title('Comparación Relativa de Tiempos\n(Menor es mejor)', fontweight='bold', pad=20)
    ax_radar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    plt.tight_layout()
    return fig

def generar_grafico_percepcion_capacitacion():
    """Gráfico 4: Percepción y capacitación (¡!)"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Calcular promedios
    promedios = df.groupby('Modelo_Seguridad')[['Percepción_1_5', 'Capacitación_1_5']].mean()
    promedios = promedios.reindex(['Perimetral', 'Híbrido', 'Zero Trust'])
    
    # Gráfico de barras agrupadas
    x = np.arange(len(promedios.index))
    width = 0.35
    
    bars1 = axes[0].bar(x - width/2, promedios['Percepción_1_5'], width, 
                       label='Percepción', color='#3498db')
    bars2 = axes[0].bar(x + width/2, promedios['Capacitación_1_5'], width, 
                       label='Capacitación', color='#2ecc71')
    
    axes[0].set_title('Percepción y Capacitación por Modelo', 
                     fontweight='bold', color='#e74c3c')
    axes[0].set_xlabel('Modelo de Seguridad')
    axes[0].set_ylabel('Puntuación (1-5)')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(promedios.index)
    axes[0].legend()
    axes[0].set_ylim(0, 5)
    
    # Añadir valores exactos
    for bars, offset in zip([bars1, bars2], [-width/2, width/2]):
        for bar in bars:
            height = bar.get_height()
            axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        f'{height:.4f}', ha='center', va='bottom', fontsize=9)
    
    # Gráfico de líneas
    axes[1].plot(promedios.index, promedios['Percepción_1_5'], 
                'o-', linewidth=3, markersize=10, label='Percepción', color='#3498db')
    axes[1].plot(promedios.index, promedios['Capacitación_1_5'], 
                's-', linewidth=3, markersize=10, label='Capacitación', color='#2ecc71')
    
    axes[1].set_title('Evolución de Percepción y Capacitación', fontweight='bold')
    axes[1].set_xlabel('Modelo de Seguridad')
    axes[1].set_ylabel('Puntuación (1-5)')
    axes[1].legend()
    axes[1].set_ylim(0, 5)
    axes[1].grid(True, alpha=0.3)
    
    # Añadir anotaciones de corrección
    axes[1].text(0.5, 0.95, '¡VALORES!', 
                transform=axes[1].transAxes, fontsize=12, 
                fontweight='bold', color='#e74c3c',
                ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    return fig

def generar_grafico_madurez():
    """Gráfico 5: Nivel de madurez por modelo"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Distribución de niveles de madurez
    madurez_counts = df.groupby(['Modelo_Seguridad', 'Nivel_Madurez']).size().unstack(fill_value=0)
    madurez_counts = madurez_counts.reindex(['Perimetral', 'Híbrido', 'Zero Trust'])
    madurez_counts = madurez_counts[['Bajo', 'Medio', 'Alto']]
    
    # Gráfico de barras apiladas
    madurez_counts.plot(kind='bar', stacked=True, ax=axes[0],
                       color=['#e74c3c', '#f39c12', '#2ecc71'])
    axes[0].set_title('Distribución de Niveles de Madurez por Modelo', fontweight='bold')
    axes[0].set_xlabel('Modelo de Seguridad')
    axes[0].set_ylabel('Número de Entidades')
    axes[0].legend(title='Nivel de Madurez')
    
    # Años de implementación vs Madurez
    sns.scatterplot(x='Años_Implementación', y='Nivel_Madurez', 
                   hue='Modelo_Seguridad', size='Especialistas',
                   sizes=(50, 300), data=df, ax=axes[1])
    axes[1].set_title('Años de Implementación vs Nivel de Madurez', fontweight='bold')
    axes[1].set_xlabel('Años de Implementación')
    axes[1].set_ylabel('Nivel de Madurez')
    axes[1].legend(title='Modelo', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Añadir línea de tendencia
    from scipy import stats
    
    # Convertir madurez a numérico
    madurez_map = {'Bajo': 1, 'Medio': 2, 'Alto': 3}
    df['Madurez_Num'] = df['Nivel_Madurez'].map(madurez_map)
    
    for modelo in ['Perimetral', 'Híbrido', 'Zero Trust']:
        subset = df[df['Modelo_Seguridad'] == modelo]
        if len(subset) > 1:
            slope, intercept, r_value, p_value, std_err = stats.linregress(
                subset['Años_Implementación'], subset['Madurez_Num'])
            x_vals = np.array([subset['Años_Implementación'].min(), 
                              subset['Años_Implementación'].max()])
            y_vals = intercept + slope * x_vals
            axes[1].plot(x_vals, y_vals, '--', alpha=0.7)
    
    plt.tight_layout()
    return fig

def generar_grafico_especialistas():
    """Gráfico 6: Especialistas por modelo"""
    df = cargar_datos_originales()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Boxplot de especialistas
    sns.boxplot(x='Modelo_Seguridad', y='Especialistas', 
                data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                ax=axes[0])
    sns.stripplot(x='Modelo_Seguridad', y='Especialistas', 
                  data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                  color='black', alpha=0.5, jitter=True, ax=axes[0])
    axes[0].set_title('Distribución de Especialistas por Modelo', fontweight='bold')
    axes[0].set_xlabel('Modelo de Seguridad')
    axes[0].set_ylabel('Número de Especialistas')
    
    # Relación con presupuesto
    scatter = axes[1].scatter(df['Presupuesto_Seguridad_USD'], df['Especialistas'],
                             c=df['Modelo_Seguridad'].map({'Perimetral': 0, 'Híbrido': 1, 'Zero Trust': 2}),
                             s=df['Especialistas']*30, alpha=0.7,
                             cmap='viridis')
    axes[1].set_title('Relación: Presupuesto vs Especialistas', fontweight='bold')
    axes[1].set_xlabel('Presupuesto de Seguridad (USD)')
    axes[1].set_ylabel('Número de Especialistas')
    
    # Añadir etiquetas para puntos extremos
    for idx, row in df.nlargest(3, 'Especialistas').iterrows():
        axes[1].annotate(row['Entidad'], 
                        (row['Presupuesto_Seguridad_USD'], row['Especialistas']),
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=9, fontweight='bold')
    
    # Crear leyenda manual
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Perimetral',
               markerfacecolor='#440154', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Híbrido',
               markerfacecolor='#21918c', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Zero Trust',
               markerfacecolor='#fde725', markersize=10)
    ]
    axes[1].legend(handles=legend_elements, title='Modelo')
    
    plt.tight_layout()
    return fig

def generar_grafico_correlaciones():
    """Gráfico 7: Mapa de correlaciones"""
    df = cargar_datos_originales()
    
    # Preparar datos para correlación
    df_corr = df.copy()
    
    # Convertir variables categóricas a numéricas
    madurez_map = {'Bajo': 1, 'Medio': 2, 'Alto': 3}
    df_corr['Nivel_Madurez_Num'] = df_corr['Nivel_Madurez'].map(madurez_map)
    
    frecuencia_map = {'Anual': 1, 'Semestral': 2, 'Trimestral': 4, 'Mensual': 12}
    df_corr['Frecuencia_Num'] = df_corr['Frecuencia_Simulacros'].map(frecuencia_map)
    
    # Seleccionar variables para correlación
    variables_corr = [
        'Años_Implementación',
        'Nivel_Madurez_Num',
        'Incidentes_Mensuales',
        'Tasa_Bloqueo_%',
        'Tiempo_Respuesta_min',
        'Tiempo_Detección_min',
        'Percepción_1_5',
        'Capacitación_1_5',
        'Especialistas',
        'Presupuesto_Seguridad_USD',
        'Frecuencia_Num'
    ]
    
    nombres_amigables = {
        'Años_Implementación': 'Años Imp.',
        'Nivel_Madurez_Num': 'Madurez',
        'Incidentes_Mensuales': 'Incidentes',
        'Tasa_Bloqueo_%': 'Tasa Bloqueo',
        'Tiempo_Respuesta_min': 'T. Respuesta',
        'Tiempo_Detección_min': 'T. Detección',
        'Percepción_1_5': 'Percepción',
        'Capacitación_1_5': 'Capacitación',
        'Especialistas': 'Especialistas',
        'Presupuesto_Seguridad_USD': 'Presupuesto',
        'Frecuencia_Num': 'Frec. Simul.'
    }
    
    # Calcular matriz de correlación
    corr_matrix = df_corr[variables_corr].corr(method='spearman')
    
    # Renombrar
    corr_matrix.index = [nombres_amigables.get(col, col) for col in corr_matrix.index]
    corr_matrix.columns = [nombres_amigables.get(col, col) for col in corr_matrix.columns]
    
    # Crear gráfico
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Usar seaborn para heatmap
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', 
                cmap='RdBu_r', center=0, square=True,
                linewidths=1, cbar_kws={"shrink": .8}, ax=ax)
    
    ax.set_title('Mapa de Correlaciones de Spearman\n(Variables Técnicas y Organizacionales)', 
                fontweight='bold', fontsize=14, pad=20)
    
    plt.tight_layout()
    return fig

def generar_grafico_boxplot_completo():
    """Gráfico 8: Boxplot completo de métricas por modelo"""
    df = cargar_datos_originales()
    
    # Seleccionar métricas clave
    metricas = [
        'Incidentes_Mensuales',
        'Tasa_Bloqueo_%',
        'Tiempo_Respuesta_min',
        'Tiempo_Detección_min',
        'Percepción_1_5',
        'Capacitación_1_5',
        'Especialistas'
    ]
    
    nombres_metricas = {
        'Incidentes_Mensuales': 'Incidentes Mensuales',
        'Tasa_Bloqueo_%': 'Tasa de Bloqueo (%)',
        'Tiempo_Respuesta_min': 'Tiempo Respuesta (min)',
        'Tiempo_Detección_min': 'Tiempo Detección (min)',
        'Percepción_1_5': 'Percepción (1-5)',
        'Capacitación_1_5': 'Capacitación (1-5)',
        'Especialistas': 'Especialistas'
    }
    
    # Crear subplots
    fig, axes = plt.subplots(3, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    for i, metrica in enumerate(metricas):
        if i < len(axes):
            # Boxplot por modelo
            sns.boxplot(x='Modelo_Seguridad', y=metrica, 
                       data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                       ax=axes[i])
            
            # Añadir puntos individuales
            sns.stripplot(x='Modelo_Seguridad', y=metrica, 
                         data=df, order=['Perimetral', 'Híbrido', 'Zero Trust'],
                         color='black', alpha=0.5, jitter=True, 
                         size=4, ax=axes[i])
            
            axes[i].set_title(nombres_metricas[metrica], fontweight='bold')
            axes[i].set_xlabel('')
            
            # Añadir líneas de referencia según la métrica
            if 'Percepción' in metrica or 'Capacitación' in metrica:
                axes[i].axhline(y=3, color='r', linestyle='--', alpha=0.3, label='Punto medio (3)')
                axes[i].legend(fontsize=8)
    
    # Ocultar ejes vacíos
    for i in range(len(metricas), len(axes)):
        axes[i].set_visible(False)
    
    fig.suptitle('Comparación Completa de Métricas por Modelo de Seguridad', 
                fontweight='bold', fontsize=16, y=1.02)
    
    plt.tight_layout()
    return fig

def generar_todos_graficos():
    """Genera y guarda todos los gráficos"""
    from analisis_estadistico import crear_carpetas_exportacion
    crear_carpetas_exportacion()
    
    # Lista de funciones de gráficos
    funciones_graficos = [
        ('1_incidentes', generar_grafico_incidentes),
        ('2_tasa_bloqueo', generar_grafico_tasa_bloqueo),
        ('3_tiempos', generar_grafico_tiempos),
        ('4_percepcion_capacitacion', generar_grafico_percepcion_capacitacion),
        ('5_madurez', generar_grafico_madurez),
        ('6_especialistas', generar_grafico_especialistas),
        ('7_correlaciones', generar_grafico_correlaciones),
        ('8_boxplot_completo', generar_grafico_boxplot_completo)
    ]
    
    print("📊 Generando todos los gráficos...")
    
    for nombre, funcion in funciones_graficos:
        try:
            print(f"  • Generando {nombre}...")
            fig = funcion()
            
            # Guardar en alta resolución
            fig.savefig(f'exportacion_capitulo_iv/graficos/{nombre}.png', 
                       dpi=300, bbox_inches='tight')
            fig.savefig(f'exportacion_capitulo_iv/graficos/{nombre}.pdf', 
                       bbox_inches='tight')
            
            plt.close(fig)
            print(f"    ✅ Guardado: {nombre}.png/.pdf")
            
        except Exception as e:
            print(f"    ❌ Error en {nombre}: {str(e)}")
    
    print("\n✅ Todos los gráficos generados exitosamente!")
    print("📁 Guardados en: 'exportacion_capitulo_iv/graficos/'")
    
    return True

# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("GENERADOR DE GRÁFICOS - CAPÍTULO IV")
    print("=" * 80)
    
    # Generar todos los gráficos
    generar_todos_graficos()
    
    print("\n🎯 Gráficos disponibles:")
    print("  1. Incidentes por modelo")
    print("  2. Tasa de bloqueo")
    print("  3. Tiempos de respuesta y detección")
    print("  4. Percepción y capacitación")
    print("  5. Nivel de madurez")
    print("  6. Especialistas por modelo")
    print("  7. Mapa de correlaciones")
    print("  8. Boxplot completo")
    
    print("\n✅ Proceso completado!")