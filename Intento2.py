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
    tipo=tk.Entry(ventana)
    tipo.pack()
    tipo=(tipo.get())
    if tipo=="1":
        tk.Label(ventana, text="Reporta de inmediato las agresiones y guarda pruebas medicas o de ropa dañada").pack()
        tk.Label(ventana, text="Evita confrontaciones fisicas para no escalar el conflicto o ser sancionado").pack()
    if tipo=="2":
        tk.Label(ventana, text="Recurda tus cualidades personales").pack()
        tk.Label(ventana, text="Apoyate de tus seres queridos").pack()
    if tipo=="3":
        tk.Label(ventana, text="Busca apoyo profesional").pack()
        tk.Label(ventana, text="No cedas ante amenazas").pack()
    if tipo=="4":
        tk.Label(ventana, text="Integrate en actividades extracurriculares").pack()
        tk.Label(ventana, text="Evita rogar atencion").pack()
    if tipo=="5":
        tk.Label(ventana, text="Evita responder a provocaciones").pack()
        tk.Label(ventana, text="Guarda evidencia").pack()
    if tipo=="6": 
        tk.Label(ventana, text="Establece limites").pack()
        tk.Label(ventana, text="Denuncia de inmediato").pack()
    if tipo=="7":
        tk.Label(ventana, text="Cualqier tipo de bullying es dañino").pack()
        tk.Label(ventana, text="No guardes silencio").pack
tk.Button(ventana, text="Bienvenido", command=registro).pack()
ventana.mainloop()