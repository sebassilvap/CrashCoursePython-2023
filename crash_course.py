# =====================
# PYTHON CRASH COURSE
# por @sebas.silva.p
# 11/2023
# =====================



# ==============================================================
# 1) Comentarios
# - con símbolo de numeral # => comentario de 1 línea
# - entre 6 comillas simples o dobles => multilínea => string
# - no afectan al código
# ==============================================================

# comentario de 1 línea

"""
comentario
de varias
líneas
"""



# =============================================
# 2) print()
# - función interna para imprimir en consola
# =============================================
print("Hola Mundo")
print('Hola Mundo') # comilla simple o doble

print('Hola a todos! Soy Sebas!') # cualquier mensaje

print(123) # números

# línea vacía
print('¿Cómo estás?')
print()
print('Estoy bien, y tú?')
print('')
print('Gracias')
print("")
print('De nada')



# ====================================
# 3) Variables
# - contenedor / espacio con memoria
# - para guardar un valor
# ====================================

a = 20
b = 10.5
c = 'Sebas'

print(a) # 20
print(b) # 10.5
print(c) # Sebas

# ----------------------------------------------------------------------
# truco print => imprimir varios valores, separando con coma
# ¿por qué?
# => print es una función => lo que recibe son argumentos de la función
# ----------------------------------------------------------------------
print(a, b, c) # 20 10.5 Sebas
print('hola', -50, -5.5)

# --------------------------------
# Redefinir / Reasignar variables
# --------------------------------
print(a) # 20
a = "I love Python"
print(a) # I love Python

# ---------------------
# Asignación Múltiple
# ---------------------
a, b, c = 100, -5.5, 'Hola'

print(a) # 100
print(b) # -5.5
print(c) # Hola

# -----------------------------------
# Asignación Múltiple a Valor Único
# -----------------------------------
a = b = c = 'Python'

print(a) # Python
print(b) # Python
print(c) # Python



# ================================================
# 4) Estándar de Nombres de Variables
# - en la programación se maneja 2 estándares:
#   (a) cammelCase => nombreEstudiante
#   (b) separación  => nombre_estudiante (PYTHON)

# - REGLAS:
#   (a) no tildes
#   (b) no empezar con número
#   (c) no empezar con caracter de símbolo
# ================================================

nombre = 'Sebas'
apellido = 'Silva'
edad = 36
pais_origen = 'Ecuador'

print(nombre, apellido, edad, pais_origen) # Sebas Silva 36 Ecuador

# => print en varias líneas

print(
    nombre,
    apellido,
    edad,
    pais_origen,
) # Sebas Silva 36 Ecuador

#123nombre = 'Sebas' # SyntaxError: invalid decimal literal
#%nombre = 'Sebas' # SyntaxError: invalid syntax



# ===========================================================
# 5) Tipos de Datos

# => Tipos Básicos
"""
Tipo de Dato     |  Denominación  |  Ej:
---------------------------------------------------------
Entero           |  int           |  -20, 0, 5
Punto Flotante   |  float         |  2.5, 0.669, -89.52
Cadena de Texto  |  str           |  'Hola', "Python"
Booleano         |  bool          |  True, False
"""

# => Todos los Tipos de Datos
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
# ===========================================================

# función interna (built-in function)
# type() => retorna tipo de dato

nombre = 'Sebas'
edad = 36
nota = 18.5
es_profesor = True
es_estudiante = False

print( nombre, type(nombre) ) # Sebas <class 'str'>
print( edad, type(edad) ) # 36 <class 'int'>
print( nota, type(nota) ) # 18.5 <class 'float'>
print( es_profesor, type(es_profesor) ) # True <class 'bool'>
print( es_estudiante, type(es_estudiante) ) # False <class 'bool'>


# None => útil para crear una variable sin valor y asignar luego
x = None
print( x , type(x) ) # None <class 'NoneType'>

x = 100
print( x , type(x) ) # 100 <class 'int'>



# ==================================
# 6) Aritmética en Python
"""
    suma               =>   +
    resta              =>   -
    producto           =>   *
    división           =>   /
    potencia           =>   **
    módulo             =>   %
    división + floor   =>   //
"""
# ==================================

# -----------------------------------
# => Aritmética con Valores Directos
# -----------------------------------
2 + 3
5 * 8
9 / 5
# más sentido imprimir para ver

print(2 + 3) # 5
print(5/6) # 0.8333333333333334
print(5  *8) # 40

# ----------------------------
# => Aritmética con variables
# ----------------------------
x = 10
y = 3

print( x, '+', y, '=', x + y ) # 10 + 3 = 13
print( x, '-', y, '=', x - y ) # 10 - 3 = 7
print( x, '*', y, '=', x * y ) # 10 * 3 = 30
print( x, '/', y, '=', x / y ) # 10 / 3 = 3.3333333333333335
print( x, '**', y, '=', x ** y ) # 10 ** 3 = 1000
print( x, '%', y, '=', x % y ) # 10 % 3 = 1
print( x, '//', y, '=', x // y ) # 10 // 3 = 3

# -----------
# => Módulo
# -----------
#    10 |___ 4
#    -8      2
#     2
print( 10 % 4 ) # 2

# ------------------------
# => División y Redondeo
# ------------------------
# divide y devuelve la parte entera
print( 5/2 , 5//2 ) # 2 1
print( 9/5 , 9//5 ) # 2 1
print( type(9/5) , type(9//5) ) # <class 'float'> <class 'int'>
# la división convierte a punto flotante !

# -------------------------------------
# => Las reglas matemáticas se cumplen
# -------------------------------------
x = 5
y = 2
resultado = x * (y + x) - y + x**y - x / (x- 2*y)
#           5 * (2 + 5) - 2 + 5**2 - 5 / (5- 2*2)
#           5 *    7    - 2 +  25  - 5 / (5 - 4)
#           35 - 2 + 25 - 5 / 1
#           35 - 2 + 25 - 5.0
#           53.0

print(resultado)


# =================================================================================================================
# 7) Secuencias de Escape

# - elementos que permiten dar un formato a string
# - se les antecede siempre el backslash => \

# SECUENCIA  NOMBRE           DEFINICIÓN
#   \\       Backslash        Para insertar el caracter \ en un String
#   \'       Comilla Simple   Para insertar la comilla simple en un String
#   \"       Comilla doble    Para insertar la comilla doble en un String
#   \b       Retroceso        Elimina un caracter del String al momento de aparecer en el output de la consola.
#   \f       Formfeed         Imprime una nueva línea indentada al final de la línea anterior.
#   \v       Tab Vertical     Realiza lo mismo que el Formfeed
#   \t       Tab Horizontal   Inserta un espaciado de tabulación
#   \r       Carriage return  Inserta los caracteres después de \r al inicio del String
#   \n       Nueva Línea      Inserta un salto del línea en tabulación 0

# - algunos no se visualizan en editores de código como VSCode
# - en Replit => se puede ver el funcionamiento de todos
# - aquí vamos a ver los más relevantes
# =================================================================================================================

print('hola mundo')
print('hola\nmundo\nhola sebas')
print('\tpython\t\tjava') # python 1 tab => 4 espacios
#print("Me gusta "Python", es chévere!")
print('Me gusta "Python", es chévere!')
print("Me gusta \"Python\", es chévere!")
print('Me gusta \'Python\', es chévere!')


# ================
# 8) String <str>
# ================

# ------------------------------------
# => formas de representar un string
# ------------------------------------
cadena_1 = 'hola python'
cadena_2 = "hola java"
cadena_3 = '''hola ecuador'''
cadena_4 = """hola alemania"""
cadena_5 = """
hola este string
tiene varias
líneas
"""

print( cadena_1 , type(cadena_1) )
print( cadena_2 , type(cadena_2) )
print( cadena_3 , type(cadena_3) )
print( cadena_4 , type(cadena_4) )
print( cadena_5 , type(cadena_5) )

# --------------------
# => concatenación +
# --------------------
nombre = 'Sebas'
apellido = 'Silva'

texto = nombre + apellido
print(texto)

nombre = 'Sebas'
apellido = ' Silva'

texto = nombre + apellido
print(texto)

nombre = 'Sebas'
apellido = 'Silva'

texto = nombre + ' ' + apellido
print(texto)
print( nombre + ' ' + apellido )

# ---------------------
# => multiplicación *
# ---------------------
letra = 'A'
print( 5 * letra ) # AAAAA
print( letra * 5 ) # AAAAA

# ----------------------------------
# => índices [i] y tamaño => len()
# ----------------------------------
palabra = 'hola'
# (+)      0123
# (-)      4321

print( palabra )
print()
print( palabra[0] )
print( palabra[1] )
print( palabra[2] )
print( palabra[3] )
print()
print( palabra[-4] )
print( palabra[-3] )
print( palabra[-2] )
print( palabra[-1] )
print()
print( len(palabra) , type(len(palabra)) )
#print( palabra[5] )  # IndexError: string index out of range

# -----------------------------
# => slicing [start:end:step]
# end - exclusivo
# start, step - opcionales
# -----------------------------

palabra = 'programación'
#          012345678901

# EJ:
# pro
# gramación

print( palabra[0:2] ) # end => exclusivo!
print( palabra[0:3] )
print( palabra[3:11] ) # end => exclusivo, slicing no tiene index error!
print( palabra[3:12] )
print( palabra[3:100] )
print()
print( palabra[:3] )
print( palabra[3:] )

# EJ:
# grama
print( palabra[3:8] )
print( palabra[3:8:1] )
print( palabra[3:8:2] )

# EJ:
# usando => step
print( palabra[::1] )
print( palabra[::2] )
print( palabra[::3] )



# ===================================================
# 9) Métodos de Formato Importantes de String <str>
# ===================================================

# ----------------------------
# => para dar formato a texto
# ----------------------------
texto = 'mE gusTA APRENDER pyTHON'
print( texto ) # mE gusTA APRENDER pyTHON
print( texto.capitalize() ) # Me gusta aprender python
print( texto.title() ) # Me Gusta Aprender Python
print( texto.upper() ) # ME GUSTA APRENDER PYTHON
print( texto.lower() ) # me gusta aprender python
print( texto.swapcase() ) # Me GUSta aprender PYthon

# ------------------------
# => alineación de texto
# ------------------------
nombre = 'Andy'

print('Hola', nombre, 'espero estés bien!') # Hola Andy espero estés bien!
print('Hola', nombre.center(10), 'espero estés bien!') # Hola    Andy    espero estés bien!
print('Hola', nombre.ljust(10), 'espero estés bien!') # Hola Andy       espero estés bien!
print('Hola', nombre.rjust(10), 'espero estés bien!') # Hola       Andy espero estés bien!

# -------------------------
# => contar coincidencias
# -------------------------
cadena = 'esta vida es hermosa'
#         01234567890123456789

print( cadena.count('a') ) # 3
print( cadena.count('es') ) # 2
print( cadena.count('a' , 4) ) # 2
print( cadena.count('a' , 4 , 10) ) # 1
print( cadena.count('x') ) # 0

# -----------------------------------
# => retornar índice de una búsqueda
# -----------------------------------
lenguaje = 'javascript'
#           0123456789

print( lenguaje.index('a') , lenguaje.find('a') ) # izquierda a derecha
print( lenguaje.rindex('a') , lenguaje.rfind('a') ) # derecha a izquierda
print( lenguaje.index('asc') , lenguaje.find('asc') ) 
print( lenguaje.index('c',3,8) , lenguaje.find('c',3,8) ) 
#print( lenguaje.index('x') ) # ValueError: substring not found
print( lenguaje.find('x') ) # -1

# --------------------------------
# => eliminar espacios / caracter
# --------------------------------
c1 = '    python'
c2 = 'python   '
c3 = '      python   '
c4 = '***python**'

print(c1)
print(c2)
print(c3)
print(c4)

print( c1.lstrip() )
print( c2.rstrip() )
print( c3.strip() )
print( c4.strip('*') )

# ----------------------------------------------
# => unir un caracter a un string en secuencia
# ----------------------------------------------
char_1 = '-'
char_2 = '#'

palabra = 'youtube'

print( char_1.join(palabra) ) # y-o-u-t-u-b-e
print( char_2.join(palabra) ) # y#o#u#t#u#b#e
print( '.'.join(palabra) ) # y.o.u.t.u.b.e

# -------------------------------------------------
# => separar un string en elementos de una lista
# (* tema lista ya lo vemos a continuación)
# -------------------------------------------------
lenguajes_1 = 'java python c++ basic'
lenguajes_2 = 'java,python,c++,basic'

lista_1 = lenguajes_1.split()
lista_2 = lenguajes_2.split(',')

print( lista_1 , type(lista_1) , len(lista_1) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4
print( lista_2 , type(lista_2) , len(lista_2) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4

# -----------------------------
# => líneas de string a lista
# -----------------------------
texto = 'Yo programa en Python.\nEl en Java.\nElla en C++.'
lista_1 = texto.splitlines()
lista_2 = texto.splitlines(keepends=True) # conserva los saltos de línea como secuencia de escape

print(texto)
print(lista_1)
print(lista_2)

texto = """hola
mundo
hola python"""

lista = texto.splitlines()
print(lista)

# -----------------------------
# => cambiar espaciado de tabs
# -----------------------------
saludo = 'hola\tamigo'

print( saludo )               # hola    amigo
print( saludo.expandtabs() )  # hola    amigo
print( saludo.expandtabs(1) ) # hola amigo
print( saludo.expandtabs(2) ) # hola  amigo
print( saludo.expandtabs(4) ) # hola    amigo

# --------------------------------------------------
# => IMPORTANTE: reemplazar un caracter del string
# --------------------------------------------------
secreto = 'pXlabrX secreXtX pXlabrX ocultX'

print( secreto.replace('X' , '***') ) # p***labr*** secre***t*** p***labr*** ocult***       
print( secreto.replace('pXl' , 'zzzzzz') ) # zzzzzzabrX secreXtX zzzzzzabrX ocultX
print( secreto.replace(' ' , 'yyy') ) # pXlabrXyyysecreXtXyyypXlabrXyyyocultX



# ==========================================================================
# 10) Métodos de String con Retorno Booleano (averiguar algo en el String)
# ==========================================================================

# ----------------------------------------------------
# .isalpha() => True si todos son letras (A-Z / a-z)
# ----------------------------------------------------
c_1 = 'abcXYZ'
c_2 = 'abc XYZ'
c_3 = '1abcXYZ'

print( c_1 , c_1.isalpha() ) # abcXYZ True
print( c_2 , c_2.isalpha() ) # abc XYZ False
print( c_3 , c_3.isalpha() ) # 1abcXYZ False

# -------------------------------------------
# .isalnum() => True si son letras y números
# -------------------------------------------
print( c_1 , c_1.isalnum() ) # abcXYZ True
print( c_2 , c_2.isalnum() ) # abc XYZ False
print( c_3 , c_3.isalnum() ) # 1abcXYZ True

# --------------------------------------------
# .isdigit() => True si es un sting numérico
# --------------------------------------------
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
c_3 = 'HOLA AMIGO' # upper
c_4 = 'hola amigo' # lower

print('string|.islower()|.isupper()|.istitle()')             # string|.islower()|.isupper()|.istitle()
print( c_1 , c_1.islower() , c_1.isupper() , c_1.istitle() ) # Hola Amigo False False True
print( c_2 , c_2.islower() , c_2.isupper() , c_2.istitle() ) # Hola amigo False False False
print( c_3 , c_3.islower() , c_3.isupper() , c_3.istitle() ) # HOLA AMIGO False True False
print( c_4 , c_4.islower() , c_4.isupper() , c_4.istitle() ) # hola amigo True False False

# ----------------------------
# .startswith() / .endswith()
# ----------------------------
c_1 = 'súper python!'
c_2 = ' Hola mundo...'

print( c_1.startswith('s') ) # True
print( c_1.startswith('sú') ) # True
print( c_2.startswith(' ') ) # True
print( c_2.startswith(' H') ) # True
print( c_2.startswith(' h') ) # False
print()
print( c_1.endswith('!') ) # True
print( c_1.endswith('n!') ) # True
print( c_1.endswith('On!') ) # False


# =========================================
# 11) Métodos para Números + Librería Math
# =========================================

# --------------------------------
# funciones internas para números
# --------------------------------
# => round() / inmediato superior
num_1 = 3.2
num_2 = 3.5
num_3 = 3.9

print( num_1, '|' , round(num_1) ) # 3.2 | 3
print( num_2, '|' , round(num_2) ) # 3.5 | 4
print( num_3, '|' , round(num_3) ) # 3.9 | 4

