from conta import Conta

conta = Conta(123, 'Renan', 55.5, 1000.0)
conta2 = Conta(312, 'Daniel', 55.5, 1000.0)

conta.deposita(300.0)
conta.extrato()
conta.saca(100.0)
conta.extrato()

conta2.extrato()
conta2.transfere(10.0, conta)
conta2.extrato()
conta.extrato()

print(Conta.codigo_banco())