from django.contrib import admin
from django.utils.html import format_html
from .models import Casino, Bonus, Slots, CasinoSlots, Review, Guide


class BonusInline(admin.TabularInline): # Или admin.StackedInline для вертикального вида
     model = Bonus
     extra = 1 # Показывать пустую форму для нового бонуса

@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
     list_display = ("name", "license_type", "rating", \
          "min_deposit", "payout_speed")
     inlines = [BonusInline]
     prepopulated_fields = {"slug": ("name",)}
     search_fields = ("name", "license_type")
     list_filter = ("license_type",)
     
     def logo_thumbnail(self, obj):
          if obj.logo:
               return format_html('<img src="{}" style="height:40px;"/>',\
                    obj.logo.url)
          return "-"
     logo_thumbnail.short_description = "Logo"
     

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
     list_display = ("casino", "bonus_type", "amount", \
          "wagering", "is_exclusive")
     list_filter = ("bonus_type", "is_exclusive")
     search_fields = ("casino__name", "bonus_code")
     
     
@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
     list_display = ("name", "provider", "rtp", "volatility")
     search_fields = ("name", "provider")
     
     
@admin.register(CasinoSlots)
class CasinoSlotsAdmin(admin.ModelAdmin):
     list_display = ("casino", "slot")
     search_fields = ("casino__name", "slot__name")
     autocomplete_fields = ["casino", "slot"]
     
     
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
     list_display = ("casino", "author", "rating", "created_at")
     list_filter = ("rating", "created_at")
     search_fields = ("casino__name", "author")
     
     
@admin.register(Guide)
class GuidAdmin(admin.ModelAdmin):
     list_display = ("title", "created_at", "updated_at")
     prepopulated_fields = {"slug": ("title",)}
     search_fields = ("title",)

# Register your models here.
