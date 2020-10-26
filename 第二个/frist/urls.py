from django.urls import path
from frist import views


urlpatterns=[
	path('',views.f1)
	,path('a/',views.f2)
]