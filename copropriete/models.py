from django.db import models


class Copropriete(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    administrateur = models.CharField(max_length=200)

class Coproprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    # autres champs nécessaires

class Charges(models.Model):
    description = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    # autres champs nécessaires

class Paiement(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    coproprietaire = models.ForeignKey(Coproprietaire, on_delete=models.CASCADE)
    # autres champs nécessaires

