from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ordersSerializer
from .models import Orders
from rest_framework.decorators import api_view


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Orders.objects.all()
    serializer_class = ordersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

@api_view(['GET'])
def upload(request):
 if request.POST and request.FILES:
    csvfile = request.FILES['csv_file']
    dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
    csvfile.open()
    reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

        # Redirect to the document list after POST
 return HttpResponseRedirect(reverse('myproject.myapp.views.list'))

