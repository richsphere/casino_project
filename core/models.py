from django.db import models
from django.utils.text import slugify


class PaymentMethod(models.Model):
     METHOD_TYPES = (
          ('deposit', 'Deposit'),
          ('withdrawal', 'Withdrawal')
     )
     name = models.CharField(max_length=100)
     method_type = models.CharField(max_length=20, choices=METHOD_TYPES)
     
     def __str__(self):
         return self.name
   
   
class Tag(models.Model):
     name = models.CharField(max_length=100)
     
     def __str__(self):
         return self.name
    
    
class Casino(models.Model):
     name = models.CharField(max_length=255)
     slug = models.SlugField(unique=True)
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
     
     
     deposit_methods = models.ManyToManyField("PaymentMethod", \
          related_name="casinos_with_deposit", \
               limit_choices_to={'method_type': 'deposit'},
               blank=True)
     withdrawal_methods = models.ManyToManyField("PaymentMethod", \
          related_name="casinos_with_withdrawal", \
               limit_choices_to={'method_type': 'withdrawal'},
               blank=True)
     tags = models.ManyToManyField(Tag, blank=True)
     
     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.name)
          if not self.meta_title:
               self.meta_title = self.name
          if not self.meta_description and self.description:
               self.meta_description = self.description[:160]
          super().save(*args, **kwargs)
          
     def __str__(self):
         return self.name
    
    
class CasinoFeature(models.Model):
     casino = models.ForeignKey('Casino', on_delete=models.CASCADE, \
          related_name='features')
     text = models.CharField(max_length=255)
     
     def __str__(self):
         return f"{self.casino.name} - {self.text}"
    
    
class CasinoReview(models.Model):
     casino = models.OneToOneField("Casino", on_delete=models.CASCADE, \
          related_name="review")
     title = models.CharField(max_length=255, default="Review")
     
     content_markdown = models.TextField(blank=True)
     content_blocks = models.JSONField(default=list, blank=True)
     
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     # class Meta:
     #      verbose_name = "Casino Review"
     #      verbose_name_plural = "Casinos Review"
          
     def __str__(self):
         return f"{self.casino.name} Review"


class Bonus(models.Model):
    BONUS_TYPES = [
        ('freespins', 'Free Spins'),
        ('wager', 'Wager'),
        ('percent', 'Bonus Percent'),
        ('amount', 'Bonus Amount'),
    ]

    casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=BONUS_TYPES, \
         default='freespins')
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"


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
     
     class Meta:
          verbose_name = "Slot"
          verbose_name_plural = "Slots"
     
     def __str__(self):
         return self.name
     
     
class CasinoSlots(models.Model):
     casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
     slot = models.ForeignKey(Slots, on_delete=models.CASCADE)
     
     class Meta:
          verbose_name = "Casino slot"
          verbose_name_plural = "Casino slots"
     
     def __str__(self):
         return f"{self.casino.name} - {self.slot.name}"


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