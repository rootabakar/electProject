from django.urls import path

import core.views
from core.views import *


handler403 = 'core.views.error_403_view'


urlpatterns = [
    path("", index, name="index"),
    path("creation/", creation_utilisateur, name="creation_utilisateur"),
    path("gestion/", gestion_utilisateur, name="gestion_utilisateur"),
    path("detail/<int:id>", detail_utilisateur, name="detail_utilisateur"),
    path("reclamation/<int:id>", reclamation_view, name="reclamation"),
    path("cours/", cours, name="cours"),
    path("cours/supprimer/<int:id_supp>", supp_cours, name="supp_cours"),
    path("cours/modifier/<int:id>", alter_cours, name="alter_cours"),
    path("heure/", gestion_heure, name="heure"),
    path("heure/alter/<int:id>", alter_heure, name="alter_heure"),
    path("heure/supprimer/<int:id>", supp_heure, name="supprimer_heure"),
    path("presence/", presence, name="presence"),
]



