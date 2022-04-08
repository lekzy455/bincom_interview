from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import AnnouncedPuResults, PollingUnit, Lga
from .serializers import PUSerializer, LgaSerializer

class PUResults(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        qs = AnnouncedPuResults.objects.filter(polling_unit_uniqueid="27")
        data = {
            "result": PUSerializer(qs, many=True).data
        }
        return Response(data)

class LGAResults(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        lga = request.GET.get("lga") or None
        total = 0
        lgas = Lga.objects.all()
        if lga:
            lga_id = Lga.objects.get(lga_name=lga)
            qs = PollingUnit.objects.filter(lga=lga_id.lga_id)
            for poll in qs:
                poll_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=str(poll.uniqueid))
                for results in poll_result:
                    print(results.party_score)
                    total += results.party_score
            
        data = {
            "results": total,
            "lgas": LgaSerializer(lgas[::-1], many=True).data,
            "lga": lga
        }

        return Response(data)