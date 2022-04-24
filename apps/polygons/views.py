from django.db.models import Sum
from rest_framework import status, viewsets
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Polygon
from .serializers import DescPolygonsSerializer, PolygonSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    permission_classes = [AllowAny]

    @action(methods=['GET'], detail=False)
    def descending(self, request):
        """
            RETURN the polygons from the DB, in descending order,
            by number of sides.
            For each polygon include its name and number of sides.
        """
        polygons_desc = self.queryset.order_by('-num_sides')
        
        return Response(status=status.HTTP_200_OK, data=DescPolygonsSerializer(polygons_desc, many=True).data)

    @action(methods=['POST'], detail=False)
    def total_sides(self, request):
        """
            GIVEN a list of polygon names present in field "to_sum",
            RETURN a number, the sum of number of sides for all polygons in the list 
        """
        polygons = self.queryset.filter(name__in=request.data.get('to_sum', []))
        sides_sum = polygons.aggregate(sides_sum=Sum('num_sides', default=0))['sides_sum']
        
        return Response(status=status.HTTP_200_OK, data=sides_sum)
