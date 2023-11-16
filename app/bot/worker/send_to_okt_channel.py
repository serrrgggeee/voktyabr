from article.models import Article
from bot.send_to_bot import send_to_telegram, check_sending_time


def sendPvesti():
	articles = Article.objects.filter(site_sighn='pvesti').exclude(send_to__contains=["pvesti"])
	if not check_sending_time(): return
	if check_sending_time() == 'late':
		for article in articles:
			article.send_to.append('pvesti')
			article.save()
		return
	article = articles.order_by('-id').first()
	chatID = 'basket_october'
	send_to_telegram(article.description, chatID)
	article.send_to.append('pvesti')
	article.save()


def sendRiac34():
	articles = Article.objects.filter(site_sighn='riac34').exclude(send_to__contains=["riac34"])
	if check_sending_time() == 'late':
		for article in articles:
			article.send_to.append('riac34')
			article.save()
		return
	article = articles.order_by('-id').first()
	chatID = 'basket_october'
	send_to_telegram(article.description, chatID)
	article.send_to.append('riac34')
	article.save()