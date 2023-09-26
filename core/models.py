from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Il faut un email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


TYPE = (
    ("ETUDIANT", "ETUDIANT"),
    ("CONTROLLER", "CONTROLLER")
)


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ProfileEtudiant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    classe = models.CharField(max_length=255, blank=True)
    id_empeinte = models.IntegerField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


heure = (
    ("08:00 - 10:00", "08:00 - 10:00"),
    ("08:00 - 12:00", "08:00 - 12:00"),
    ("10:00 - 12:00", "10:00 - 12:00"),
    ("14:30 - 16:30", "14:30 - 16:30"),
    ("Toutes la journee", "Toutes la journee")
)


class Time(models.Model):
    heure = models.CharField(max_length=255, choices=heure)


etat = (
    ("En cours", "En cours"),
    ("Accepter", "Accepter"),
    ("Refuser", "Refuser")
)


class Heure(models.Model):
    horaire = models.CharField(max_length=200)

    def __str__(self):
        return self.horaire


class Cours(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Reclamation(models.Model):
    motif = models.CharField(max_length=255)
    preuve = models.FileField(upload_to="Preuve")
    etudiant = models.ForeignKey(ProfileEtudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    dateDeCreation = models.DateField(auto_now_add=True)
    etat = models.CharField(max_length=255, choices=etat, default="En cours")



ETAT = (
    ("Present", "Present"),
    ("Absent", "Absent")
)


class Presence(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    heure = models.CharField(max_length=255, choices=heure)
    etat = models.CharField(max_length=255, choices=ETAT, default="Absent")
    etudiant = models.ForeignKey(ProfileEtudiant, on_delete=models.CASCADE)

    def __str__(self):
        return self.id