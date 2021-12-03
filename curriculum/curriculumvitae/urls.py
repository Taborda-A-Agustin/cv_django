from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
    path("create-cv", views.cv_create, name="cv_create"),
        path("update-cv/<int:pk>", views.cv_update, name="cv_update"),
    path("thanks/", views.thanks, name="thanks"),

]