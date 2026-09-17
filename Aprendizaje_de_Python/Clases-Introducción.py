# Vamos a trabajar con clases y POO. Para empezar creamos clase Gato
print("1. Clase Gato")
class Gato: 
    def __init__(self, nombre, edad):
        # init es el que crea la instancia de la clase
        self.nombre = nombre
        self.edad = edad
    def maullar(self):
        # Método para que al ejecutarse escriba Miau!
        print("Miau!")
    def salir_a_caminar(self):
        print(f"{self.nombre} salió a caminar")
    def años_que_tendra(self, incremento):
        # Al recibir el incremento, le suma el valor a la edad
        return self.edad + incremento
#Probemos a crear una instancia mi_gato
mi_gato = Gato('Claudio', 4)
print(f"Mi gato se llama {mi_gato.nombre}")
print(f"Mi gato tiene {mi_gato.edad} año/s")
mi_gato.maullar()
mi_gato.salir_a_caminar()
#Luego, creamos otro gato.
gato2 = Gato('Gepeto', 2)
print(f"Mi gato se llama {gato2.nombre}")
print(f"Mi gato tiene {gato2.edad} año/s")
gato2.maullar()
gato2.salir_a_caminar()
# Los métodos también pueden funcionar con un valor de retorno
print(mi_gato.años_que_tendra(4))
class CuentaBancaria:
    # Un intento simple de representar una cuenta bancaria
 
    def __init__(self, titular, numero_cuenta):
        # Inicializa los atributos que describen la cuenta
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = 0  # valor por defecto: toda cuenta nueva arranca en 0
 
    def obtener_resumen(self):
        # Devuelve un texto prolijamente formateado con los datos de la cuenta
        resumen = f"Cuenta N° {self.numero_cuenta} - Titular: {self.titular}"
        return resumen
 
    def consultar_saldo(self):
        # Imprime un mensaje mostrando el saldo actual
        print(f"Saldo disponible: ${self.saldo}")
 
    def depositar(self, monto):
        # Suma el monto dado al saldo (equivale a "incrementar" un atributo)
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto a depositar debe ser positivo.")
 
    def retirar(self, monto):
        # Resta el monto dado al saldo, rechazando el retiro si no hay fondos
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes para realizar el retiro.")
 
 
print("\n2. Clase CuentaBancaria")
cuenta_ana = CuentaBancaria('Ana Pérez', '001-234')
print(cuenta_ana.obtener_resumen())
cuenta_ana.consultar_saldo()
 
# Forma 1: modificar el atributo directamente
cuenta_ana.saldo = 500
cuenta_ana.consultar_saldo()
 
# Forma 2: modificar el atributo a traves de un metodo (retirar dinero)
cuenta_ana.retirar(150)
cuenta_ana.consultar_saldo()
 
# Intento de retiro sin fondos suficientes: el metodo lo rechaza
cuenta_ana.retirar(10_000)
 
# Forma 3: incrementar el atributo a traves de un metodo (depositar dinero)
cuenta_lourdes = CuentaBancaria('Lourdes Díaz', '002-987')
print(cuenta_lourdes.obtener_resumen())
cuenta_lourdes.depositar(1000)
cuenta_lourdes.consultar_saldo()
cuenta_lourdes.depositar(250)
cuenta_lourdes.consultar_saldo()

class Tarjeta:
    # Un intento simple de modelar la tarjeta de debito de una cuenta
 
    def __init__(self, limite_diario=50_000):
        # Inicializa los atributos de la tarjeta
        self.limite_diario = limite_diario
        self.activa = True
 
    def describir_tarjeta(self):
        # Imprime un mensaje describiendo la tarjeta
        estado = "activa" if self.activa else "bloqueada"
        print(f"Tarjeta {estado}, con límite diario de ${self.limite_diario}.")
 
    def bloquear(self):
        # Bloquea la tarjeta
        self.activa = False
 
    def aumentar_limite(self, nuevo_limite):
        # Aumenta el limite diario de la tarjeta si el nuevo valor es mayor
        if nuevo_limite > self.limite_diario:
            self.limite_diario = nuevo_limite

# Ahora veamos como se realiza la herencia en Python
class CuentaAhorro(CuentaBancaria):
    # Representa aspectos de una cuenta, especificos de las cajas de ahorro
 
    def __init__(self, titular, numero_cuenta, tasa_interes=0.05):
        # super() llama al __init__() de la clase padre (CuentaBancaria),
        # asi vamos a heredar titular, numero_cuenta y saldo
        super().__init__(titular, numero_cuenta)
        # tasa_interes es un atributo especifico de la caja de ahorro
        self.tasa_interes = tasa_interes
        # Composicion: la tarjeta es una instancia de otra clase,
        # guardada como atributo de la cuenta de ahorro
        self.tarjeta = Tarjeta()
 
    def aplicar_interes(self):
        # Metodo especifico de CuentaAhorro que acredita interes sobre el saldo
        interes_ganado = self.saldo * self.tasa_interes
        self.saldo += interes_ganado
        print(f"Se acreditaron ${interes_ganado:.2f} de interés.")
 
    def retirar(self, monto):
        # Sobrescribe el metodo de la clase padre
        # las cajas de ahorro cobran una pequeña comision por retiro
        comision = 10
        if monto + comision <= self.saldo:
            self.saldo -= (monto + comision)
            print(f"Se retiraron ${monto} más ${comision} de comisión.")
        else:
            print("Fondos insuficientes (incluyendo la comisión).")
 
 
print("\nHerencia y composición con clase CuentaAhorro")
cuenta_clara = CuentaAhorro('Clara Gómez', '003-555')
print(cuenta_clara.obtener_resumen())  # metodo heredado de CuentaBancaria
 
cuenta_clara.depositar(1000)          # metodo heredado, sin cambios
cuenta_clara.consultar_saldo()
 
# Para usar los metodos de la tarjeta, accedemos a traves del atributo tarjeta
cuenta_clara.tarjeta.describir_tarjeta()
 
# Metodo con override, se ejecuta la version de CuentaAhorro, no la de CuentaBancaria
cuenta_clara.retirar(200)
cuenta_clara.consultar_saldo()
 
# Metodo propio de la clase hija
cuenta_clara.aplicar_interes()
cuenta_clara.consultar_saldo()
 
# Aumentamos el limite de la tarjeta y la volvemos a describir
print("\nAumentando el límite de la tarjeta...")
cuenta_clara.tarjeta.aumentar_limite(100_000)
cuenta_clara.tarjeta.describir_tarjeta()  

# Si en otra clase se utiliza from Clases-Introducción.py import CuentaBancaria, CuentaAhorro
# Pueden ser usadas en otros .py