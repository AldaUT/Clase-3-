def historia_colectiva():
    print("Bienvenidos a la gran historia de nuestros alumnos y Python.")
    nombre = input("Dime tu nombre (personaje principal): ")
    
    estado = input("¿Cómo te sientes al llegar a la clase? (ejemplo: curioso, dormido, emocionado): ").strip().lower()

    print(f"\n{nombre} llegó a la primera clase con mucha curiosidad.")
    
    if estado == "dormido":
        print(f"Pero llegó un poco dormido ya que estaba de vacaciones y se atrasó en las semanas de actividades. ¡Pero esta semana se pondrá al corriente!")
    elif estado == "emocionado":
        print(f"{nombre} estaba muy emocionado por aprender cosas nuevas y listo para el desafío.")
    else:
        print(f"{nombre} llegó con una actitud tranquila, dispuesto a aprender a su propio ritmo.")


historia_colectiva()

