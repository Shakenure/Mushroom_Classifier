from django.shortcuts import render
from django.http import HttpResponse
import os
from .predictNB import calcProbFactor, edibility
from .kmeans import main
import matplotlib.pyplot as plt

# Create your views here.

def home(request):
    return render(request, 'home.html')

def naiveBayes(request):
    return render(request, 'naiveBayes.html')

def trainNB(request):
	os.system('python mushroom/trainNaiveBayes.py')
	return HttpResponse("Training Data...")

def kmeans(request):
	return render(request, 'kmeans.html')

def chart(request):
	return render(request, 'chart.html')

def predictKM(request):
	value1 = request.GET.get('attr1', False) 
	value2 = request.GET.get('attr2', False) 
	value3 = request.GET.get('attr3', False) 
	value4 = request.GET.get('attr4', False) 
	main(int(value1), int(value2), int(value3), int(value4))
	return render(request, 'chart.html')
	#return HttpResponse(value1)

def predictNB(request):
	columns = ["CapShape", "CapSurface",
		"CapColor", "Bruises", "Odor",
		"GillAttachment", "GillSpacing", "GillSize",
		"GillColor", "StalkShape", "StalkRoot",
		"StalkSurfaceAboveRing", "StalkSurfaceBelowRing", "StalkColorAboveRing",
		"StalkColorBelowRing", "VeilType", "VeilColor",
		"RingNumber", "RingType", "SporePrintColor",
		"Population", "Habitat"
	]
	selected = {}

	for col in columns:
		value = request.GET.get(col, False) 
		if(value!='Select'):
		    selected[col] = value
			
	edible, poisonous, result = calcProbFactor(selected)
	plt.plot(edible, label='Edible')
	plt.plot(poisonous, label='Poisonous')
	plt.xlabel('Attributes')
	plt.ylabel('Posteriori Probability Factor')
	plt.legend(['Edible', 'Poisonous'])
	plt.savefig('Resources/chart.png')
	plt.close()


	return HttpResponse(result+"<a href='/chart'>SEE RESULTS</a>")