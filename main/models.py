from django.db import models


class Player(models.Model):
    photo = models.ImageField(upload_to="players-phot/", blank=True, null=True)
    number = models.IntegerField()
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    games_played = models.IntegerField()
    minuts_played = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()
    def __str__(self):
        self.first_name

class Commant(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="Command/", blank=True, null=True)
    player_id = models.ManyToManyField(Player)
    def __str__(self):
        self.name

class Match_time(models.Model):
    first_command= models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="team1")
    second_command = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="team2")
    date = models.DateTimeField()
    


class Media(models.Model):
    photo = models.ImageField(blank=True, null=True)
    video = models.FileField(upload_to="files/%Y/%m/%d")
    date = models.DateField()
    first_command_name = models.ForeignKey(Commant, on_delete=models.CASCADE,  related_name="teams1")
    second_command_name = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="teams2")
    what_account = models.CharField(max_length=255)
    def __str__(self):
        self.what_account


class News(models.Model):
    photo = models.ImageField(upload_to='news/', blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    is_banner = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.title
        

class Shop(models.Model):
    product = models.CharField(max_length=255)
    img_file = models.ImageField(upload_to=('product/'), null=True, blank=True)


class Team_jersey(models.Model):
    Choose_the_form = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        self.name
    
class Quarter(models.Model):
    quarter_number = models.CharField(max_length=255)
    first_command = models.ForeignKey(Commant, on_delete=models.CASCADE,  related_name="teames1")
    second_command = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="teames2")
    def __str__(self):
        self.quarter_number

class Statistic(models.Model):
    match = models.ForeignKey(Match_time, on_delete=models.CASCADE)
    def __str__(self):
        self.match


class About_academy(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ImageField(upload_to="about-academy/", blank=True, null=True)
    def __str__(self):
        self.name

class Info(models.Model):
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    def __str__(self):
        self.description

class Social_media(models.Model):
    url = models.URLField()
    logo = models.ImageField(upload_to='Social_media/', blank=True, null=True)
    def __str__(self):
        self.logo






