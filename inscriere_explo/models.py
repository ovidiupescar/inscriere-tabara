from django.db import models

# Create your models here.

class Rezervare(models.Model):
    numar_rezervare = models.CharField(max_length=10)           # va trebui generat cumva
    nume = models.CharField(max_length=60)
    tip = models.CharField(max_length=20)                  # rolul celui care inscrie. Poate fi instructor sau parinte
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    data_rezervarii = models.DateTimeField('data rezervarii')
    data_modificare = models.DateTimeField(auto_now=True)
    data_expirarii = models.DateTimeField('data expirarii')
    notificare_plata = models.BooleanField(default='False')
    notificare_expirare = models.BooleanField(default='False')
    platit = models.IntegerField(default=0)                      # contine suma platita. Va fi adaugata de Coordonator sau de Narcis
    def __str__(self):
        return self.numar_rezervare


class Participant(models.Model):
    rezervare = models.ForeignKey(Rezervare, on_delete=models.CASCADE)
    nume = models.CharField(max_length=60)
    data_nasterii = models.DateTimeField('data nasterii')
    sex = models.CharField(max_length=1)                        # m sau f
    tip = models.CharField(max_length=20)                       # licuric / explorator / parinte / instructor / ajutor
    cort = models.BooleanField()
    cladire = models.CharField(max_length=1)                    # B sau F
    camera = models.CharField(max_length=2)                     # numarul camerei
    pat = models.CharField(max_length=2)                        # patul din camera
    comunitate = models.CharField(max_length=60)
    grupa = models.CharField(max_length=60)
    probleme = models.CharField(max_length=1000)

    def __str__(self):
        return self.nume + ' ' + self.rezervare  

