def comprobar_entero(cadena: str) -> bool:
   cadena = cadena.strip()
   return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

def dame_número() -> int: 
    print("Dame un entero")
    cadena=input()
    comprobar_entero(cadena)
    while comprobar_entero(cadena) == False:
        cadena = input("\n**ERROR NO ES UN ENTERO!!!!!\n\n Dame un entero de verdad:")

    return int(cadena)

def main():
    num= dame_número()
    print(f"Escribiste el número {num}")
    


if __name__ =="__main__":
    main()