from django.db import models

# Ici le model de ma base de donnée sur les trains
class Traindelinfinies(models.Model) :
    #ici on a une clé définit automatiquement a mes différents trains
    trainID = models.AutoField(primary_key=True)
    city = models.CharField(max_length = 50)
    hour = models.CharField(max_length = 5)
    #j'ai ajouté plan après jai donc mis 'null = true' pour éviter des erreurs
    plan = models.CharField(max_length = 100, null = True)