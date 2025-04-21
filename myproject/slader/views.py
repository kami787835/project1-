from rest_framework import generics
from .models import Slider,Item,AboutUs,Contacts,ClientReview
from .serializers import SliderSerializer,ItemSerializer,AboutUsSerializer,ContactsSerializer,ClientReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SliderListAPIView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ItemListAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ContactsListCreateView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ClientReviewListCreateView(generics.ListCreateAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer

