from policestations.models import Station 
from django.shortcuts import render_to_response 
    
def map(request):
	stats = Station.objects.all()
	count = stats.count()
	return render_to_response("policestations-map.html", { "stats": stats, "count": count })	
