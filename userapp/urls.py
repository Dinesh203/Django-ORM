from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("Show/", views.show, name="Showpage"),
    path("showdata/<int:id>", views.showdata, name="Showdata"),
    path("show/<int:id>", views.showcomp, name="showcomp"),
    path("responce/", views.responce, name="responce_exception")

]

# path("showemp/<id>", views.showemp, name="showemp"),