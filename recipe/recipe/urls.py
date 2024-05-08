
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.recipes,name="home"),
    path("add_recipe/",views.addRecipe,name="add_recipe"),
    path("remove_recipe/<int:pk>/",views.removeRecipe,name='remove_recipe'),
    path("update_recipe/<int:pk>/",views.updateRecipe,name="update_recipe")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()