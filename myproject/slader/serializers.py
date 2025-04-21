from rest_framework import serializers
from .models import Slider,Item,AboutUs,Contacts,ClientReview

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'subtitle', 'img', 'link', 'is_active')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'content', 'created_at']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'email', 'phone', 'address']

class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = ['id', 'author', 'content', 'rating', 'created_at']
