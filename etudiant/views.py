from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import ProfileEtudiant, Reclamation
from etudiant.forms import ReclamationForm


@login_required
def index(request):
    user_id = int (request.user.id)
    etudiant = ProfileEtudiant.objects.get(user_id=user_id)
    reclamations = Reclamation.objects.filter(etudiant=etudiant)
    return render(request, 'etudiant/index.html', locals())


@login_required
def ajouter(request):
    if request.method == 'POST':
        motif = request.POST.get('motif')
        cours = request.POST.get('cours')
        preuve = request.FILES.get('preuve')
        id_user = request.user.id
        id_conv = int(id_user)
        etudiant = ProfileEtudiant.objects.get(user_id=id_conv)
        reclamation = Reclamation.objects.create(
            motif=motif,
            preuve=preuve,
            etudiant=etudiant,
            cours=cours
        )
        if reclamation:
            done = "Reclamation envoye"
        else:
            err = "ERRRRRRR"
    return render(request, 'etudiant/ajouter.html', locals())


@login_required
def supprimer(request, id):
    reclamation = Reclamation.objects.get(id=id)
    reclamation.delete()
    done_sup = "Reclamation supprimer avec succes !"
    return redirect("index_etudiant")
