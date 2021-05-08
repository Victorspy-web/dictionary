from django.urls import path
from .views import index, word


urlpatterns = [
	path('', index, name='home'),
	path('word/', word, name='word')
]


