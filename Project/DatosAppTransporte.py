# es una librería de Python especializada en el manejo y análisis de estructuras de datos.
import pandas as pd
import uuid  # define un sistema para crear identificadores universalmente únicos de recursos 
# de una manera que no requiere un registro central
import random  # contiene una serie de funciones relacionadas con los valores aleatorios
# Faker es un paquete de Python que genera datos falsos para ti. Ya sea que necesite iniciar su base de datos
from faker import Faker
import datetime  # módulo proporciona clases para manipular fechas y horas.

numUsuarios = 10000  # Número de usuarios a generar
numTaxistas = 10000  # Número de taxistas a generar
numCompanias = 10000  # Número de compañías a generar
numVehiculos = 10000  # Número de vehículos a generar
numServicios = 10000  # Número de servicios a generar
numTarifa = 10000  # Número de tarifas a generar
numParroquias = 10000  # Número de parroquias a generar
numAdministrador = 1  # Numero de administradores a generar
# Solo se genera un administrador
numCanton = 1  # Solo es un canton por lo que no es necesario generar mas de 1 dato
numApp = 1  # Numero de apps a crear solo va ser una

###################################################################################################
# CREACION DATA SET DE USUARIOS
features = [  # 5 atributos
    "IdUs",
    "nombreUs",
    "emailUs",
    "nac",
    "phoneUs",
]
# Creamos un DataFrame con las columnas, Estructura de dos dimensiones (tablas).
df = pd.DataFrame(columns=features)
# generamos los datos id y guardarlos en el DataFrame
df['IdUs'] = [uuid.uuid4().hex for i in range(numUsuarios)]
# Imprime verdadero si el usuario es unico
print(df['IdUs'].nunique() == numUsuarios)

genders = ["Masculino", "Femenino"]
df['genero'] = random.choices(  # Generar una lista aleatoria de géneros
    genders,
    # 60% de hombres, 30% de mujeres
    weights=(60, 30),
    k=numUsuarios
)  # Genera aleatoriamente el género de cada usuario

faker = Faker()  # Generar los datos falsos


def name_gen(gender):  # Genera un nombre basado en el género
    if gender == 'Masculino':
        return faker.name_male()  # Genera un nombre de hombre segun el genero
    elif gender == 'Femenino':
        return faker.name_female()  # Genera un nombre de mujer segun el genero
    return faker.name()  # Genera de nombres para cada usuario

# guarda el nombre en la columna name
df['nombreUs'] = [name_gen(i) for i in df['genero']]
# Genera una dirección de correo electrónico aleatoria basada en el nombre dado

def emailGen(name, duplicateFound=False):
    dom = "@firemail.es"  # Nombre del dominio falso para usar
    name = name.lower().split(" ")  # Separa el nombre en dos partes
    chars = [".", "_"]  # carácter aleatorio para insertar en el nombre
    new_name = name[0] + random.choice(chars) + name[1]
    if duplicateFound:  # adicional del correo electrónico si se encontró un duplicado
        num = random.randint(0, 100)  # Número aleatorio para insertar al final
        new_name = new_name + str(num)  # Insertado en el final
    return new_name + dom  # Devuelve la dirección de correo electrónico unico con el dominio

emails = []  # Generar la lista de mails
for name in df['nombreUs']:  # Generar una dirección de correo electrónico para cada nombre
    email = emailGen(name)  # Generando el correo electrónico
    while email in emails:  # Bucle hasta que se genere un correo electrónico único
        # Crear un correo electrónico con un número aleatorio
        email = emailGen(name, duplicateFound=True)
    emails.append(email)  # Adjuntar el nuevo correo electrónico a la lista
df['emailUs'] = emails  # Guarda el mail en la columna mail


def random_nac(start, end, n):  # Generar una lista aleatoria entre dos marcas de tiempo dadas

    frmt = "%Y-%m-%d"  # El formato de tiempo
    # Formatear los dos periodos de tiempo
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime  # Creando el grupo para tiempos aleatorios
    times = [(random.random() * td + stime).strftime(frmt)
             for _ in range(n)]  # Generando una lista con los tiempos aleatorios
    return times  # Generar una lista de fechas de nacimiento aleatorias


# guarda la fecha de nacimiento en la columna nac en un intervalo de 1970 a 2006
df['nac'] = random_nac("1970-01-01", "2006-01-01", numUsuarios)

# Genera un número de teléfono aleatorio para cada usuario
df['phoneUs'] = [faker.phone_number() for i in range(numUsuarios)]

df.to_csv('dataset_usuarios.csv')  # Guarda el DataFrame en un archivo csv

#############################################################################################
# CREACION DE LOS DATA SET DE TAXISTAS
features = [  # Una lista de 7 características
    "id",
    "nombre",
    "email",
    "phone",
    "Status"
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista
# Lista de booleanos para elegir si es verdadero o falso
choice = [True, False]

# generamos los datos id y guardarlos en el DataFrame
df['id'] = [uuid.uuid4().hex for i in range(numTaxistas)]
# Imprime verdadero si el usuario es unico
print(df['id'].nunique() == numTaxistas)

genders = ["Masculino", "Femenino"]  # Lista de géneros
df['genero'] = random.choices(  # Generar una lista aleatoria de géneros
    genders,
    # 80% de hombres, 10% de mujeres y 10% de no especificado
    weights=(100, 0),
    k=numTaxistas  # El número a generar
)  # Genera aleatoriamente el género de cada usuario

def name_gen(gender):  # Genera un nombre basado en el género
    if gender == 'male':
        return faker.name_male()  # Genera un nombre de hombre segun el genero
    elif gender == 'female':
        return faker.name_female()  # Genera un nombre de mujer segun el genero
    return faker.name()  # Genera de nombres para cada usuario
# guarda el nombre en la columna name
df['nombre'] = [name_gen(i) for i in df['genero']]

# Genera una dirección de correo electrónico aleatoria basada en el nombre dado


def emailGen(name, duplicateFound=False):

    dom = "@icemail.es"  # Nombre del dominio falso para usar
    name = name.lower().split(" ")  # Separa el nombre en dos partes
    chars = [".", "_"]  # carácter aleatorio para insertar en el nombre
    new_name = name[0] + random.choice(chars) + name[1]
    if duplicateFound:  # adicional del correo electrónico si se encontró un duplicado
        num = random.randint(0, 100)  # Número aleatorio para insertar al final
        new_name = new_name + str(num)  # Insertado en el final
    return new_name + dom  # Devuelve la dirección de correo electrónico unico con el dominio

emails = []  # Generar la lista de mails
for name in df['nombre']:  # Generar una dirección de correo electrónico para cada nombre
    email = emailGen(name)  # Generando el correo electrónico
    while email in emails:  # Bucle hasta que se genere un correo electrónico único
        # Crear un correo electrónico con un número aleatorio
        email = emailGen(name, duplicateFound=True)
    emails.append(email)  # Adjuntar el nuevo correo electrónico a la lista
df['email'] = emails  # Guarda el mail en la columna mail


def random_nac(start, end, n):  # Generar una lista aleatoria entre dos marcas de tiempo dadas
    frmt = "%Y-%m-%d"  # El formato de tiempo
    # Formatear los dos periodos de tiempo
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime  # Creando el grupo para tiempos aleatorios
    times = [(random.random() * td + stime).strftime(frmt)
             for _ in range(n)]  # Generando una lista con los tiempos aleatorios
    return times  # Generar una lista de fechas de nacimiento aleatorias

# guarda la fecha de nacimiento en la columna nac en un intervalo de 1970 a 2002
# df['nac'] = random_nac("1970-01-01", "2002-01-01", numUsuarios)


# Genera un número de teléfono aleatorio para cada usuario
df['phone'] = [faker.phone_number() for i in range(numUsuarios)]

# Verificamos
Status = ["Disponible", "No Disponible"]
df['Status'] = random.choices(
    Status,
    weights=(90, 10),
    k=numUsuarios
)
del (df['genero'])
df.to_csv('dataset_taxistas.csv')  # Guarda el DataFrame en un archivo csv

##########################################################################################
# CREACION DE DATA SET DE VEHICULOS
faker = Faker(['es_CO'])  # Generar los datos falsos
features = [  # Una lista de 5 para vehiculos
    "id",
    "marca",
    "color",
    "placa",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# Lista de booleanos para elegir si es verdadero o falso
#choice = [True, False]

# df['subscriber'] = random.choices(  # Generar una lista aleatoria de booleanos
#  choice,
#   k=numVehiculos  # El número a generar
# )  # Guarda aleatoriamente la suscripción con verdadero o falso

# generamos los datos id de la compania y guardarlos en el DataFrame
df['id'] = [faker.aba() for i in range(numVehiculos)]

marcas = ["audi", "bmw", "ford", "mercedes", "toyota", "volkswagen", "volvo",
          "seat", "renault", "citroen", "peugeot", "hyundai", "kia", "nissan"]
# Lista de marcas de coches
df['marca'] = random.choices(  # Generar una lista aleatoria de marcas de coches
    marcas,
    k=numVehiculos  # El número a generar
)  # Genera aleatoriamente marca de cada usuario

# Genera un color aleatorio y lo guarda en el DataFrame
df['color'] = [faker.color_name() for i in range(numVehiculos)]

# Genera una matricula aleatoria y la guarda en el DataFrame
df['placa'] = [faker.license_plate() for i in range(numVehiculos)]

df.to_csv('dataset_vehiculos.csv')  # Guarda el DataFrame en un archivo csv

############################################################################################
# CREACION DE DATA SET DE SERVICIOS
features = [  # Una lista de 3 para los servicios
    "id",
    "tipo",
    "status",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# generamos los datos id de la servicio y guardarlos en el DataFrame
df['id'] = [faker.ssn() for i in range(numServicios)]

tipo_servicio = ["viaje", "paquetes", "comida", "encomienda",
                 "puerta a puerta"]  # Lista de tipos de servicio

df['tipo'] = random.choices(  # Generar una lista aleatoria de tipos de servicio
    tipo_servicio,
    k=numServicios  # El número a generar de servicios
)  # Genera aleatoriamente tipo de servicio de cada usuario

status_servicio = ["en curso", "finalizado", "cancelado",
                   "aceptado", "Disponible", "No Dsiponible"]  # Lista de estado de servicio

df['status'] = random.choices(  # Generar una lista aleatoria de tipos de servicio
    status_servicio,
    k=numServicios  # El número a generar de estados de servicio
)  # Genera aleatoriamente estado de servicio de cada usuario

df.to_csv('dataset_servicios.csv')  # Guarda el DataFrame en un archivo csv


##################################################################################################
# CREACION DE DATA SET DE TARIFAS
features = [  # Una lista de 3 para tarifas
    "id",
    "forma_pago",
    "status",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista
# generamos los datos id de la tarifa y guardarlos en el DataFrame

df['id'] = [faker.swift(length=8) for i in range(numTarifa)]
pago = ["tarjeta", "efectivo", "transferencia"]  # Lista de formas de pago
df['forma_pago'] = random.choices(  # Generar una lista aleatoria de tarifas
    pago,
    k=numTarifa  # El número a generar de tarifas
)  # Genera aleatoriamente formas de pago de cada usuario

estado_de_pago = ["pendiente", "pagado"]  # Lista estado de pago

df['status'] = random.choices(  # Generar una lista aleatoria de tarifas
    estado_de_pago,
    weights=(10, 90),
    k=numTarifa  # El número a generar de tarifas
)  # Genera aleatoriamente formas de pago de cada usuario

df.to_csv('dataset_tarifas.csv')  # Guarda el DataFrame en un archivo csv

################################################################################################
# CREACION DATASET CANTON
features = [  # Una lista de 3 para las parroquias de quito
    "idC",
    "nombreC",
    "statusC",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# generamos los datos id del canton y guardarlos en el DataFrame
df['idC'] = [faker.postcode() for i in range(numCanton)]
# Verificamos que no se repitan los id
print(df['idC'].nunique() == numCanton)

Canton = ["Quito"]  # Lista de géneros

df['nombreC'] = random.choices(  # Generar una lista del canton
    Canton,
    k=numCanton  # El número a generar Canton
)  # Genera para cada usuario

statusC = ["activo", "no activo"]  # Lista estado del Canton

df['statusC'] = random.choices(  # Generar una lista aleatoria de tarifas
    statusC,
    weights=(100, 0),
    k=numCanton  # El número a generar de canton
)
#df.to_csv('dataset_canton.csv')  # Guarda el DataFrame en un archivo csv

################################################################################################
# CREACION DATASET PARROQUIA
features = [  # Una lista de 3 para las parroquias de quito
    "id",
    "nombre",
    "status",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# generamos los datos id de la parroquia y guardarlos en el DataFrame
df['id'] = [faker.postcode() for i in range(numParroquias)]

# Verificamos que no se repitan los id
print(df['id'].nunique() == numParroquias)

parroquias = ["Chavezpamba", "Checa", "El Quinche", "Gualea", "Guangopolo", "Guayllabamba",
              "La Merced", "Llano Chico", "Lloa, Nanegal", "Nanegalito", "Nayon", "Nono",
              "Pacto", "Perucho", "Pifo", "Píntag", "Pomasqui", "Puéllaro", "Puembo",
              "San Antonio de Pichincha", "San Jose de Minas", "Tababela", "Tumbaco", "Yaruquí", "Zambiza",
              "Alangasí", "Amaguaña", "Atahualpa", "Calacali", "Calderon", "Conocoto", "Cumbayá",
              "Carcelen", "Centro Historico", "Chilibulo", "Chillogallo", "Chimbacalle", "Cochapamba",
              "Comite del Pueblo", "Concepción", "Cotocollao", "El Condado", "Magdalena",
              "Guamaní", "Iñaquito", "Itchimbia", "Jipijapa", "Kennedy", "La Argelia",
              "La Ecuatoriana", "La Ferroviaria", "La Libertad, La Mena", "Mariscal Sucre",
              "Ponceano", "Puengasí", "Quitumbe", "Rumipamba", "San Bartolo",
              "San Juan", "Solanda", "Turubamba"]  # Lista de géneros

df['nombre'] = random.choices(  # Generar una lista aleatoria de parroquias
    parroquias,
    k=numParroquias  # El número a generar de parroquias
)  # Genera aleatoriamente parroquias de cada usuario

estado = ["activo", "pasivo"]  # Lista estado de la parroquia

df['status'] = random.choices(  # Generar una lista aleatoria de tarifas
    estado,
    weights=(100, 0),
    k=numParroquias  # El número a generar de tarifas
)  # Genera aleatoriamente formas de pago de cada usuario
df.to_csv('dataset_parroquias.csv')  # Guarda el DataFrame en un archivo csv

###########################################################################################
# CREACION DATASET ADMINISTRADOR
features = [  # Una lista de  1 atributo
    "id",
    "nombreAdmin"
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# generamos los datos id de la parroquia y guardarlos en el DataFrame
df['id'] = [faker.swift(length=8) for i in range(numAdministrador)]

# Verificamos que no se repitan los id
print(df['id'].nunique() == numAdministrador)

GeneroAdmin = ["Masculino", "Femenino"]
# Generación de los nombres de los usuarios.
df['GeneroAdmin'] = random.choices(
    GeneroAdmin,
    weights=(50, 50),
    k=numAdministrador
)

def name_gen(GeneroAdmin):
    # En caso de que el genero sea hombre nos retornara un nombre masculino
    if GeneroAdmin == 'Masculino':
        return faker.name_male()
    # En caso de que el genero sea mujer nos retornara un nombre femenino
    elif GeneroAdmin == 'Femenino':
        return faker.name_female()
    return faker.name()  # Generamos los nombres de los usuarios

# Guardamos los nombres de los usuarios en todo el atributo
df['nombreAdmin'] = [name_gen(i) for i in df['GeneroAdmin']]
del (df['GeneroAdmin'])
df.to_csv('dataset_administrador.csv')  # Guarda el DataFrame en un archivo csv

################################################################################
# CREACION DATASET APP
features = [  #atributos App
    "id",
    "nombre",
]
df = pd.DataFrame(columns=features)  # Creamos un DataFrame para esta lista

# generamos los datos id de la APP y guardarlos en el DataFrame
df['id'] = [faker.postcode() for i in range(numApp)]

# Verificamos que no se repitan los id
print(df['id'].nunique() == numApp)

app = ["Taxi Plus"]  # Nombre de la App
df['nombre'] = random.choices( 
    app,
    k=numApp
) 
df.to_csv('dataset_app.csv')  # Guarda el DataFrame en un archivo csv
##############################################################################