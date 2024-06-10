from django.http import JsonResponse
from place.models import Place


def get_image(image):
	try:
		return image.url
	except Exception as e:
		print(e)
		return
	
def places(request):
	data = [
        {
            'id': i.pk,
            'is_root_node': i.is_root_node(),
            'is_leaf_node': i.is_leaf_node(),
            'name': i.name,
            'parent': i.parent.pk if i.parent else None,
            'type_place': i.type_place,
            'show': i.show,
            'first_order': i.first_order,
            'pub_date': i.pub_date,
            'image_description': get_image(i.image_description),
            'description': i.description,
            'photo':[{'name': i.name, 'image': get_image(i.image)} for i in i.photo.all()]
        } for i in Place.objects.filter(show=True).prefetch_related('photo')
	]
	return JsonResponse(data, safe=False)