from modeltranslation.translator import register, TranslationOptions
from .models import Guide, Casino, Bonus


@register(Guide)
class GuidTranslationOptions(TranslationOptions):
     fields = ('title', 'content', 'meta_title', 'meta_description')
     
     
@register(Casino)
class CasinoTranslationOptions(TranslationOptions):
     fields = ('name', 'description', 'meta_title', 'meta_description')
     
     