from libraries.models import Library
from django.shortcuts import render_to_response 
    
def map(request):
	libs = Library.objects.all()
	count = libs.count()
	return render_to_response("libraries-map.html", { "libs": libs, "count": count })	
