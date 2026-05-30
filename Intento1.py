import tkinter as tk
ventana=tk.Tk()
ventana.title("Prevencion_del_bullying")
def registro():
    print("Hola soy un asistente virtual que atiende diversos tipos de bullying y brinda consejos sobre como enfrentarse a estas situaciones")
    print("Tipos de bullying")
    print("1. Fisico")
    print("2. Verbal")
    print("3. Psicologico")
    print("4. Social")
    print("5. Ciberbullying")
    print("6. Sexual")
    print("7. Otros")
    tk.Label(ventana, text="Selecciona el tipo de bullying que estas viviendo").pack()
    tipo=tk.Entry(ventana)
    tipo.pack()
    tipo=(tipo.get())
    if tipo==1:
        print("Reporta de inmediato las agresiones y guarda pruebas medicas o de ropa dañada")
        print("Evita confrontaciones fisicas para no escalar el conflicto o ser sancionado")
    if tipo==2:
        print("Recurda tus cualidades personales")
        print("Apoyate de tus seres queridos")
    if tipo==3:
        print("Busca apoyo profesional")
        print("No cedas ante amenazas")
    if tipo==4:
        print("Integrate en actividades extracurriculares")
        print("Evita rogar atencion")
    if tipo==5:
        print("Evita responder a provocaciones")
        print("Guarda evidencia")
    if tipo==6: 
        print("Establece limites")
        print("Denuncia de inmediato")
    if tipo==7:
        print("Cualqier tipo de bullying es dañino")
        print("No guardes silencio")
tk.Button(ventana, text="Bienvenido", command=registro).pack()
ventana.mainloop()

