from article.models import Article
from bot.send_to_bot import send_to_telegram, check_sending_time


def sendPvestiToAvosyka():
	articles = Article.objects.filter(site_sighn='pvesti').exclude(send_to__contains=["pvesti_avosyka"])
	if not check_sending_time(): return
	if check_sending_time() == 'late':
		for article in articles:
			article.send_to.append('pvesti')
			article.save()
		return
	chatID = 'avoska_october'
	article = articles.order_by('-id').first()
	send_to_telegram(article.description, chatID)
	article.send_to.append('pvesti_avosyka')
	article.save()


def sendRiac34ToAvosyka():
	articles = Article.objects.filter(site_sighn='riac34').exclude(send_to__contains=["riac34_avosyka"])
	if not check_sending_time(): return
	if check_sending_time() == 'late':
		for article in articles:
			article.send_to.append('pvesti')
			article.save()
		return
	chatID = 'avoska_october'
	article = articles.order_by('-id').first()
	send_to_telegram(article.description, chatID)
	article.send_to.append('riac34_avosyka')
	article.save()


def sendPikabuToAvosyka():
	articles = Article.objects.filter(site_sighn='pikabu').exclude(send_to__contains=["pikabu"]).order_by('-id')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('pikabu')
		article.save()


def sendAvitoToAvosyka():
	articles = Article.objects.filter(site_sighn='avito').exclude(send_to__contains=["avito"]).order_by('?')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('avito')
		article.save()


def sendOlanToAvosyka():
	articles = Article.objects.filter(site_sighn='olan_avito').exclude(send_to__contains=["olan_avito"]).order_by('-id')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('olan_avito')
		article.save()


def sendPinterestToAvosyka():
	articles = Article.objects.filter(site_sighn='pinterest_okt').exclude(send_to__contains=["pinterest_okt"]).order_by('-id')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('pinterest_okt')
		article.save()


def sendKuplusrazuToAvosyka():
	articles = Article.objects.filter(site_sighn='kuplusrazu_okt').exclude(send_to__contains=["kuplusrazu_okt"]).order_by('-id')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('kuplusrazu_okt')
		article.save()


def sendCianToAvosyka():
	articles = Article.objects.filter(site_sighn='cian_okt').exclude(send_to__contains=["cian_okt_avosyka"]).order_by('-id')[:1]
	for article in articles:
		chatID = 'avoska_october'
		send_to_telegram(article.description, chatID)
		article.send_to.append('cian_okt_avosyka')
		article.save()

