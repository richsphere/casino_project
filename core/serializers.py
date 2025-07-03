from rest_framework import serializers
from .models import Guide, Casino, Bonus


class GuideSerializer(serializers.ModelSerializer):
     class Meta:
          model = Guide
          fields = ['id', 'slug', 'title', 'content', \
               'meta_title', 'meta_description', 'title_en', \
                    'title_nb', 'content_en', 'content_nb']
          
class CasinoListSerializer(serializers.ModelSerializer):
     class Meta:
          model = Casino
          fields = [
			'name', 'slug', 'logo', 'rating',
               'bonus_percent', 'bonus_amount',
               'freespins', 'wager',
		]
          
class CasinoSerializer(serializers.ModelSerializer):
     class Meta:
          model = Casino
          fields = '__all__'
          
class BonusSerializer(serializers.ModelSerializer):
     class Meta:
          model = Bonus
          fields = '__all__'