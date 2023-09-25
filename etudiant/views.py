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
        form = ReclamationForm(request.POST, request.FILES)
        if form.is_valid():
            id_user = request.user.id
            etudiant = ProfileEtudiant.objects.get(user_id=id_user)
            form.instance.etudiant = etudiant
            form.save()
            form = ReclamationForm()
            done = "Reclamation envoye"
            return render(request, 'etudiant/ajouter.html', locals())
        else:
            err = "ERRRRRRR"
            return render(request, 'etudiant/ajouter.html', locals())
    else:
        form = ReclamationForm()
    return render(request, 'etudiant/ajouter.html', locals())


@login_required
def supprimer(request, id):
    reclamation = Reclamation.objects.get(id=id)
    reclamation.delete()
    done_sup = "Reclamation supprimer avec succes !"
    return redirect("index_etudiant")


def modifier(request, id):
    reclamation = Reclamation.objects.get(id=id)
    if request.method == 'POST':
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid():
            reclamation.save()
            done = "Element modifier avec succes"
            return render(request, 'etudiant/modifier.html', locals())
        else:
            err = "ERR LORS DE LA MODIFICATION"
    return render(request, 'etudiant/modifier.html', locals())
