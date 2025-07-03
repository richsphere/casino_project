from django.db import models
from django.utils.text import slugify


class Casino(models.Model):
     name = models.CharField(max_length=255)
     slug = models.SlugField(unique=True, blank=True)
     description = models.TextField()
     website_url = models.URLField()
     logo = models.ImageField(upload_to='logos/')
     license_type = models.CharField(max_length=100)
     rating = models.DecimalField(max_digits=3, decimal_places=2)
     min_deposit = models.DecimalField(max_digits=10, decimal_places=2)
     payout_speed = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
     
     # SEO
     meta_title = models.CharField(max_length=255, blank=True, null=True)
     meta_description = models.TextField(blank=True, null=True)
     
     # Доп поля для бонуса
     freespins = models.PositiveIntegerField(default=0)
     wager = models.CharField(max_length=50, blank=True)
     bonus_percent = models.PositiveIntegerField(default=0)
     bonus_amount = models.PositiveIntegerField(default=0, help_text="NOK or EUR")
     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.name)
          if not self.meta_title:
               self.meta_title = self.title
          if not self.meta_description and self.description:
               self.meta_description = self.description[:160]
          super().save(*args, **kwargs)
          
     def __str__(self):
         return self.name


class Bonus(models.Model):
     BONUS_TYPES = [
		('no_deposit', 'No Deposit'),
		('deposit', 'Deposit Bonus'),
		('cashback', 'Cashback'),
		('freespins', 'Free Spins'),
	]
     
     casino = models.ForeignKey(Casino, on_delete=models.CASCADE, \
          related_name='bonuses')
     bonus_type = models.CharField(max_length=50, choices=BONUS_TYPES)
     amount = models.CharField(max_length=100)
     wagering = models.CharField(max_length=100)
     bonus_code = models.CharField(max_length=100, \
          blank=True, null=True)
     terms_url = models.URLField(blank=True, null=True)
     is_exclusive = models.BooleanField(default=False)
     
     def __str__(self):
         return f"{self.get_bonus_type_display()} - {self.amount}"


class Slots(models.Model):
     name = models.CharField(max_length=255)
     provider = models.CharField(max_length=255)
     rtp = models.DecimalField(max_digits=4, decimal_places=2)
     volatility = models.CharField(max_length=100)
     demo_url = models.URLField()
     image = models.ImageField(upload_to='slots/')
     meta_title = models.CharField(max_length=255, blank=True, null=True)
     meta_description = models.TextField(blank=True, null=True)
     slug = models.SlugField(unique=True, blank=True)
     
     def __str__(self):
         return self.name
     
     
class CasinoSlots(models.Model):
     casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
     slot = models.ForeignKey(Slots, on_delete=models.CASCADE)
     
     def __str__(self):
         return f"{self.casino.name} - {self.slot.name}"


class Review(models.Model):
     casino = models.ForeignKey(Casino, on_delete=models.CASCADE, \
          related_name='reviews')
     author = models.CharField(max_length=255)
     rating = models.IntegerField()
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return f"{self.author} - {self.rating}/5"


class Guide(models.Model):
     title = models.CharField(max_length=255)
     slug = models.SlugField(unique=True, blank=True)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     meta_title = models.CharField(max_length=255, blank=True, null=True)
     meta_description = models.TextField(blank=True, null=True)
     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title)
          if not self.meta_title:
               self.meta_title = self.title
          if not self.meta_description:
               self.meta_description = self.content[:160]
          super().save(*args, **kwargs)
          
     def __str__(self):
         return self.title
	
     
	
	
	
     
	