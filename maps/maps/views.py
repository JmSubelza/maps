from libraries.models import Library
from firestations.models import Station as FStation 
from policestations.models import Station as PStation
from django.shortcuts import render_to_response 
    
def map(request):
	libs = Library.objects.all()
	fstats = FStation.objects.all()
	pstats = PStation.objects.all()
	lcount = libs.count() 
	fcount = fstats.count() 
	pcount = pstats.count() 
	return render_to_response("all-map.html", { "libs": libs, "fstats": fstats, "pstats": pstats, "lcount": lcount, "pcount": pcount, "fcount": fcount })	
