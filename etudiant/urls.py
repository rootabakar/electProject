from django.conf.urls.static import static
from django.urls import path

from electProject import settings
from etudiant.views import *

urlpatterns = [
    path("", index, name="index_etudiant"),
    path('ajout/', ajouter, name="ajouter"),
    path('supprimer/<int:id>/', supprimer, name="supprimer"),
    path('modifier/<int:id>/', modifier, name="modifier"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



