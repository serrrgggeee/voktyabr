from rest_framework.serializers import ModelSerializer
from article.models import Article

class ArticleSerializer(ModelSerializer):
	class Meta:
		model = Article
		fields = ('pk', 'name','description', 'show',)