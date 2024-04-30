from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name="main"
urlpatterns = [
        path("",views.index,name="index"),
        path("category-quote/<int:cat_id>/",views.cat_detail,name="cat_detail"),
        path("quote-detail/<int:q_id>/",views.quote,name="quote"),
        path("favorite/",TemplateView.as_view(template_name="fav.html"),name="fav"),
        ]
