from django.urls import path
from .views import PUResults, LGAResults
from .main_view import poll_results, lga_results

urlpatterns = [
    path("", poll_results, name="poll_results"),
    path("lga-results", lga_results, name="lga_results"),
    path("polling-result/", PUResults.as_view(), name="pu_results"),
    path("lga-result/", LGAResults.as_view(), name="lga_result"),
    
]