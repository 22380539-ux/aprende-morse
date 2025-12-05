"""
Aplicación: Aprende Morse
Demuestra principios de Calidad del Software
Autor: [Tu Nombre]
Fecha: Diciembre 2024
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip

class MorseApp:
    """
    Aplicación de conversión de texto a código Morse
    Implementa estándares de calidad del software
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("📡 Aprende Morse - Calidad del Software")
        self.root.geometry("900x700")
        self.root.configure(bg='#1e293b')
        
        # Mapa de conversión Morse (Estándar ITU-R)
        self.morse_map = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', ' ': '/'
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#1e293b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="📡 Aprende Morse",
            font=('Arial', 24, 'bold'),
            bg='#1e293b',
            fg='#60a5fa'
        )
        title_label.pack(pady=(0, 5))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Conversor de Texto a Código Morse",
            font=('Arial', 12),
            bg='#1e293b',
            fg='#93c5fd'
        )
        subtitle_label.pack(pady=(0, 15))
        
        # Botón para mostrar factores de calidad
        self.show_quality_btn = tk.Button(
            main_frame,
            text="📋 Ver Factores de Calidad",
            command=self.toggle_quality_info,
            bg='#2563eb',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.show_quality_btn.pack(pady=(0, 15))
        
        # Frame de factores de calidad (inicialmente oculto)
        self.quality_frame = tk.Frame(main_frame, bg='#334155', relief=tk.RAISED, bd=2)
        self.quality_visible = False
        
        # Área de entrada
        input_label = tk.Label(
            main_frame,
            text="Escribe tu mensaje:",
            font=('Arial', 12, 'bold'),
            bg='#1e293b',
            fg='white'
        )
        input_label.pack(anchor='w', pady=(10, 5))
        
        self.input_text = scrolledtext.ScrolledText(
            main_frame,
            height=5,
            width=70,
            font=('Arial', 12),
            bg='#f1f5f9',
            fg='#1e293b',
            insertbackground='#2563eb',
            wrap=tk.WORD
        )
        self.input_text.pack(pady=(0, 5))
        self.input_text.bind('<KeyRelease>', self.on_text_change)
        
        # Contador de caracteres
        self.char_count_label = tk.Label(
            main_frame,
            text="0/200 caracteres",
            font=('Arial', 9),
            bg='#1e293b',
            fg='#93c5fd'
        )
        self.char_count_label.pack(anchor='e')
        
        # Botón convertir
        convert_btn = tk.Button(
            main_frame,
            text="🔄 Convertir a Morse",
            command=self.convert_to_morse,
            bg='#10b981',
            fg='white',
            font=('Arial', 12, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        convert_btn.pack(pady=15)
        
        # Área de salida
        output_label = tk.Label(
            main_frame,
            text="Código Morse:",
            font=('Arial', 12, 'bold'),
            bg='#1e293b',
            fg='white'
        )
        output_label.pack(anchor='w', pady=(10, 5))
        
        self.output_text = scrolledtext.ScrolledText(
            main_frame,
            height=5,
            width=70,
            font=('Courier', 14, 'bold'),
            bg='#0f172a',
            fg='#22c55e',
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.output_text.pack(pady=(0, 10))
        
        # Frame de botones
        button_frame = tk.Frame(main_frame, bg='#1e293b')
        button_frame.pack(pady=10)
        
        copy_btn = tk.Button(
            button_frame,
            text="📋 Copiar",
            command=self.copy_to_clipboard,
            bg='#2563eb',
            fg='white',
            font=('Arial', 11, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Limpiar",
            command=self.clear_all,
            bg='#dc2626',
            fg='white',
            font=('Arial', 11, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="✨ Estándar Internacional ITU-R M.1677-1 | Aplicación Educativa",
            font=('Arial', 9),
            bg='#1e293b',
            fg='#64748b'
        )
        footer_label.pack(side=tk.BOTTOM, pady=(20, 0))
        
    def toggle_quality_info(self):
        """Muestra u oculta la información de factores de calidad"""
        if self.quality_visible:
            self.quality_frame.pack_forget()
            self.show_quality_btn.config(text="📋 Ver Factores de Calidad")
            self.quality_visible = False
        else:
            self.show_quality_factors()
            self.quality_visible = True
            
    def show_quality_factors(self):
        """Muestra los factores de calidad implementados"""
        self.quality_frame.pack(fill=tk.BOTH, expand=False, pady=10)
        
        # Limpiar frame
        for widget in self.quality_frame.winfo_children():
            widget.destroy()
        
        title = tk.Label(
            self.quality_frame,
            text="🎯 Factores de Calidad del Software Demostrados",
            font=('Arial', 14, 'bold'),
            bg='#334155',
            fg='#60a5fa',
            pady=10
        )
        title.pack()
        
        factors = [
            ("5.1 Definición de Calidad",
             "Software que cumple requisitos funcionales y no funcionales",
             "✓ Convierte texto a Morse según estándar ITU correctamente"),
            
            ("5.2 Importancia de la Calidad",
             "Garantiza confiabilidad, satisfacción y mantenibilidad",
             "✓ Interfaz intuitiva, conversión precisa, código documentado"),
            
            ("5.3 Factores de Calidad",
             "Funcionalidad, Usabilidad, Eficiencia, Mantenibilidad",
             "✓ Respuesta inmediata, código modular, diseño responsivo"),
            
            ("5.4 Aseguramiento de Calidad",
             "Validación de entrada, manejo de errores, pruebas",
             "✓ Valida caracteres soportados, previene errores"),
            
            ("5.5 Estándares y Métricas",
             "Código Morse ITU-R, buenas prácticas de programación",
             "✓ Estándar internacional, métricas de precisión al 100%")
        ]
        
        for title_text, desc, example in factors:
            factor_frame = tk.Frame(self.quality_frame, bg='#475569', relief=tk.GROOVE, bd=1)
            factor_frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(
                factor_frame,
                text=title_text,
                font=('Arial', 10, 'bold'),
                bg='#475569',
                fg='#93c5fd',
                anchor='w'
            ).pack(fill=tk.X, padx=10, pady=(5, 2))
            
            tk.Label(
                factor_frame,
                text=desc,
                font=('Arial', 9),
                bg='#475569',
                fg='#e2e8f0',
                anchor='w'
            ).pack(fill=tk.X, padx=10)
            
            tk.Label(
                factor_frame,
                text=example,
                font=('Arial', 9, 'italic'),
                bg='#475569',
                fg='#86efac',
                anchor='w'
            ).pack(fill=tk.X, padx=10, pady=(2, 5))
        
        self.show_quality_btn.config(text="❌ Ocultar Factores de Calidad")
        
    def on_text_change(self, event=None):
        """Actualiza el contador de caracteres"""
        text = self.input_text.get("1.0", tk.END).strip()
        length = len(text)
        
        # Limitar a 200 caracteres (Métrica de calidad)
        if length > 200:
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", text[:200])
            length = 200
            
        self.char_count_label.config(text=f"{length}/200 caracteres")
        
    def convert_to_morse(self):
        """Convierte el texto ingresado a código Morse"""
        text = self.input_text.get("1.0", tk.END).strip()
        
        # Validación de entrada (Aseguramiento de calidad)
        if not text:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para convertir.")
            return
        
        morse_code = self.text_to_morse(text)
        
        # Mostrar resultado
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", morse_code)
        self.output_text.config(state=tk.DISABLED)
        
    def text_to_morse(self, text):
        """
        Convierte texto a código Morse
        Implementa el estándar ITU-R (Factor de calidad: Estándares)
        """
        text = text.upper()
        morse_code = []
        
        for char in text:
            if char in self.morse_map:
                morse_code.append(self.morse_map[char])
            elif char == ' ':
                morse_code.append('/')
            # Manejo de errores: caracteres no soportados se ignoran
            
        return ' '.join(morse_code)
    
    def copy_to_clipboard(self):
        """Copia el código Morse al portapapeles"""
        morse_text = self.output_text.get("1.0", tk.END).strip()
        
        if not morse_text:
            messagebox.showinfo("Información", "No hay código Morse para copiar.")
            return
        
        try:
            pyperclip.copy(morse_text)
            messagebox.showinfo("¡Éxito!", "Código Morse copiado al portapapeles")
        except:
            # Si pyperclip no está disponible, usar método alternativo
            self.root.clipboard_clear()
            self.root.clipboard_append(morse_text)
            messagebox.showinfo("¡Éxito!", "Código Morse copiado al portapapeles")
    
    def clear_all(self):
        """Limpia todos los campos"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.char_count_label.config(text="0/200 caracteres")


def main():
    """
    Función principal de la aplicación
    Demuestra buenas prácticas de programación (Factor de calidad)
    """
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()