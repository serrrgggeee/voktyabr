from article.models import Article
from django.conf import settings
from vk.send_to_vk_group import send_to_vk_group, check_time



def sendAvitoToOktyabrskiyRayon():
	if not check_time(): return
	articles = Article.objects.filter(site_sighn='avito').exclude(send_to__contains=["oktyabrskiy_rayon_avito"]).order_by('-id')[:1]
	for article in articles:
		send_to_vk_group(article.description, settings.CHAT_OKTOBER_ID_VK)
		article.send_to.append('oktyabrskiy_rayon_avito')
		article.save()


def sendPvestiToOktyabrskiyRayon():
	if not check_time(): return
	articles = Article.objects.filter(site_sighn='pvesti').exclude(send_to__contains=["oktyabrskiy_rayon_pvesti"]).order_by('-id')[:1]
	for article in articles:
		send_to_vk_group(article.description.replace("http","https"), settings.CHAT_OKTOBER_ID_VK)
		article.send_to.append('oktyabrskiy_rayon_pvesti')
		article.save()


def sendPinterestToOktyabrskiyRayon():
	if not check_time(): return
	articles = Article.objects.filter(site_sighn='cian_okt').exclude(send_to__contains=["avosika_cian_okt"]).order_by('-id')[:1]
	for article in articles:
		send_to_vk_group(article.description, settings.CHAT_OKTOBER_ID_VK)
		article.send_to.append('avosika_cian_okt')
		article.save()

