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
def relacionar():
     opcion=tipo.get()
     if opcion=="1":
        bullying_fisico()
     elif opcion=="2":
        bullying_verbal()
     elif opcion=="3":
        bullying_psicologico()
     elif opcion=="4":
        bullying_social()
     elif opcion=="5":
        ciberbullying()
     elif opcion=="6": 
        bullying_sexual()
     elif opcion=="7":
        otros()
def bullying_fisico():
    ventana1 = tk.Toplevel(ventana)
    ventana1.title("Bullying Fisico")
    tk.Label(ventana1, text="Reporta de inmediato las agresiones y guarda pruebas medicas o de ropa dañada").pack()
    tk.Label(ventana1, text="Evita confrontaciones fisicas para no escalar el conflicto o ser sancionado").pack()
def bullying_verbal():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("Bullying Verbal")
    tk.Label(ventana2, text="Recuerda tus cualidades personales").pack()
    tk.Label(ventana2, text="Apoyate de tus seres queridos").pack()
def bullying_psicologico():
    ventana3 = tk.Toplevel(ventana)
    ventana3.title("Bullying Psicologico")
    tk.Label(ventana3, text="Busca apoyo profesional").pack()
    tk.Label(ventana3, text="No cedas ante amenazas").pack()
def bullying_social():
    ventana4 = tk.Toplevel(ventana)
    ventana4.title("Bullying Social")
    tk.Label(ventana4, text="Evita rogar atencion").pack()
    tk.Label(ventana4, text="Integrate en actividades extracurriculares").pack()
def ciberbullying():
    ventana5 = tk.Toplevel(ventana)
    ventana5.title("Ciberbullying")
    tk.Label(ventana5, text="Evita responder a provocaciones").pack()
    tk.Label(ventana5, text="Guarda evidencia").pack()
def bullying_sexual():
    ventana6 = tk.Toplevel(ventana)
    ventana6.title("Bullying Sexual")
    tk.Label(ventana6, text="Establece limites").pack()
    tk.Label(ventana6, text="Denuncia de inmediato").pack()
def otros():
    ventana7 = tk.Toplevel(ventana)
    ventana7.title("Otros")
    tk.Label(ventana7, text="Cualqier tipo de bullying es dañino").pack()
    tk.Label(ventana7, text="No guardes silencio").pack()


def reportar():
     global nombre_completo, tipo_bullying, lugar, descripcion
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
def guardar():
             tk.Label(ventana, text="Reporte registrado correctamente").pack()
             tk.Label(ventana, text="Nombre:"+nombre_completo.get()).pack()
             tk.Label(ventana, text="Tipo de bullying:"+tipo_bullying.get()).pack()
             tk.Label(ventana, text="Lugar del incidente:"+lugar.get()).pack()
             tk.Label(ventana, text="Descripcion:"+descripcion.get()).pack()
tk.Button(ventana, text="Relacionar", command=relacionar).pack()
tk.Label(ventana, text="¿Quieres hacer un reporte?").pack()
reporte=tk.Entry(ventana)
reporte.pack()
tk.Button(ventana, text="Presiona para hacer un reporte", command=reportar).pack()
tk.Button(ventana, text="Presiona para guardar tu reporte", command=guardar).pack()
tk.Label(ventana, text="Gracias por confiar en mi. Hasta luego :)")
ventana.mainloop()