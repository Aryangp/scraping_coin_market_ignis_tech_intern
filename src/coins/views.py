from django.http import JsonResponse
from .tasks import scrape_coin_data
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data



# this just a test view i created to check if i configured everything correctly
def scrape_view(request):
    result = scrape_coin_data.delay()
    return JsonResponse({"task_id": result.id})


"""
This is main class view that is used to start the scraping of the coins and also to get the status of the scraping  
"""

class CoinMarketCapView(APIView):
    def post(self, request, format=None):
        coins = request.data.get('coins', [])  # Assuming the coins are sent as a list in the request body
        job_ids = []
        for coin in coins:
            if coin == "GORILLA":
                coin = "gorilla-token"
            elif coin == "NOT":
                coin = "notcoin"    
            job = Job.objects.create()
            scrape_coin_data.delay(job_id=str(job.job_id), coinNeed=coin)
            job_ids.append(str(job.job_id))
        return Response({'job_ids': job_ids}, status=status.HTTP_200_OK)

    def get(self, request,job_id,format=None):
        try:
            job = Job.objects.get(pk=job_id)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)