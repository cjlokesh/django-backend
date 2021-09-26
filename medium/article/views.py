from django.shortcuts import render
#Request object that extends the regular HttpRequest, and provides more flexible request parsing
from rest_framework.response import Response 
# REST framework provides an APIView class, which subclasses Django's View class.

# APIView classes are different from regular View classes in the following ways:
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # print("articles[0]", )
        print('type articles', type(articles))
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        print("post req")
        # article = request.data.get('article')
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        # return Response({"success": "Article '{}' created successfully".format(article_saved.title)})