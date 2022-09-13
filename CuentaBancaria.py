class CuentaBancaria:

    lista_cuentas = [] #lista de cuentas banacarias

    def __init__(self, nro_cuenta, balance):
        self.nro_cuenta = nro_cuenta
        self.tasa_interes = 0.01
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)

    def depósito(self, monto_deposito):
        self.balance += monto_deposito
        return self

    def retiro(self,monto_retiro):
        if self.balance > monto_retiro: 
            self.balance -= monto_retiro
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"El balance de {self.nro_cuenta} es de {round(self.balance)} pesos")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
            
        return self

    @classmethod
    def info_cuentas(cls):
        print("Total de cuentas bancarias:", len(cls.lista_cuentas))
        for cuenta in cls.lista_cuentas:
            print(f"{cuenta.nro_cuenta} : Su balance es de {round(cuenta.balance)} pesos, con una tasa de interés de {cuenta.tasa_interes}%")
    