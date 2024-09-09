# pour la 1ère migration choisir option 1 + "entrer" pour les dates ; + "5" pour rating)
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


"""class Photo(models.Model): #03-09
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2)
    date_created = models.DateTimeField(auto_now_add=True) - supp le 08/09/24"""



class Ticket(models.Model):
    """Demande d'une critique"""
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048, null=True, blank=True)
    #photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    image = models.ImageField(null=True, blank=True) #08/09/24
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) # 03-09 default=timezone.now
    
    def __str__(self):
        return f'{self.title}'
    

class Review(models.Model):
    """Critique avec comme champs : title, comment"""
    title = models.fields.CharField(max_length=128)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.fields.CharField(max_length=8192)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'



