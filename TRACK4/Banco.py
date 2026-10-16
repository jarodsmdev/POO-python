class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular # atributo privado
        self.__saldo = saldo

    def __str__(self):
        return f"Nombre: {self.__titular} Saldo: ${self.__saldo}"

    def getTitular(self):
        return self.__titular

    def setTitular(self, nuevoTitular: str):
        if len(nuevoTitular.trim()) == 0:
            print("No puede estar vacio")
        if len(nuevoTitular) > 2:
            self.__titular = nuevoTitular.capitalize()
        else:
            print("El nombre del titular debe tener al menos 2 caracteres")

    def getSaldo(self):
        return self.__saldo

    def retirar(self, monto):
        if self.getSaldo() >= monto:
            #self.__saldo = self.__saldo - monto
            self.__saldo -= monto
        else:
             print("Saldo insuficiente")


    def depositar(self, monto):
        if monto >= 0:
            #self.__saldo = self.__saldo + monto
            self.__saldo += monto
        else:
            print("El monto debe ser positivo")

cuentaJuan = CuentaBancaria("Juan", 0)
cuentaAna = CuentaBancaria("Ana", 1000)
print(cuentaJuan)
print(cuentaJuan.getTitular())

cuentaJuan.retirar(1000)
print(cuentaJuan.getSaldo())

cuentaJuan.depositar(-1000)
print(cuentaJuan)

print(cuentaAna)
cuentaAna.retirar(1000)
print(cuentaAna)