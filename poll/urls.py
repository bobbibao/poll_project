
from django.urls import path
from . import views as poll_views
from .views import Login, Logout
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('results/', poll_views.results, name='results'),
    path('view-one-question/<poll_id>/', poll_views.view_one_question, name='view-one-question'),
    path('delete/<poll_id>/', poll_views.delete, name='delete'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(),name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
