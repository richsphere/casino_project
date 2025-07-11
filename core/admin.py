from django.contrib import admin
from django.utils.html import format_html
from .models import Casino, Bonus, Slots, CasinoSlots, \
     Guide, CasinoFeature, CasinoReview, PaymentMethod, Tag


class BonusInline(admin.TabularInline): # Или admin.StackedInline для вертикального вида
     model = Bonus
     extra = 1 # Показывать пустую форму для нового бонуса
     
     
class CasinoFeatureInline(admin.TabularInline):
     model = CasinoFeature
     extra = 1
     
     
class CasinoReviewInline(admin.StackedInline):
     model = CasinoReview
     extra = 0 #  Не показывать пустых форм
     

@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
     list_display = ("name", "license_type", "rating", \
          "min_deposit", "payout_speed", "logo_thumbnail")
     inlines = [
          BonusInline, 
          CasinoFeatureInline, 
          CasinoReviewInline,
          ]
     prepopulated_fields = {"slug": ("name",)}
     search_fields = ("name", "license_type")
     list_filter = ("license_type",)
     filter_horizontal = ['deposit_methods', 'withdrawal_methods', 'tags']
     
     def logo_thumbnail(self, obj):
          if obj.logo:
               return format_html('<img src="{}" style="height:40px;"/>',\
                    obj.logo.url)
          return "-"
     logo_thumbnail.short_description = "Logo"


@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
     list_display = ("name", "provider", "rtp", "volatility")
     search_fields = ("name", "provider")
     
     
@admin.register(CasinoSlots)
class CasinoSlotsAdmin(admin.ModelAdmin):
     list_display = ("casino", "slot")
     search_fields = ("casino__name", "slot__name")
     autocomplete_fields = ["casino", "slot"]

     
@admin.register(Guide)
class GuidAdmin(admin.ModelAdmin):
     list_display = ("title", "created_at", "updated_at")
     prepopulated_fields = {"slug": ("title",)}
     search_fields = ("title",)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
     list_display = ("name", "method_type")
     list_filter = ("method_type",)
     
     
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
     list_display = ("name",)
