from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER = [
      
        ('viewr','Viewr'),
        ('recipent','Recipent'),
        ('adminuser','Adminuser'),
    ]
    user_type = models.CharField(choices=USER , max_length=100)
    city=models.CharField(max_length=100,null=True)
    otp_token = models.CharField(max_length=10, null= True, blank=True)


class Recipi_catagoriesModel(models.Model):
     Catagoriy=models.CharField(max_length=100,null=True)
     def __str__(self) -> str:
        return self.Catagoriy


        
class RecipiModel(models.Model):
    Tags = [
      
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non-vegetarian'),
        
    ]
    RecipiTitle=models.CharField(max_length=100,null=True)
    Ingredients=models.TextField(max_length=100,null=True)
    PreparationTime=models.TimeField(null=True)
    CookingTime=models.TimeField(max_length=100,null=True)
    Image=models.ImageField(upload_to="media/recipi_pic",null=True)
    TotalTime=models.CharField(max_length=100,null=True)
    DifficultyLevel=models.CharField(max_length=100,null=True)
    Nutrational_Information=models.CharField(max_length=100,null=True)
    catagory=models.ForeignKey(Recipi_catagoriesModel, on_delete=models.CASCADE,null=True)
    tags=models.CharField(choices=Tags,null=True,max_length=120)
    price=models.IntegerField(null=True)


class viewrProfile(models.Model):
    user = models.OneToOneField(Custom_User,null=True, on_delete = models.CASCADE, related_name='recruiter')
    
    def __str__(self):
        return self.user.display_name

class recipentProfile(models.Model):

    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='khadija')
    

    def __str__(self):
        return self.user.display_name
    
class FavoriteRecipe(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipiModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.recipe.title}'