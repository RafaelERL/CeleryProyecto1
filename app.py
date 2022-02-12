
from tasks import hola, sumar_numeros, comprimir

# Para ejecutar una función en forma de tarea lo tenemos que hacer de esta forma:

hola.delay('Mundo!')


# Para ejecutar la función sumar:

sumar_numeros.delay(3, 2)

# Para ejecutar la tarea de comprimir:

comprimir.delay('sin_comprimir/un.pdf', 'unPDF.zip', 'comprimidos')

