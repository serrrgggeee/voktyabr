from django.http import JsonResponse

def generate_years(request, id):
	years = [2019, 2018, 2017, 2016, 2015]
	return JsonResponse({'years':years})