lista = [1, 2]

def isFloat(valor):
    try:
        if float(valor):
            return True
    except ValueError:
        return False
            
def calculo():
    while True:
        celsius_fahrenheit = input("Selecione a opçao de conversao:\n"
                            "1: Converter de Celsius para Fahrenheit;\n"
                            "2: Converter de Fahrenheit para Celsius;\n"
                            "Resposta: ")    
        if celsius_fahrenheit == "1":
            c = input("Digite quantos graus Celsius: ")
            while isinstance(c,str):
                try:
                    float(c)
                except:
                    print("Tente novamente com um numero.")
                    c = input("Digite quantos graus Celsius: ")
                finally:
                    if isFloat(c):
                        f = float(c) * (9/5) + 32
                        return print("{} graus Celsius são {} graus Fahrenheit." .format(float(c), f))   
            return           
        
        elif celsius_fahrenheit == "2":
            f = input("Digite quantos graus Fahrenheit: ")
            while isinstance(f,str):
                try:
                    float(f)
                except:
                    print("Tente novamente com um numero.")
                    f = input("Digite quantos graus Fahrenheint: ")
                finally:
                    while isFloat(f):
                        c = (float(f) - 32) * (5/9)
                        return print("{} graus Fahrenheit sao {} graus Celsius." .format(float(f), c))
        else:
            print("Opcao invalida, tente novamente.")
            continue

calculo()