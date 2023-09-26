from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from core.forms import UserForm, CoursForm, HeureForm
from core.models import User, ProfileEtudiant, Reclamation, Cours, Heure, Presence

Utilisateur = get_user_model()


def index(request):
    reclamations = Reclamation.objects.filter(etat="En cours")
    return render(request, 'core/index.html', locals())


def gestion_utilisateur(request):
    users = User.objects.all()
    return render(request, 'core/utilisateur.html', locals())


def creation_utilisateur(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        type_ = request.POST.get("type")
        password = request.POST.get("password")
        user_exist = User.objects.filter(email=email)
        if user_exist:
            err = "L'utilisateur existe deja"
        else:
            user_create = Utilisateur.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                type=type_,
                password=password
            )
            if type_ == "ETUDIANT":
                ProfileEtudiant.objects.create(
                    nom=last_name,
                    prenom=first_name,
                    email=email,
                    classe="",
                    id_empeinte=1,
                    user=user_create
                )
                if user_create:
                    done = "Utilisateur creer avec succes !"
            else:
                pass
    else:
        form = UserForm()
    return render(request, 'core/creation_utilisateur.html', locals())


def detail_utilisateur(request, id):
    user = User.objects.get(id=id)
    etudiant = ProfileEtudiant.objects.get(user_id=id)
    reclamations = Reclamation.objects.filter(etudiant=etudiant)
    return render(request, 'core/detail_utilisateur.html', locals())


def reclamation_view(request, id):
    valeur = request.POST.get("valeur")
    reclamation = Reclamation.objects.get(id=id)
    reclamation.etat = valeur
    reclamation.save()
    return redirect("index")


def connexion(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            if user.type == 'ETUDIANT':
                return redirect('/etudiant/')
            else:
                return redirect('/controller/')
        else:
            err = "ERR LORS DE LA CONNEXION"
            return render(request, 'core/connexion.html', locals())
    return render(request, 'core/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect('connexion')


def cours(request):
    cours = Cours.objects.all()
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            done = "Cours ajouter avec succes !"
            return render(request, 'core/cours.html', locals())
        else:
            err = "ERR LORS DE LA CREATION DU COURS "
            return render(request, 'core/cours.html', locals())
    else:
        form = CoursForm()
    return render(request, 'core/cours.html', locals())


def supp_cours(request, id_supp):
    id = int(id_supp)
    cours = Cours.objects.get(id=id)
    cours.delete()
    return redirect('cours')


def alter_cours(request, id):
    cours = Cours.objects.get(id=id)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            done = "Element modifier avec succes"
        else:
            err = "Err lors de la modification"
    else:
        form = CoursForm(instance=cours)
    return render(request, 'core/cours_alter.html', locals())


def gestion_heure(request):
    heures = Heure.objects.all()
    form = HeureForm()
    if request.method == 'POST':
        form = HeureForm(request.POST)
        if form.is_valid():
            form.save()
            done = "Element ajouter avec succes !"
            form = HeureForm()
            return render(request, 'core/heure.html', locals())
        else:
            err = "ERR LORS DE LA CREATION DE L'ELEMENT"
            return render(request, 'core/heure.html', locals())
    else:
        form = HeureForm()
    return render(request, 'core/heure.html', locals())


def alter_heure(request, id):
    heure = Heure.objects.get(id=id)
    if request.method == 'POST':
        form = HeureForm(request.POST, instance=heure)
        if form.is_valid():
            form.save()
            done = "Element modifier avec succes"
        else:
            err = "Err lors de la modification"
    else:
        form = HeureForm(instance=heure)
    return render(request, 'core/heure_alter.html', locals());


def supp_heure(request, id):
    Heure.objects.get(id=id).delete()
    return redirect('heure')


def prinpical(request):
    return render(request, 'core/principal.html', locals())


def presence(request):
    etudiants = ProfileEtudiant.objects.all()
    return render(request, 'core/liste_presence.html', locals())


def error_403_view(request, exception):
    return render(request, 'core/403.html', status=403)
