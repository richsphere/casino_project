from rest_framework import serializers
from .models import Guide, Casino, Bonus, CasinoFeature, CasinoReview


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
          
class CasinoFeatureSerializer(serializers.ModelSerializer):
     class Meta:
          model = CasinoFeature
          fields = ['text']
          
class CasinoReviewSerializer(serializers.ModelSerializer):
     class Meta:
          model = CasinoReview
          fields = ["title", "content_markdown", "content_blocks"]
          
class CasinoSerializer(serializers.ModelSerializer):
     features = CasinoFeatureSerializer(many=True, read_only=True)
     review = CasinoReviewSerializer(read_only=True)
     class Meta:
          model = Casino
          fields = '__all__'
          
class BonusSerializer(serializers.ModelSerializer):
     class Meta:
          model = Bonus
          fields = '__all__'