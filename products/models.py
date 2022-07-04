from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price  = models.DecimalField(max_digits=100000, decimal_places=2)
    image = models.ImageField(upload_to='images',blank=True)
    # SlugField permet de gerer les espace au niveau de l'url ex orange product = orange-product
    # null=True permet de donner la valeur null aux autres tables qui seront ajouter dans le model
    slug = models.SlugField(null=True) 
    actif = models.BooleanField(default=True)


    # Eviter qu'il ait double s sur le Products au niveau de l'interface
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    # fonction surcharge pour renvoyer le nom des produits sur l'interface aulieu de Product object
    def __str__(self):
        return self.name

"""
python -m pip install Pillow (commande d'installation de Pillow)
Pillow est une bibliothèque de traitement d’image,
qui est un fork et successeur du projet PIL (Python Imaging Library).
Elle est conçue de manière à offrir un accès rapide aux données contenues dans une image,
et offre un support pour différents formats de fichiers tels que PPM, PNG, JPEG, GIF, TIFF et BMP.
------------------------
chaque fois que je modifie ma class model voici les deux commandes
a inserer :
python manage.py makemigrations
python manage.py migrate
"""