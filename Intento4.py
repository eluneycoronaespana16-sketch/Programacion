import tkinter as tk
ventana=tk.Tk()
ventana.title("Prevencion_del_bullying")
def registro():
    tk.Label(ventana, text="Hola soy un asistente virtual que atiende diversos tipos de bullying y brinda consejos sobre como enfrentarse a estas situaciones").pack()
    tk.Label(ventana, text="Tipos de bullying").pack()
    tk.Label(ventana, text="1. Fisico").pack()
    tk.Label(ventana, text="2. Verbal").pack()
    tk.Label(ventana, text="3. Psicologico").pack()
    tk.Label(ventana, text="4. Social").pack()
    tk.Label(ventana, text="5. Ciberbullying").pack()
    tk.Label(ventana, text="6. Sexual").pack()
    tk.Label(ventana, text="7. Otros").pack()
    tk.Label(ventana, text="Selecciona el tipo de bullying que estas viviendo").pack()
registro()
tipo=tk.Entry(ventana)
tipo.pack()
mensaje1=tk.Label(ventana)
mensaje1.pack()
mensaje2=tk.Label(ventana)
mensaje2.pack()
def relacionar():
     opcion=tipo.get()
     if opcion=="1":
        mensaje1.config(text="Reporta de inmediato las agresiones y guarda pruebas medicas o de ropa dañada")
        mensaje2.config(text="Evita confrontaciones fisicas para no escalar el conflicto o ser sancionado")
     elif opcion=="2":
        mensaje1.config(text="Recurda tus cualidades personales")
        mensaje2.config(text="Apoyate de tus seres queridos")
     elif opcion=="3":
        mensaje1.config(text="Busca apoyo profesional")
        mensaje2.config(text="No cedas ante amenazas")
     elif opcion=="4":
        mensaje1.config(text="Integrate en actividades extracurriculares")
        mensaje2.config(text="Evita rogar atencion")
     elif opcion=="5":
        mensaje1.config(text="Evita responder a provocaciones")
        mensaje2.config(text="Guarda evidencia")
     elif opcion=="6": 
        mensaje1.config(text="Establece limites")
        mensaje2.config(text="Denuncia de inmediato")
     elif opcion=="7":
        mensaje1.config(text="Cualqier tipo de bullying es dañino")
        mensaje2.config(text="No guardes silencio")

def reportar():
     respuesta=reporte.get()
     if respuesta=="si":
         tk.Label(ventana, text="Ingresa tu nombre completo:").pack()
         nombre_completo=tk.Entry(ventana)
         nombre_completo.pack()
         tk.Label(ventana, text="Tipo de bullying:").pack()
         tipo_bullying=tk.Entry(ventana)
         tipo_bullying.pack()
         tk.Label(ventana, text="Lugar del incidente:").pack()
         lugar=tk.Entry(ventana)
         lugar.pack()
         tk.Label(ventana, text="Describe lo ocurrido:").pack()
         descripcion=tk.Entry(ventana)
         descripcion.pack()
         tk.Label(ventana, text="Reporte registrado correctamente").pack()
     else:
         tk.Label(ventana, text="Recuerda que no estas sol@").pack()
         tk.Label(ventana, text="Pedir ayuda es una muestra de valentia").pack()
tk.Button(ventana, text="Relacionar", command=relacionar).pack()
tk.Label(ventana, text="¿Quieres hacer un reporte?").pack()
reporte=tk.Entry(ventana)
reporte.pack()
tk.Button(ventana, text="Reportar", command=reportar).pack()
ventana.mainloop()