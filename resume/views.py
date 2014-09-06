from django.shortcuts import render
from resume.models import Bio

# Create your views here.

def index(request):
	bio = Bio.objects.filter()
	return render(request, 'resume/index.html', {'bio':bio})