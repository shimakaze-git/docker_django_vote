from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import IndexView


app_name = 'base_site'
urlpatterns = [
    path('', IndexView.as_view(), name="index")

    # 60*15 = 900 second = 15 min
    # path('', cache_page(60 * 15)(views.index), name='index'),
]
