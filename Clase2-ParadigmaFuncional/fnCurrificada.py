def log(level):
    def logger(message):
        print("[{}] {}".format(level, message))
    return logger

# Crear instancias de funciones log para diferentes niveles
error_log = log("ERROR")
alert_log = log("ALERTA")
info_log = log("INFORMACIÓN")

# Uso de las funciones log
error_log("Este es un mensaje de error")
alert_log("¡Alerta! Se ha detectado una condición inesperada")
info_log("Este es un mensaje de información")
