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

# comentario de una línea 1
# comentario número 2
# comentario número 3
# comentario número 4

'''
esto es un comentario
de varias líneas
'''

"""
esta es otra manera de 
poner comentarios de varias líneas
pero
con comillas dobles !!!
"""

# => ≡ alt + 240




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 2) print()
print('\n\n\n2) print()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función interna para imprimir en consola
# - función interna en python => built-in function

print('Hola Mundo')
print("Hola Mundo")
print('Hola a todos! Soy Sebastián, me gusta Python!')
print(123456)
print(555)
print(12.5)


# -------------
# Línea Vacía
# -------------
print('¿Cómo estás?')
print() # línea vacía
print("Estoy bien, gracias, y tú cómo estás?")
print('') # línea vacía
print("Gracias")
print("") # línea vacía
print('De nada!!!!')




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 3) Variables
print('\n\n\n3) Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - contenedor / espacio con memoria
# - para guardar un valor

a = 20
b = 10.5
c = 'Sebas'

print(a) # 20
print(b) # 10.5
print(c) # Sebas


# ----------------------------------------------------------------------
# Truco print => imprimir varios valores, separando con coma
# ¿por qué? => print es una función => recibe argumentos de función
# ----------------------------------------------------------------------
print(a,b,c) # 20 10.5 Sebas
print('hola' , -50 , -5.5) # hola -50 -5.5
print('hola',-50,-5.5) # hola -50 -5.5
print('hola'    ,    -50   ,    -5.5) # hola -50 -5.5


# --------------------------------
# Redefinir / Reasignar variables
# --------------------------------
print(a) # 20
a = "I love Python, Sebas is the best!!!"
print(a) # I love Python, Sebas is the best!!!


# ---------------------
# Asignación Múltiple
# ---------------------
a , b , c = 100, -5.5, 'Hola' # 1 sola línea de código !!!
print(a) # 100
print(b) # -5.5
print(c) # Hola


# -----------------------------------
# Asignación Múltiple a Valor Único
# -----------------------------------
a = b = c = "Python"
print(a) # Python
print(b) # Python
print(c) # Python



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

nombre = 'Sebas'
apellido = 'Silva'
edad = 36
pais_origen = 'Ecuador'

print( nombre, apellido, edad, pais_origen ) # Sebas Silva 36 Ecuador


# ------------------------
# print en varias líneas
# ------------------------

print(
nombre,
apellido,
edad,
pais_origen
) # Sebas Silva 36 Ecuador

#123nombre = 'Sebas' # ERROR
#%nombre = 'Silva'   # ERROR



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

nombre = 'Sebas'
edad = 36
nota = 18.5
es_profesor = True
es_estudiante = False

print( nombre , type(nombre) ) # Sebas <class 'str'>
print( edad , type(edad) ) # 36 <class 'int'>
print( nota , type(nota) ) # 18.5 <class 'float'>
print( es_profesor , type(es_profesor) ) # True <class 'bool'>
print( es_estudiante , type(es_estudiante) ) # False <class 'bool'>


# ----------------------------------------------------------------
# None => útil para crear una variable sin valor y asignar luego
# ----------------------------------------------------------------
# declaración => int a;
# asignación => a = 20;

#a = 20

x = None 
print( x , type(x) ) # None <class 'NoneType'>

# ... han pasado bastantes líneas de código aquí!!!

x = 100
print( x , type(x) ) # 100 <class 'int'>




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
var_str = '100' # string numérico
print( var_str , type(var_str) ) # 100 <class 'str'>

var_int = int(var_str)
var_float = float(var_str)
var_bool = bool(var_str)

print( var_int , type(var_int) ) # 100 <class 'int'>
print( var_float , type(var_float) ) # 100.0 <class 'float'>
print( var_bool , type(var_bool) ) # True <class 'bool'>

num_int = 5
num_float = float(num_int)

print( num_int , type(num_int) ) # 5 <class 'int'>
print( num_float , type(num_float) ) # 5.0 <class 'float'>


# -------------------------
# Todo es CASTEABLE a bool
# -------------------------
str_1 = 'h'
str_2 = ' '
str_3 = ''
int_1 = 10
int_2 = -5
int_3 = 0
float_1 = 5.5
float_2 = -6.88
float_3 = 0.0
none_1 = None 

print( str_1 , '=>' , bool(str_1) ) # h => True
print( str_2 , '=>' , bool(str_2) ) #   => True
print( str_3 , '=>' , bool(str_3) ) #  => False
print( int_1 , '=>' , bool(int_1) ) # 10 => True
print( int_2 , '=>' , bool(int_2) ) # -5 => True
print( int_3 , '=>' , bool(int_3) ) # 0 => False
print( float_1 , '=>' , bool(float_1) ) # 5.5 => True
print( float_2 , '=>' , bool(float_2) ) # -6.88 => True
print( float_3 , '=>' , bool(float_3) ) # 0.0 => False
print( none_1 , '=>' , bool(none_1) ) # None => False


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

a = 'hola'
b = 100

print( a , type(a) ) # hola <class 'str'>
print( b , type(b) ) # 100 <class 'int'>

# el valor a es un string ???
print( isinstance( a , str ) ) # True
print( isinstance( a , int ) ) # False
print( isinstance( b , str ) ) # False
print( isinstance( b , int ) ) # True




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
#help(print)
#help(str)
#help(type)

# ------------------
# Navegar en help()
# ------------------
# - help() + topics + seleccionar tema + enter
#help()




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
#2 + 3
#5 * 8
#9 / 5

# tiene más sentido imprimir para ver esto
print( 2 + 3 ) # 5
print( 5 * 8 ) # 40
#print(9/5) # 1.8
print( 9 / 5 ) # 1.8


# -------------------------
# Aritmética con variables
# -------------------------
x = 10
y = 3

print( x, '+', y, '=', x + y ) # 10 + 3 = 13
print( x, '-', y, '=', x - y ) # 10 - 3 = 7
print( x, '*', y, '=', x * y ) # 10 * 3 = 30
print( x, '/', y, '=', x / y ) # 10 / 3 = 3.3333333333333335
print( x, '**', y, '=', x ** y ) # 10 ** 3 = 1000
print( x, '%', y, '=', x % y ) # 10 % 3 = 1 ??
print( x, '//', y, '=', x // y ) # 10 // 3 = 3 ??


# -------
# Módulo
# -------
#    10 |___ 4
#    -8      2
#     2

print( 10 % 4 ) # 2


# --------------------
# División y Redondeo
# --------------------
# divide y devuelve la parte entera
print( 5/2 , 5//2 ) # 2.5 2
print( 9/5 , 9//5 ) # 1.8 1
print( type(9/5) , type(9//5) ) # <class 'float'> <class 'int'>

# la división convierte a punto flotante !

print( 4/2 ) # 2.0

# ----------------------------------
# Las reglas matemáticas se cumplen
# ----------------------------------
x = 5
y = 2
resultado = x * (y + x) - y + x**y - x / (x - 2*y)
#           5 * (2 + 5) - 2 + 5**2 - 5 / (5 - 2*2)
#           5 *    7    - 2 + 25   - 5 / (5 - 4)
#           35 - 2 + 25 - 5 / 1
#           35 - 2 + 25 - 5.0
#           53.0

print( resultado , type(resultado) ) # 53.0 <class 'float'>




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

print('hola mundo')
print('hola\nmundo\n\n\n\nhola sebas')

print('\tpython\t\tjava')

#print("El lenguaje de programación "Python" es chévere!!")
print("El lenguaje de programación \"Python\" es chévere!!")
print('El lenguaje de programación "Python" es chévere!!')

print('El lenguaje de programación \'Python\' es chévere!!')
print("El lenguaje de programación 'Python' es chévere!!")

print('HolaAmigos')
print('Hola\bAmigos') # retroceso

print('hola\mundo') # hola\mundo
print('hola\barbacoa') # holarbacoa
print('hola\\barbacoa') # hola\barbacoa




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 11) String <str>
print('\n\n\n11) String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------------
# formas de representar un string
# --------------------------------
cadena_1 = 'hola python'
cadena_2 = "hola java"
cadena_3 = '''hola ecuador'''
cadena_4 = """hola alemania"""

"""
comentario
de varias
líneas
"""

cadena_5 = """
hola, este string
tiene

\tvarias
líneas!!\n
Saludos cordiales!
"""

print( cadena_1 , type(cadena_1) )
print( cadena_2 , type(cadena_2) )
print( cadena_3 , type(cadena_3) )
print( cadena_4 , type(cadena_4) )
print( cadena_5 , type(cadena_5) )


# -----------------
# concatenación +
# -----------------
nombre = 'Sebas'
apellido = 'Silva'
texto = nombre + apellido
print(texto) # SebasSilva

nombre = 'Sebas'
apellido = ' Silva'
texto = nombre + apellido
print(texto) # Sebas Silva

nombre = 'Sebas'
apellido = 'Silva'
texto = nombre + ' ' + apellido
print(texto) # Sebas Silva

# ------------------
# multiplicación *
# ------------------
letra = 'A'
print( 5 * letra ) # AAAAA
print( letra * 5 ) # AAAAA

# ------------------------------
# índices [i] y tamaño => len()
# ------------------------------
palabra = 'hola'
# (+)      0123
# (-)      4321

print( palabra ) # hola
print()
print( palabra[0] ) # h
print( palabra[1] ) # o
print( palabra[2] ) # l
print( palabra[3] ) # a
print()
print( palabra[-4] ) # h
print( palabra[-3] ) # o
print( palabra[-2] ) # l
print( palabra[-1] ) # a
print()
print( len(palabra) , type( len(palabra) ) ) # 4 <class 'int'>

#print( palabra[100] ) # IndexError: string index out of range

# ---------------------------
# slicing [start:end:step]
# end - exclusivo
# start, step - opcionales
# ---------------------------

palabra = 'programación'
#          012345678901
#          0         1

# EJ:
# pro
# gramación

print( palabra[0:2] ) # pr => END - exclusivo
print( palabra[0:3] ) # pro
print( palabra[3:11] ) # gramació
print( palabra[3:12] ) # gramación
print( palabra[3:50] ) # gramación
print()
print( palabra[:3] ) # pro
print( palabra[3:] ) # gramación

# EJ:
# grama

print( palabra[3:8] ) # grama
print( palabra[3:8:1] ) # grama
print( palabra[3:8:2] ) # gaa

# EJ
# => usando step / salto
print( palabra[::] ) # programación
print( palabra[::1] ) # programación
print( palabra[::2] ) # pormcó
print( palabra[::3] ) # pgmi
print( palabra[::4] ) # prc



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 12) Métodos de Formato Importantes de String <str>
print('\n\n\n12) Métodos de Formato Importantes de String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------
# Para dar formato a texto
# --------------------------
texto = 'mE gusTA APRENDER pyTHON'

print(texto) # mE gusTA APRENDER pyTHON
print( texto.capitalize() ) # Me gusta aprender python
print( texto.title() ) # Me Gusta Aprender Python
print( texto.upper() ) # ME GUSTA APRENDER PYTHON
print( texto.lower() ) # me gusta aprender python
print( texto.swapcase() ) # Me GUSta aprender PYthon


# ---------------------
# Alineación de texto
# ---------------------
nombre = 'Andy'

print('Hola', nombre, 'espero que estés bien!') # Hola Andy espero que estés bien!
print('Hola', nombre.center(10), 'espero que estés bien!') # Hola    Andy    espero que estés bien!
print('Hola', nombre.ljust(10), 'espero que estés bien!') # Hola Andy       espero que estés bien!
print('Hola', nombre.rjust(10), 'espero que estés bien!') # Hola       Andy espero que estés bien!


# ---------------------
# Contar Coincidencias
# ---------------------
cadena = 'esta vida es hermosa'
#         01234567890123456785
#         0         1

print( cadena.count('a') ) # 3
print( cadena.count('es') ) # 2
print( cadena.count('a',4) ) # 2
print( cadena.count('a',4,10) ) # 1
print( cadena.count('x') ) # 0


# --------------------------------
# Retornar índice de una búsqueda
# --------------------------------
lenguaje = 'javascript'
#           0123456789

print( lenguaje.index('a') , lenguaje.find('a') ) # 1 1 => por defecto: de izq a der
print( lenguaje.rindex('a') , lenguaje.rfind('a') ) # 3 3 => der a izq
print( lenguaje.index('asc') , lenguaje.find('asc') ) # 3 3
print( lenguaje.rindex('asc') , lenguaje.rfind('asc') ) # 3 3
print( lenguaje.rindex('c',3,8) , lenguaje.rfind('c',3,8) ) # 5 5
#print( lenguaje.index('x') ) # ValueError: substring not found
print( lenguaje.find('x') ) # -1


# ------------------------------
# Eliminar espacios / caracter
# ------------------------------
# IMPORTANTE

c1 = '    python'
c2 = 'python     '
c3 = '    python    '
c4 = '*****python****'

print(c1) #     python
print(c2) # python     
print(c3) #     python    
print(c4) # *****python****

print( c1.lstrip() ) # python
print( c2.rstrip() ) # python
print( c3.strip() ) # python
print( c1.strip() ) # python
print( c2.strip() ) # python
print( c4.strip('*') ) # python


# -------------------------------------------
# Unir un caracter a un string en secuencia
# -------------------------------------------
char_1 = '-'
char_2 = '#'

palabra = 'youtube'

print( char_1.join(palabra) ) # y-o-u-t-u-b-e
print( char_2.join(palabra) ) # y#o#u#t#u#b#e

print( '....'.join(palabra) ) # y....o....u....t....u....b....e

# ---------------------------------------------
# Separar un string en elementos de una lista
# (* tema lista ya lo vemos a continuación)
# ---------------------------------------------
lenguajes_1 = 'java python c++ basic'
lenguajes_2 = 'java,python,c++,basic'

lista_1 = lenguajes_1.split()
lista_2 = lenguajes_2.split(',')

print( lista_1 , type(lista_1) , len(lista_1) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4
print( lista_2 , type(lista_2) , len(lista_2) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4

# --------------------------
# Líneas de string a lista
# --------------------------
texto = 'Yo programo en Python.\nEl en Java.\nElla en C++'
print(texto)

lista_1 = texto.splitlines()
print(lista_1) # ['Yo programo en Python.', 'El en Java.', 'Ella en C++']

lista_2 = texto.splitlines(keepends=True)
print(lista_2) # ['Yo programo en Python.\n', 'El en Java.\n', 'Ella en C++']


texto = """hola
mundo
hola python"""

print(texto)

lista = texto.splitlines()
print(lista)

# --------------------------
# Cambiar espaciado de tabs
# --------------------------
saludo = 'hola\tamigo'

print(saludo) # hola    amigo
print( saludo.expandtabs() ) # hola    amigo
print( saludo.expandtabs(1) ) # hola amigo
print( saludo.expandtabs(2) ) # hola  amigo
print( saludo.expandtabs(3) ) # hola  amigo
print( saludo.expandtabs(4) ) # hola    amigo


# -----------------------------------------------
# IMPORTANTE: reemplazar un caracter del string
# -----------------------------------------------
secreto = 'palabra secreta palabra oculta'
secreto = 'pXlabrX secrXtX pXlabrX ocultX'

print( secreto )

print( secreto.replace('X' , '***') ) # p***labr*** secr***t*** p***labr*** ocult***
print( secreto.replace('pXl' , 'ZZZZZ') ) # ZZZZZabrX secrXtX ZZZZZabrX ocultX
print( secreto.replace(' ' , 'yyy') ) # pXlabrXyyysecrXtXyyypXlabrXyyyocultX

print( secreto )

# => ¿se puede modificar los strings con métodos?
# la variable original ?
# NO
# => mutabilidad / inmutabilidad




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 13) Métodos de String con Retorno Booleano (averiguar algo en el String)
print('\n\n\n13) Métodos de String con Retorno Booleano (averiguar algo en el String)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------------------------------
# .isalpha() => True si todos son letras (A-Z / a-z)
# ----------------------------------------------------
c_1 = 'abcXYZ'
c_2 = 'abc XYZ'
c_3 = '1abcXYZ'
c_4 = 'abcXYZ1'

print( c_1 , c_1.isalpha() ) # abcXYZ True
print( c_2 , c_2.isalpha() ) # abc XYZ False
print( c_3 , c_3.isalpha() ) # 1abcXYZ False
print( c_4 , c_4.isalpha() ) # abcXYZ1 False


# -------------------------------------------
# .isalnum() => True si son letras y números
# -------------------------------------------
print( c_1 , c_1.isalnum() ) # abcXYZ True
print( c_2 , c_2.isalnum() ) # abc XYZ False
print( c_3 , c_3.isalnum() ) # 1abcXYZ True
print( c_4 , c_4.isalnum() ) # abcXYZ1 True

# ----------------------------------------------------
# .isdigit() => True si es un sting numérico (ENTERO)
# ----------------------------------------------------
c_1 = '12345'
c_2 = '123 45'
c_3 = '12.345'
c_4 = 'a12345'

print( c_1 , c_1.isdigit() ) # 12345 True
print( c_2 , c_2.isdigit() ) # 123 45 False
print( c_3 , c_3.isdigit() ) # 12.345 False
print( c_4 , c_4.isdigit() ) # a12345 False

# --------------------------
# Verificadores de formato
# .islower()
# .isupper()
# .istitle()
# --------------------------
c_1 = 'Hola Amigo' # title
c_2 = 'Hola amigo'
c_3 = 'HOLA AMIGO'
c_4 = 'hola amigo'

print( 'string|.islower()|.isupper()|.istitle()' )
print( c_1 , c_1.islower(), c_1.isupper(), c_1.istitle() )
print( c_2 , c_2.islower(), c_2.isupper(), c_2.istitle() )
print( c_3 , c_3.islower(), c_3.isupper(), c_3.istitle() )
print( c_4 , c_4.islower(), c_4.isupper(), c_4.istitle() )

# string|.islower()|.isupper()|.istitle()
# Hola Amigo False False True
# Hola amigo False False False
# HOLA AMIGO False True False
# hola amigo True False False

# ----------------------------
# .startswith() / .endswith()
# ----------------------------
c_1 = 'súper python!'
c_2 = ' Hola mundo...'

print( c_1.startswith('s') ) # True
print( c_1.startswith('sú') ) # True
print( c_1.startswith('su') ) # False
print( c_2.startswith(' ') ) # True
print( c_2.startswith(' H') ) # True
print( c_2.startswith(' h') ) # False
print()
print( c_1.endswith('!') ) # True
print( c_1.endswith('n!') ) # True
print( c_1.endswith('On!') ) # False




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 14) Métodos para Números + Librería Math
print('\n\n\n14) Métodos para Números + Librería Math\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ==> funciones internas para números

# ---------------------------------
# round() / inmediato superior
# ---------------------------------
num_1 = 3.2
num_2 = 3.5
num_3 = 3.9

print( num_1 , '|' , round(num_1) ) # 3.2 | 3
print( num_2 , '|' , round(num_2) ) # 3.5 | 4
print( num_3 , '|' , round(num_3) ) # 3.9 | 4

# ---------------------------
# abs() / valor absoluto
# ---------------------------
num_1 = -9
num_2 = -10.5

print( num_1, abs(num_1) ) # -9 9
print( num_2, abs(num_2) ) # -10.5 10.5


# ---------------------
# pow() / exponencial
# ---------------------
print( 2**3 ) # 8
print( pow(2,3) ) # 8

print( 25**0.5 ) # 5.0
print( 25**(1/2) ) # 5.0
print( pow(25,0.5) ) # 5.0
print( pow(25,1/2) ) # 5.0

# -----------------------------------
# sum() / max() / min() / En Listas
# -----------------------------------
lista_1 = [-5, 20, 5, 8.6, -1.2]

print( sum(lista_1) ) # 27.400000000000002
print( max(lista_1) ) # 20
print( min(lista_1) ) # -5


# ==> librería math
# https://www.w3schools.com/python/python_math.asp

# --------------------------
# Importación de un módulo
# --------------------------
#math.cos(45) # NameError: name 'math' is not defined
import math

# ------------
# Constantes
# ------------
print( math.e ) # 2.718281828459045
print( math.pi ) # 3.141592653589793

# ------------------------
# Representación numérica
# ------------------------
num = 3.5
print( num ) # 3.5
print( round(num) ) # 4
print( math.ceil(num) ) # ceil => techo # 4
print( math.floor(num) ) # floor => piso # 4

num = 1.01
print( math.ceil(num) ) # 2
print( math.floor(num) ) # 1

# ------------------
# Raíces y Potencia
# ------------------
print( math.pow(2,3) ) # 8.0 => flotante
print( pow(2,3) ) # 8
print( math.sqrt(25) ) # 5.0 => flotante
#print( math.cbrt(8) ) # AttributeError: module 'math' has no attribute 'cbrt'

# -----------
# Logaritmos
# -----------
# log 5 => e ^ x = 5
# log(10) 1000 => 10 ^ x = 1000 => 3

print( math.log(2.71**5) ) # logaritmo natural # 4.984743174458048
print( math.log10(10000) ) # logaritmo base 10 # 4.0

# -----------------------------
# Ángulos
# 360 grados == 2*pi radianes
# 180 grados = pi radianes
# -----------------------------
print( math.degrees( math.pi / 3 ) ) # pasar de rad a grados => 59.99999999999999
print( math.radians(180) ) # pasar de grados a rad => 3.141592653589793

# angulos en radianes para funciones trigonométricas
print( math.sin( math.pi/6 ) ) # seno de 30 grados => 0.49999999999999994
print( math.cos( math.pi/3 ) ) # coseno de 60 grados => 0.5000000000000001
print( math.tan( math.pi/4 ) ) # tangente de 45 grados => 0.9999999999999999

# funciones trigonométricas inversas
print( math.asin(0.5) ) # 0.5235987755982989 (30 grados en radianes)
print( math.acos(0.5) ) # 1.0471975511965979 (60 grados en radianes)
print( math.atan(1) ) # 0.7853981633974483 (45 grados en radianes)

print( math.degrees( math.asin(0.5) ) ) # 30.000000000000004
print( math.degrees( math.acos(0.5) ) ) # 60.00000000000001
print( math.degrees( math.atan(1) ) ) # 45.0

# ----------------------------
# Otras funciones importantes
# ----------------------------
# factorial
# 4! = 4*3*2*1 = 24
# 6! = 6*5*4*3*2*1 = 720

print( math.factorial(4) ) # 24
print( math.factorial(6) ) # 720

lista = [-5, 20, 5, 8.6, -1.2]
print( sum(lista) ) # 27.400000000000002
print( math.fsum(lista) ) # 27.4

num = -55.66
print( math.fabs(num) ) # 55.66
print( abs(num) ) # 55.66




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 15) Encadenamiento / Chaining - Funciones & Métodos
print('\n\n\n15) Encadenamiento / Chaining - Funciones & Métodos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# Métodos
# => izquierda a derecha
# ------------------------
str_1 = '      hOlA MunDO    '
print( str_1 ) #       hOlA MunDO    
print( str_1.title().strip(' ') ) # Hola Mundo


# -------------------------
# Funciones
# => de dentro hacia fuera
# -------------------------
print( type( len(str_1) ) ) # <class 'int'>




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 16) Función Interna => eval()
print('\n\n\n16) Función Interna => eval()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - evaluar una expresión matemática
# - expresada a manera de string

expr_1 = '2*5 - (10+3)/2 - 2**3'
expr_2 = "2*5 - (10 + 3)/2 - 2**3 - pow(3,2) + sum([1,2,3])"

print( eval(expr_1) ) # -4.5
print( eval(expr_2) ) # -7.5

expr_3 = '2 * 3 */ 8'

#print( eval(expr_3) ) # SyntaxError: invalid syntax




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 17) input => entrada de datos
print('\n\n\n17) input => entrada de datos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - OJO: todo lo que viene del input viene como string <str>

# -----------
# SIN input
# -----------
nombre = 'Sebas'
edad = 36

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
print('El próximo año 2024, usted tendrá', edad+1, 'años')

# -----------------
# Utilizando input
# -----------------
"""
nombre = input('¿Cuál es su nombre? : ')
edad = input('¿Cuántos años tiene usted? : ')

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
#print('El próximo año 2024, usted tendrá', edad+1, 'años')
# TypeError: can only concatenate str (not "int") to str

# ==> OJO: todo lo que viene del input es str

print( type(nombre) ) # <class 'str'>
print( type(edad) ) # <class 'str'>
"""

# -------------------
# Utilizando casting
# -------------------
"""
nombre = input('¿Cuál es su nombre? : ')
edad = input('¿Cuántos años tiene usted? : ')
edad = int(edad)

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
print('El próximo año 2024, usted tendrá', edad+1, 'años')
"""




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
   ==    |  Igual que (valores)
   !=    |  Diferente de (valores)
'''

# ------------
# Con Números
# ------------
print( 5 > 2 ) # True
print( 2 < 5 ) # True
print( 2 >= 2 ) # True
print( 3 <= 4 ) # True
print( 3 <= 3 ) # True
print( 8 == 8 ) # True
print( 8 == 9 ) # False
print( 8 != 9 ) # True
print( 10 != 10 ) # False

# ------------
# Con Strings
# ------------
print( 'a' > 'z' ) # False
print( '&' > '@' ) # False


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
and      |  X and Y  |  True si todos son True
or       |  X or Y   |  Basta que 1 sea True, resultado es True
not      |  not X    |  Niega al booleano
'''

print('\nTabla AND')
# => basta que tengamos 1 False : resultado es False
print( True and False ) # False
print( False and True ) # False
print( False and False ) # False
print( True and True ) # True
print( True and True and True and True ) # True
print( True and True and False and True ) # False

print('\nTabla OR')
# => basta que tengamos 1 True : resultado es True
print( True or False ) # True
print( False or True ) # True
print( False or False ) # False
print( True or True ) # True
print( True or True or True or True ) # True
print( True or True or False or True ) # True

print('\nTabla NOT')
print( not True ) # False
print( not False ) # True

print('\nCombinando')
print( True and False or (True and not False) ) # True
#      False or (True)
#      True




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

lista = [ True, -100, 'ABC', 8.5, None, [1,2,3] ]
print( lista , type(lista) , len(lista) )
# [True, -100, 'ABC', 8.5, None, [1, 2, 3]] <class 'list'> 6


# ----------------------------
# Creación con Función list()
# ----------------------------
lista = list([1,2,'A'])
print( lista , type(lista) , len(lista) )
# [1, 2, 'A'] <class 'list'> 3


# ------------
# Lista Vacía
# ------------
lista_vacia_1 = []
lista_vacia_2 = list()

print( lista_vacia_1 , len(lista_vacia_1) ) # [] 0
print( lista_vacia_2 , len(lista_vacia_2) ) # [] 0


# ---------------------------
# Palabra Clave / Keyword in
# ---------------------------
lista = [ True, -100, 'ABC', 8.5, None, [1,2,3] ]

print( 'ABC' in lista ) # True
print( -100 in lista ) # True
print( '-100' in lista ) # False


# ------------------------------
# Concatenación + y Operador *
# ------------------------------
lista_1 = [10, 20]
lista_2 = ['A', 'B']

r1 = lista_1 + lista_2
r2 = lista_2 + lista_1
r3 = 2 * lista_1
r4 = lista_2 * 3

print( r1 ) # [10, 20, 'A', 'B']
print( r2 ) # ['A', 'B', 10, 20]
print( r3 ) # [10, 20, 10, 20]
print( r4 ) # ['A', 'B', 'A', 'B', 'A', 'B']


# -------------------
# Indexing & Slicing
# -------------------
lista = [10,20,30,40]
#         0  1  2  3

print( lista[0] ) # 10
print( lista[1] ) # 20
print( lista[2] ) # 30
print( lista[3] ) # 40
print( lista[-1] ) # 40
print( lista[1:3] ) # [20, 30]
print( lista[:3] ) # [10, 20, 30]
print( lista[3:] ) # [40]
print( lista[::2] ) # [10, 30]


# ==> Métodos Importantes

# -----------
# .append()
# -----------
print()
lista = [1,2,3]
print(lista) # [1, 2, 3]
lista.append('a')
print(lista) # [1, 2, 3, 'a']
lista.append([10,20])
print( lista , len(lista) ) # [1, 2, 3, 'a', [10, 20]] 5

# -----------
# .insert()
# -----------
lista = ['A' , 'B' , 'C']
#         0     1     2

lista.insert(1 , 'Sebas')
print(lista) # ['A', 'Sebas', 'B', 'C']

lista.insert(-1 , 1520)
print(lista) # ['A', 'Sebas', 'B', 1520, 'C']


# -------------------------------------------
# métodos / funciones para borrar elementos

# del lista[indice]
# .pop()
# .remove()
# .clear()
# -------------------------------------------

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
#         0    1    2    3   4   5    6        7

print(lista , len(lista)) # ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5] 8

del lista[4]
print(lista , len(lista)) # ['A', 'B', 'C', 10, 30, -100.5, -200.5] 7

lista.pop() # elimina el último
print(lista , len(lista)) # ['A', 'B', 'C', 10, 30, -100.5] 6

lista.pop()
print(lista , len(lista)) # ['A', 'B', 'C', 10, 30] 5

lista.pop(2)
print(lista , len(lista)) # ['A', 'B', 10, 30] 4

lista.pop()
lista.pop()
lista.pop()
lista.pop()
#lista.pop() # IndexError: pop from empty list

print(lista)

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]

elemento_eliminado = lista.pop()
print( lista ) # ['A', 'B', 'C', 10, 20, 30, -100.5]
print( elemento_eliminado ) # -200.5

# => .remove()
lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]

lista.remove('C')
print(lista)

# ==> ERROR cuando trato de eliminar algo que no existe

#lista.remove('Z') # ValueError: list.remove(x): x not in list
#del lista[50] # IndexError: list assignment index out of range
#lista.pop(50) # IndexError: pop index out of range


# => .clear()

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
print( lista , len(lista) )

lista.clear()
print( lista , len(lista) ) # [] 0

str_1 = 'sebas'
print(str_1) # sebas
str_1.upper()
print(str_1) # sebas
print( str_1.upper() ) # SEBAS


# ---------
# .count()
# ---------
lista = [1,2,3,10,20,30,1,5,9,-1,-2,-3,1]
print( lista.count(1) ) # 3
print( lista.count(100) ) # 0


# -----------
# .reverse()
# -----------
lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
print(lista)

lista.reverse()
print(lista) # [-200.5, -100.5, 30, 20, 10, 'C', 'B', 'A']


# --------
# .sort()
# --------
l1 = [20, 5, 2, 15]
l2 = ['a', 'x', 'm', 'h']
l3 = ['sol', 'hola', 'palabra']

# .sort() => # números: menor a mayor / strings: a-z
# .sort(reverse=False)
l1.sort()
l2.sort()
print(l1) # [2, 5, 15, 20]
print(l2) # ['a', 'h', 'm', 'x']

# .sort(reverse=True)
# números: mayor a menor / strings: z-a
l1.sort(reverse=True)
l2.sort(reverse=True)
print(l1) # [20, 15, 5, 2]
print(l2) # ['x', 'm', 'h', 'a']

# .sort(reverse , key)
l3 = ['sol', 'palabra', 'hola']
print(l3) # ['sol', 'palabra', 'hola']

l3.sort( reverse=False , key=len )
print(l3) # ['sol', 'hola', 'palabra']

l3.sort( key=len )
print(l3) # ['sol', 'hola', 'palabra']

l3.sort( reverse=True, key=len )
print(l3) # ['palabra', 'hola', 'sol']


# --------
# .copy()
# --------
lista = [1,2,3]
print(lista , len(lista))

lista.append('A')
print(lista , len(lista))

lista = [1,2,3]
lista_2 = lista ##### OJO

print(lista)
print(lista_2)

lista_2.append('Z')

print(lista) # [1, 2, 3, 'Z']
print(lista_2) # [1, 2, 3, 'Z']


# SOLUCION
lista = [1,2,3]
lista_copy = lista.copy()
# lista y lista_copy son INDEPENDIENTES !!!!

lista.append('AAA')
lista_copy.append('ZZZ')

print(lista) # [1, 2, 3, 'AAA']
print(lista_copy) # [1, 2, 3, 'ZZZ']




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 21) Condicional IF
print('\n\n\n21) Condicional IF\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----
# EJ 1
# -----
nota = 14

if nota >= 15 and nota <= 20:
    print('Usted ha pasado la materia')
elif nota < 15 and nota >= 0:
    print('Usted ha perdido la materia')
else:
    print('ERROR - Nota debe ser entre 0 y 20')
# end if

# => if / elif / elif / elif ... / else 
# => if / else
# => if / elif


# -----
# EJ 2
# -----
"""
nota = input('¿Cuál fue su nota? : ')
nota = int(nota)

if nota >= 15 and nota <= 20:
    print('Usted ha pasado la materia')
elif nota < 15 and nota >= 0:
    print('Usted ha perdido la materia')
else:
    print('ERROR - Nota debe ser entre 0 y 20')
# end if
"""

# -----
# EJ 3
# -----
temp = 20
temp = 2

if temp < 5 or temp > 35:
   print('Clima está muy malo!!')
else:
   print('Qué buen clima!!')
# end if




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 22) Condicional Match-Case
print('\n\n\n22) Condicional Match-Case\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - a partir de python 3.10 >
# - simula el switch...case de otros lenguajes

"""
opcion = '5'
opcion = input('Ingrese su opción : ')

match opcion:
   case '1':
       print('Opción 1 - Guardar Archivo')
   case '2':
       print('Opción 2 - Eliminar Archivo')
   case '3':
       print('Opción 3 - Salir del Programa')
   case _:
       print('ERROR - Opción no EXISTE !!')
# end match-case
"""

# => if / elif / elif / elif / elif .... / else ==> match-case
# => + 3 elif => match-case




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
edad = 14

if edad >= 18:
   print('Usted es mayor de edad!')
else:
   print('Usted es menor de edad...')
# end if

# ----------------------
# Con Operador Ternario
# ----------------------
print()

edad = 19

resultado = 'MAYOR DE EDAD' if edad >= 18 else 'MENOR DE EDAD'
print(resultado)

print( 'MAYOR' if edad >= 18 else 'MENOR!!!' ) # operador ternario dentro del print




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 24) Bucle For
print('\n\n\n24) Bucle For\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# elemento iterable => acceder a los índices []

lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']


# --------------------
# recorrido de listas
# --------------------
for elemento in lista:
    print(elemento)
# end for

print('---')

for x in lista:
    print(x)
# end for



# --------------------------------------------
# la variable usada para el recorrido se crea
# --------------------------------------------
print(x) # Julia

# ----------------------
# recorrido de Strings
# ----------------------
nombre = 'Ximena'
print(nombre)

for letra in nombre:
    print(letra)
# end for

# ----------------------------
# función interna range + for
# range (start, end, step)
# end => EXCLUSIVO
# ----------------------------
print()

rango_1_10 = range(1,11)

for numero in rango_1_10:
    print(numero)
# end for

rango_1_10_2 = range(1,11,2)

for numero in rango_1_10_2:
    print('Número =', numero)
# end for

# -----------------------
# for + contador externo
# -----------------------
print()
lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']

contador = 1

for nombre in lista:
    print('Estudiante #', contador, '=>', nombre)
    #contador = contador + 1
    contador += 1 # importante !!!
# end for

# ----------------
# for + enumerate
# ----------------
print()

for index, elemento in enumerate(lista):
    print('Estudiante Número', index + 1, '===>', elemento)
# end for

# -----------
# for + else
# -----------
# - se ejecuta 1 vez al final de la iteración
print()

for nombre in lista:
    print('Estudiante ' + nombre + ' => PRESENTE !')
else:
    print('Fin de tomar lista')


# -------------
# for + break
# -------------
# - para romper / terminar la iteración por completo
print()

for x in range(1, 21):
    print(x)
    if x == 10:
        print('fin del bucle for...')
        break
    # end if
# end for


# ---------------
# for + continue
# ---------------
# - para saltar una iteración
print()

for x in range(1,21):
    
    if x == 10 or x == 15:
        print('Salto en la iteración cuando x =', x)
        continue
    # end if

    print('ITERACIÓN = ', x)
# end for


# -----------
# for + pass
# -----------
# - pass nos sirve para dejar expresando algo que vamos a trabajar luego

print()

for x in range(1,21):
    
    if x == 10 or x == 15:
        pass
    # end if

    print('ITERACIÓN = ', x)
# end for


# -----------------------------------
# aplicación for => cálculo numérico
# -----------------------------------
# EJ: sumatoria y producto de números del 1 al 10
print()

# 10
# sumatoria = 1+2+3+4+5+6+7+8+9+10
# producto  = 1*2*3*4*5*6*7*8*9*10

sumatoria = 0
producto = 1

for x in range(1,11):
    #sumatoria = sumatoria + x
    sumatoria += x # SUMA EN LA ASIGNACIÓN / Operador de Incremento
# end for

for x in range(1,11):
    #producto = producto * x 
    producto *= x # PRODUCTO EN LA ASIGNACIÓN
# end for

print('sumatoria =', sumatoria) # sumatoria = 55
print('producto =', producto) # producto = 3628800




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 25) Bucle while
print('\n\n\n25) Bucle while\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - nunca olvidar el contador + incremento / decremento
# - cuidado con loop infinito

# ----------------------
# ERROR: bucle infinito
# ----------------------
# => evitar por favor esto
"""
x = 1

while x <= 10:
    print('x =', x)
# end while
"""

# ---------------------------------------
# Incremento / Decremento indispensable
# ---------------------------------------
print()

x = 1

while x <= 10:
    print('x =', x)
    x += 1 # suma en la asignación / incremento
# end while

print()

x = 10

while x >= 1:
    print('El valor de x =', x)
    x -= 1 # resta en la asignación / decremento
# end while


# ----------------------------------
# Recorrido de Elementos Iterables
# ----------------------------------
# - también puede recorrer strings, listas, range, etc...
# - pero para hacer eso se debe usar mejor el bucle for

lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']
nombre = 'Ximena'
rango_1_10 = range(1,11)


# -- recorrido de lista + while
print()

i = 0

while i < len(lista):
    print(lista[i])
    i += 1
# end while

# -- recorrido de string + while
print()

i = 0

while i < len(nombre):
    print(nombre[i])
    i += 1
# end while


# -- recorriendo range + while
print()

i = 0

while i < len(rango_1_10):
    print(rango_1_10[i])
    i += 1
# end while

# UN POCO MÁS SOBRE RANGE
# range(start, end, step)
# => end obligatorio
# => start, step => opcionales

print( range(5) ) # range(0, 5)

print()

for x in range(5):
    print('Valor X =', x)
# end for


# --------------
# while + else
# --------------
# - se ejecuta una vez al final
# - así se cumpla la condición o no

x = 10

while x > 20:
    print('Hola desde while')
else:
    print('Siempre se ejecuta esto !!!')
# end while

print()

while x >= 1:
    print('Hola, x =', x)
    x -= 1
else:
    print('Fin del bucle while...')
# end while

# ---------------
# while + break
# ---------------
# - romper / terminar el bucle
print()

x = 0

while x <= 5:
    if x == 3:
        break
    print('Contador x =', x)
    x += 1
# end while

print()

x = 0

while x <= 5:
    if x == 3:
        break
    print('Contador, Ejemplo 2 x =', x)
    x += 1
else:
    print('Fin del bucle while')
# end while


# -------------------------
# while + continue 
# -------------------------
# - saltarse iteraciones
print()

x = 0

while x <= 5:
    if x == 2 or x == 4:
        x += 1
        continue
    print('El valor de x es igual a', x)
    x += 1
# end while

# --------------
# while + pass
# --------------
# - para dejar expresado algo que vamos a trabajar luego
# - pero cuando tenemos un while + if

# ejemplo básico de pass
x = 5

if x == 5:
    pass
# end if

print('Hola')

# pass + while => no se hace esto
"""
while x >= 0:
    pass
# end while
"""

# while + if => pass
x = 0

while x <= 5:
    if x == 2:
        pass
    # end if
    print('x =', x)
    x += 1
# end while

# ------------
# while True
# ------------
# - técnica de bucle para ejecutar un programa
# - siempre entramos al bucle
# - CUIDADO: obliga el uso de un break para terminar el bucle en algún momento

"""
while True:
    print('Bienvenido a mi Programa - sebas.silva.p')
    print('Opciones:')
    print('(A) - Comprar')
    print('(B) - Vender')
    print('(C) - Salir del Programa (s/q)\n')

    opcion = input('Elija su opción : ')
    opcion = opcion.upper().strip(' ') # MUY IMPORTANTE !!!
    print()

    if opcion == 'A':
        print('Usted ha seleccionado la opción de COMPRAR !!!')
    elif opcion == 'B':
        print('Usted ha seleccionado la opción de VENDER !!!')
    elif opcion == 'C' or opcion == 'S' or opcion == 'Q':
        print('Gracias por utilizar el programa...')
        break
    else:
        print('ERROR - Opción no EXISTE :(')
# end while
"""




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
lista_estudiantes = [
'goku', 'krilin', 'piccolo', 'vegeta', 'majin boo', 'yamcha'
]

print(lista)

estudiantes_pares = []
estudiantes_impares = []

for index, estudiante in enumerate(lista_estudiantes):
    if (index + 1) % 2 == 0:
        estudiantes_pares.append(estudiante)
    else:
        estudiantes_impares.append(estudiante)
# end for

print('ESTUDIANTES PARES =', estudiantes_pares)
print('ESTUDIANTES IMPARES =', estudiantes_impares)


# ------
# EJ 2
# ------
# - múltiplos de 4 en números del 1 al 100

multiplos_4 = []

for x in range(1,101):
    if x % 4 == 0:
        multiplos_4.append(x)
# end for

print('Múltiplos de 4 =', multiplos_4)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 27) Print Avanzado + String Format
print('\n\n\n27) Print Avanzado + String Format\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# print básico aprendido
# ------------------------
print('hola mundo') # print => built-in function
print('hola mundo', 'hola sebas', 123)

# --------------------------
# parámetro opcional (end)
# --------------------------
# oir default end = '\n'
print('hola mundo', end=' ')
print('hola python')

print('hola mundo', end='*********')
print('hola python')


# -----------------
# string.format()
# -----------------
nombre = 'Sebas'
edad = 36
nota_final = 15.5
es_estudiante = False

# print con parámetros
print( nombre, edad, nota_final, es_estudiante )

# print + str en concatenación
print( nombre + ' ' + str(edad) + ' ' + str(nota_final) + ' ' + str(es_estudiante) )
e = ' '
print( nombre + e + str(edad) + e + str(nota_final) + e + str(es_estudiante) )

# str.format
print( '{} {} {} {}'.format(nombre, edad, nota_final, es_estudiante) )
print( '{} / {} - {} **** {}'.format(nombre, edad, nota_final, es_estudiante) ) # Sebas / 36 - 15.5 **** False

print( '\nNombre: {}\nEdad: {}\nNota Final: {}\n¿Es Estudiante?: {}'.format(
nombre, edad, nota_final, es_estudiante
) )

print( '\nNombre: {}\nEdad: {}\nNota Final: {}\n¿Es Estudiante?: {}'.format(
    nombre.upper(),
    edad + 10,
    nota_final * 1.05,
    not es_estudiante
) )

# -----------
# f'String'
# -----------
print( f"Nombre: {nombre} | Edad: {edad} | Nota Final: {nota_final} | ¿Es Estudiante?: {es_estudiante}" )

# ---------------------------------------
# str.format() + argumentos posicionales
# ---------------------------------------
n1 = 'Andy'
n2 = 'Paola'
n3 = 'Ximena'

print( '{} es increíble! {} es inteligente! {} es una gran persona!'.format(
n1, n2, n3
) )

print( '{2} es increíble! {1} es inteligente! {0} es una gran persona!'.format(
n1, n2, n3
) )

# IndexError
"""
print( '{5} es increíble! {1} es inteligente! {0} es una gran persona!'.format(
n1, n2, n3
) )
"""
# IndexError: Replacement index 5 out of range for positional args tuple


# ---------------------------------------
# str.format() + argumentos con keyword
# ---------------------------------------
print('Me gusta el pastel de {comida} con una {bebida}'.format(
    comida = 'vainilla',
    bebida = 'coca cola'
))




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 28) String Format + Números
print('\n\n28) String Format + Números\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------------
# Número de dígitos & decimales
# ------------------------------
PI = 3.14159265358979323846 # constantes => mayúsculas
#print(PI)

print( 'PI = {}'.format(PI) ) # PI = 3.141592653589793
# número de dígitos
print( 'PI = {:.2}'.format(PI) ) # PI = 3.1
print( 'PI = {:.4}'.format(PI) ) # PI = 3.142
# números decimales
print( 'PI = {:.2f}'.format(PI) ) # PI = 3.14
print( 'PI = {:.4f}'.format(PI) ) # PI = 3.1416

print( '{:.2f}'.format(PI) )

num = '{:.2f}'.format(PI)
print( num , type(num) ) # 3.14 <class 'str'>

num = float(num)
print( num , type(num) ) # 3.14 <class 'float'>

# -----------
# Alineación
# -----------
num = 1.234
print( 'Valor = {} | Es un número Flotante'.format(num) )
print( 'Valor = {:10} | Es un número Flotante'.format(num) ) # alineación a la derecha
print( 'Valor = {:>10} | Es un número Flotante'.format(num) ) # alineación a la derecha
print( 'Valor = {:<10} | Es un número Flotante'.format(num) ) # alineación a la izquierda
print( 'Valor = {:^10} | Es un número Flotante'.format(num) ) # alineación al centro

# -------------------
# Relleno de ceros 
# -------------------
# - OJO: Toma en cuenta todos los caracteres

num = 1.23
print( 'Número = {:05}'.format(num) )
print( 'Número = {:08}'.format(num) )

# -------------------
# Separador de miles
# -------------------
num = 12345678
print( '{}'.format(num) ) # 12345678
print( '{:,}'.format(num) ) # 12,345,678

# --------------------
# Notación Científica
# --------------------
num = 12345678
print( '{:E}'.format(num) ) # 1.234568E+07
print( '{:e}'.format(num) ) # 1.234568e+07
print( '{:.3e}'.format(num) ) # 1.235e+07

# ----------------
# Combinando todo
# ----------------
num = 1.23456
print( 'El valor = {} | Es un flotante.'.format(num) )
print( 'El valor = {:15.2f} | Es un flotante.'.format(num) )
print( 'El valor = {:<15.2f} | Es un flotante.'.format(num) )
print( 'El valor = {:^15.2f} | Es un flotante.'.format(num) )

# --------------
# CON f'String'
# --------------
print( f'El valor = {num:<15.2f} | Es un flotante.' )




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 29) String Format + Texto
print('\n\n\n29) String Format + Texto\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

pais = 'ECUADOR'

print( 'Mi país {}, es un país muy hermoso!'.format(pais) ) # sin formato =>  Mi país ECUADOR, es un país muy hermoso!
print( 'Mi país {:<15}, es un país muy hermoso!'.format(pais) ) # alineación a izquierda =>  Mi país ECUADOR        , es un país muy hermoso!
print( 'Mi país {:>15}, es un país muy hermoso!'.format(pais) ) # alineación a derecha =>  Mi país         ECUADOR, es un país muy hermoso!
print( 'Mi país {:^15}, es un país muy hermoso!'.format(pais) ) # alineación a centro =>  Mi país     ECUADOR    , es un país muy hermoso!

print( 'Mi país {:.3}, es un país muy hermoso!'.format(pais) ) # truncamiento => Mi país ECU, es un país muy hermoso!

print( 'Mi país {:^10.3}, es un país muy hermoso!'.format(pais) ) # alineación + truncamiento => Mi país    ECU    , es un país muy hermoso!

# utilizando f'String'
print( f'Mi país {pais:^10.3}, es un país muy hermoso!' ) # Mi país    ECU    , es un país muy hermoso!




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 30) Librería / Módulo random
print('\n\n\n30) Librería / Módulo random\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -------------------
# importación módulo
# -------------------
import random


# ----------
# .random()
# ----------
# - número al azar entre 0 y 1
# - sin incluir el 1
x = random.random()
print( x )
# 0.40959174249127883
# 0.6648617000335229
# 0.5399202665685434


# ---------------
# .random() * N
# ---------------
# - para generar números aleatorios de 0 a N
# - sin incluir N
print()

lista_numeros = []

for i in range(1,21):
    lista_numeros.append( round(random.random() * 100) )
# end for

print(lista_numeros) # [1, 10, 4, 85, 67, 16, 50, 4, 24, 7, 70, 44, 1, 7, 40, 28, 95, 60, 49, 41]


# -----------------------------------------
# Truco str.format() para reducir decimales
# -----------------------------------------
print()

lista_numeros = []

for i in range(1,21):
    x = random.random() * 100
    x = '{:.2f}'.format(x)
    x = float(x)
    lista_numeros.append(x)
# end for

print(lista_numeros)
# [52.14, 56.11, 63.52, 24.06, 47.64, 80.54, 94.1, 83.42, 80.3, 56.58, 6.97, 41.39, 28.89, 30.11, 94.06, 90.5, 36.26, 65.01, 56.06, 93.36]

# --------------
# .randint(x,y)
# --------------
# - número entero aleatorio entre x, y
print()

lista_numeros = []

for i in range(1,21):
    lista_numeros.append( random.randint(1000, 2000) )
# end for

print(lista_numeros)
# [1062, 1130, 1025, 1076, 1123, 1405, 1569, 1546, 1758, 1992, 1202, 1091, 1077, 1053, 1502, 1519, 1087, 1991, 1893, 1205]


# ----------
# .choice()
# ----------
# - aplicado en lista !!

heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']

print(heroes)
# no es fijo, cada vez que ejecutamos el programa, es algo distinto
print( random.choice(heroes) ) # vegeta
print( random.choice(heroes) ) # vegeta
print( random.choice(heroes) ) # yamcha
print( random.choice(heroes) ) # gohan


# -----------
# .shuffle()
# -----------
# - aplicado en lista !!
# - barajar una lista
# - OJO: se modifica la lista original

heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']
print(heroes)

random.shuffle(heroes)
print(heroes)
# ['yamcha', 'krilin', 'goku', 'vegeta', 'gohan']
# ['yamcha', 'gohan', 'goku', 'krilin', 'vegeta']
# ['krilin', 'gohan', 'goku', 'yamcha', 'vegeta']

# ==> sin cambiar la lista original
heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']
heroes_copy = heroes.copy()
random.shuffle(heroes_copy)

print(heroes) # ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']
print(heroes_copy) # ['goku', 'gohan', 'yamcha', 'krilin', 'vegeta']




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 31) Condicional Anidado
print('\n\n\n31) Condicional Anidado\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - if dentro de if
# - Juego de Piedra / Papel / Tijera

"""
opciones_juego = ['Piedra', 'Papel', 'Tijera']

opcion_player = None
opcion_cpu = None

while True:
    print('Bienvenidos a nuestro juego de Piedra / Papel / Tijera')
    print('(A) - Piedra')
    print('(B) - Papel')
    print('(C) - Tijera')
    print('(D) - Salir(s/q)\n')

    opcion_player = input('Elija su opción : ')
    opcion_player = opcion_player.title().strip(' ')

    opcion_cpu = random.choice(opciones_juego)

    if opcion_player == 'A' or opcion_player == 'Piedra':
        
        opcion_player = 'Piedra'
        print( 'Player ha elegido => {}'.format( opcion_player.upper() ) )
        print( 'Computadora ha elegido => {}'.format( opcion_cpu.upper() ) )
        print()

        if opcion_cpu == 'Piedra':
            print('EMPATE !')
        elif opcion_cpu == 'Papel':
            print( '{} le gana a {} - Computadora GANA!'.format( opcion_cpu.upper() , opcion_player.upper() ) )
        elif opcion_cpu == 'Tijera':
            print( '{} le gana a {} - Player GANA!'.format( opcion_player.upper() , opcion_cpu.upper() ) )

    elif opcion_player == 'B' or opcion_player == 'Papel':

        opcion_player = 'Papel'
        print( 'Player ha elegido => {}'.format( opcion_player.upper() ) )
        print( 'Computadora ha elegido => {}'.format( opcion_cpu.upper() ) )
        print()

        if opcion_cpu == 'Papel':
            print('EMPATE !')
        elif opcion_cpu == 'Tijera':
            print( '{} le gana a {} - Computadora GANA!'.format( opcion_cpu.upper() , opcion_player.upper() ) )
        elif opcion_cpu == 'Piedra':
            print( '{} le gana a {} - Player GANA!'.format( opcion_player.upper() , opcion_cpu.upper() ) )

    elif opcion_player == 'C' or opcion_player == 'Tijera':

        opcion_player = 'Tijera'
        print( 'Player ha elegido => {}'.format( opcion_player.upper() ) )
        print( 'Computadora ha elegido => {}'.format( opcion_cpu.upper() ) )
        print()

        if opcion_cpu == 'Tijera':
            print('EMPATE !')
        elif opcion_cpu == 'Piedra':
            print( '{} le gana a {} - Computadora GANA!'.format( opcion_cpu.upper() , opcion_player.upper() ) )
        elif opcion_cpu == 'Papel':
            print( '{} le gana a {} - Player GANA!'.format( opcion_player.upper() , opcion_cpu.upper() ) )

    elif opcion_player == 'D' or opcion_player == 'S' or opcion_player == 'Q':
        print('Gracias por Jugar! :)')
        break

    else:
        print('ERROR - Opción Equivocada! :(')
    # end if
# end while
"""




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

matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print(matriz)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    print(fila)
# end for


# --------------------
# Acceso de elementos
# --------------------
print( len(matriz) ) # 3

# acceso a las filas
print( matriz[0] )
print( matriz[1] )
print( matriz[2] )

# acceso individual => doble indexing
print()

# ej: acceder al 6
print( matriz[1][2] ) # 6

# ej: acceder al 8
print( matriz[2][1] ) # 8

# =>matriz[fila][columna] => indexing empieza desde 0




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 33) Bucles Anidados
print('\n\n\n33) Bucles Anidados\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------------------
# Recorrido básico con while
# ---------------------------
# - NO OLVIDAR: while obliga tener un contador

matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]

# simbología de vectores unitarios
i = 0 # filas
j = 0 # columnas


# ==> recorrido básico
print()
while i < len(matriz):
    while j < len( matriz[i] ):
        print( matriz[i][j] )
        j += 1
    i += 1
    j = 0
# end while


# ==> recorrido + print => forma de matriz
print()

i = 0 # filas
j = 0 # columnas

while i < len(matriz):
    while j < len( matriz[i] ):
        print( matriz[i][j] , end='\t' )
        j += 1
    i += 1
    j = 0
    print()
# end while

# -------------------------
# Recorrido básico con for
# -------------------------

matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]

# i => filas
# j => columnas

# ==> recorrido básico
print()

for i in matriz:
    for j in i:
        print(j)
# end for

# ==> recorrido + print en forma de matriz
print()

for i in matriz:
    for j in i:
        print(j , end='\t')
    print()
# end for




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

numero = 10
string = 'python'
lista = [1,2,3]

print( id(numero) ) # 139781892178448
print( id(string) ) # 139781890350448
print( id(lista) )  # 139781890217856

print( hex(id(numero)) ) # 0x7efc31b38210
print( hex(id(string)) ) # 0x7efc31979d70
print( hex(id(lista)) )  # 0x7efc31959740


# ----------------------
# concepto de INMUTABLE
# ----------------------
# - cualquier tipo básico

string = 'python'
print( string[0] )  # p
print( string[-1] ) # n

#string[0] = 'X' # TypeError: 'str' object does not support item assignment
# string es inmutable !!!!

string = 'python'
print( string )
print( hex(id(string)) ) # 0x7f9fd08add70

string = string[0].upper() + string[1:] # NO ES MODIFICAR => reasignación de variable
# al reasignar => nuevo espacio en la memoria !!!!
print( string )
print( hex(id(string)) ) # 0x7f9fd088d9f0

print()

string_1 = 'java'
string_2 = 'java'

print( hex(id(string_1)) ) # 0x7fd091873670
print( hex(id(string_2)) ) # 0x7fd091873670


# ---------------------
# concepto de MUTABLE
# ---------------------
# - típico ejemplo son las listas
print('\nMUTABLE')

lista_1 = [1,2,3]
lista_2 = [1,2,3]

print( hex(id(lista_1)) ) # 0x7fd0c6f82840
print( hex(id(lista_2)) ) # 0x7fd0c6f829c0

lista_1.append('Z')

print(lista_1)
print(lista_2)

print()
lista_1 = [1,2,3]
lista_3 = lista_1 # asignando la misma dirección en la memoria
print( hex(id(lista_1)) ) # 0x7f990654c9c0
print( hex(id(lista_3)) ) # 0x7f990654c9c0

lista_1.append('ZZZ')

print(lista_1) # [1, 2, 3, 'ZZZ']
print(lista_3) # [1, 2, 3, 'ZZZ']

lista_3.append('AAA')

print(lista_1)
print(lista_3)

lista_1[0] = 'Y' # no es posible en String => lista es MUTABLE !!!

print(lista_1)
print(lista_3)

print('\nConclusión')

lista_1 = [1,2,3]
lista_2 = [1,2,3]
lista_3 = lista_1.copy()

print( hex(id(lista_1)) ) # 0x7f6494ac6ac0
print( hex(id(lista_2)) ) # 0x7f6494aa5cc0
print( hex(id(lista_3)) ) # 0x7f6494ac6c40

lista_3.append('A')
lista_1.pop()

print(lista_1) # [1, 2]
print(lista_2) # [1, 2, 3]
print(lista_3) # [1, 2, 3, 'A']




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 35) keyword is
print('\n\n35) keyword is\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
#   ==  | True: si 2 variables tienen el mismo valor
#   is  | True: mismo valor y dirección en la memoria

#   RECORDAR: hex(id()) => dirección en la memoria en valor hexadecimal !!

lista_1 = [1,2,3]
lista_2 = [1,2,3]
lista_3 = lista_1.copy()
lista_4 = lista_1 # OJO # mismo espacio en la memoria + mismo valor

print(lista_1 , lista_2, lista_3, lista_4)

print( lista_1 == lista_2, lista_1 == lista_3, lista_1 == lista_4 ) # True True True
print( lista_1 is lista_2, lista_1 is lista_3, lista_1 is lista_4 ) # False False True

# int / float / str / bool => INMUTABLES => is / == vienen a ser lo mismo




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

t1 = (100, 'sebas', False, -5.8)

# ==> función interna tuple()
t2 = tuple( (100, 'diego', True, -8.9) )

print( t1 , len(t1), type(t1) ) # (100, 'sebas', False, -5.8) 4 <class 'tuple'>
print( t2 , len(t2), type(t2) ) # (100, 'diego', True, -8.9) 4 <class 'tuple'>

# ==> creando tupla vacía
tupla_vacia_1 = ()
tupla_vacia_2 = tuple() 

print( tupla_vacia_1 , len(tupla_vacia_1), type(tupla_vacia_1) ) # () 0 <class 'tuple'>
print( tupla_vacia_2 , len(tupla_vacia_2), type(tupla_vacia_2) ) # () 0 <class 'tuple'>

# -------------------
# Indexing & Slicing
# -------------------
t1 = (100, 'sebas', False, -5.8)
#      0      1       2      3

print( t1[0] ) # 100
print( t1[1] ) # sebas
print( t1[-1] ) # -5.8
print( t1[1:3] ) # ('sebas', False)

#print( t1[50] ) # IndexError: tuple index out of range

# -----------
# keyword in
# -----------
t1 = (100, 'sebas', False, -5.8)
#      0      1       2      3

print( 100 in t1 ) # True
print( '100' in t1 ) # False

# ---------------
# Son INMUTABLES
# ---------------
lista = [100, 'sebas', True, -5.8]
tupla = (100, 'sebas', True, -5.8)

lista[1] = 'Python'
print(lista) # [100, 'Python', True, -5.8]
print(tupla) # (100, 'sebas', True, -5.8)

#tupla[1] = 'Java' # TypeError: 'tuple' object does not support item assignment
# tupla es INMUTABLE !!!

# ----------------------
# Truco para Modificar*
# ----------------------
tupla = (100, 'sebas', True, -5.8)
print( hex(id(tupla)) ) # 0x7f861c9712b0
lista = list(tupla)
lista[1] = 'Python'
tupla = tuple(lista)
print(tupla) # (100, 'Python', True, -5.8)
print( hex(id(tupla)) ) # 0x7f861c9987c0

# ---------------
# Concatenación
# ---------------
t1 = (10,20,30)
t2 = ('a', 'b', 'c')

r1 = t1 + t2
r2 = t2 + t1

print(r1) # (10, 20, 30, 'a', 'b', 'c')
print(r2) # ('a', 'b', 'c', 10, 20, 30)

# -------------------------------
# Métodos => .count() / .index()
# -------------------------------
tupla = (10, 50, 'A', 10, '10', 'A', 'A')

print( tupla.count('A') ) # 3
print( tupla.count(10) ) # 2
print( tupla.count(100) ) # 0

print( tupla.index('A') ) # 2
print( tupla.index(10) ) # 0 => izq a der
#print( tupla.index(100) ) # ValueError: tuple.index(x): x not in tuple


# --------------------
# Recorrido de tuplas
# --------------------
print()

for elemento in tupla:
    print(elemento)
# end for




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 37) Sets / Conjuntos
print('\n\n37) Sets / Conjuntos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - una colección de ELEMENTOS ÚNICOS
# - colección desordenada => OJO !!!
# - no se pueden alterar sus elementos, pero el set si
# - se crean con {}

# -------------------
# Creación de un Set
# -------------------
# - también tiene la función len()

conjunto_1 = {10, 'ABC', -9.6}
conjunto_2 = set( (10, 'XYZ', -8.7) )

print( conjunto_1 , type(conjunto_1), len(conjunto_1) ) # {'ABC', 10, -9.6} <class 'set'> 3
print( conjunto_2 , type(conjunto_2), len(conjunto_2) ) # {-8.7, 'XYZ', 10} <class 'set'> 3

# ==> creando un conjunto vacío
#set_vacio_1 = {} # INCORRECTO => diccionario vacío
#print( set_vacio_1 , type(set_vacio_1) ) # {} <class 'dict'>

set_vacio = set()
print( set_vacio , len(set_vacio), type(set_vacio) ) # set() 0 <class 'set'>


# -------------------------------------
# No existe Indexing & Slicing en Sets
# -------------------------------------
# - ¿por qué? => los sets son colecciones desordenadas
s1 = {'A', 'B', 'C'}

#s1[0] # TypeError: 'set' object is not subscriptable
#s1[0:2] # TypeError: 'set' object is not subscriptable


# -------------------------------
# Elementos repetidos se eliminan
# -------------------------------
# - los elementos de un set son ÚNICOS
s1 = {'A', 'B', 'C', 'A', 'A', 'B'}
print(s1) # {'B', 'C', 'A'}


# -----------------------------------------
# No existe concatenación & producto (+ *)
# -----------------------------------------
s1 = {'A', 'B', 'C'}
s2 = {10, 20, 30}

#r1 = s1 + s2 # TypeError: unsupported operand type(s) for +: 'set' and 'set'
#r2 = 2 * s1 # TypeError: unsupported operand type(s) for *: 'int' and 'set'

# -----------------
# Recorrido de Set
# -----------------
s1 = {'A', 'B', 'C'}

for elem in s1:
    print(elem)
# end for


# => Métodos Importantes para SET
# - no es posible modificar elementos de un set
# - pero es posible modificar el set como tal

# -------
# .add()
# -------
s1 = {'A', 'B', 'C'}
s1.add(10)
s1.add(False)
s1.add('B')

print(s1)



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
print()
s1 = {'A', 'B', 'C'}
s1.remove('A')
print(s1) # {'C', 'B'}
#s1.remove('Z') # KeyError: 'Z'


# -----------
# .discard() 
# -----------
# - igual que remove pero no me da error
print()
s1 = {'A', 'B', 'C'}
s1.discard('A')
print(s1) # {'B', 'C'}
s1.discard('Z') 
print(s1) # {'B', 'C'}

# -------
# .pop()
# -------
# - elimina elemento al azar
print()
s1 = {'A', 'B', 'C'}
s1.pop()
print(s1)


# ---------
# .clear()
# ---------
# - deja un set vacío
print()
s1 = {'A', 'B', 'C'}
print(s1) # {'A', 'B', 'C'}
s1.clear()
print(s1) # set()

# ---------
# del set
# ---------
# elimina la variable por completo
print()
s1 = {'A', 'B', 'C'}
print(s1)
del s1 # s1 deja de existir en nuestro programa !!!
#print(s1) # NameError: name 's1' is not defined.



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
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

union = s1.union(s2)
print(union)
print(s1)
print(s2)

# update => modifica el conjunto
print()
s1.update(s2)
print(s1)
print(s2)

s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

print()
s2.update(s1)
print(s1)
print(s2)

# ---------------------------------------------
# .intersection()   /  .intersection_update()
# ---------------------------------------------
# - RETORNA elementos en común entre 2 conjuntos
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

resultado_interseccion_1 = s1.intersection(s2)
resultado_interseccion_2 = s2.intersection(s1)

print( resultado_interseccion_1 ) # {'A', 'B'}
print( resultado_interseccion_2 ) # {'A', 'B'}

# intersection_update
print()
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

s1.intersection_update(s2)
print(s1) # {'A', 'B'}
print(s2) # {10, 20, 'A', 'B'}

print()
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

s2.intersection_update(s1)
print(s1) # {'C', 'A', 'B', 'D'}
print(s2) # {'A', 'B'}


# ----------------------------------------
# .difference()   /  .difference_update()
# ----------------------------------------
# - ELIMINA elementos en común entre 2 conjuntos
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

diff_1 = s1.difference(s2)
diff_2 = s2.difference(s1)

print(diff_1) # {'D', 'C'}
print(diff_2) # {10, 20}
print()
print(s1) # {'A', 'B', 'D', 'C'}
print(s2) # {'A', 10, 'B', 20}

# => difference_update
print()
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

s1.difference_update(s2)
print(s1) # {'C', 'D'}
print(s2) # {10, 'A', 20, 'B'}

print()
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

s2.difference_update(s1)
print(s1) # {'D', 'A', 'C', 'B'}
print(s2) # {20, 10}

# --------
# .copy()
# --------
# - igual que en listas
s1 = {'A', 'B', 'C'}
s2 = s1 # están en la misma dirección de la memoria !!!

s2.add(100)
s1.add(500)

print(s1) # {100, 'C', 'B', 'A', 500}
print(s2) # {100, 'C', 'B', 'A', 500}

# => aplicando copy
s1 = {'A', 'B', 'C'}
s2 = s1.copy()

s2.add(100)
s1.add(500)

print(s1) # {'A', 'B', 'C', 500}
print(s2) # {'A', 'B', 'C', 100}




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

# => JSON = javascript object

# clave : valor
dict_1 = {
'A' : 100,
'B' : 200,
'C' : 300,
}

# ==> función interna dict()
dict_2 = dict( X=500 , Y=600, Z=700 )

print( dict_1 , type(dict_1), len(dict_1) ) # {'A': 100, 'B': 200, 'C': 300} <class 'dict'> 3
print( dict_2 , type(dict_2), len(dict_2) ) # {'X': 500, 'Y': 600, 'Z': 700} <class 'dict'> 3

# ==> claves pueden ser números enteros
dict_3 = {
100 : 'Ecuador',
200 : 'USA',
300 : 'Alemania'
}

print( dict_3 , type(dict_3), len(dict_3) )
# {100: 'Ecuador', 200: 'USA', 300: 'Alemania'} <class 'dict'> 3

# ------------------
# Diccionario Vacío
# ------------------
dict_vacio_1 = {}
dict_vacio_2 = dict()

print( dict_vacio_1 , type(dict_vacio_1), len(dict_vacio_1) ) # {} <class 'dict'> 0
print( dict_vacio_2 , type(dict_vacio_2), len(dict_vacio_2) ) # {} <class 'dict'> 0

# ------------------------------
# NO existe Indexing y Slicing
# ------------------------------
dict_1 = {
'A' : 100,
'B' : 200,
'C' : 300,
}

#dict_1[0]   # KeyError: 0
#dict_1[0:2] # TypeError: unhashable type: 'slice'

# -----------------
# Acceso con Clave
# -----------------
print( dict_1['A'] ) # 100
print( dict_1['C'] ) # 300


# --------------------------------------------
# Creación / Modificación con Acceso de Clave
# --------------------------------------------
dict_1 = {
'A' : 100,
'B' : 200,
'C' : 300,
}

dict_1['B'] = 555
dict_1['Z'] = 'python'
print(dict_1)
# {'A': 100, 'B': 555, 'C': 300, 'Z': 'python'}


# -----------------------------------------------
# 2 valores iguales es posible pero no 2 claves
# -----------------------------------------------
# - se sobrescribe el último valor ingresado

dict_1 = {
'Carlos' : 15,
'Sebas' : 14,
'Ana' : 18,
'Ximena' : 15
}

print( dict_1 , len(dict_1) )
# {'Carlos': 15, 'Sebas': 14, 'Ana': 18, 'Ximena': 15} 4

dict_2 = {
'Carlos' : 15,
'Sebas' : 14,
'Ana' : 18,
'Sebas' : 15
}

print( dict_2 , len(dict_2) )
# {'Carlos': 15, 'Sebas': 15, 'Ana': 18} 3

# ----------------------------------
# keyword in => averiguar una clave
# ----------------------------------
# - True si existe la clave, False si no

dict_1 = {
'Carlos' : 15,
'Sebas' : 14,
'Ana' : 18,
'Ximena' : 15
}

# => para averiguar las CLAVES !!!
print( 'Carlos' in dict_1 ) # True
print( 18 in dict_1 ) # False


"""
MÉTODOS IMPORTANTES DE DICCIONARIOS
Métodos de Acceso => .get / .keys / .values / .items
Métodos de Modificación => .update / .setdefault
Métodos de Eliminación => .pop / .popitem / .clear / del
"""

# -------
# .get()
# -------
heroes = {
'dbz' : 'goku',
'dc' : 'superman',
'marvel' : 'spiderman',
'starwars' : 'obi-wan'
}

print( heroes.get('dbz') ) # goku
print( heroes['dbz'] ) # goku


# --------
# .keys()
# --------
claves = heroes.keys() 
print( claves , type(claves) )
# dict_keys(['dbz', 'dc', 'marvel', 'starwars']) <class 'dict_keys'>

# ----------
# .values()
# ----------
valores = heroes.values()
print( valores , type(valores) )
# dict_values(['goku', 'superman', 'spiderman', 'obi-wan']) <class 'dict_values'>

# ---------
# .items()
# ---------
# - retorna tupla de (clave, valor)
items = heroes.items()
print( items, type(items) )
# dict_items([('dbz', 'goku'), ('dc', 'superman'), ('marvel', 'spiderman'), ('starwars', 'obi-wan')]) <class 'dict_items'>

lista = list(items)
print( lista , type(lista) )
# [('dbz', 'goku'), ('dc', 'superman'), ('marvel', 'spiderman'), ('starwars', 'obi-wan')] <class 'list'>

# ----------
# .update()
# ----------
# modifica / crea clave - valor
print()

heroes = {
'dbz' : 'goku',
'dc' : 'superman',
'marvel' : 'spiderman',
'starwars' : 'obi-wan'
}

print(heroes , len(heroes))
# {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'} 4

mod_heroes = {
'dc' : 'wonderwoman',
'tortugas ninja' : 'donatello'
}

heroes.update(mod_heroes)

print(heroes , len(heroes))
# {'dbz': 'goku', 'dc': 'wonderwoman', 'marvel': 'spiderman', 'starwars': 'obi-wan', 'tortugas ninja': 'donatello'} 5

# => Con acceso a clave
heroes = {
'dbz' : 'goku',
'dc' : 'superman',
'marvel' : 'spiderman',
'starwars' : 'obi-wan'
}

print( heroes, len(heroes) )
# {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'} 4

heroes['dbz'] = 'gohan'
heroes['power rangers'] = 'zordon'

print( heroes, len(heroes) )
# {'dbz': 'gohan', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan', 'power rangers': 'zordon'} 5

# => Pasar directamente un diccionario
heroes = {
'dbz' : 'goku',
'dc' : 'superman',
'marvel' : 'spiderman',
'starwars' : 'obi-wan'
}

heroes.update( {'dbz' : 'piccolo'} )
print( heroes, len(heroes) )
# {'dbz': 'piccolo', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'} 4

# --------------
# .setdefault()
# --------------
# - recibe como argumentos clave & valor
# - .setdefault(clave, valor)
# - si existe la clave => NO la modifica !!!
# - si no existe => la crea

persona = {
'nombre' : 'Andy',
'edad' : 32,
'nota' : 15.8,
'es_estudiante' : True
}

print( persona, len(persona) )
#{'nombre': 'Andy', 'edad': 32, 'nota': 15.8, 'es_estudiante': True} 4

persona.setdefault( 'apellido' , 'Pérez' )
print( persona, len(persona) )
#{'nombre': 'Andy', 'edad': 32, 'nota': 15.8, 'es_estudiante': True, 'apellido': 'Pérez'} 5

persona.setdefault( 'nombre' , 'Carlos' ) # intento ?? => no es error, pero no lo hace
print( persona, len(persona) )
#{'nombre': 'Andy', 'edad': 32, 'nota': 15.8, 'es_estudiante': True, 'apellido': 'Pérez'} 5


# -------
# .pop()
# -------
# - no como en las listas
# - hay que pasar la clave como argumento
# - caso contrario da error
# - devuelve VALOR de elemento eliminado

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

#heroes.pop() # TypeError: pop expected at least 1 argument, got 0
heroes.pop('marvel')
print( heroes )

elemento_eliminado = heroes.pop('dc')
print( heroes ) # {'dbz': 'goku', 'starwars': 'obi-wan'}
print( elemento_eliminado ) # superman


# -----------
# .popitem()
# -----------
# - python 3.7 >= -- borra último elemento (colecciones ordenadas)
# - python 3.6 <= -- borra elemento al azar (colecciones DESORDENADAS)
# - devuelve tupla de clave valor del elemento eliminado
print()

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

print( heroes.popitem() ) # ('starwars', 'obi-wan')
print( heroes ) # {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman'}


# ----------
# .clear()
# ----------
# - deja un diccionario vacío

print()

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

print(heroes) # {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'}

heroes.clear()

print(heroes) # {}


# -------------------
# del dict['clave']
# -------------------
# - elimina par de clave/valor pasando la clave
# - también elimina toda la variable de diccionario

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

del heroes['marvel']
print(heroes)

# ojo=> también podemos eliminar la variable como tal
del heroes
#print(heroes) # NameError: name 'heroes' is not defined

# ---------------------------
# Recorrido de diccionarios
# ---------------------------
# - la mejor manera es con for + .items()

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

# => .items()
print()

for clave, valor in heroes.items():
    print( 'Clave : {} // Valor: {}'.format(clave, valor) )
# end for

"""
Clave : dbz // Valor: goku
Clave : dc // Valor: superman
Clave : marvel // Valor: spiderman
Clave : starwars // Valor: obi-wan
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 39) Casting entre Colecciones
print('\n\n39) Casting entre Colecciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------
# lista a tupla
# --------------
# - para dar mayor seguridad
# - recordar, las tuplas no son modificables

lista = [1,2,3,4]
tupla = tuple(lista)

print( lista , type(lista) ) # [1, 2, 3, 4] <class 'list'>
print( tupla , type(tupla) ) # (1, 2, 3, 4) <class 'tuple'>

lista[0] = 'A'
#tupla[0] = 'Z' # TypeError: 'tuple' object does not support item assignmentvvvvvvvvvvvvvvvvvv

# ----------------------
# lista / tuplas a sets
# ----------------------
# - manera fácil de eliminar elementos repetidos

lista = [10, -5, 20, 10, 30, 25, 20]
tupla = [10, -5, 20, 10, 30, 25, 20]

print(lista)
print(tupla)

set_1 = set(lista)
set_2 = set(tupla)
print(set_1) # {10, 20, 25, -5, 30}
print(set_2) # {10, 20, 25, -5, 30}

lista = list(set_1)
tupla = tuple(set_2)

print(lista) # [10, 20, 25, -5, 30]
print(tupla) # (10, 20, 25, -5, 30)

# ---------------------------------
# Casting a Diccionario => CUIDADO
# ---------------------------------
# - la colección debe tener sentido
# - con la estructura del diccionario
# - debe ser una colección de colecciones de 2 elementos (clave/valor)


# ==> Esto es ERROR
lista = [1,2,3]
#dict_1 = dict(lista) # TypeError: cannot convert dictionary update sequence element #0 to a sequence


# ==> Esto es POSIBLE!
lista = [
['A' , 10],
['B' , 15],
['C' , 20],
['D' , 25],
]

print( lista )

dict_1 = dict(lista)
print(dict_1) # {'A': 10, 'B': 15, 'C': 20, 'D': 25}

# ==> de nuevo ERROR

lista = [
['A' , 10, 100],
['B' , 15, 200],
['C' , 20, 300],
['D' , 25, 400],
]

#dict_1 = dict(lista) # ValueError: dictionary update sequence element #0 has length 3; 2 is required

coleccion = (
(1,2),
(3,4),
(5,6),
)

print(coleccion) # ((1, 2), (3, 4), (5, 6))

dict_1 = dict(coleccion)
print(dict_1) # {1: 2, 3: 4, 5: 6}




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 40) Funciones
print('\n\n40) Funciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------
# Función Básica
# ----------------

nombre = 'Sebas'
edad = 36
nota = 18.5

print( '{} tiene {} años y su nota final es de {}'.format(
    nombre, edad, nota
) )
# Sebas tiene 36 años y su nota final es de 18.5

# ==> definición de una función
def presentar_estudiante(a, b, c): # PARÁMETROS => definición
    print( '{} tiene {} años y su nota final es de {}'.format(a, b, c) )
# end def

# ==> inovación de una función / llamar a la función / ejecutar a la función
presentar_estudiante(nombre, edad, nota) # ARGUMENTOS => invocación
# Sebas tiene 36 años y su nota final es de 18.5

presentar_estudiante('Daniel', 15, 10.6) # Daniel tiene 15 años y su nota final es de 10.6
presentar_estudiante('Juan', 53, 18.5) # Juan tiene 53 años y su nota final es de 18.5


# ---------------------
# Parámetros y Retorno
# ---------------------
# - Un función puede o no tener parámetros
# - y puede o no retornar algún valor => keyword 'return'
# - (las funciones tienen nombres de verbos)

# ==> sin parámetros / sin retorno
def saludar():
    print('hola') # imprimir en la consola / no es retorno
# end def

saludar() # hola

# ==> con parámetros / sin retorno
def despedirse(nombre):
    print('Chao {} !!'.format(nombre))
# end def

despedirse('Mateo') # Chao Mateo !!
despedirse('Santiago') # Chao Santiago !!


# ==> con parámetros / con retorno
def sumar(a, b):
    return a + b
# end def

sumar(5,6)

# imprimiendo el valor retornado por la función
print( sumar(5,6) ) # 11

resultado = sumar(80,15)
print(resultado , type(resultado)) # 95 <class 'int'>


# ==> sin parámetros / con retorno
# (no tiene mucho sentido, pero no es error)
def devolver_10():
    return 10
# end def

print( devolver_10() ) # 10


# ---------------------------
# Pueden Redefinirse N veces
# ---------------------------
def sumar(a, b):
    return a + b
# end def

print( sumar(10,15) ) # 25

def sumar(a, b):
    print( a + b + 100 )
# end def

sumar(1,2) # 103

# --------------------------------------------
# Parámetros => Existen solo en las funciones
# --------------------------------------------
# - pueden repetirse
# - pueden tener el mismo nombre que variables creadas afuera
# - no afecta la función

a = 10
b = 20

def multiplicar(a,b):
    return a*b
# end def

def restar(a,b):
    return a-b
# end def

print()
print(a,b) # 10 20
print( multiplicar(a,b) ) # 200
print( multiplicar(7,2) ) # 14
print( restar(a,b) ) # -10
print( restar(7,2) ) # 5
print(a,b) # 10 20


# ---------------------------------------
# pass => definir función y trabar luego
# ---------------------------------------
def calcular_algo(a,b,c,d,e):
    pass
# end def

# -------
# return
# -------
# - marca el fin de la función
# - pueden haber varios, con un condicional


# ==> return marca el fin de la función
def saludar(nombre, edad):
    return 'Hola {}, tienes {} años!'.format(nombre, edad)
    print('hola de nuevo...')
# end def

print( saludar('Dani',20) ) # Hola Dani, tienes 20 años!

# ==> varios return
def saludar(idioma):
    if idioma.lower() == 'esp':
        return 'buenos días'
    elif idioma.lower() == 'eng':
        return 'good morning'
    elif idioma.lower() == 'deu':
        return 'Guten Tag...'
    else:
        return 'holaaaaaaaaaa'
# end def

print( saludar('a') ) # holaaaaaaaaaa
print( saludar('esp') ) # buenos días
print( saludar('ENG') ) # good morning
print( saludar('deU') ) # Guten Tag...
#print( saludar() ) # TypeError: saludar() missing 1 required positional argument: 'idioma'

# --------------------
# función en función
# --------------------

def doblar_numero(x):
    return x * 2
# end def

def triplicar_numero(x):
    return x * 3
# end def

def presentar_resultados(x):
    print( 'El número doblado es =', doblar_numero(x) )
    print( 'El número triplicado es =', triplicar_numero(x) )
# end def

presentar_resultados(6)
#El número doblado es = 12
#El número triplicado es = 18


# -----------------------
# parámetros por defecto
# -----------------------

# ==> recordar print + end
# - este end es un parámetro por defecto '\n'
print('Hola')
print('Sebas')
print('Hola', end='-----')
print('Dani')

# ==> podemos definir las nuestras
def que_aprendemos( lenguaje='Python' ):
    print('Nosotros aprendemos', lenguaje)
# end def

que_aprendemos('Fisica') # Nosotros aprendemos Fisica
que_aprendemos('Química') # Nosotros aprendemos Química
que_aprendemos() # Nosotros aprendemos Python

# ==> SIEMPRE al final
def ingredientes_pasta(tipo_pasta, salsa, carne='carne molida', condimento='oregano'):
    print('La pasta tiene: {}, {}, {} y {}'.format(
    tipo_pasta,
    salsa,
    carne,
    condimento
    ))
# end def

ingredientes_pasta('spagethi', 'pesto') # La pasta tiene: spagethi, pesto, carne molida y oregano
ingredientes_pasta('spagethi', 'pesto', 'pollo') # La pasta tiene: spagethi, pesto, pollo y oregano
ingredientes_pasta('spagethi', 'pesto', 'pollo bbq', 'ajo molido') # La pasta tiene: spagethi, pesto, pollo bbq y ajo molido
ingredientes_pasta('spagethi', 'pesto', condimento='pimienta', carne='bolitas de res' ) # La pasta tiene: spagethi, pesto, bolitas de res y pimienta




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
def conteo_atras(x):
    if x > 0:
        print( '{} segundos para año nuevo!'.format(x) )
        conteo_atras(x-1)
# end def

conteo_atras(5)

# Ej de consola:
"""
5 segundos para año nuevo!
4 segundos para año nuevo!
3 segundos para año nuevo!
2 segundos para año nuevo!
1 segundos para año nuevo!
"""


# -----
# EJ 2
# -----
# sumatorio(5) = 1+2+3+4+5 = 15

def sumatorio(x):
    if x > 0:
        return x + sumatorio(x-1)
    else:
        return 0
# end def

print( sumatorio(5) ) # 15
print( sumatorio(3) ) # 6


# -----
# EJ 3
# -----
# factorial(5) = 5*4*3*2*1 = 120
# 5 !

print( math.factorial(5) ) # 120

# ==> con función recursiva
def factorial(x):
    if x > 0:
        return x * factorial(x-1)
    else:
        return 1
# end def

print( factorial(5) ) # 120
print( factorial(3) ) # 6

# ==> con función normal + bucle

def factorial_2(x):
    resultado = 1
    while x > 0:
        #resultado = resultado * x
        resultado *= x
        x -= 1 # x = x - 1
    # end while
    return resultado
# end def

print( factorial_2(5) ) # 120
print( factorial_2(3) ) # 6

"""
def factorial(x):
    if x > 0:
        return x * factorial(x-1)
    else:
        return 1
# end def

factorial(3) = 3*2*1
1) return 3 * factorial(3-1)
2) factorial(3-1) = factorial(2) = return 2 * factorial(2-1)
3) factorial(2-1) = factorial(1) = return 1 * factorial(1-1)
4) factorial(1-1) = factorial(0) = return 1
# => 3 * 2 * 1 * 1
# => 6
"""




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

variable_a = 10 # GLOBAL

def hacer_algo():
    variable_b = 20
    print(variable_b) # LOCAL
# end def

print( variable_a )
#print( variable_b ) # NameError: name 'variable_b' is not defined.

"""
def hacer_algo_mas():
    print(variable_b)
# end def

hacer_algo_mas() # NameError: name 'variable_b' is not defined.
"""

hacer_algo() # 20


# ---------------
# Keyword global
# ---------------

# ==> podemos mostrar una variable global dentro de local
print()

a = 20

def mostrar():
    a
    print(a)
    print(a * 5)
# end def

mostrar()
#20
#100


# ==> NO se puede modificar directamente la variable global dentro de local
# - en el siguiente ejemplo
# - ambas variables se llaman => a
# - pero son distintas, una es global / otra es local

a = 20 # global

def intento_modificar():
    a = 100
    return a
# end def

print(a) # 20
print( intento_modificar() ) # 100
print(a) # 20


def intento_2(a):
    a = 150
    print(a)
# end def

print('\nintento 2:')
intento_2(2) # 150
print(a) # 20
intento_2(a) # 150
print(a) # 20

# ==> Se puede modificar con keyword global

a = 30 # global

def cambiar_variable():
    global a # IMPORTANTE !!!!
    a += 20 # a = a + 20
    print('Se cambió el valor de a , a = {}'.format(a))
# end def

print('\nkeyword global:')
print(a) # 30
cambiar_variable() # Se cambió el valor de a , a = 50
print(a) # 50




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
def que_son_args(*args):
    print( args , type(args) )
# end def

que_son_args(1,2,3,4,5,'a',True)
# (1, 2, 3, 4, 5, 'a', True) <class 'tuple'>


# ---------------------
# aplicación con *args
# ---------------------
def sumatoria(*args):
    resultado = 0
    for valor in args:
        resultado += valor # resultado = resultado + valor
    # end for
    return resultado
# end def

print( sumatoria(1,5,6) ) # 12
print( sumatoria(1,2,3,4,5) ) # 15


# ----------------------------------------------
# el nombre args => no es relevante, pero si *
# ----------------------------------------------
def calcular_promedio(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    # end for
    resultado = resultado / len(numeros)
    return resultado
# end def

print( calcular_promedio(10,18,15,20) ) # 15.75




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
def que_son_kwargs(**kwargs):
    print( kwargs , type(kwargs) )
# end def

que_son_kwargs( nombre='sebas', edad=36, nota=18.5 )
# {'nombre': 'sebas', 'edad': 36, 'nota': 18.5} <class 'dict'>


# ------------------------
# aplicación con **kwargs
# ------------------------
def calcular_nota_final(**kwargs):
    nota_final = kwargs['nota_deberes'] * 0.3 + kwargs['nota_examen'] * 0.7
    print('La nota final es de =', nota_final)
# end def

calcular_nota_final( nota_deberes=18, nota_examen=14 ) # La nota final es de = 15.2
calcular_nota_final( nota_deberes=20, nota_examen=11 ) # La nota final es de = 13.7
#calcular_nota_final( nota_deberes=20, nota_examn=11 ) # KeyError: 'nota_examen'


# ------------------------------------------------
# el nombre kwargs => no es relevante, pero si **
# ------------------------------------------------

def describir_persona(**caracteristicas):
    print('Características de Persona:')
    for clave, valor in caracteristicas.items():
        print( '{} : {}'.format(clave, valor) )
    # end for
# end def

describir_persona(
nombre='Sebas',
apellido='Silva',
edad=36,
profesion='Ing. Mecánico',
pais='Alemania'
)

"""
Características de Persona:
nombre : Sebas
apellido : Silva
edad : 36
profesion : Ing. Mecánico
pais : Alemania
"""




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
def suma_normal(a,b):
    return a + b
# end def

print( suma_normal(4,5) ) # 9

# ==> función lambda
suma_lambda = lambda a,b : a + b

print( suma_lambda(2,6) ) # 8


# --------------------------
# Lambda con valores String
# --------------------------
saludar = lambda nombre, edad : 'Hola soy {}, tengo {} años'.format(nombre, edad)

print( saludar('Diego', 20) ) # Hola soy Diego, tengo 20 años
print( saludar('Andrea', 34) ) # Hola soy Andrea, tengo 34 años

# ------------------------------
# Lambda con Operador Ternario
# ------------------------------

# ==> Recordar: Operador Ternario
edad = 12
mensaje = 'mayor de edad' if edad >= 18 else 'menor de edad'
print(mensaje) # menor de edad

# ==> Lambda + Operador Ternario
check_temperatura = lambda temp : 'Frío' if temp < 10 else 'Buen Clima'

print( check_temperatura(10) ) # Buen Clima
print( check_temperatura(15) ) # Buen Clima
print( check_temperatura(8) ) # Frío


# --------------------------
# Lambda => Función Anónima
# --------------------------
# - lambda puede ser el retorno de una función por ej.

def multiplicador(x):
    return lambda numero : numero * x
# end def

mult_5 = multiplicador(5)
print(mult_5)
# <function multiplicador.<locals>.<lambda> at 0x7fe9065f1870>

print( mult_5(20) ) # 100

# ==> 1 sola línea !!
mult_5_20 = multiplicador(5)(20)
print(mult_5_20) # 100




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 46) Funciones como Variables
print('\n\n46) Funciones como Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - todo en Python puede ser variable
# - en Python todo es un objeto (POO)

a = 20
print(type(a)) # <class 'int'>

# --------------------
# Función a Variable
# --------------------
def resta(x,y):
    return x - y
# end def

print( resta , type(resta) ) # <function resta at 0x7efc3c495900> <class 'function'>
print( hex(id(resta)) ) # 0x7efc3c495900

# -------------------------------
# Funciones Internas a Variables
# -------------------------------
print( 'hola mundo' )
print( print , type(print) )
# <built-in function print> <class 'builtin_function_or_method'>

# => puedo cambiarle el nombre a print ???
imprimir_en_consola = print

imprimir_en_consola('hola mundo') # hola mundo




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
def gritando(msg):
    return msg.upper()
# end def

def en_voz_baja(msg):
    return msg.lower()
# end def

# ===> función de alto grado (high order function)
def saludar(funcion):
    saludo = funcion('Hola mi Estimado! Saludos!!')
    print(saludo)
# end def

# ===> Ejecutando high order function
# - las funciones-argumento se pasan como firma, sin ejecutar !!

saludar(gritando) # HOLA MI ESTIMADO! SALUDOS!!
saludar(en_voz_baja) # hola mi estimado! saludos!!


# ------------------------------------------------------
# b) Cuando retorna una 2da función definida en la 1era
# ------------------------------------------------------
# - EJ: una fórmula sencilla de la física
#   velocidad = distancia / tiempo

# ===> como función normal
def velocidad(distancia, tiempo):
    return distancia / tiempo
# end def

d = 10 # 10 metros
t = 60 # 60 segundos = 1 minuto

print( velocidad(d,t) ) # 0.16666666666666666


# ===> como high order function
def distancia(d):
    def tiempo(t):
        return d/t
    # end def
    return tiempo
# end def

calcular_velocidad_distancia = distancia(10)
calcular_velocidad_distacia_tiempo = calcular_velocidad_distancia(60)

print(calcular_velocidad_distancia) # <function distancia.<locals>.tiempo at 0x7f907f7adbd0>
print(calcular_velocidad_distacia_tiempo) # 0.16666666666666666

# otra manera
resultado = distancia(10)(60) # (d)(t)
print(resultado) # 0.16666666666666666




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 48) Decoradores
print('\n\n48) Decoradores\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - patrón de diseño
# - añadir nueva funcionalidad a un elemento / sin modificar la estructura

# ---------------
# SIN decorador
# ---------------
def saludo_sin_decorador():
    print('Hola, un abrazo!')
# end def

saludo_sin_decorador() # Hola, un abrazo!


# --------------
# CON decorador
# --------------

# ==> función decoradora
def funcion_decoradora(funcion):
    def funcion_wrapper():
        print('HOLA !!!!')
        funcion()
        print('Cuídate mucho!....')
    # end def
    
    return funcion_wrapper
# end def

# ==> función con decorador
@funcion_decoradora
def saludo_con_decorador():
    print('Hola, un abrazo, qué bonito es programar!!')
# end def

# ==> invocando
saludo_con_decorador()

"""
HOLA !!!!
Hola, un abrazo, qué bonito es programar!!
Cuídate mucho!....
"""



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
lista = [20, 15, 8, 90, -5, -50, 20.2]

lista_menor_mayor = sorted(lista)
lista_mayor_menor = sorted(lista , reverse=True)

print('lista =', lista) # lista = [20, 15, 8, 90, -5, -50, 20.2]
print('lista_menor_mayor =', lista_menor_mayor) # lista_menor_mayor = [-50, -5, 8, 15, 20, 20.2, 90]
print('lista_mayor_menor =', lista_mayor_menor) # lista_mayor_menor = [90, 20.2, 20, 15, 8, -5, -50]
print('lista =', lista) # lista = [20, 15, 8, 90, -5, -50, 20.2]


# -----
# EJ 2
# -----
palabras = ['sol', 'planeta', 'investigacion']

orden_menos_mas = sorted(palabras , key=len)
orden_mas_menos = sorted(palabras , key=len, reverse=True)

print( 'palabras =', palabras ) # palabras = ['sol', 'planeta', 'investigacion']
print( 'orden_menos_mas =', orden_menos_mas ) # orden_menos_mas = ['sol', 'planeta', 'investigacion']
print( 'orden_mas_menos =', orden_mas_menos ) # orden_mas_menos = ['investigacion', 'planeta', 'sol']



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
def funcion(x):
    return 3*x - 5
# end def

valores = [-20, 5, 16, -8, 12]
resultado_map = map( funcion , valores )
print( resultado_map , type(resultado_map) )
# <map object at 0x7fd55991a2c0> <class 'map'>

# ==> conveniente hacer un CASTING a otro iterable, ej: lista
resultado_final = list(resultado_map)
print( resultado_final , type(resultado_final) )
# [-65, 10, 43, -29, 31] <class 'list'>


# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------
# - ej: notas de 3 alumnos ordenadas en lista
# - nota_final = 0.2*deberes + 0.3*proyecto + 0.5*examen

#              A     B   C
nota_deberes = [15, 18, 14]
nota_proyecto = [18, 16, 20]
nota_examen = [16, 17, 15]

nota_final = map(
lambda deberes, proyecto, examen : 0.2*deberes + 0.3*proyecto + 0.5*examen,
nota_deberes,
nota_proyecto,
nota_examen
)

nota_final = list(nota_final)
print(nota_final) # [16.4, 16.9, 16.3]

# ==> con función normal
def calcular_nota_final(deberes, proyecto, examen):
    return 0.2*deberes + 0.3*proyecto + 0.5*examen
# end def

"""
nota_final_2 = map(
calcular_nota_final,
nota_deberes,
nota_proyecto,
nota_examen
)
"""

nota_final_2 = list(map(
calcular_nota_final,
nota_deberes,
nota_proyecto,
nota_examen
))

print(nota_final_2) # [16.4, 16.9, 16.3]




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
calificaciones = [13, 14, 18, 10, 20, 15, 16, 14, 19, 11] # / 20

def notas_altas(nota):
    if nota > 14:
        return True
    else:
        return False
# end def

calificaciones_altas = filter( notas_altas , calificaciones )
print( calificaciones_altas , type(calificaciones_altas) )
# <filter object at 0x7f2b0ca02140> <class 'filter'>

calificaciones_altas = tuple(calificaciones_altas)
print( calificaciones_altas , type(calificaciones_altas) )
# (18, 20, 15, 16, 19) <class 'tuple'>


# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------

calificaciones_bajas = list(filter(
lambda nota : True if nota <= 14 else False,
calificaciones
))

print(calificaciones_bajas)
# [13, 14, 10, 14, 11]




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
import functools

# ----------------
# Ejemplo Básico
# ----------------
compras_usd = [100.50, 200, 85, 15, 20.99]
suma_compras = lambda x, y : x + y
valor_a_pagar = functools.reduce( suma_compras , compras_usd )
print( valor_a_pagar ) # 421.49

# sería lo mismo
valor_total_2 = sum(compras_usd)
print(valor_total_2) # 421.49


# ------------------
# Ejemplo Complejo
# ------------------
gastos = [
    ['Empleado','gastos_administrativos' , 'gastos_combustible'],
    ['Sebastián', 20.54 , 15.85],
    ['Ximena', 18.24 , 17.98],
    ['Eduardo', 42.65 , 31.23],
    ['Carlos', 18.78 , 14.36],
    ['Andrea', 50.48 , 16.87],
]

gastos_administrativos_totales = functools.reduce(
lambda x,y : x + y, # función de suma para mi reduce

list(map(
lambda x : x[1],
gastos[1:]
))

)

print(gastos_administrativos_totales, 'USD') # 150.69 USD

gastos_administrativos = list(map(
lambda x : x[1],
gastos[1:]
))

print(gastos_administrativos)


# ==> gastos de combustible

gastos_combustible_totales = functools.reduce(
lambda x,y : x + y,

list(map(
lambda x : x[2],
gastos[1:]
))
)

print(gastos_combustible_totales , 'USD') # 96.29 USD




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
valores = [10, -50, 62, -5, 22, 15, -9]

resultado_1 = [ 2*x - 5 for x in valores ]
print(resultado_1) # [15, -105, 119, -15, 39, 25, -23]

resultado_2 = [ math.sqrt(z) for z in range(1,11) ]
print(resultado_2)
# [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]


# ---------------------------------------------------------------------
# B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
# ---------------------------------------------------------------------
valores = [10, -50, 62, -5, 22, 15, -9]
print( len(valores) ) # 7

resultado = [ 2.5*y - 5/y for y in valores if y > 0 ]
print( resultado , len(resultado) )
# [24.5, 154.91935483870967, 54.77272727272727, 37.166666666666664] 4


# --------------------------------------------------------------------------
# C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
# --------------------------------------------------------------------------
valores = [10, -50, 62, -5, 22, 15, -9]
resultado = [ 'positivo' if z > 0 else 'negativo' for z in valores ]
print(resultado)
# ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'positivo', 'negativo']




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

# notas / 20
# clave : valor
notas = {
    'Daniel' : 16,
    'Pedro' : 14,
    'Sebastián' : 13,
    'Santiago' : 19,
    'Eduardo' : 11,
    'Rodrigo' : 20,
    'Francisco' : 12,
    'María' : 14,
}


# --------------------------------------------------------------------
# A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
# --------------------------------------------------------------------
print()
notas_100 = { key : (value/20 * 100) for (key, value) in notas.items() }
print(notas_100)
# {'Daniel': 80.0, 'Pedro': 70.0, 'Sebastián': 65.0, 'Santiago': 95.0, 'Eduardo': 55.00000000000001, 'Rodrigo': 100.0, 'Francisco': 60.0, 'María': 70.0}

# ==> key / value, los nombres no son importantes, pero si el orden!!
notas_100 = { c : float('{:.2f}'.format(v/20*100)) for (c, v) in notas.items() }
print(notas_100)
# {'Daniel': 80.0, 'Pedro': 70.0, 'Sebastián': 65.0, 'Santiago': 95.0, 'Eduardo': 55.0, 'Rodrigo': 100.0, 'Francisco': 60.0, 'María': 70.0}


# -------------------------------------------------------------------------------------
# B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
# -------------------------------------------------------------------------------------
print()
estudiantes_aprobados = { clave : valor for (clave, valor) in notas.items() if valor > 14 }
estudiantes_NO_aprobados = { clave : valor for (clave, valor) in notas.items() if valor <= 14 }

print(estudiantes_aprobados) # {'Daniel': 16, 'Santiago': 19, 'Rodrigo': 20}
print(estudiantes_NO_aprobados) # {'Pedro': 14, 'Sebastián': 13, 'Eduardo': 11, 'Francisco': 12, 'María': 14}


# ------------------------------------------------------------------------------
# C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
# ------------------------------------------------------------------------------
print()
aprobado_reprobado = { c : ('aprobado' if v > 14 else 'reprobado') for (c,v) in notas.items() }
print(aprobado_reprobado)
# {'Daniel': 'aprobado', 'Pedro': 'reprobado', 'Sebastián': 'reprobado', 'Santiago': 'aprobado', 'Eduardo': 'reprobado', 'Rodrigo': 'aprobado', 'Francisco': 'reprobado', 'María': 'reprobado'}

for c, v in aprobado_reprobado.items():
    print(c,'->',v)
# end for


# -------------------------------------------------------------------------
# D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
# -------------------------------------------------------------------------
print()

# => ecuador hace 20 años

def check_estudiante(nota):
    if nota > 14 and nota <= 20:
        return 'Aprobado'
    elif nota == 14:
        return 'Supletorio'
    elif nota >= 12 and nota < 14:
        return 'Pierde el Cupo'
    elif nota >= 0 and nota < 12:
        return 'Pierde el Año'
    else:
        return 'ERROR - Nota debe estar entre 0 y 20'
# end def

analisis_estudiante = { clave : check_estudiante(valor) for (clave, valor) in notas.items() }

print(analisis_estudiante)
# {'Daniel': 'Aprobado', 'Pedro': 'Supletorio', 'Sebastián': 'Pierde el Cupo', 'Santiago': 'Aprobado', 'Eduardo': 'Pierde el Año', 'Rodrigo': 'Aprobado', 'Francisco': 'Pierde el Cupo', 'María': 'Supletorio'}

for c,v in analisis_estudiante.items():
    print('Estudiante: {} / {}'.format(c,v))
# end for

"""
Estudiante: Daniel / Aprobado
Estudiante: Pedro / Supletorio
Estudiante: Sebastián / Pierde el Cupo
Estudiante: Santiago / Aprobado
Estudiante: Eduardo / Pierde el Año
Estudiante: Rodrigo / Aprobado
Estudiante: Francisco / Pierde el Cupo
Estudiante: María / Supletorio
"""




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
l1 = ['A', 'B', 'C']
l2 = [100, 200, 300]

zip_l1_l2 = zip(l1, l2)
print( zip_l1_l2 , type(zip_l1_l2) )
# <zip object at 0x7f5d757e1c80> <class 'zip'>

# ==> más sentido haciendo un casting
resultado = list(zip_l1_l2)
print(resultado)
# [('A', 100), ('B', 200), ('C', 300)]

zip_l1_l2 = zip(l1, l2)

dict_1 = dict(zip_l1_l2)
print(dict_1)
# {'A': 100, 'B': 200, 'C': 300}


# --------------------------------------------------------
# N iterables / el de menor tamaño decide el tamaño final
# --------------------------------------------------------
iter_1 = ['A', 'B', 'C']
iter_2 = [100, 200, 300]
iter_3 = ('USA', 'ECU', 'DEU', 'JPN')

resultado_zip = zip(iter_1, iter_2, iter_3)
resultado_final = tuple( resultado_zip )

print(resultado_final)
# (('A', 100, 'USA'), ('B', 200, 'ECU'), ('C', 300, 'DEU'))




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
import time

# -----------
# punto cero
# -----------
print( time.ctime(0) ) # Thu Jan  1 00:00:00 1970

# ------------------------------------
# milisegundos a partir del tiempo 0
# ------------------------------------
# - desde el punto 0
# - hasta el preciso momento de ejecución de este script
print( time.time() ) # 1701659285.7050157


# -------------
# fecha actual
# -------------
# - en el preciso momento de ejecución del script
print( time.ctime( time.time() ) )
# Mon Dec  4 03:09:47 2023


# ---------------------------------------
# aplicación útil => estampas de tiempo
# ---------------------------------------
# - crear una identificación única para algún dato
lista_estudiantes = [
    'Carlos', 'Ana', 'Diego', 'Ximena', 'Adri', 'Sebas', 'Marcelo'
]

identificacion_unica = []

for estudiante in lista_estudiantes:
    identificacion_unica.append( round(time.time() * random.random()) )
# end for

print(identificacion_unica)
# [63458501, 307877323, 271684009, 27168269, 356612388, 1057728778, 385017988]

id_estudiante = zip(identificacion_unica , lista_estudiantes)
tupla_id_estudiante = tuple(id_estudiante)

for elemento in tupla_id_estudiante:
    print(elemento)
# end for

"""
(941751948, 'Carlos')
(93386415, 'Ana')
(909686399, 'Diego')
(70049301, 'Ximena')
(359844215, 'Adri')
(1502787801, 'Sebas')
(1441999506, 'Marcelo')
"""

# -------------
# time.sleep()
# -------------

"""
contador = 5

while contador > 0:
    print('Quedan {} segundos para año nuevo!'.format(contador))
    contador -= 1
    time.sleep(1)
else:
    print('Feliz año nuevo!!')
# end while

#Quedan 5 segundos para año nuevo!
#Quedan 4 segundos para año nuevo!
#Quedan 3 segundos para año nuevo!
#Quedan 2 segundos para año nuevo!
#Quedan 1 segundos para año nuevo!
#Feliz año nuevo!!
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 58) Librería datetime
print('\n\n58) Librería datetime\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - la librería / módulo adecuado para trabajar hora y fecha

# ---------------------------------------------
# importación de la librería / módulo datetime
# ---------------------------------------------
import datetime

# -------------
# fecha actual
# -------------
# - al momento de ejecución del script !!
# - retorna un objeto del tipo "datetime.datetime"

fecha_actual = datetime.datetime.now()
print( fecha_actual ) # 2023-12-04 03:17:50.772528
print( type(fecha_actual) ) # <class 'datetime.datetime'>


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

print( fecha_actual.year ) # 2023
print( fecha_actual.month ) # 12
print( fecha_actual.hour ) # 3


# ------------------------------
# creando fechas personalizadas
# ------------------------------
# - de 2 maneras
#   a) tupla de 3 valores (año, mes, día)
#   b) tupla de 6 valores (año, mes, día, hora, minutos, segundos)

fecha_1 = datetime.datetime(2001, 7, 20)
fecha_2 = datetime.datetime(2025, 12, 19, 19, 51, 25)

print(fecha_1) # 2001-07-20 00:00:00
print(fecha_2) # 2025-12-19 19:51:25


# -----------------------------
# formato personalizado fácil
# -----------------------------
# - hay muchas maneras de complicarse aquí
# - pero como breve introducción aprenderemos una manera muy fácil

fecha_actual = datetime.datetime.now()
print(fecha_actual) # 2023-12-04 03:23:12.372530

formato_personalizado = '{}/{}/{} - {}h:{}m:{}s'.format(
fecha_actual.year,
fecha_actual.month,
fecha_actual.day,
fecha_actual.hour,
fecha_actual.minute,
fecha_actual.second,
)

print( formato_personalizado ) # 2023/12/4 - 3h:23m:12s

# ---------------------
# reloj en tiempo real
# ---------------------
# => chévere ejercicio

"""
def imprimir_reloj_tiempo_real():
    hoy = datetime.datetime.now()
    print('{}/{}/{} - {}h:{}m:{}s'.format(
           hoy.year,
           hoy.month,
           hoy.day,
           hoy.hour,
           hoy.minute,
           hoy.second,
         ))
# end def

while True:
    imprimir_reloj_tiempo_real()
    time.sleep(1)
# end while
""" 




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 59) keywords as / from
print('\n\n59) keyword as / from\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - as   ==> para redefinir el nombre de una librería módulo
# - from ==> para importar algo específico de un módulo

"""
import random as r
import datetime as dt

print( r.random() ) # 0.38543460526168283
print( dt.datetime.now() ) # 2023-12-04 03:29:30.016278

from math import cos
print( cos(3.1416/3) ) # 0.4999978792725457

from math import pi as constante_pi, sin as seno, cos as coseno
print( coseno( constante_pi / 6 ) ) # 0.8660254037844387
print( seno( constante_pi / 6 ) ) # 0.49999999999999994
"""




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
nombre = 'Sebas'
print(nombre) # Sebas

print( nombre_completo := 'Sebas Silva P.' ) # Sebas Silva P.
print( nombre_completo ) # Sebas Silva P.


# ---------------------
# Ejemplo más complejo
# ---------------------

# ==> sin walrus :=
"""
ingredientes = []
opcion_user = ''

print('Lista de Ingredientes para una Receta:')
while opcion_user != 'salir':
    opcion_user = input('Ingrese un Ingrediente : ')
    ingredientes.append(opcion_user)
else:
    ingredientes.pop()
# end while

print(ingredientes)
"""    


# ==> con walrus :=
"""
ingredientes = []

print('Lista de Ingredientes para una Receta:')
while( opcion_user := input('Ingrese un Ingrediente : ') ) != 'salir':
    ingredientes.append(opcion_user)
# end while

print(ingredientes)
"""




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
print('hola')
#prin('hola')


# -------------------
# Error de Ejecución
# -------------------
lista = ['a','b','c']
print( lista[0] )
#print( lista[5] ) # IndexError: list index out of range

#resultado = 5/0 # ZeroDivisionError: division by zero


# ------------------
# try-except Básico
# ------------------
# - try => alberga el código peligroso que puede causar error
# - except => presenta el error sin parar la ejecución del programa
print()

try:
    print( 5/0 )
except:
    print('ERROR - algo salió mal...')
# end try-except

print('otra línea')


# ------------------
# Mostrando el error
# ------------------
# - usando Exception y un alias
print()

try:
    print( 5/0 )
except Exception as e:
    print('ERROR - algo salió mal...', e)
# end try-except

print('otra línea')


# ---------------------------------------------
# Estructura Completa: try-except-else-finally
# ---------------------------------------------
"""
try:     aquí va el código que tiene el riesgo de producir error
except:  bloque que se ejecuta en caso de error sin interrumpir el flujo del programa
else:    bloque que se ejecuta cuando NO se da error
finally: bloque que se ejecuta SIEMPRE, haya error o no
"""

def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print('ERROR | Lo siento, algo salió mal |', e)
    else: # cuando no hay error
        print('Operación con Éxito | Resultado => {}/{} = {:.2f}'.format(a,b,resultado))
    finally: # haya o no error
        print('FIN del método dividir')
    # end try-except
# end method

print('\nTEST:')
dividir(5,0)
dividir(5,2)
dividir(5,'a')


# -----------------
# type(e).__name__
# -----------------
# - devuelve el tipo del error

def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print('ERROR | Lo siento, algo salió mal |', e, '|', type(e).__name__)
    else: # cuando no hay error
        print('Operación con Éxito | Resultado => {}/{} = {:.2f}'.format(a,b,resultado))
    finally: # haya o no error
        print('FIN del método dividir')
    # end try-except
# end method

print('\nTEST:')
print('----------------------')
dividir(5,0) # ZeroDivisionError
print('----------------------')
dividir(5,2)
print('----------------------')
dividir(5,'a') # TypeError

"""
TEST:
----------------------
ERROR | Lo siento, algo salió mal | division by zero | ZeroDivisionError
FIN del método dividir
----------------------
Operación con Éxito | Resultado => 5/2 = 2.50
FIN del método dividir
----------------------
ERROR | Lo siento, algo salió mal | unsupported operand type(s) for /: 'int' and 'str' | TypeError
FIN del método dividir
"""

# ---------------------------------
# Capturar Excepciones Específicas
# ---------------------------------

def dividir(a,b):
    try:
        resultado = a/b
    except TypeError as e:
        print( type(e).__name__, '||', e )
        print('ERROR - Por favor ingrese un número!')
    except ZeroDivisionError as e:
        print( type(e).__name__, '||', e )
        print('ERROR - La división para CERO no existe!')
    except Exception as e:
        print( type(e).__name__, '||', e )
        print('ERROR - La división no es posible...')
    else: # cuando no hay error
        print('Operación con Éxito | Resultado => {}/{} = {:.2f}'.format(a,b,resultado))
    finally: # haya o no error
        print('FIN del método dividir')
    # end try-except
# end method

print('\nTEST:')
print('----------------------')
dividir(5,0) # ZeroDivisionError
print('----------------------')
dividir(5,2)
print('----------------------')
dividir(5,'a') # TypeError

"""
TEST:
----------------------
ZeroDivisionError || division by zero
ERROR - La división para CERO no existe!
FIN del método dividir
----------------------
Operación con Éxito | Resultado => 5/2 = 2.50
FIN del método dividir
----------------------
TypeError || unsupported operand type(s) for /: 'int' and 'str'
ERROR - Por favor ingrese un número!
FIN del método dividir
"""


# --------------------------------
# Generar Errores Personalizados
# --------------------------------
# - raise => invocamos un error
# - OJO: debemos capturarlo, caso contrario, se para la ejecución del programa

# ==> definición de una función sencilla
print()

def saludar(nombre):
    print('Hola', nombre)
# end def

#saludar()
saludar('Carlos') # Hola Carlos
saludar('123') # Hola 123


# ==> prohibiendo al usuario poner números en el nombre
def saludar(nombre):
    if nombre.isalpha():
        print('Hola', nombre,'!!')
    else:
        print('ERROR')
# end def

print('\nTEST:')
saludar('Carlos') # Hola Carlos !!
saludar('123') # ERROR
saludar('') # ERROR

# ==> utilizando raise
def saludar(nombre):
    if nombre.isalpha():
        print('Hola', nombre,'!!')
    else:
        #print('ERROR')
        raise Exception('ERROR - El nombre solo puede contener letras')
# end def

print('\nTEST:')
saludar('Carlos') # Hola Carlos !!
#saludar('123') # ERROR
#saludar('') # ERROR


# ==> raise + try-except

def saludar(nombre):
    try:
        if nombre.isalpha():
            print('Hola mi estimado', nombre, '!!')
        else:
            raise Exception('ERROR - El nombre solo puede contener letras!')
    except Exception as e:
        print( type(e).__name__, '||', e )
# end def

print('\nTEST:')
saludar('Carlos') # Hola mi estimado Carlos !!
saludar('123') # Exception || ERROR - El nombre solo puede contener letras!
saludar('') # Exception || ERROR - El nombre solo puede contener letras!




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 62) Breve Introducción a numpy
print('\n\n62) Breve Introducción a numpy\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----------------
# ¿Por qué numpy?
# -----------------
lista_1 = [5, 3, 7]
lista_2 = [2, 4, 1]

resultado = lista_1 + lista_2
print(resultado) # [5, 3, 7, 2, 4, 1]

# -----------------------------------------------------
# ¿Hay alguna manera de hacer operaciones aritméticas?
# -----------------------------------------------------

# ==> utilizando for
suma_listas = []

for index, numero in enumerate(lista_1):
    suma_listas.append( lista_1[index] + lista_2[index] )
# end for

print( suma_listas ) # [7, 7, 8]


# ==> utilizando while
resta_listas = []
index = 0

while index < len(lista_1):
    resta_listas.append( lista_1[index] - lista_2[index] )
    index += 1
# end while

print( resta_listas ) # [3, -1, 6]


# --------------------------------------------------
# ¿Existe otra manera más fácil? => librería numpy
# --------------------------------------------------

# ==> importando la librería numpy
# - instalar primero: pip install numpy
# - verificar si está instalado: pip list + buscar numpy
# - Replit, tenemos que instalarlo en el shell

import numpy as np # RECORDAR ESTA LÍNEA

# ==> averiguando versión en terminal
print( np.__version__ ) # 1.26.2


# ==> creando un array con numpy / arreglo => [10, 20, 30]
lista_1 = np.array( [5, 3, 7] )
lista_2 = np.array( [2, 4, 1] )

print( lista_1, type(lista_1), len(lista_1) ) # [5 3 7] <class 'numpy.ndarray'> 3
print( lista_2, type(lista_2), len(lista_2) ) # [2 4 1] <class 'numpy.ndarray'> 3

# ==> creando array de numpy con variable de lista
lista_1 = [5, 3, 7]
lista_2 = [2, 4, 1]

array_1 = np.array(lista_1)
array_2 = np.array(lista_2)

print(array_1) # [5 3 7]
print(array_2) # [2 4 1]

# ==> operaciones aritméticas de listas con numpy
suma_listas = array_1 + array_2
resta_listas = array_1 - array_2
producto_listas = array_1 * array_2
division_listas = array_1 / array_2
modulo_listas = array_1 % array_2
potencia_listas = array_1 ** array_2

print( suma_listas ) # [7 7 8]
print( resta_listas ) # [ 3 -1  6]
print( producto_listas ) # [10 12  7]
print( division_listas ) # [2.5  0.75 7.  ]
print( modulo_listas ) # [1 3 0]
print( potencia_listas ) # [25 81  7]


# ==> operaciones escalar & array
lista = [1,2,3]
print( 2 * lista ) # [1, 2, 3, 1, 2, 3]

array = np.array(lista)
r1 = 2 * array
r2 = 10 / array

print(r1) # [2 4 6]
print(r2) # [10.          5.          3.33333333]

# ==> funciones normales con numpy
array = np.array([2,4,1])

def funcion_x(x):
    return 2*x - 5 + x**2
# end def

r1 = funcion_x(2)
r2 = funcion_x(4)
r3 = funcion_x(1)

print( r1 , r2 , r3 ) # 3 19 -2

r = funcion_x(array)
print(r) # [ 3 19 -2]

# ==> libería math & array => NO ES POSIBLE, pero no necesitamos
array = np.array([2,4,1])

r1 = math.sin(2)
r2 = math.sin(4)
r3 = math.sin(1)
print(r1, r2, r3) # 0.9092974268256817 -0.7568024953079282 0.8414709848078965

#r = math.sin(array) # TypeError: only length-1 arrays can be converted to Python scalars


# ==> funciones aritméticas numpy
# https://numpy.org/doc/stable/reference/routines.math.html
array = np.array([2,4,1])

array_seno = np.sin(array)
array_coseno = np.cos(array)
array_tangente = np.tan(array)
array_log_e = np.log(array)
array_log_10 = np.log10(array)

print('\nTEST:')
print( array ) # [2 4 1]
print( array_seno ) # [ 0.90929743 -0.7568025   0.84147098]
print( array_coseno ) # [-0.41614684 -0.65364362  0.54030231]
print( array_tangente ) # [-2.18503986  1.15782128  1.55740772]
print( array_log_e ) # [0.69314718 1.38629436 0.        ]
print( array_log_10 ) # [0.30103    0.60205999 0.        ]


# ==> linspace
# - generar una distribución estándar de números desde un inicio a un final

distribucion_1_100_10 = np.linspace(1.0, 100.0, num=10)
#print(distribucion_1_100_10)
# [  1.  12.  23.  34.  45.  56.  67.  78.  89. 100.]

distribucion_500_1000_50 = np.linspace(50.0, 1000.0, num=50)
#print(distribucion_500_1000_50)




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

import matplotlib


# -------------------------------
# Averiguar versión en Terminal
# -------------------------------
print( matplotlib.__version__ ) # 3.8.2


# ----------------------------------
# importación específica de pyplot
# ----------------------------------
import matplotlib.pyplot as plt  # RECORDAR ESTA LÍNEA


# -----------------------
# plot básico con listas
# -----------------------
"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.plot( valores_x , valores_y )
plt.show()
"""

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

"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.plot( valores_x , valores_y, 'X--g' )
plt.show()
"""

# -----------------------------------------------
# Tamaño marcador => markersize => ms
# Color borde marcador => markeredgecolor => mec
# Color fondo marcador => markerfacecolor  => mfc
# -----------------------------------------------

"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.plot( 
valores_x,
valores_y,
'o--g',
ms = 15,
mfc = 'b',
mec = 'r'
)

plt.show()
"""

# ------------------------------------
# Tamaño de línea => linewidth => lw
# ------------------------------------

"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.plot( 
valores_x,
valores_y,
'o--g',
linewidth = 3,
ms = 15,
mfc = 'b',
mec = 'r'
)

plt.show()
"""

# ----------------------------
# Título & Etiquetas de Ejes
# ----------------------------
# Título => plt.title('')
# Etiqueta / Label en X => plt.xlabel('')
# Etiqueta / Label en Y => plt.ylabel('')

"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.title('Valores de X vs. Valores de Y')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.plot( 
valores_x,
valores_y,
'o--g',
linewidth = 3,
ms = 8,
mfc = 'b',
mec = 'r'
)

plt.show()
"""

# --------------------------------
# Incorporar Grilla => plt.grid()
# --------------------------------
# - Grilla en X, Y => plt.grid()
# - Grilla en X    => plt.grid(axis = 'x')
# - Grilla en Y    => plt.grid(axis = 'y')

"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.title('Valores de X vs. Valores de Y')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.plot( 
valores_x,
valores_y,
'o--g',
linewidth = 3,
ms = 8,
mfc = 'b',
mec = 'r'
)

#plt.grid()
#plt.grid(axis='x')
plt.grid(axis='y')

plt.show()
"""

# -------------------
# Tipos de Gráficos
# -------------------
# - Dispersión / Scatter => plt.scatter(x,y)
# - Barras / Bars => plt.bar(x,y)
# - Pastel / Pie => plt.pie(y)

# DISPERSIÓN & BARRAS
"""
valores_x = [1,2,3,4,5]
valores_y = [10,15,12,18,20]

plt.title('Valores de X vs. Valores de Y')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

#plt.scatter(valores_x, valores_y)
plt.bar(valores_x, valores_y)

plt.show()
"""

# PASTEL
"""
valores_y = [15, 20, 25, 30, 10] # sumados deben dar 100 / 1 pastel = 100 %
etiquetas = ['USA', 'ECU', 'DEU', 'JPN', 'ESP']
#plt.pie(valores_y)
plt.pie(valores_y , labels=etiquetas)
plt.show()
"""



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 64) Matplotlib + Numpy
print('\n\n64) Matplotlib + Numpy\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# => ojo recordar siempre la importación al inicio del script!!

# ----------------------------
# A) Función de valores de X
# ----------------------------
def funcion_x(x):
    return x**2 - 3/x + 15
# end def

# -------------------------------------------
# B) Valores de X / Valores de Y con numpy
# -------------------------------------------
valores_x = np.linspace(1.0, 100.0, num=50)
valores_y = funcion_x(valores_x)

#print(valores_x)
#print(valores_y)


# -------------------------------------
# C) Configurar + Ejecutar Matplotlib
# -------------------------------------

plt.title('y = x**2 - 3/x + 15')
plt.xlabel('Valores en X')
plt.ylabel('Valores en Y')

plt.plot(
valores_x,
valores_y,
'o-r',
linewidth = 1,
ms = 1.5,
mfc = 'b',
mec = 'b'
)

plt.grid()

plt.show() # IMPORTANTE !!!
