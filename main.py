# main.py
"""
Programa principal con interfaz gráfica para análisis estadístico
CAPÍTULO IV: RESULTADOS Y DISCUSIÓN - VERSIÓN CORREGIDA
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import pandas as pd
import numpy as np
import threading
import os
import sys

# Configurar para evitar problemas con matplotlib
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

# Importar funciones
from analisis_estadistico import (
    generar_tabla3, generar_tabla6, generar_tabla7, generar_tabla8,
    generar_tabla9, generar_tabla10, generar_tabla11, generar_tabla12,
    guardar_todas_tablas, crear_carpetas_exportacion
)

from graficos_completos import (
    generar_grafico_incidentes, generar_grafico_tasa_bloqueo,
    generar_grafico_tiempos, generar_grafico_percepcion_capacitacion,
    generar_grafico_madurez, generar_grafico_especialistas,
    generar_grafico_correlaciones, generar_grafico_boxplot_completo,
    generar_todos_graficos
)

class AplicacionTesisCorregida:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 CAPÍTULO IV: RESULTADOS Y DISCUSIÓN")
        self.root.geometry("1300x800")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.tabla_actual = None
        self.figura_actual = None
        self.canvas_actual = None
        self.toolbar_actual = None
        
        # Configurar icono
        try:
            self.root.iconbitmap('icono.ico')
        except:
            pass
        
        # Crear carpetas necesarias
        crear_carpetas_exportacion()
        
        # Crear interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barra superior
        self.crear_barra_superior(main_frame)
        
        # Área principal
        paned_window = tk.PanedWindow(main_frame, orient=tk.HORIZONTAL, bg='#34495e', sashwidth=10)
        paned_window.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Panel izquierdo (botones)
        left_frame = tk.Frame(paned_window, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        paned_window.add(left_frame, minsize=350)
        
        # Panel derecho (resultados)
        right_frame = tk.Frame(paned_window, bg='#ffffff', relief=tk.RAISED, bd=2)
        paned_window.add(right_frame, minsize=900)
        
        # Crear paneles
        self.crear_panel_botones(left_frame)
        self.crear_panel_resultados(right_frame)
        
    def crear_barra_superior(self, parent):
        # Frame para la barra superior
        top_frame = tk.Frame(parent, bg='#1a252f', height=100)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        top_frame.pack_propagate(False)
        
        # Título principal
        title_label = tk.Label(top_frame, 
                              text="📊 CAPÍTULO IV: RESULTADOS Y DISCUSIÓN",
                              font=('Arial', 18, 'bold'),
                              fg='#ecf0f1',
                              bg='#1a252f')
        title_label.pack(side=tk.LEFT, padx=30, pady=20)
        
        # Subtítulo
        subtitle_label = tk.Label(top_frame,
                                 text="Análisis Estadístico - Modelos de Seguridad Informática",
                                 font=('Arial', 11),
                                 fg='#bdc3c7',
                                 bg='#1a252f')
        subtitle_label.pack(side=tk.LEFT, pady=20)
        
        # Botones de acción en la barra superior
        button_frame = tk.Frame(top_frame, bg='#1a252f')
        button_frame.pack(side=tk.RIGHT, padx=20, pady=20)
        
        # Botón de exportar todo
        export_btn = tk.Button(button_frame,
                              text="📥 EXPORTAR TODO",
                              font=('Arial', 10, 'bold'),
                              bg='#27ae60',
                              fg='white',
                              relief=tk.RAISED,
                              padx=15,
                              pady=8,
                              command=self.exportar_todo)
        export_btn.pack(side=tk.LEFT, padx=5)
        
        # Botón de recalcular
        refresh_btn = tk.Button(button_frame,
                               text="🔄 RECALCULAR",
                               font=('Arial', 10, 'bold'),
                               bg='#3498db',
                               fg='white',
                               relief=tk.RAISED,
                               padx=15,
                               pady=8,
                               command=self.recalcular_todo)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Botón de verificación
        verify_btn = tk.Button(button_frame,
                              text="✅ VERIFICAR CÁLCULOS",
                              font=('Arial', 10, 'bold'),
                              bg='#f39c12',
                              fg='white',
                              relief=tk.RAISED,
                              padx=15,
                              pady=8,
                              command=self.verificar_calculos)
        verify_btn.pack(side=tk.LEFT, padx=5)
        
    def crear_panel_botones(self, parent):
        # Canvas con scroll para los botones
        canvas = tk.Canvas(parent, bg='#ecf0f1', highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#ecf0f1')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Título del panel
        title_label = tk.Label(scrollable_frame,
                              text="📋 TABLAS ESTADÍSTICAS",
                              font=('Arial', 14, 'bold'),
                              bg='#2c3e50',
                              fg='white',
                              padx=15,
                              pady=12)
        title_label.pack(fill=tk.X, pady=(0, 10))
        
        # Botones para las tablas (con colores diferenciados)
        botones_tablas = [
            ("📊 Tabla 3: Características generales", self.mostrar_tabla3, '#3498db'),
            ("📈 Tabla 6: Distribución de modelos", self.mostrar_tabla6, '#2ecc71'),
            ("🎯 Tabla 7: Nivel de madurez", self.mostrar_tabla7, '#e74c3c'),
            ("⚡ Tabla 8: Desempeño promedio", self.mostrar_tabla8, '#9b59b6'),
            ("👥 Tabla 9: Percepción y capacitación", self.mostrar_tabla9, '#1abc9c'),
            ("📊 Tabla 10: Kruskal-Wallis", self.mostrar_tabla10, '#f39c12'),
            ("🔍 Tabla 11: Mann-Whitney", self.mostrar_tabla11, '#e67e22'),
            ("📊 Tabla 12: Correlaciones", self.mostrar_tabla12, '#34495e'),
        ]
        
        for texto, comando, color in botones_tablas:
            btn_frame = tk.Frame(scrollable_frame, bg='#ecf0f1')
            btn_frame.pack(fill=tk.X, padx=15, pady=3)
            
            btn = tk.Button(btn_frame,
                           text=texto,
                           font=('Arial', 11),
                           bg=color,
                           fg='white',
                           relief=tk.RAISED,
                           bd=2,
                           padx=20,
                           pady=12,
                           command=comando,
                           anchor='w',
                           justify='left')
            btn.pack(fill=tk.X)
            
            # Añadir tooltip
            self.crear_tooltip(btn, f"Muestra {texto.split(':')[0]}")
        
        # Separador
        separator = tk.Frame(scrollable_frame, height=2, bg='#bdc3c7')
        separator.pack(fill=tk.X, padx=20, pady=15)
        
        # Título para gráficos
        title_graf = tk.Label(scrollable_frame,
                             text="📊 GRÁFICOS Y VISUALIZACIONES",
                             font=('Arial', 14, 'bold'),
                             bg='#2c3e50',
                             fg='white',
                             padx=15,
                             pady=12)
        title_graf.pack(fill=tk.X, pady=(0, 10))
        
        # Botones para gráficos
        botones_graficos = [
            ("📉 Incidentes por modelo", self.mostrar_grafico_incidentes, '#e74c3c'),
            ("📊 Tasa de bloqueo", self.mostrar_grafico_tasa_bloqueo, '#3498db'),
            ("⏱️ Tiempos de respuesta", self.mostrar_grafico_tiempos, '#2ecc71'),
            ("👤 Percepción y capacitación", self.mostrar_grafico_percepcion, '#9b59b6'),
            ("📈 Nivel de madurez", self.mostrar_grafico_madurez, '#1abc9c'),
            ("👥 Especialistas por modelo", self.mostrar_grafico_especialistas, '#f39c12'),
            ("📊 Correlaciones", self.mostrar_grafico_correlaciones, '#34495e'),
            ("📦 Boxplot completo", self.mostrar_grafico_boxplot, '#e67e22'),
        ]
        
        for texto, comando, color in botones_graficos:
            btn_frame = tk.Frame(scrollable_frame, bg='#ecf0f1')
            btn_frame.pack(fill=tk.X, padx=15, pady=3)
            
            btn = tk.Button(btn_frame,
                           text=texto,
                           font=('Arial', 11),
                           bg=color,
                           fg='white',
                           relief=tk.RAISED,
                           bd=2,
                           padx=20,
                           pady=12,
                           command=comando,
                           anchor='w',
                           justify='left')
            btn.pack(fill=tk.X)
            
            # Añadir tooltip
            self.crear_tooltip(btn, f"Genera gráfico: {texto}")
        
        # Separador
        separator2 = tk.Frame(scrollable_frame, height=2, bg='#bdc3c7')
        separator2.pack(fill=tk.X, padx=20, pady=15)
        
        # Botones de utilidad
        util_buttons = [
            ("📋 Ver dataset completo", self.mostrar_dataset, '#2c3e50'),
            ("📊 Generar todos los gráficos", self.generar_todos_graficos, '#27ae60'),
            ("📄 Generar reporte PDF", self.generar_reporte_pdf, '#e74c3c'),
            ("ℹ️  Acerca de / Ayuda", self.mostrar_ayuda, '#3498db'),
        ]
        
        for texto, comando, color in util_buttons:
            btn_frame = tk.Frame(scrollable_frame, bg='#ecf0f1')
            btn_frame.pack(fill=tk.X, padx=15, pady=3)
            
            btn = tk.Button(btn_frame,
                           text=texto,
                           font=('Arial', 10, 'bold'),
                           bg=color,
                           fg='white',
                           relief=tk.RAISED,
                           padx=20,
                           pady=10,
                           command=comando)
            btn.pack(fill=tk.X)
        
    def crear_panel_resultados(self, parent):
        # Notebook para pestañas
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestañas
        self.tab_tabla = tk.Frame(self.notebook, bg='#ffffff')
        self.tab_grafico = tk.Frame(self.notebook, bg='#ffffff')
        self.tab_texto = tk.Frame(self.notebook, bg='#ffffff')
        self.tab_dataset = tk.Frame(self.notebook, bg='#ffffff')
        
        self.notebook.add(self.tab_tabla, text="📋 Tabla Actual")
        self.notebook.add(self.tab_grafico, text="📊 Gráfico Actual")
        self.notebook.add(self.tab_texto, text="📄 Información")
        self.notebook.add(self.tab_dataset, text="📁 Dataset Completo")
        
        # Configurar cada pestaña
        self.configurar_pestana_tabla()
        self.configurar_pestana_grafico()
        self.configurar_pestana_texto()
        self.configurar_pestana_dataset()
        
    def configurar_pestana_tabla(self):
        # Frame para controles de tabla
        controls_frame = tk.Frame(self.tab_tabla, bg='#ecf0f1', height=40)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        controls_frame.pack_propagate(False)
        
        # Botones de control
        btn_style = {'font': ('Arial', 9), 'padx': 10, 'pady': 5}
        
        self.export_table_btn = tk.Button(controls_frame,
                                         text="💾 Exportar tabla (CSV)",
                                         bg='#27ae60',
                                         fg='white',
                                         state=tk.DISABLED,
                                         command=self.exportar_tabla_actual,
                                         **btn_style)
        self.export_table_btn.pack(side=tk.LEFT, padx=2)
        
        self.export_excel_btn = tk.Button(controls_frame,
                                         text="📊 Exportar tabla (Excel)",
                                         bg='#2980b9',
                                         fg='white',
                                         state=tk.DISABLED,
                                         command=self.exportar_excel_actual,
                                         **btn_style)
        self.export_excel_btn.pack(side=tk.LEFT, padx=2)
        
        self.copy_btn = tk.Button(controls_frame,
                                 text="📋 Copiar al portapapeles",
                                 bg='#3498db',
                                 fg='white',
                                 state=tk.DISABLED,
                                 command=self.copiar_tabla,
                                 **btn_style)
        self.copy_btn.pack(side=tk.LEFT, padx=2)
        
        self.print_btn = tk.Button(controls_frame,
                                  text="🖨️  Imprimir valores",
                                  bg='#9b59b6',
                                  fg='white',
                                  state=tk.DISABLED,
                                  command=self.imprimir_valores,
                                  **btn_style)
        self.print_btn.pack(side=tk.LEFT, padx=2)
        
        # Área para mostrar tabla
        table_frame = tk.Frame(self.tab_tabla, bg='#ffffff')
        table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
        # Crear Treeview con scrollbars
        self.tree_scroll_y = ttk.Scrollbar(table_frame)
        self.tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree_scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        self.tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(table_frame,
                                yscrollcommand=self.tree_scroll_y.set,
                                xscrollcommand=self.tree_scroll_x.set,
                                selectmode='browse')
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.tree_scroll_y.config(command=self.tree.yview)
        self.tree_scroll_x.config(command=self.tree.xview)
        
        # Configurar estilos
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        style.configure("Treeview", font=('Arial', 10), rowheight=25)
        
    def configurar_pestana_grafico(self):
        # Frame para controles de gráfico
        controls_frame = tk.Frame(self.tab_grafico, bg='#ecf0f1', height=40)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        controls_frame.pack_propagate(False)
        
        btn_style = {'font': ('Arial', 9), 'padx': 10, 'pady': 5}
        
        self.export_graph_btn = tk.Button(controls_frame,
                                         text="💾 Exportar gráfico (PNG)",
                                         bg='#27ae60',
                                         fg='white',
                                         state=tk.DISABLED,
                                         command=self.exportar_grafico_actual,
                                         **btn_style)
        self.export_graph_btn.pack(side=tk.LEFT, padx=2)
        
        self.export_pdf_btn = tk.Button(controls_frame,
                                       text="📄 Exportar gráfico (PDF)",
                                       bg='#e74c3c',
                                       fg='white',
                                       state=tk.DISABLED,
                                       command=self.exportar_pdf_actual,
                                       **btn_style)
        self.export_pdf_btn.pack(side=tk.LEFT, padx=2)
        
        self.refresh_graph_btn = tk.Button(controls_frame,
                                          text="🔄 Actualizar gráfico",
                                          bg='#3498db',
                                          fg='white',
                                          state=tk.DISABLED,
                                          command=self.actualizar_grafico,
                                          **btn_style)
        self.refresh_graph_btn.pack(side=tk.LEFT, padx=2)
        
        # Área para mostrar gráfico
        self.graph_frame = tk.Frame(self.tab_grafico, bg='#ffffff')
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
    def configurar_pestana_texto(self):
        # Área de texto con scroll
        self.text_area = scrolledtext.ScrolledText(self.tab_texto,
                                                  wrap=tk.WORD,
                                                  font=('Consolas', 10),
                                                  bg='#f8f9fa',
                                                  fg='#2c3e50',
                                                  padx=10,
                                                  pady=10)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Frame para controles
        controls_frame = tk.Frame(self.tab_texto, bg='#ecf0f1', height=40)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        controls_frame.pack_propagate(False)
        
        save_btn = tk.Button(controls_frame,
                            text="💾 Guardar como texto",
                            font=('Arial', 9),
                            bg='#27ae60',
                            fg='white',
                            padx=10,
                            pady=5,
                            command=self.guardar_texto)
        save_btn.pack(side=tk.LEFT, padx=2)
        
        clear_btn = tk.Button(controls_frame,
                             text="🗑️  Limpiar",
                             font=('Arial', 9),
                             bg='#e74c3c',
                             fg='white',
                             padx=10,
                             pady=5,
                             command=self.limpiar_texto)
        clear_btn.pack(side=tk.LEFT, padx=2)
        
        copy_text_btn = tk.Button(controls_frame,
                                 text="📋 Copiar texto",
                                 font=('Arial', 9),
                                 bg='#3498db',
                                 fg='white',
                                 padx=10,
                                 pady=5,
                                 command=self.copiar_texto)
        copy_text_btn.pack(side=tk.LEFT, padx=2)
        
    def configurar_pestana_dataset(self):
        # Frame para mostrar dataset
        dataset_frame = tk.Frame(self.tab_dataset, bg='#ffffff')
        dataset_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbars
        y_scrollbar = ttk.Scrollbar(dataset_frame)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        x_scrollbar = ttk.Scrollbar(dataset_frame, orient=tk.HORIZONTAL)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview para dataset
        self.dataset_tree = ttk.Treeview(dataset_frame,
                                        yscrollcommand=y_scrollbar.set,
                                        xscrollcommand=x_scrollbar.set,
                                        selectmode='extended')
        self.dataset_tree.pack(fill=tk.BOTH, expand=True)
        
        y_scrollbar.config(command=self.dataset_tree.yview)
        x_scrollbar.config(command=self.dataset_tree.xview)
        
        # Cargar dataset
        self.cargar_dataset()
        
    def crear_tooltip(self, widget, text):
        """Crea un tooltip para un widget"""
        def enter(event):
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(self.tooltip, text=text, 
                            background="#ffffe0", 
                            relief="solid", 
                            borderwidth=1,
                            font=("Arial", 8))
            label.pack()
        
        def leave(event):
            if hasattr(self, 'tooltip'):
                self.tooltip.destroy()
        
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)
    
    # ============================================================================
    # FUNCIONES PARA MOSTRAR TABLAS
    # ============================================================================
    
    def mostrar_tabla3(self):
        tabla = generar_tabla3()
        self.mostrar_tabla_generica(tabla, "Tabla 3: Características generales de las entidades evaluadas")
    
    def mostrar_tabla6(self):
        tabla = generar_tabla6()
        self.mostrar_tabla_generica(tabla, "Tabla 6: Distribución de modelos de seguridad en las entidades públicas")
    
    def mostrar_tabla7(self):
        tabla = generar_tabla7()
        self.mostrar_tabla_generica(tabla, "Tabla 7: Nivel de madurez del modelo de seguridad según años de implementación")
    
    def mostrar_tabla8(self):
        tabla = generar_tabla8()
        self.mostrar_tabla_generica(tabla, "Tabla 8: Desempeño promedio de los modelos de seguridad")
    
    def mostrar_tabla9(self):
        tabla = generar_tabla9()
        self.mostrar_tabla_generica(tabla, "Tabla 9: Indicadores de percepción y capacitación del personal")
    
    def mostrar_tabla10(self):
        tabla = generar_tabla10()
        self.mostrar_tabla_generica(tabla, "Tabla 10: Prueba de Kruskal–Wallis para métricas de desempeño")
    
    def mostrar_tabla11(self):
        tabla = generar_tabla11()
        self.mostrar_tabla_generica(tabla, "Tabla 11: Comparaciones pareadas entre modelos de seguridad")
    
    def mostrar_tabla12(self):
        tabla = generar_tabla12()
        self.mostrar_tabla_generica(tabla, "Tabla 12: Correlaciones de Spearman entre variables organizacionales y técnicas")
    
    def mostrar_tabla_generica(self, dataframe, titulo):
        """Muestra una tabla genérica en el Treeview"""
        # Limpiar tabla anterior
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Configurar columnas
        columnas = list(dataframe.columns)
        self.tree["columns"] = columnas
        self.tree["show"] = "headings"
        
        # Configurar encabezados
        for col in columnas:
            self.tree.heading(col, text=col)
            # Ajustar ancho según contenido
            max_len = max(len(str(col)), dataframe[col].astype(str).str.len().max())
            width = min(max_len * 9, 200)  # Ancho máximo de 200
            self.tree.column(col, width=width, minwidth=50, anchor=tk.CENTER)
        
        # Insertar datos
        for index, row in dataframe.iterrows():
            self.tree.insert("", "end", values=list(row))
        
        # Actualizar estado de botones
        self.export_table_btn.config(state=tk.NORMAL)
        self.export_excel_btn.config(state=tk.NORMAL)
        self.copy_btn.config(state=tk.NORMAL)
        self.print_btn.config(state=tk.NORMAL)
        self.tabla_actual = (dataframe, titulo)
        
        # Cambiar a pestaña de tabla
        self.notebook.select(self.tab_tabla)
        
        # Mostrar información en texto
        info_text = f"{titulo}\n\n"
        info_text += dataframe.to_string(index=False, float_format=lambda x: f"{x:.4f}" if isinstance(x, float) else str(x))
        info_text += f"\n\n📊 Dimensiones: {dataframe.shape[0]} filas × {dataframe.shape[1]} columnas"
        self.mostrar_texto_info(info_text)
    
    # ============================================================================
    # FUNCIONES PARA MOSTRAR GRÁFICOS
    # ============================================================================
    
    def mostrar_grafico_incidentes(self):
        self.mostrar_grafico_generico(generar_grafico_incidentes, 
                                     "Distribución de Incidentes Mensuales por Modelo de Seguridad")
    
    def mostrar_grafico_tasa_bloqueo(self):
        self.mostrar_grafico_generico(generar_grafico_tasa_bloqueo,
                                     "Tasa de Bloqueo Promedio por Modelo de Seguridad")
    
    def mostrar_grafico_tiempos(self):
        self.mostrar_grafico_generico(generar_grafico_tiempos,
                                     "Tiempos de Respuesta y Detección por Modelo de Seguridad")
    
    def mostrar_grafico_percepcion(self):
        self.mostrar_grafico_generico(generar_grafico_percepcion_capacitacion,
                                     "Percepción y Capacitación por Modelo de Seguridad")
    
    def mostrar_grafico_madurez(self):
        self.mostrar_grafico_generico(generar_grafico_madurez,
                                     "Nivel de Madurez por Modelo de Seguridad")
    
    def mostrar_grafico_especialistas(self):
        self.mostrar_grafico_generico(generar_grafico_especialistas,
                                     "Especialistas por Modelo de Seguridad")
    
    def mostrar_grafico_correlaciones(self):
        self.mostrar_grafico_generico(generar_grafico_correlaciones,
                                     "Mapa de Correlaciones entre Variables")
    
    def mostrar_grafico_boxplot(self):
        self.mostrar_grafico_generico(generar_grafico_boxplot_completo,
                                     "Boxplot Completo de Métricas por Modelo")
    
    def mostrar_grafico_generico(self, funcion_grafico, titulo):
        """Muestra un gráfico genérico en el panel"""
        # Limpiar gráfico anterior
        self.limpiar_grafico_actual()
        
        # Generar gráfico
        try:
            self.figura_actual = funcion_grafico()
            
            # Crear canvas para el gráfico
            self.canvas_actual = FigureCanvasTkAgg(self.figura_actual, self.graph_frame)
            self.canvas_actual.draw()
            
            # Crear toolbar de navegación
            self.toolbar_actual = NavigationToolbar2Tk(self.canvas_actual, self.graph_frame)
            self.toolbar_actual.update()
            
            # Empaquetar toolbar y canvas
            self.canvas_actual.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Actualizar estado de botones
            self.export_graph_btn.config(state=tk.NORMAL)
            self.export_pdf_btn.config(state=tk.NORMAL)
            self.refresh_graph_btn.config(state=tk.NORMAL)
            
            # Cambiar a pestaña de gráfico
            self.notebook.select(self.tab_grafico)
            
            # Mostrar mensaje
            self.mostrar_texto_info(f"📊 Gráfico generado: {titulo}\n\nEl gráfico está listo para visualización. Use la barra de herramientas para navegar, hacer zoom y guardar.")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el gráfico:\n{str(e)}")
    
    def limpiar_grafico_actual(self):
        """Limpia el gráfico actual"""
        if self.toolbar_actual:
            self.toolbar_actual.destroy()
            self.toolbar_actual = None
        
        if self.canvas_actual:
            self.canvas_actual.get_tk_widget().destroy()
            self.canvas_actual = None
    
    def actualizar_grafico(self):
        """Actualiza el gráfico actual"""
        if self.figura_actual:
            self.figura_actual = self.figura_actual
            if self.canvas_actual:
                self.canvas_actual.draw()
    
    # ============================================================================
    # FUNCIONES DE EXPORTACIÓN
    # ============================================================================
    
    def exportar_tabla_actual(self):
        """Exporta la tabla actual a CSV"""
        if self.tabla_actual:
            dataframe, titulo = self.tabla_actual
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                initialfile=f"{titulo[:30].replace(':', '').replace('/', '_')}.csv",
                title="Guardar tabla como CSV"
            )
            
            if filename:
                try:
                    dataframe.to_csv(filename, index=False, encoding='utf-8-sig')
                    messagebox.showinfo("Éxito", f"✅ Tabla exportada exitosamente a:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ No se pudo exportar la tabla:\n{str(e)}")
    
    def exportar_excel_actual(self):
        """Exporta la tabla actual a Excel"""
        if self.tabla_actual:
            dataframe, titulo = self.tabla_actual
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                initialfile=f"{titulo[:30].replace(':', '').replace('/', '_')}.xlsx",
                title="Guardar tabla como Excel"
            )
            
            if filename:
                try:
                    dataframe.to_excel(filename, index=False)
                    messagebox.showinfo("Éxito", f"✅ Tabla exportada exitosamente a:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ No se pudo exportar la tabla:\n{str(e)}")
    
    def exportar_grafico_actual(self):
        """Exporta el gráfico actual a PNG"""
        if self.figura_actual:
            filename = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
                initialfile="grafico.png",
                title="Guardar gráfico como imagen"
            )
            
            if filename:
                try:
                    self.figura_actual.savefig(filename, dpi=300, bbox_inches='tight')
                    messagebox.showinfo("Éxito", f"✅ Gráfico exportado exitosamente a:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ No se pudo exportar el gráfico:\n{str(e)}")
    
    def exportar_pdf_actual(self):
        """Exporta el gráfico actual a PDF"""
        if self.figura_actual:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile="grafico.pdf",
                title="Guardar gráfico como PDF"
            )
            
            if filename:
                try:
                    self.figura_actual.savefig(filename, bbox_inches='tight')
                    messagebox.showinfo("Éxito", f"✅ Gráfico exportado exitosamente a:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ No se pudo exportar el gráfico:\n{str(e)}")
    
    def exportar_todo(self):
        """Exporta todas las tablas y gráficos"""
        def tarea_exportacion():
            try:
                # Crear ventana de progreso
                progress_window = tk.Toplevel(self.root)
                progress_window.title("Exportando...")
                progress_window.geometry("400x150")
                progress_window.transient(self.root)
                progress_window.grab_set()
                progress_window.configure(bg='#2c3e50')
                
                # Centrar ventana
                progress_window.update_idletasks()
                width = progress_window.winfo_width()
                height = progress_window.winfo_height()
                x = (progress_window.winfo_screenwidth() // 2) - (width // 2)
                y = (progress_window.winfo_screenheight() // 2) - (height // 2)
                progress_window.geometry(f'{width}x{height}+{x}+{y}')
                
                # Configurar contenido
                tk.Label(progress_window, 
                        text="📥 Exportando todas las tablas y gráficos...",
                        font=('Arial', 12, 'bold'),
                        bg='#2c3e50',
                        fg='white').pack(pady=20)
                
                tk.Label(progress_window, 
                        text="Por favor espere, esto puede tomar unos momentos...",
                        font=('Arial', 9),
                        bg='#2c3e50',
                        fg='#bdc3c7').pack()
                
                progress = ttk.Progressbar(progress_window, 
                                          mode='indeterminate',
                                          length=300)
                progress.pack(pady=20)
                progress.start()
                
                # Ejecutar exportación
                guardar_todas_tablas()
                generar_todos_graficos()
                
                # Cerrar ventana de progreso
                progress_window.destroy()
                
                # Mostrar mensaje de éxito
                messagebox.showinfo("Exportación completa", 
                                   f"✅ TODOS LOS ARCHIVOS EXPORTADOS EXITOSAMENTE\n\n"
                                   f"📁 Carpeta: 'exportacion_capitulo_iv/'\n\n"
                                   f"📄 Tablas (8): Formato Markdown y CSV\n"
                                   f"📊 Gráficos (8): Formato PNG (300 DPI) y PDF\n"
                                   f"📋 Dataset completo en Excel\n\n"
                                   f"🎯 Listo!")
                
            except Exception as e:
                messagebox.showerror("Error", f"❌ Error en la exportación:\n{str(e)}")
        
        # Ejecutar en hilo separado
        threading.Thread(target=tarea_exportacion, daemon=True).start()
    
    # ============================================================================
    # FUNCIONES DE INFORMACIÓN Y UTILIDAD
    # ============================================================================
    
    def cargar_dataset(self):
        """Carga y muestra el dataset completo"""
        # Obtener datos
        from analisis_estadistico import cargar_datos_originales
        df = cargar_datos_originales()
        
        # Limpiar treeview
        for item in self.dataset_tree.get_children():
            self.dataset_tree.delete(item)
        
        # Configurar columnas
        columnas = list(df.columns)
        self.dataset_tree["columns"] = columnas
        self.dataset_tree["show"] = "headings"
        
        # Configurar encabezados
        for col in columnas:
            self.dataset_tree.heading(col, text=col)
            self.dataset_tree.column(col, width=100, minwidth=50, anchor=tk.CENTER)
        
        # Insertar datos
        for index, row in df.iterrows():
            self.dataset_tree.insert("", "end", values=list(row))
    
    def mostrar_dataset(self):
        """Muestra el dataset completo"""
        self.notebook.select(self.tab_dataset)
        self.mostrar_texto_info("📁 DATASET COMPLETO\n\nSe muestra la tabla completa con los 20 registros de entidades públicas.\n\nUse las barras de desplazamiento para navegar por todos los datos.")
    
    def generar_todos_graficos(self):
        """Genera todos los gráficos"""
        def tarea_generacion():
            try:
                generar_todos_graficos()
                messagebox.showinfo("Éxito", 
                                   "✅ Todos los gráficos han sido generados exitosamente\n\n"
                                   "📁 Guardados en: 'exportacion_capitulo_iv/graficos/'\n\n"
                                   "📊 8 gráficos en formato PNG y PDF")
            except Exception as e:
                messagebox.showerror("Error", f"❌ Error al generar gráficos:\n{str(e)}")
        
        threading.Thread(target=tarea_generacion, daemon=True).start()
    
    def generar_reporte_pdf(self):
        """Genera un reporte PDF (placeholder)"""
        messagebox.showinfo("Generar PDF", 
                           "📄 La funcionalidad de PDF está en desarrollo.\n\n"
                           "Por ahora, exporte las tablas y gráficos individualmente.\n"
                           "Puede usar los archivos Markdown para crear su documento.")
    
    def verificar_calculos(self):
        """Verifica todos los cálculos"""
        from analisis_estadistico import verificar_todos_calculos
        resultado = verificar_todos_calculos()
        self.mostrar_texto_info(resultado)
        self.notebook.select(self.tab_texto)
    
    def recalcular_todo(self):
        """Recalcula todo"""
        messagebox.showinfo("Recalcular", 
                           "🔄 Todos los cálculos se generan automáticamente al mostrar cada tabla.\n\n"
                           "Los valores mostrados son los cálculos exactos basados en el dataset original.")
    
    def mostrar_ayuda(self):
        """Muestra la ayuda"""
        ayuda_text = """❓ AYUDA DEL PROGRAMA - CAPÍTULO IV

🎯 CARACTERÍSTICAS PRINCIPALES:

📊 TABLAS ESTADÍSTICAS (8):
  • Tabla 3: Características generales de las entidades
  • Tabla 6: Distribución de modelos de seguridad
  • Tabla 7: Nivel de madurez vs años de implementación
  • Tabla 8: Desempeño promedio por modelo
  • Tabla 9: Percepción y capacitación
  • Tabla 10: Prueba de Kruskal-Wallis (¡CÁLCULOS EXACTOS!)
  • Tabla 11: Pruebas Mann-Whitney pareadas
  • Tabla 12: Matriz de correlaciones de Spearman

📈 GRÁFICOS COMPLETOS (8):
  1. Incidentes mensuales por modelo
  2. Tasa de bloqueo promedio
  3. Tiempos de respuesta y detección
  4. Percepción y capacitación
  5. Nivel de madurez
  6. Especialistas por modelo
  7. Mapa de correlaciones
  8. Boxplot completo de métricas

🛠️ FUNCIONALIDADES:

• Exportación individual: Cada tabla/gráfico puede exportarse por separado
• Exportación completa: Todos los archivos con un solo clic
• Verificación: Comprobación automática de cálculos
• Dataset completo: Visualización de todos los datos originales
• Precisión: Todos los cálculos con 4 decimales de precisión

📁 ESTRUCTURA DE ARCHIVOS:

exportacion_capitulo_iv/
├── tablas/              # Tablas en Markdown y CSV
├── graficos/           # Gráficos en PNG y PDF
└── dataset_completo.xlsx

🎓 PARA TU TESIS:

1. Los valores mostrados son los CORRECTOS basados en cálculos exactos
2. Use "Verificar cálculos" para confirmar precisiones
3. Exporte todo y use los archivos directamente en su documento
4. Los gráficos son de calidad de publicación (300 DPI)

⚠️ NOTAS IMPORTANTES:

• La Tabla 9 ha sido CORREGIDA con valores exactos
• La Tabla 10 muestra los valores REALES de Kruskal-Wallis
• Todos los cálculos usan el dataset ORIGINAL sin modificaciones

📞 SOPORTE:

Para cualquier duda sobre los cálculos estadísticos,
realice manuelamente.
"""
        self.mostrar_texto_info(ayuda_text)
        self.notebook.select(self.tab_texto)
    
    def mostrar_texto_info(self, texto):
        """Muestra texto en el área de información"""
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(1.0, texto)
    
    def guardar_texto(self):
        """Guarda el texto actual a un archivo"""
        texto = self.text_area.get(1.0, tk.END)
        if texto.strip():
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="informacion_analisis.txt"
            )
            
            if filename:
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(texto)
                    messagebox.showinfo("Éxito", f"✅ Texto guardado exitosamente en:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ No se pudo guardar el texto:\n{str(e)}")
    
    def limpiar_texto(self):
        """Limpia el área de texto"""
        self.text_area.delete(1.0, tk.END)
    
    def copiar_texto(self):
        """Copia el texto al portapapeles"""
        texto = self.text_area.get(1.0, tk.END)
        if texto.strip():
            self.root.clipboard_clear()
            self.root.clipboard_append(texto)
            messagebox.showinfo("Copiado", "✅ Texto copiado al portapapeles")
    
    def copiar_tabla(self):
        """Copia la tabla actual al portapapeles"""
        if self.tabla_actual:
            dataframe, titulo = self.tabla_actual
            
            # Convertir a texto formateado
            tabla_texto = f"{titulo}\n\n"
            tabla_texto += dataframe.to_string(index=False, float_format=lambda x: f"{x:.4f}" if isinstance(x, float) else str(x))
            
            # Copiar al portapapeles
            self.root.clipboard_clear()
            self.root.clipboard_append(tabla_texto)
            
            messagebox.showinfo("Copiado", "✅ Tabla copiada al portapapeles")
    
    def imprimir_valores(self):
        """Imprime los valores de la tabla actual"""
        if self.tabla_actual:
            dataframe, titulo = self.tabla_actual
            
            info = f"📊 VALORES DE {titulo}\n\n"
            for col in dataframe.columns:
                if pd.api.types.is_numeric_dtype(dataframe[col]):
                    info += f"{col}:\n"
                    info += f"  • Mínimo: {dataframe[col].min():.4f}\n"
                    info += f"  • Máximo: {dataframe[col].max():.4f}\n"
                    info += f"  • Media: {dataframe[col].mean():.4f}\n"
                    info += f"  • Desv. Estándar: {dataframe[col].std():.4f}\n\n"
            
            self.mostrar_texto_info(info)
            self.notebook.select(self.tab_texto)
    
    # ============================================================================
    # FUNCIÓN PRINCIPAL
    # ============================================================================
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        # Mostrar mensaje de bienvenida
        bienvenida = """🎓 BIENVENIDO AL SISTEMA DE ANÁLISIS ESTADÍSTICO
CAPÍTULO IV: RESULTADOS Y DISCUSIÓN

✅ VERSIÓN - CÁLCULOS EXACTOS

Este sistema genera automáticamente todas las tablas y gráficos
necesarios para tu capítulo IV de tesis, con cálculos precisos.

📊 TABLAS DISPONIBLES:
• Tabla 3: Características generales
• Tabla 6: Distribución de modelos
• Tabla 7: Nivel de madurez
• Tabla 8: Desempeño promedio
• Tabla 9: Percepción y capacitación (¡CORREGIDA!)
• Tabla 10: Kruskal-Wallis (¡CÁLCULOS EXACTOS!)
• Tabla 11: Mann-Whitney
• Tabla 12: Correlaciones

📈 GRÁFICOS DISPONIBLES:
• 8 gráficos profesionales listos para tesis
• Exportación en PNG (300 DPI) y PDF
• Interactivos con zoom y navegación

🛠️ INSTRUCCIONES:
1. Seleccione una tabla o gráfico del panel izquierdo
2. Use los botones de exportación para guardar
3. Verifique cálculos con el botón correspondiente
4. Exporte todo con un solo clic

🎯 RECOMENDACIÓN:
Use "Verificar cálculos" para confirmar la precisión
de todos los valores estadísticos.
"""
        self.mostrar_texto_info(bienvenida)
        self.root.mainloop()

def main():
    """Función principal"""
    root = tk.Tk()
    app = AplicacionTesisCorregida(root)
    app.ejecutar()

if __name__ == "__main__":
    main()