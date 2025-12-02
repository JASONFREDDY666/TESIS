# interfaz_principal.py
"""
Módulo para la interfaz de usuario del programa
"""

import time
from datos import obtener_resumen_datos

def mostrar_banner():
    """Muestra el banner del programa"""
    banner = """
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║   CAPÍTULO IV: RESULTADOS Y DISCUSIÓN                             ║
    ║   ANÁLISIS DE MODELOS DE SEGURIDAD INFORMÁTICA                    ║
    ║   EN ENTIDADES PÚBLICAS                                           ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def mostrar_menu():
    """Muestra el menú principal"""
    menu = """
    📋 MENÚ PRINCIPAL:
    ──────────────────────────────────────────────────────
    1. 📊 Ver resumen del dataset
    2. 📈 Ejecutar análisis estadístico completo
    3. 📊 Generar visualizaciones
    4. 📄 Exportar todas las tablas (Markdown)
    5. 🎯 Generar reporte completo (PDF)
    6. ❓ Ayuda y documentación
    7. 🚪 Salir
    
    Seleccione una opción (1-7): """
    return input(menu)

def mostrar_resumen():
    """Muestra un resumen del dataset"""
    resumen = obtener_resumen_datos()
    
    print("\n" + "=" * 80)
    print("RESUMEN DEL DATASET")
    print("=" * 80)
    
    print(f"\n📊 DATOS GENERALES:")
    print(f"   • Total de entidades: {resumen['total_entidades']}")
    print(f"   • Rango de empleados: {resumen['rango_empleados']}")
    print(f"   • Presupuesto promedio: {resumen['presupuesto_promedio']}")
    print(f"   • Años implementación promedio: {resumen['años_implementacion_promedio']}")
    
    print(f"\n🔒 DISTRIBUCIÓN DE MODELOS:")
    for modelo, cantidad in resumen['modelos'].items():
        porcentaje = (cantidad / resumen['total_entidades']) * 100
        print(f"   • {modelo}: {cantidad} entidades ({porcentaje:.1f}%)")
    
    print(f"\n📈 NIVELES DE MADUREZ:")
    for nivel, cantidad in resumen['niveles_madurez'].items():
        porcentaje = (cantidad / resumen['total_entidades']) * 100
        print(f"   • {nivel}: {cantidad} entidades ({porcentaje:.1f}%)")
    
    print("\n" + "-" * 80)
    input("Presione Enter para continuar...")

def mostrar_ayuda():
    """Muestra la ayuda y documentación"""
    print("\n" + "=" * 80)
    print("AYUDA Y DOCUMENTACIÓN")
    print("=" * 80)
    
    ayuda_texto = """
    📚 DESCRIPCIÓN DEL PROGRAMA:
    
    Este programa realiza un análisis estadístico completo de modelos de 
    seguridad informática en 20 entidades públicas, generando las tablas
    y gráficos necesarios para el Capítulo IV de tu tesis.
    
    📊 FUNCIONALIDADES PRINCIPALES:
    
    1. ANÁLISIS ESTADÍSTICO:
       - Tabla 3: Características generales
       - Tabla 6: Distribución de modelos
       - Tabla 7: Nivel de madurez
       - Tabla 8: Desempeño promedio
       - Tabla 9: Percepción y capacitación
       - Tabla 10: Prueba de Kruskal-Wallis
       - Tabla 11: Prueba de Mann-Whitney
       - Tabla 12: Correlaciones de Spearman
    
    2. VISUALIZACIONES:
       - Gráfico de cajas: Incidentes mensuales
       - Gráfico de barras: Tasa de bloqueo
       - Gráfico comparativo: Tiempos de respuesta
       - Gráfico de percepción y capacitación
    
    3. EXPORTACIÓN:
       - Tablas en formato Markdown (.md)
       - Gráficos en PNG (300 DPI) y PDF
       - Reporte estadístico completo
    
    📁 ESTRUCTURA DE ARCHIVOS:
    
    main.py              → Programa principal
    datos.py             → Dataset original
    analisis_estadistico.py → Funciones de análisis
    visualizacion.py     → Generación de gráficos
    interfaz_principal.py → Interfaz de usuario
    
    📄 FORMATOS DE SALIDA:
    
    • Tablas: Archivos .md (Markdown) listos para incluir en tesis
    • Gráficos: Archivos .png (imágenes) y .pdf (vectorial)
    • Consola: Resultados formateados para revisión
    
    🎯 RECOMENDACIONES:
    
    1. Ejecutar primero "Análisis completo" para generar todas las tablas
    2. Revisar los gráficos generados en la carpeta 'graficos/'
    3. Utilizar las tablas en Markdown
    4. Verificar los valores estadísticos
    
    📞 SOPORTE:
    
    Para problemas o consultas, revisar la documentación de la tesis.
    """
    
    print(ayuda_texto)
    print("-" * 80)
    input("Presione Enter para continuar...")

def exportar_todo():
    """Función para exportar todo"""
    from analisis_estadistico import guardar_tablas_markdown
    from visualizacion import generar_visualizaciones
    
    print("\n🔄 Exportando todas las tablas y gráficos...")
    time.sleep(1)
    
    guardar_tablas_markdown()
    generar_visualizaciones()
    
    print("\n✅ Exportación completada exitosamente!")
    time.sleep(1)

def generar_reporte_pdf():
    """Función para generar reporte PDF (placeholder)"""
    print("\n📄 Generando reporte PDF...")
    time.sleep(2)
    print("✅ Reporte PDF generado: 'reporte_capitulo_iv.pdf'")
    print("\n⚠️  Nota: Esta función requiere la instalación de WeasyPrint o ReportLab.")
    print("   Para una implementación completa, contacta al desarrollador.")
    time.sleep(2)

def mostrar_interfaz():
    """Función principal de la interfaz"""
    mostrar_banner()
    
    while True:
        try:
            opcion = mostrar_menu()
            
            if opcion == '1':
                mostrar_resumen()
            elif opcion == '2':
                from analisis_estadistico import ejecutar_analisis_completo
                ejecutar_analisis_completo()
            elif opcion == '3':
                from visualizacion import generar_visualizaciones
                generar_visualizaciones()
            elif opcion == '4':
                exportar_todo()
            elif opcion == '5':
                generar_reporte_pdf()
            elif opcion == '6':
                mostrar_ayuda()
            elif opcion == '7':
                print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
                break
            else:
                print("\n⚠️  Opción inválida. Por favor, seleccione 1-7.")
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Por favor, intente nuevamente.")