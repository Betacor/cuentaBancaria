from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria("Cuenta 001", 0)
cuenta2 = CuentaBancaria("Cuenta 002", 0)

cuenta1.depósito(300).depósito(500).depósito(1000).retiro(100).generar_interes().mostrar_info_cuenta()

cuenta2.depósito(1000).depósito(3000).retiro(400).retiro(200).retiro(500).retiro(5000).generar_interes().mostrar_info_cuenta()

CuentaBancaria.info_cuentas()












