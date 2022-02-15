# from datetime import datetime, timedelta
# from celery import Celery
# from celery.schedules import crontab
# import zipfile


# app = Celery( 'tasks' , broker = 'redis://localhost:6379/0' )


# @app.task
# def check():
#  print("I am checking your stuff")
# app.conf.beat_schedule = {
#  "run-me-every-ten-seconds": {
#  "task": "tasks.check",
#  "schedule": 10.0
#  }
# }

from celery import Celery
app = Celery('tasks',broker='redis://localhost:6379/0')
@app.task
def check():
 print("I am checking your stuff")
app.conf.beat_schedule = {
 "run-me-every-ten-seconds": {
 "task": "tasks.check",
 "schedule": 10.0
 }
}

# # @app.on_after_configure.connect
# # def setup_periodic_tasks(sender, **kwargs):
# #     # Calls test('hello') every 10 seconds.
# #     sender.add_periodic_task(crontab(), hello.s())

#     # sender.add_periodic_task(5.0, hello.s('hello'), name='add every 10')

#     # # Calls test('world') every 30 seconds
#     # sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(
#     #     crontab(hour=7, minute=30, day_of_week=1),
#     #     test.s('Happy Mondays!'),
    


# # Creamos una tarea llamada sumar_numeros usando el decorador @app.task

# # Se imprime un mensaje con la fecha simulando un LOG

# @app.task

# def sumar_numeros(x, y):

#     print ("-> Se generó una tarea [{}]: {} + {}".format(datetime.now(), x, y))

#     return x + y


# # Creamos una tarea llamada hola

# @app.task

# def hola(nombre):

#         return 'Hola %s' % nombre

# # Tarea comprimir archivos

@app.task

def comprimir(filename, zipname, new_path):

    print ('\n-> Se va a comprimir el archivo: {}'.format(filename))

    zfile = zipfile.ZipFile(new_path + '/' + zipname, 'w')

    zfile.write(filename, compress_type = zipfile.ZIP_DEFLATED)

    zfile.close()

    print ('\n-> El archivo comprimido se copió a : {}'.format(new_path))


# @app.task()
# def hello():
#     return 'hello world'


# tomorrow = datetime.utcnow() + timedelta(seconds=30)
# hello.apply_async(eta=tomorrow)