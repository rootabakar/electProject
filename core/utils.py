from core.models import ProfileEtudiant, Presence


def add_presence(id_empreinte, heure, etat=False):
    id = int(id_empreinte)
    etudiant = ProfileEtudiant.objects.get(id_empeinte=id)
    if etat:
        Presence.objects.create(nom=etudiant.nom, prenom=etudiant.prenom, heure=heure, etudiant=etudiant, etat="Present")
    else:
        Presence.objects.create(nom=etudiant.nom, prenom=etudiant.prenom, heure=heure, etudiant=etudiant, etat="Absent")
