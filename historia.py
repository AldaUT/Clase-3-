def historia_colectiva():
    print("Bienvenidos a la gran historia de nuestros alumnos y Python.")
    text_valid = 0
    while text_valid < 1:
        nombre = input("Dime tu nombre (personaje principal): ").capitalize()
        if nombre.isalpha() and len(nombre) > 3:
            print(f"Mucho gusto de conocerte, {nombre}.")
            text_valid+=1
        else:
            print ('¿Me recuerdas tu nombre por favor?')
    
    while text_valid < 2:
        try:
            edad = int(input('¿Cuantos años tienes? '))
            if edad >= 5 and edad < 18:
                print ('¡Increible! Es fantastico que alguien tan joven conozca acerca de lenguajes de programación.')
                text_valid+=1
            elif edad >= 18 and edad <= 99:
                print ('Excelente. Te felicito por tu deseo de aprender Python.')
                text_valid+=1
            else:
                print ('No entendí tu respuesta.')
        except ValueError:
            print ('No entendí tu respuesta.')
    
    while text_valid < 3:
        estado = input("¿Cómo te sientes al llegar a una clase? (ejemplo: curioso, dormido, emocionado): ").strip().lower()
        if nombre.isalpha() and len(nombre) >= 3:
            text_valid+=1
        else:
            print ('¿Cómo te sientes?')

    while text_valid < 4:
        print (f'¿Cómo resolverias un problema mediante el uso de código en poco tiempo?')
        try:
            respuesta = int(input('Usando mis conocimientos y aprendizajes (1) / Plagio de internet (2) / A la última hora y a ver que sale (3): '))
            if respuesta >= 1 or respuesta <=3:
                text_valid+=1
            else:
                print ('No entendí tu respuesta.') 
        except ValueError:
            print ('No entendí tu respuesta.') 

    print(f"\n{nombre} llegó a la primera clase de Python y preparó su equipo de trabajo.")
    if estado == "curioso":
        print(f"{nombre} tenia mucha curiosidad de saber nuevas formas de resolver problemas usando Python.")
    elif estado == "dormido":
        print(f"{nombre} llegó un poco dormido ya que estaba de vacaciones y se atrasó en las semanas de actividades. ¡Pero esta semana se pondrá al corriente!")
    elif estado == "emocionado":
        print(f"{nombre} estaba muy emocionado por aprender cosas nuevas y listo para el desafío.")
    elif estado == "triste":
        print(f"{nombre} propusó concentrare en la clase para no pensar en ideas negativas.")
    elif estado == "enojado" or estado == "frustrado":
        print(f"Por más que intentaba, {nombre} divagaba mucho y no prestaba atención a lo que pasaba a su alrededor.")
    else:
        print(f"{nombre} llegó con una actitud tranquila, dispuesto a aprender a su propio ritmo.")

    print ('\nEn un momento dado, la maestra dió instrucciones para hacer un trabajo en clase.')
    print ('Se otorgaron veinte minutos para preparar un ejercicio que sería resuelto por otro compañero.')
    if respuesta == 1:
        print (f'{nombre} cumplió la tarea con exito y envió su trabajo al repositorio grupal.')
        print (f'El código de {nombre} cumplió su función adecuadamente y sirvió como modelo a usar para la clase del día siguiente.')
    elif respuesta == 2:
        print (f'{nombre} solo cambio una que otra oración. Costo poco trabajo, pero al final se envió algo.')
        print (f'El trabajo fue entregado y recibido por la otra persona. \nSin embargo, no pudo ejecutarse el código y {nombre} no recibió calificación alguna.')
    elif respuesta == 3:
        print (f'{nombre} no sabia bien lo que estaba haciendo. Hizo su esfuerzo pero su trabajo era rebuscado y poco organizado.')
        print ('Al momento de mandar el trabajo, se lo pasó en privado a su compañero y le pidió que le hiciera el paro.')
        print (f'{nombre} logró aprobar la clase, pero tiene un area de conocimiento que debe de trabajar a lo largo del curso.')


historia_colectiva()
