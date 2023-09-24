from django.urls import path
from core.views import *

urlpatterns = [
    path("", index, name="index"),
    path("creation/", creation_utilisateur, name="creation_utilisateur"),
    path("gestion/", gestion_utilisateur, name="gestion_utilisateur"),
    path("detail/<int:id>", detail_utilisateur, name="detail_utilisateur"),
    path("reclamation/<int:id>", reclamation_view, name="reclamation"),
    path("cours/", cours, name="cours")
]



