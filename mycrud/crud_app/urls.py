from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home, name='index'),
    path('blog/', views.postView, name='blog'),
    path('form/', views.blog_form, name="form"),
    path('blog/delete/<int:book_id>', views.delete_view, name="delete"),
    path('blog/update/<int:book_id>', views.edit_view, name='update'),
    path('fetch/', views.my_fetch_data, name="fetch"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)