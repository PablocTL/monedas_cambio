from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

patron = {
    0: [],
    1: [1],
    2: [2],
    3: [2, 1],
    4: [2, 2],
    5: [5],
    6: [5, 1],
    7: [5, 2],
    8: [5, 2, 1],
    9: [5, 2, 2]
}

def desglosar_cantidad(entrada):
    # Normalizar coma decimal
    entrada = entrada.replace(",", ".")
    
    try:
        cantidad = Decimal(entrada)
    except InvalidOperation:
        print("Error: Introduce un número válido.")
        return
    
    if cantidad < 0:
        print("Error: La cantidad no puede ser negativa.")
        return
    
    # Redondear a 2 decimales (céntimos) con redondeo half-up
    cantidad = cantidad.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total_centimos = int(cantidad * 100)
    
    euros_totales = total_centimos // 100
    centimos_totales = total_centimos % 100
    
    digito_x1 = centimos_totales % 10
    digito_x2 = centimos_totales // 10
    digito_x3 = euros_totales % 10
    digito_x4 = (euros_totales // 10) % 10
    resto_x5 = (euros_totales // 100) * 100
    
    x1 = [f"{v} cent" for v in patron[digito_x1]]
    x2 = [f"{v * 10} cent" for v in patron[digito_x2]]
    x3 = [f"{v} eur" for v in patron[digito_x3]]
    x4 = [f"{v * 10} eur" for v in patron[digito_x4]]
    
    x5 = []
    for billete in [500, 200, 100]:
        while resto_x5 >= billete:
            x5.append(f"{billete} eur")
            resto_x5 -= billete
    
    todas = x5 + x4 + x3 + x2 + x1
    
    print("\n--- Listas por posición ---")
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)
    print("x5:", x5)
    
    print("\n--- Cantidad exacta a entregar ---")
    if not todas:
        print("0 monedas o billetes (importe 0)")
    else:
        for divisa in dict.fromkeys(todas):
            cantidad_piezas = todas.count(divisa)
            print(f"{cantidad_piezas} de {divisa}")

if __name__ == "__main__":
    entrada = input("Introduce la cantidad en euros: ")
    desglosar_cantidad(entrada)