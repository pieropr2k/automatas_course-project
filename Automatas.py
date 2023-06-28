##¡Claro! Aquí te dejo el código completo en Python que utiliza todas las clases y métodos para generar cadenas aleatorias a partir de una gramática y una semilla para el generador de números pseudoaleatorios:
###```python
import random

class Aleatorio:
    def __init__(self, semilla):
        self.semilla = semilla
        self.a = 7**5
        self.m = (2**31)-1

    def siguiente(self):
        self.semilla = (self.a * self.semilla) % self.m
        return self.semilla

    def elegir(self, limite):
        return self.siguiente() % limite

class Regla:
    def __init__(self, izquierda, derecha):
        self.left = izquierda
        self.right = derecha
        self.cont = 1

    def __repr__(self):
        right_str = " ".join(self.right)
        return f"{self.cont} {self.left} -> {right_str}"

class Gramatica:
    def __init__(self, semilla):
        self.aleatorio = Aleatorio(semilla)
        self.reglas = {}
    
    def regla(self, izquierda, derecha):
        nueva_regla = Regla(izquierda, derecha)
        if izquierda not in self.reglas:
            self.reglas[izquierda] = [nueva_regla]
        self.reglas[izquierda].append(nueva_regla)
        ##print(self.reglas)
        
    def generar(self):
        """
        Genera una cadena aleatoria utilizando las reglas de la gramática.
        La cadena generada comienza con el símbolo inicial "< inicio >".
        """
        simbolo_inicial = ["< inicio >"]
        cadena_generada = self.generando(simbolo_inicial)
        return cadena_generada
    
    def generando(self, strings):
        resultado = ""
        print(strings)
        print("self.reglas:", self.reglas)
        ##strings.append(cadena_generada)
        for cadena in strings:
            print(cadena)
            if cadena in self.reglas:
                ## simbolo no terminal
                tupla = self.seleccionar(cadena)
                end = self.generando(tupla)
                resultado += end
            else:
                ## simbolo terminal
                end = cadena + " "
                resultado += end
        return resultado
    
    def seleccionar_alt(self, left):
        """
        Selecciona una regla al azar cuyo lado izquierdo es el símbolo no
        terminal proporcionado.
        """
        ## Elige una regla al azar cuyo lado izquierdo es la cadena left.
        reglas = self.reglas[left]
        print(reglas)
        print(reglas[0].cont)
        ##total = sum([cont for (right, cont) in reglas])
        total = sum(obj.cont for obj in reglas)
        print(total)
        ## 2. Establezca la variable índice en un número entero elegido al azar. 
        ## Debe ser mayor o igual que 0, pero menor que el total.
        ##aleatorio = self.aleatorio.generar(1, total)
        aleatorio = self.aleatorio.elegir(total)
        print(aleatorio)
        acumulado = 0

        ##for (right, cont) in reglas:
        for obj in reglas:
            acumulado += obj.cont
            ##acumulado += cont
            if aleatorio <= acumulado:
                ##return right
                return obj.right
    
    def seleccionar(self, left):
        reglas = self.reglas[left]
        ##left
        print("reglas:", reglas)
        total = sum(regla.cont for regla in reglas)
        indice = self.aleatorio.elegir(total)
        elegido = None
        for regla in reglas:
            indice -= regla.cont
            if indice <= 0:
                elegido = regla
                break
        for regla in reglas:
            if regla != elegido:
                regla.cont += 1
        return elegido

# Ejemplo de uso
semilla = 12345
# Crear una instancia de la clase Gramatica
gramatica = Gramatica(semilla)

# Agregar reglas a la gramática
gramatica.regla("< inicio >", ["< historia >"])
gramatica.regla("< historia >", ["< frase >", "y", "< historia >"])
gramatica.regla("< historia >", ["< frase >", "sino", "< historia >"])
gramatica.regla("< frase >", ["< articulo >", "< sustantivo >", "< verbo >", "< articulo >", "< sustantivo >"])
gramatica.regla("< articulo >", ["el"])
gramatica.regla("< articulo >", ["la"])
gramatica.regla("< articulo >", ["al"])
gramatica.regla("< sustantivo >", ["gato"])
gramatica.regla("< sustantivo >", ["niño"])
gramatica.regla("< sustantivo >", ["perro"])
gramatica.regla("< sustantivo >", ["niña"])
gramatica.regla("< verbo >", ["perseguia"])
gramatica.regla("< verbo >", ["besaba"])

print(gramatica.reglas)
# Generar una cadena aleatoria utilizando las reglas de la gramática
cadena_generada = gramatica.generar()
print(cadena_generada)

# Imprimir la gramática
print(gramatica)