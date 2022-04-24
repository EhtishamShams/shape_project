from rest_framework import viewsets
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Polygon
from .serializers import PolygonSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    permission_classes = [AllowAny]

    @action(methods=['GET'], detail=False)
    def descending(self, request):
        """
            TODO 
            RETURN the polygons from the DB, in descending order,
            by number of sides.
            For each polygon include its name and number of sides.

            - Don't import apps.polygons.constants
            - Don't write things like reverse(). Rather, do all the ordering while fetching DB results
        """
        
        return Response()

    @action(methods=['POST'], detail=False)
    def total_sides(self, request):
        """
            TODO
            GIVEN a list of polygon names present in field "to_sum",
            RETURN a number, the sum of number of sides for all polygons in the list 
        """
        
        return Response()
