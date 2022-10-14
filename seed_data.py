from entregable.models import Familiar

Familiar(nombre="Freddy", direccion="Barrio Copelo", numero_pasaporte=123123).save()
Familiar(nombre="Erika", direccion="La Valetta - Malta", numero_pasaporte=890890).save()
Familiar(nombre="Grecia", direccion="Av. Carabobo 318", numero_pasaporte=345345).save()
Familiar(nombre="Maylin", direccion="Barrio Copelo", numero_pasaporte=567567).save()
Familiar(nombre="Aylin", direccion="Barrio Copelo", numero_pasaporte=121212).save()

print("Se cargo con éxito los usuarios de pruebas")