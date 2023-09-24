from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from core.forms import UserForm, CoursForm
from core.models import User, ProfileEtudiant, Reclamation, Cours

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
        id_empreinte = request.POST.get("id_empeinte")
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
            ProfileEtudiant.objects.create(
                nom=last_name,
                prenom=first_name,
                email=email,
                classe="",
                id_empeinte=20,
                user=user_create
            )
            if user_create:
                done = "Utilisateur creer avec succes !"
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
    return render(request, 'core/connexion.html', locals())


def cours(request):
    if request.method == 'POST':
        nom = request.POST.get("nom_cours")
        Cours.objects.create(nom_cours=nom)
        cours = Cours.objects.all()
        done = "Cours ajouter avec succes !"
    else:
        form = CoursForm()
    return render(request, 'core/cours.html', locals())
