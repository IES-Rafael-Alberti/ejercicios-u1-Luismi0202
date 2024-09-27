print("INTRODUCE CUÁNTO DINERO TIENES AHORRADO")
dinero = int(input())
cuenta = dinero
for i in range (1,4):
    cuenta = cuenta * 1.4
    DINERO = round(cuenta, 2)
    print(f"Al final del año{i} tendrás {DINERO}€ en la cuenta.")