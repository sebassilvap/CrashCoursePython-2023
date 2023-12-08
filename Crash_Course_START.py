# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# PYTHON CRASH COURSE LEGACY 2023
# por @sebas.silva.p
# Diciembre 2023
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 1) Comentarios
print('\n\n\n1) Comentarios\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - con símbolo de numeral # => comentario de 1 línea
# - entre 6 comillas simples o dobles => multilínea => string
# - no afectan al código




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 2) print()
print('\n\n\n2) print()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función interna para imprimir en consola
# - función interna en python => built-in function


# -------------
# Línea Vacía
# -------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 3) Variables
print('\n\n\n3) Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - contenedor / espacio con memoria
# - para guardar un valor


# ----------------------------------------------------------------------
# Truco print => imprimir varios valores, separando con coma
# ¿por qué? => print es una función => recibe argumentos de función
# ----------------------------------------------------------------------


# --------------------------------
# Redefinir / Reasignar variables
# --------------------------------


# ---------------------
# Asignación Múltiple
# ---------------------


# -----------------------------------
# Asignación Múltiple a Valor Único
# -----------------------------------



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 4) Reglas para Nombres de Variables
print('\n\n\n4) Reglas para Nombres de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - En programación se maneja 2 estándares:
#   (a) cammelCase => nombreEstudiante
#   (b) separación  => nombre_estudiante (PYTHON)

# - REGLAS:
#   (a) no tildes
#   (b) no empezar con número
#   (c) no empezar con caracter de símbolo


# ------------------------
# print en varias líneas
# ------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 5) Tipos de Datos
print('\n\n\n5) Tipos de Datos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------
# Tipos Básicos
# ---------------

"""
Tipo de Dato     |  Denominación  |  Ej:
---------------------------------------------------------
Entero           |  int           |  -20, 0, 5
Punto Flotante   |  float         |  2.5, 0.669, -89.52
Cadena de Texto  |  str           |  'Hola', "Python"
Booleano         |  bool          |  True, False
"""

# --------------------------
# Todos los Tipos de Datos
# --------------------------

"""
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
"""
# https://www.w3schools.com/python/python_datatypes.asp


# --------------------------------------
# type() => retorna tipo de dato
# --------------------------------------
# - función interna (built-in function)



# ----------------------------------------------------------------
# None => útil para crear una variable sin valor y asignar luego
# ----------------------------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 6) Casting de Variables
print('\n\n6) Casting de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - cambiar el tipo de una variable a otro
# - se utilizan funciones-internas
# - con el mismo nombre que las variables, el nombre que utiliza python
# - int / float / str / bool
# - OJO: no todas las conversiones son posibles

# --------------------------
# Generalidades de Casting
# --------------------------


# -------------------------
# Todo es CASTEABLE a bool
# -------------------------


# ------------
# Conclusión
# ------------
# - Número 0 / 0.0 => False
# - String vacío => False
# - Tipo None => False
# - Todo lo demás => True




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 7) Función Interna => isinstance()
print('\n\n7) Función Interna => isinstance()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función complemento de type()
# - verificar si una variable / dato es de un tipo




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 8) Función Interna => help()
print('\n\n8) Función Interna => help()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - funciones internas de python (built-in functions)
# - no necesitan importación / instalación
# - están ahí desde que se instala python
# - ej: print() / type() / int() / float() / etc...
# - help() => biblioteca offline de Python

# - Tema de funciones internas:
# - https://www.w3schools.com/python/python_ref_functions.asp


# -------------------------------------
# Averiguar sobre 1 tema en específico
# -------------------------------------


# ------------------
# Navegar en help()
# ------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 9) Aritmética en Python
print('\n\n\n9) Aritmética en Python\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------------
# Operaciones Básicas en Python
# ------------------------------

"""
    suma               =>   +
    resta              =>   -
    producto           =>   *
    división           =>   /
    potencia           =>   **
    módulo             =>   %
    división + floor   =>   //
"""

# ---------------------------------
# Aritmética con Valores Directos
# ---------------------------------


# -------------------------
# Aritmética con variables
# -------------------------


# -------
# Módulo
# -------
#    10 |___ 4
#    -8      2
#     2


# --------------------
# División y Redondeo
# --------------------
# divide y devuelve la parte entera


# ----------------------------------
# Las reglas matemáticas se cumplen
# ----------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 10) Secuencias de Escape
print('\n\n\n10) Secuencias de Escape\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - elementos que permiten dar un formato a string
# - se les antecede siempre el backslash => \

"""
SECUENCIA  NOMBRE           DEFINICIÓN
  \\       Backslash        Para insertar el caracter \ en un String
  \'       Comilla Simple   Para insertar la comilla simple en un String
  \"       Comilla doble    Para insertar la comilla doble en un String
  \b       Retroceso        Elimina un caracter del String al momento de aparecer en el output de la consola.
  \f       Formfeed         Imprime una nueva línea indentada al final de la línea anterior.
  \v       Tab Vertical     Realiza lo mismo que el Formfeed
  \t       Tab Horizontal   Inserta un espaciado de tabulación
  \r       Carriage return  Inserta los caracteres después de \r al inicio del String
  \n       Nueva Línea      Inserta un salto del línea en tabulación 0
"""
# - algunos no se visualizan en editores de código como VSCode
# - en Replit => se puede ver el funcionamiento de todos
# - aquí vamos a ver los más relevantes




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 11) String <str>
print('\n\n\n11) String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------------
# formas de representar un string
# --------------------------------


# -----------------
# concatenación +
# -----------------


# ------------------
# multiplicación *
# ------------------


# ------------------------------
# índices [i] y tamaño => len()
# ------------------------------


# ---------------------------
# slicing [start:end:step]
# end - exclusivo
# start, step - opcionales
# ---------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 12) Métodos de Formato Importantes de String <str>
print('\n\n\n12) Métodos de Formato Importantes de String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------
# Para dar formato a texto
# --------------------------


# ---------------------
# Alineación de texto
# ---------------------


# ---------------------
# Contar Coincidencias
# ---------------------


# --------------------------------
# Retornar índice de una búsqueda
# --------------------------------


# ------------------------------
# Eliminar espacios / caracter
# ------------------------------


# -------------------------------------------
# Unir un caracter a un string en secuencia
# -------------------------------------------


# ---------------------------------------------
# Separar un string en elementos de una lista
# (* tema lista ya lo vemos a continuación)
# ---------------------------------------------


# --------------------------
# Líneas de string a lista
# --------------------------


# --------------------------
# Cambiar espaciado de tabs
# --------------------------


# -----------------------------------------------
# IMPORTANTE: reemplazar un caracter del string
# -----------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 13) Métodos de String con Retorno Booleano (averiguar algo en el String)
print('\n\n\n13) Métodos de String con Retorno Booleano (averiguar algo en el String)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------------------------------
# .isalpha() => True si todos son letras (A-Z / a-z)
# ----------------------------------------------------


# -------------------------------------------
# .isalnum() => True si son letras y números
# -------------------------------------------


# --------------------------------------------
# .isdigit() => True si es un sting numérico
# --------------------------------------------


# --------------------------
# Verificadores de formato
# .islower()
# .isupper()
# .istitle()
# --------------------------


# ----------------------------
# .startswith() / .endswith()
# ----------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 14) Métodos para Números + Librería Math
print('\n\n\n14) Métodos para Números + Librería Math\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ==> funciones internas para números

# ---------------------------------
# round() / inmediato superior
# ---------------------------------


# ---------------------------
# abs() / valor absoluto
# ---------------------------


# ---------------------
# pow() / exponencial
# ---------------------


# -----------------------------------
# sum() / max() / min() / En Listas
# -----------------------------------


# ==> librería math
# https://www.w3schools.com/python/python_math.asp

# --------------------------
# Importación de un módulo
# --------------------------


# ------------
# Constantes
# ------------


# ------------------------
# Representación numérica
# ------------------------


# ------------------
# Raíces y Potencia
# ------------------


# -----------
# Logaritmos
# -----------


# ---------------------------
# Ángulos
# 360 grados == 2*pi radianes
# ---------------------------


# ----------------------------
# Otras funciones importantes
# ----------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 15) Encadenamiento / Chaining - Funciones & Métodos
print('\n\n\n15) Encadenamiento / Chaining - Funciones & Métodos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# Métodos
# => izquierda a derecha
# ------------------------


# -------------------------
# Funciones
# => de dentro hacia fuera
# -------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 16) Función Interna => eval()
print('\n\n\n16) Función Interna => eval()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - evaluar una expresión matemática
# - expresada a manera de string




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 17) input => entrada de datos
print('\n\n\n17) input => entrada de datos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - OJO: todo lo que viene del input viene como string <str>

# -----------
# SIN input
# -----------


# -----------------
# Utilizando input
# -----------------


# -------------------
# Utilizando casting
# -------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 18) Operadores de Comparación
print('\n\n\n18) Operadores de Comparación\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - al usarlos nos devuelven un valor booleano

# -----------------------------------
# Tabla de Operadores de Comparación
# -----------------------------------
'''
Operador |  Definición
-------------------------------
   >     |  Mayor que
   <     |  Menor que
   >=    |  Mayor o igual que
   <=    |  Menor o igual que
   ==    |  Igual que
   !=    |  Diferente de
'''

# ------------
# Con Números
# ------------


# ------------
# Con Strings
# ------------


# https://elcodigoascii.com.ar/
# @ => alt + 64
# & => alt + 38




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 19) Operadores Lógicos
print('\n\n\n19) Operadores Lógicos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------
# Tabla de Operadores Lógicos
# ----------------------------

'''
Operador |  Ejemplo  |  Descripción
----------------------------------------------------------------
not      |  X and Y  |  True si todos son True
and      |  X or Y   |  Basta que 1 sea True, resultado es True
or       |  not X    |  Niega al booleano
'''



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 20) Listas en Python
print('\n\n\n20) Listas en Python\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - la colección de datos MÁS IMPORTANTE

# ----------------
# Creación Básica
# ----------------
# - corchetes y separando elementos con coma
# - con len() => tamaño de lista / número de elementos


# ----------------------------
# Creación con Función list()
# ----------------------------


# ------------
# Lista Vacía
# ------------


# ---------------------------
# Palabra Clave / Keyword in
# ---------------------------


# ---------------------------
# Concatenación y Operador *
# ---------------------------


# -------------------
# Indexing & Slicing
# -------------------


# ==> Métodos Importantes

# -----------
# .append()
# -----------


# -----------
# .insert()
# -----------


# -------------------------------------------
# métodos / funciones para borrar elementos

# del lista[indice]
# .pop()
# .remove()
# .clear()
# -------------------------------------------


# ==> ERROR cuando trato de eliminar algo que no existe


# ---------
# .count()
# ---------


# -----------
# .reverse()
# -----------


# --------
# .sort()
# --------


# --------
# .copy()
# --------


# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 21) Condicional IF
print('\n\n\n21) Condicional IF\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----
# EJ 1
# -----


# -----
# EJ 2
# -----


# -----
# EJ 3
# -----




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 22) Condicional Match-Case
print('\n\n\n22) Condicional Match-Case\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - a partir de python 3.10 >
# - simula el switch...case de otros lenguajes




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 23) Operador Ternario
print('\n\n\n23) Operador Ternario\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - una manera corta / sencilla de expresar una condición
# - aconsejable usarla para algo sencillo
# - siempre en 1 línea

# --------------------
# Con condicional IF
# --------------------


# ----------------------
# Con Operador Ternario
# ----------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 24) Bucle For
print('\n\n\n24) Bucle For\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# elemento iterable => acceder a los índices []


# --------------------
# recorrido de listas
# --------------------


# --------------------------------------------
# la variable usada para el recorrido se crea
# --------------------------------------------


# ----------------------
# recorrido de Strings
# ----------------------


# ----------------------------
# función interna range + for
# range (start, end, step)
# end => EXCLUSIVO
# ----------------------------


# -----------------------
# for + contador externo
# -----------------------


# ----------------
# for + enumerate
# ----------------


# -----------
# for + else
# -----------
# - se ejecuta 1 vez al final de la iteración


# -------------
# for + break
# -------------
# - para romper / terminar la iteración por completo


# ---------------
# for + continue
# ---------------
# - para saltar una iteración


# -----------
# for + pass
# -----------
# - en este caso pass funciona como continue


# -----------------------------------
# aplicación for => cálculo numérico
# -----------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 25) Bucle while
print('\n\n\n25) Bucle while\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - nunca olvidar el contador + incremento / decremento
# - cuidado con loop infinito

# ----------------------
# ERROR: bucle infinito
# ----------------------


# ---------------------------------------
# Incremento / Decremento indispensable
# ---------------------------------------


# ----------------------------------
# Recorrido de Elementos Iterables
# ----------------------------------
# - también puede recorrer strings, listas, tange, etc...
# - pero para hacer eso se debe usar mejor el bucle for


# -- recorrido de lista + while


# -- recorrido de string + while


# -- recorriendo range + while


# --------------
# while + else
# --------------
# - se ejecuta una vez al final
# - así se cumpla la condición o no


# ---------------
# while + break
# ---------------
# - romper / terminar el bucle


# -------------------------
# while + continue / pass
# -------------------------
# - saltarse iteraciones


# ------------
# while True
# ------------
# - técnica de bucle para ejecutar un programa
# - siempre entramos al bucle
# - CUIDADO: obliga el uso de un break para terminar el bucle en algún momento




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 26) Pares / Impares / Múltiplos
print('\n\n26) Pares / Impares / Múltiplos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Recordemos un poco de la primaria
# - Las partes de una división:

#   Dividendo  |____ Divisor
#     Residuo        Cociente

# Cociente = Dividendo / Divisor
# Residuo / Resto = Dividendo % Divisor => Operador de Módulo

# - Si un número es par => divisible para 2 => resto = 0

#   4 |__ 2
#   0     2

# - Si un número es impar => NO divisible para 2 => resto = 1

#   5 |__ 2
#   1     2

# - Un múltiplo => el número es divisble para este número => resto = 0
# - EJ: 6, 9, 12 múltiplos de 3

#   12 |__ 3
#   0      4

# => esto puede ser de ayuda en la programación

# ------
# EJ 1
# ------


# ------
# EJ 2
# ------
# - múltiplos de 4 en números del 1 al 100




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 27) Print Avanzado + String Format
print('\n\n\n27) Print Avanzado + String Format\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# print básico aprendido
# ------------------------


# --------------------------
# parámetro opcional (end)
# --------------------------


# -----------------
# string.format()
# -----------------


# -----------
# f'String'
# -----------


# ---------------------------------------
# str.format() + argumentos posicionales
# ---------------------------------------


# ---------------------------------------
# str.format() + argumentos con keyword
# ---------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 28) String Format + Números
print('\n\n28) String Format + Números\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------------
# Número de dígitos & decimales
# ------------------------------


# -----------
# Alineación
# -----------


# -------------------
# Relleno de ceros 
# -------------------
# - OJO: Toma en cuenta todos los caracteres


# -------------------
# Separador de miles
# -------------------


# --------------------
# Notación Científica
# --------------------


# ----------------
# Combinando todo
# ----------------


# --------------
# CON f'String'
# --------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 29) String Format + Texto
print('\n\n\n29) String Format + Texto\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 30) Librería / Módulo random
print('\n\n\n30) Librería / Módulo random\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -------------------
# importación módulo
# -------------------


# ----------
# .random()
# ----------
# - número al azar entre 0 y 1
# - sin incluir el 1


# ---------------
# .random() * N
# ---------------
# - para generar números aleatorios de 0 a N
# - sin incluir N


# -----------------------------------------
# Truco str.format() para reducir decimales
# -----------------------------------------


# --------------
# .randint(x,y)
# --------------
# - número entero aleatorio entre x, y


# ----------
# .choice()
# ----------
# - aplicado en lista !!


# -----------
# .shuffle()
# -----------
# - aplicado en lista !!




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 31) Condicional Anidado
print('\n\n\n31) Condicional Anidado\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 32) Listas Multidimensionales
print('\n\n\n32) Listas Multidimensionales\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Una lista puede contener otras listas

# ---------------------------------------------
# Representación de una lista multidimensional
# ---------------------------------------------
# - esto nos recuerda a una matriz de números
# - ejemplo: matriz de 3 filas y 3 columnas


# --------------------
# Acceso de elementos
# --------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 33) Bucles Anidados
print('\n\n\n33) Bucles Anidados\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------------------
# Recorrido básico con while
# ---------------------------
# - NO OLVIDAR: while obliga tener un contador


# ==> recorrido básico


# ==> recorrido + print => forma de matriz


# -------------------------
# Recorrido básico con for
# -------------------------


# ==> recorrido básico


# ==> recorrido + print en forma de matriz




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 34) Mutabilidad / Inmutabilidad
print('\n\n34) Mutabilidad / Inmutabilidad\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Mutabilidad => que puede cambiar
# - Inmutabilidad => que no puede cambiar

# --------------------------------
# funciones internas id() & hex()
# --------------------------------
# id()  => dirección en la memoria de una variable
# hex() => transforma un entero a valor hexadecimal


# ----------------------
# concepto de INMUTABLE
# ----------------------
# - cualquier tipo básico


# ---------------------
# concepto de MUTABLE
# ---------------------
# - típico ejemplo son las listas




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 35) keyword is
print('\n\n35) keyword is\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
#   ==  | True: si 2 variables tienen el mismo valor
#   is  | True: mismo valor y dirección en la memoria

#   RECORDAR: hex(id()) => dirección en la memoria en valor hexadecimal !!




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 36) Tuplas
print('\n\n36) Tuplas\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - parecidos a las listas
# - son ordenadas
# - son inmutables / no se pueden modificar
# - se declaran con () / listas con []

# -----------------------
# Creación de una Tupla
# -----------------------
# - también tiene la función len()



# -------------------
# Indexing & Slicing
# -------------------


# -----------
# keyword in
# -----------


# ---------------
# Son INMUTABLES
# ---------------


# ---------------------
# Truco para Modificar
# ---------------------


# ---------------
# Concatenación
# ---------------


# -------------------------------
# Métodos => .count() / .index()
# -------------------------------


# --------------------
# Recorrido de tuplas
# --------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 37) Sets / Conjuntos
print('\n\n37) Sets / Conjuntos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - elementos únicos / conjuntos
# - colección desordenada
# - no se pueden alterar sus elementos, pero el set si
# - se crean con {}

# -------------------
# Creación de un Set
# -------------------
# - también tiene la función len()


# -------------------------------------
# No existe Indexing & Slicing en Sets
# -------------------------------------
# - ¿por qué? => los sets son colecciones desordenadas


# -------------------------------
# Elementos repetidos se eliminan
# -------------------------------
# - los elementos de un set son ÚNICOS


# -----------------------------------------
# No existe concatenación & producto (+ *)
# -----------------------------------------


# -----------------
# Recorrido de Set
# -----------------


# => Métodos Importantes para SET
# - no es posible modificar elementos de un set
# - pero es posible modificar el set como tal

# -------
# .add()
# -------



"""
Métodos para eliminar / borrar
    .remove()
    .discard()
    .pop()
    .clear()
    del set
"""

# ----------
# .remove()
# ----------


# -----------
# .discard() 
# -----------
# - igual que remove pero no me da error


# -------
# .pop()
# -------
# - elimina elemento al azar


# ---------
# .clear()
# ---------
# - deja un set vacío


# ---------
# del set
# ---------
# elimina la variable por completo



"""
Métodos de Operaciones de Conjuntos

    .union()         /  .update()
    .intersection()  /  .intersection_update()
    .difference()    /  .difference_update()

==> los update son para modificar un set existente
"""
# https://www.w3schools.com/python/python_ref_set.asp


# ------------------------
# .union()   /  .update()
# ------------------------
# - unión de conjuntos
# - se excluye elementos repetidos


# ---------------------------------------------
# .intersection()   /  .intersection_update()
# ---------------------------------------------
# - RETORNA elementos en común entre 2 conjuntos


# ----------------------------------------
# .difference()   /  .difference_update()
# ----------------------------------------
# - ELIMINA elementos en común entre 2 conjuntos


# --------
# .copy()
# --------
# - igual que en listas




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 38) Diccionarios
print('\n\n38) Diccionarios\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - es una también de las más importantes (después de LISTAS)
# - estructura de clave y valor (key-value pair)
# - python 3.7 >=  -- ORDENADOS
# - python 3.6 <=  -- DESORDENADOS

# -------------------------------
# Creación Básica de Diccionario
# -------------------------------
# - también funciona el len (tamaño de diccionario)


# ------------------
# Diccionario Vacío
# ------------------


# ------------------------------
# NO existe Indexing y Slicing
# ------------------------------


# -----------------
# Acceso con Clave
# -----------------


# --------------------------------------------
# Creación / Modificación con Acceso de Clave
# --------------------------------------------


# -----------------------------------------------
# 2 valores iguales es posible pero no 2 claves
# -----------------------------------------------
# - se sobrescribe el último valor ingresado


# ----------------------------------
# keyword in => averiguar una clave
# ----------------------------------
# - True si existe la clave, False si no


"""
MÉTODOS IMPORTANTES DE DICCIONARIOS
Métodos de Acceso => .get / .keys / .values / .items
Métodos de Modificación => .update / .setdefault
Métodos de Eliminación => .pop / .popitem / .clear / del
"""

# -------
# .get()
# -------


# --------
# .keys()
# --------


# ----------
# .values()
# ----------


# ---------
# .items()
# ---------
# - retorna tupla de (clave, valor)


# ----------
# .update()
# ----------
# modifica / crea clave - valor


# => Con acceso a clave


# => Pasar directamente un diccionario


# --------------
# .setdefault()
# --------------
# - recibe como argumentos clave & valor
# - .setdefault(clave, valor)
# - si existe la clave => no la modifica
# - si no existe => la crea


# -------
# .pop()
# -------
# - hay que pasar la clave como argumento
# - caso contrario da error
# - devuelve VALOR de elemento eliminado


# -----------
# .popitem()
# -----------
# - python 3.7 > -- borra último elemento
# - python 3.6 < -- borra elemento al azar
# - devuelve tupla de clave valor del elemento eliminado


# ----------
# .clear()
# ----------
# - deja un diccionario vacío


# -------------------
# del dict['clave']
# -------------------
# - elimina par de clave/valor pasando la clave
# - también elimina toda la variable de diccionario


# ---------------------------
# Recorrido de diccionarios
# ---------------------------
# - la mejor manera es con for + .items()




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 39) Casting entre Colecciones
print('\n\n39) Casting entre Colecciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------
# lista a tupla
# --------------
# - para dar mayor seguridad
# - recordar, las tuplas no son modificables


# ----------------------
# lista / tuplas a sets
# ----------------------
# - manera fácil de eliminar elementos repetidos


# ---------------------------------
# Casting a Diccionario => CUIDADO
# ---------------------------------
# - la colección debe tener sentido
# - con la estructura del diccionario
# - debe ser una colección de colecciones de 2 elementos (clave/valor)


# ==> Esto es ERROR


# ==> Esto es POSIBLE!




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 40) Funciones
print('\n\n40) Funciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------
# Función Básica
# ----------------


# ---------------------
# Parámetros y Retorno
# ---------------------
# - Un función puede o no tener parámetros
# - y puede o no retornar algún valor => keyword 'return'

# ==> sin parámetros / sin retorno


# ==> con parámetros / sin retorno


# ==> con parámetros / con retorno


# ==> sin parámetros / con retorno
# (no tiene mucho sentido, pero no es error)


# ---------------------------
# Pueden Redefinirse N veces
# ---------------------------


# --------------------------------------------
# Parámetros => Existen solo en las funciones
# --------------------------------------------
# - pueden repetirse
# - pueden tener el mismo nombre que variables creadas afuera
# - no afecta la función


# ---------------------------------------
# pass => definir función y trabar luego
# ---------------------------------------


# -------
# return
# -------
# - marca el fin de la función
# - pueden haber varios, con un condicional


# --------------------
# función en función
# --------------------


# -----------------------
# parámetros por defecto
# -----------------------

# ==> recordar print + end
# - este end es un parámetro por defecto '\n'


# ==> podemos definir las nuestras


# ==> SIEMPRE al final




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 41) Funciones Recursivas
print('\n\n41) Funciones Recursivas\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función que se llama a sí misma
# - cualquier cosa que se pueda hacer con una función recursiva
# - se puede hacer con función normal / bucle / condicional
# - CUIDADO: de caer en una función que nunca termina

# -----
# EJ 1
# -----


# -----
# EJ 2
# -----
# sumatorio(5) = 1+2+3+4+5 = 15


# -----
# EJ 3
# -----
# factorial(5) = 5*4*3*2*1 = 120




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 42) Scope de Variables
print('\n\n42) Scope de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------
# Global y Local
# ---------------
# - global => todo en el código con indentación 0
# - local  => todo lo que está dentro de las funciones
# - 1 sólo ámbito GLOBAL / N ámbitos LOCALES


# ---------------
# Keyword global
# ---------------

# ==> podemos mostrar una variable global dentro de local


# ==> NO se puede modificar directamente la variable global dentro de local
# - en el siguiente ejemplo
# - ambas se llaman a
# - pero son distintas, una es global / otra es local


# ==> Se puede modificar con keyword global




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 43) Funciones *args
print('\n\n43) Funciones *args\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función con argumentos arbitrarios
# - número indefinido de parámetros
# - que se guardan como tupla

# ----------------
# ¿qué son *args?
# ----------------

    
# ---------------------
# aplicación con *args
# ---------------------


# ----------------------------------------------
# el nombre args => no es relevante, pero si *
# ----------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 44) Funciones **kwargs
print('\n\n44) Funciones **kwargs\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función con argumentos arbitrarios asociados a clave
# - número indeterminado de parámetros
# - asociados a una clave
# - se los puede empacar en un diccionario

# --------------------
# ¿qué son **kwargs?
# --------------------


# ------------------------
# aplicación con **kwargs
# ------------------------


# ------------------------------------------------
# el nombre kwargs => no es relevante, pero si **
# ------------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 45) Función Lambda
print('\n\n45) Función Lambda\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función anónima
# - N argumentos => 1 sola expresión
# - como un "shortcut" => lo usamos luego lo descartamos

# ---------------------------
# Función Normal vs. Lambda
# ---------------------------

# ==> función normal


# ==> función lambda


# --------------------------
# Lambda con valores String
# --------------------------


# ------------------------------
# Lambda con Operador Ternario
# ------------------------------

# ==> Recordar: Operador Ternario


# ==> Lambda + Operador Ternario


# --------------------------
# Lambda => Función Anónima
# --------------------------
# - lambda puede ser el retorno de una función por ej.




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 46) Funciones como Variables
print('\n\n46) Funciones como Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - todo en Python puede ser variable
# - en Python todo es un objeto (POO)

# --------------------
# Función a Variable
# --------------------


# -------------------------------
# Funciones Internas a Variables
# -------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 47) Funciones de Orden Superior (High Order Functions)
print('\n\n47) Funciones de Orden Superior (High Order Functions)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Una función de orden superior puede ser 1 de las 2 siguientes:
#   a) Cuando acepta otra función como ARGUMENTO
#   b) Cuando retorna una 2da función definida en la 1era

# ----------------------------------------------
# a) Cuando acepta otra función como ARGUMENTO
# ----------------------------------------------

# ===> funciones normales


# ===> función de alto grado (high order function)


# ===> Ejecutando high order function
# - las funciones-argumento se pasan como firma, sin ejecutar !!


# ------------------------------------------------------
# b) Cuando retorna una 2da función definida en la 1era
# ------------------------------------------------------
# - EJ: una fórmula sencilla de la física
#   velocidad = distancia / tiempo


# ===> como función normal


# ===> como high order function




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 48) Decoradores
print('\n\n48) Decoradores\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - patrón de diseño
# - añadir nueva funcionalidad a un elemento / sin modificar la estructura

# ---------------
# SIN decorador
# ---------------


# --------------
# CON decorador
# --------------

# ==> función decoradora


# ==> función con decorador


# ==> invocando
 



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 49) sorted / map / filter / reduce
print('\n\n49) sorted / map / filter / reduce\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Funciones muy muy útiles para tratamiento de datos
# - Su fundamento se aplica en otros lenguajes de programación
# - ej: en javascript (programación web)

"""
    sorted => establecer ordenamiento
    map    => transformar una colección por medio de un cálculo
    filter => filtrado de datos de colección
    reduce => reducir grupo de datos a 1 sólo valor
"""



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 50) sorted()
print('\n\n50) sorted()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - las mismas nociones que .sort() de listas
# - la diferencia es que no modifica la lista

# -----
# EJ 1
# -----


# -----
# EJ 2
# -----




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 51) map()
print('\n\n51) map()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - map( funcion , elementos_iterables )
# - transforma una colección por medio de una función
# - "elementos_iterables" => puede ser más de 1 !!
# - retorna un objeto de tipo map

# ----------------------------------
# Ejemplo Básico con Función Normal
# ----------------------------------


# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------
# - ej: notas de 3 alumnos ordenadas en lista
# - nota_final = 0.2*deberes + 0.3*proyecto + 0.5*examen




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 52) filter()
print('\n\n52) filter()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - filter( funcion , elemento_iterable )
# - la función debe retornar True / False => de acuerdo al criterio de filtrado
# - la función puede ser normal / lambda
# - filter => retorna un objeto de tipo filter

# ----------------------------------
# Ejemplo Básico con Función Normal
# ----------------------------------


# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 53) reduce()
print('\n\n53) reduce()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - reduce ( función , elemento_iterable )
# - OJO: para usarlo hay que importar la librería functools !!!
# - reduce los valores de una colección a 1 sólo !
# - puede considerar un valor inicial

# -------------------------------------
# importar módulo / librería functools
# -------------------------------------


# ----------------
# Ejemplo Básico
# ----------------


# ------------------
# Ejemplo Complejo
# ------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 54) List Comprehension
print('\n\n54) List Comprehension\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - manera corta/dinámica/inteligente de crear una lista
# - se lo puede realizar por medio de 3 sintaxis:

"""
    A) lista = [ expresión + bucle FOR en un iterable ]
    B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
    C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
"""

# ----------------------------------------------------
# A) lista = [ expresión + bucle FOR en un iterable ]
# ----------------------------------------------------


# ---------------------------------------------------------------------
# B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
# ---------------------------------------------------------------------


# --------------------------------------------------------------------------
# C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
# --------------------------------------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 55) Dictionary Comprehension
print('\n\n55) Dictionary Comprehension\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - manera corta/dinámica/inteligente de crear un diccionario
# - a partir de otro diccionario
# - se lo puede realizar por medio de 4 sintaxis:

"""
    A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
    B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
    C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
    D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
"""


# --------------------------------------------------------------------
# A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
# --------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
# -------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
# ------------------------------------------------------------------------------


# -------------------------------------------------------------------------
# D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
# -------------------------------------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 56) Función Interna - zip
print('\n\n56) Función Interna - zip\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - empaca 2 o + iterables en un objeto tipo zip
# - el iterable de menor tamaño decide el tamaño del zip
# - básicamente se unen los valores en una tupla

# ---------------
# Ejemplo Básico
# ---------------


# --------------------------------------------------------
# N iterables / el de menor tamaño decide el tamaño final
# --------------------------------------------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 57) Librería time
print('\n\n57) Librería time\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - una opción para trabajar fecha y hora en Python => PERO no la más recomendable
# - crea fechas en función de la hora cero (EPOCH)
# - la hora cero (EPOCH) de la computadora se considera el 1 de enero de 1970
# - útil para crear estampas de tiempo y sleep !!!
# - para fechas / horas => veremos la librería datetime !!!

# ------------------------------
# importación de librería time
# ------------------------------


# -----------
# punto cero
# -----------


# ------------------------------------
# milisegundos a partir del tiempo 0
# ------------------------------------
# - desde el punto 0
# - hasta el preciso momento de ejecución de este script


# -------------
# fecha actual
# -------------
# - en el preciso momento de ejecución del script


# ---------------------------------------
# aplicación útil => estampas de tiempo
# ---------------------------------------
# - crear una identificación única para algún dato


# -------------
# time.sleep()
# -------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 58) Librería datetime
print('\n\n58) Librería datetime\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - la librería / módulo adecuado para trabajar hora y fecha

# ---------------------------------------------
# importación de la librería / módulo datetime
# ---------------------------------------------


# -------------
# fecha actual
# -------------
# - al momento de ejecución del script !!
# - retorna un objeto del tipo "datetime.datetime"


# -----------------------------------
# acceso a los elementos de datetime
# -----------------------------------
# - OJO: no son métodos
# - son atributos / propiedades del objeto (teoría de POO)
# - en pocas palabras => no usar los paréntesis al final

"""
Elemento de Acceso          |  Manera de Acceder
-----------------------------------------------------------
acceder al año              |  fecha_datetime.year 
acceder al mes              |  fecha_datetime.month 
acceder al día              |  fecha_datetime.day 
acceder a la hora           |  fecha_datetime.hour
acceder a los minutos       |  fecha_datetime.minute
acceder a los segundos      |  fecha_datetime.second
acceder a los microsegundos |  fecha_datetime.microsecond
"""


# ------------------------------
# creando fechas personalizadas
# ------------------------------
# - de 2 maneras
#   a) tupla de 3 valores (año, mes, día)
#   b) tupla de 6 valores (año, mes, día, hora, minutos, segundos)


# -----------------------------
# formato personalizado fácil
# -----------------------------
# - hay muchas maneras de complicarse aquí
# - pero como breve introducción aprenderemos una manera muy fácil


# ---------------------
# reloj en tiempo real
# ---------------------




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 59) keywords as / from
print('\n\n59) keyword as / from\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - as   ==> para redefinir el nombre de una librería módulo
# - from ==> para importar algo específico de un módulo




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 60) Operador Walrus :=
print('\n\n60) Operador Walrus :=\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - a partir de python 3.8 >
# - asignador de expresión
# - asignar variables dentro de alguna función / expresión

# ---------------
# Ejemplo Básico
# ---------------


# ---------------------
# Ejemplo más complejo
# ---------------------

# ==> sin walrus :=


# ==> con walrus :=



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 61) Gestión de Errores => try-except
print('\n\n61) Gestión de Errores => try-except\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - errores en programación hay básicamente 2
#   a) errores de sintaxis => algo escribimos mal (lo detecta el editor de código)
#   b) errores de ejecución => todo bien escrito, pero algo usamos mal
# - ambos paran la ejecución del programa
# - try-except => para capturar el error y gestionarlo
# - raise => para definir un error personalizado

# ------------------
# Error de Sintaxis
# ------------------


# -------------------
# Error de Ejecución
# -------------------


# ------------------
# try-except Básico
# ------------------
# - try => alberga el código peligroso que puede causar error
# - except => presenta el error sin parar la ejecución del programa


# ------------------
# Mostrando el error
# ------------------
# - usando Exception y un alias


# ---------------------------------------------
# Estructura Completa: try-except-else-finally
# ---------------------------------------------
"""
try:     aquí va el código que tiene el riesgo de producir error
except:  bloque que se ejecuta en caso de error sin interrumpir el flujo del programa
else:    bloque que se ejecuta cuando no se da error
finally: bloque que se ejecuta SIEMPRE, haya error o no
"""


# -----------------
# type(e).__name__
# -----------------
# - devuelve el tipo del error


# ---------------------------------
# Capturar Excepciones Específicas
# ---------------------------------


# --------------------------------
# Generar Errores Personalizados
# --------------------------------
# - raise => invocamos un error
# - OJO: debemos capturarlo, caso contrario, se para la ejecución del programa


# ==> definición de una función sencilla


# ==> prohibiendo al usuario poner números en el nombre


# ==> utilizando raise


# ==> raise + try-except




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 62) Breve Introducción a numpy
print('\n\n62) Breve Introducción a numpy\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----------------
# ¿Por qué numpy?
# -----------------


# -----------------------------------------------------
# ¿Hay alguna manera de hacer operaciones aritméticas?
# -----------------------------------------------------

# ==> utilizando for


# ==> utilizando while


# --------------------------------------------------
# ¿Existe otra manera más fácil? => librería numpy
# --------------------------------------------------

# ==> importando la librería numpy
# - instalar primero: pip install numpy
# - verificar si está instalado: pip list + buscar numpy
# - Replit, tenemos que instalarlo en el shell


# ==> averiguando versión en terminal


# ==> creando un array con numpy


# ==> creando array de numpy con variable de lista


# ==> operaciones aritméticas de listas con numpy


# ==> operaciones escalar & array


# ==> funciones normales con numpy


# ==> libería math & array


# ==> funciones aritméticas numpy
# https://numpy.org/doc/stable/reference/routines.math.html


# ==> linspace
# - generar una distribución estándar de números desde un inicio a un final




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 63) Breve Introducción a Matplotlib
print('\n\n63) Breve Introducción a Matplotlib\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------------
# ¿Por qué matplotlib?
# ---------------------
# - una librería externa de python, súper útil
# - nos ayuda a realizar gráficas con datos numéricos
# - Referencia: https://www.w3schools.com/python/matplotlib_intro.asp


# ------------------------
# importación del módulo
# ------------------------
# - no viene por defecto cuando se instala python
# - instalar en el CMD:
"""
python -m pip install -U pip
python -m pip install -U matplotlib
"""
# - verificar si está instalado: pip list + buscar matplotlib
# - Replit permite instalarlo con el SHELL


# -------------------------------
# Averiguar versión en Terminal
# -------------------------------


# ----------------------------------
# importación específica de pyplot
# ----------------------------------


# -----------------------
# plot básico con listas
# -----------------------


# ---------------------------
# Marcadores / Línea / Color
# ---------------------------
# - marker|line|color
# - https://www.w3schools.com/python/matplotlib_markers.asp

# MARCADORES
"""
    Marcador        Descripción
    'o'             Círculo
    '*'             Estrella
    'X'             Equis
"""

# LÍNEA
"""
    Sintaxis        Descripción
    '-'             Línea Sólida
    ':'             Línea de puntos
    '--'            Línea entrecortada
"""

# COLORES
"""
    Sintaxis        Descripción
    'r'             Rojo
    'g'             Verde
    'b'             Azul
"""


# -----------------------------------------------
# Tamaño marcador => markersize => ms
# Color borde marcador => markeredgecolor => mec
# Color fondo marcador =>markerfacecolor  => mfc
# -----------------------------------------------


# ------------------------------------
# Tamaño de línea => linewidth => lw
# ------------------------------------


# ----------------------------
# Título & Etiquetas de Ejes
# ----------------------------
# Título => plt.title('')
# Etiqueta / Label en X => plt.xlabel('')
# Etiqueta / Label en Y => plt.ylabel('')


# --------------------------------
# Incorporar Grilla => plt.grid()
# --------------------------------
# - Grilla en X, Y => plt.grid()
# - Grilla en X    => plt.grid(axis = 'x')
# - Grilla en Y    => plt.grid(axis = 'y')


# -------------------
# Tipos de Gráficos
# -------------------
# - Dispersión / Scatter => plt.scatter(x,y)
# - Barras / Bars => plt.bar(x,y)
# - Pastel / Pie => plt.pie(y)

# DISPERSIÓN & BARRAS


# PASTEL




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 64) Matplotlib + Numpy
print('\n\n64) Matplotlib + Numpy\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------
# A) Función de valores de X
# ----------------------------


# -------------------------------------------
# B) Valores de X / Valores de Y con numpy
# -------------------------------------------


# -----------------------
# C) Ejecutar Matplotlib
# -----------------------
