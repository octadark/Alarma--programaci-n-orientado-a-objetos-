class despertador:
    #constructor
    def __init__(self, alarma, boton, hora, configuracion):
        #atributos instancia
        self.alarma = alarma
        self.boton = boton
        self.hora = hora
        self.configuracion = configuracion
#metodos instancia
    def activar_informacion(self):
        print(f"Alarma: {self.alarma}")
        print(f"boton: {self.boton}")
        print(f"Hora: {self.hora}")
        print(f"configuracion: {self.configuracion}")
#creando el objeto
Alarma = despertador("Hometime","El boton de la alarma esta encendida", "20:30 PM", "Ajustar la hora")
Alarma.activar_informacion();