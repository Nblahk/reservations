from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.conf import settings 
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test 

from catalogue.forms.ArtistForm import ArtistForm 
from catalogue.models import Artist, Troupe

# Vérifie un super-user (exemple personnalisé)
def admin_check(user):
    return user.is_superuser

def index(request):
    artists = Artist.objects.all()
    title = 'Liste des artistes'
    return render(request, 'artist/index.html', {
        'artists': artists,
        'title': title,
    })

def show(request, artist_id):
    # Récupère l'artiste ou 404
    artist = get_object_or_404(Artist, id=artist_id)
    title = "Fiche d'un artiste"

    # Si on reçoit un POST, on tente de mettre à jour l'affiliation
    if request.method == 'POST':
        # Seul le super-user peut modifier
        if not request.user.is_superuser:
            messages.error(request, "Vous n'avez pas la permission de modifier l'affiliation.")
            return redirect('catalogue:artist_show', artist_id=artist.id)

        # Récupère l'ID de la troupe sélectionnée (vide => non affilié)
        troupe_pk = request.POST.get('troupe')
        if troupe_pk:
            artist.troupe_id = troupe_pk
        else:
            artist.troupe = None
        artist.save()
        messages.success(request, "Affiliation mise à jour avec succès.")
        return redirect('catalogue:artist_show', artist_id=artist.id)

    # Pour l'affichage GET, on fournit la liste des troupes au template
    troupes = Troupe.objects.all()
    return render(request, 'artist/show.html', {
        'artist': artist,
        'title': title,
        'troupes': troupes,
    })

@user_passes_test(admin_check)
@login_required(login_url=settings.LOGIN_URL)
@permission_required('catalogue.add_artist', raise_exception=True)
def create(request):
    form = ArtistForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Nouvel artiste créé avec succès.")
            return redirect('catalogue:artist_index')
        else:
            messages.error(request, "Échec de l'ajout d'un nouvel artiste !")
    return render(request, 'artist/create.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('catalogue.add_artist', raise_exception=True)
def delete(request, artist_id): 
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == "POST":
        artist.delete()
        messages.success(request, "Artiste supprimé avec succès.")
        return redirect('catalogue:artist_index')
    messages.error(request, "Échec de la suppression de l'artiste !")
    return render(request, 'artist/show.html', {'artist': artist})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('catalogue.add_artist', raise_exception=True)
def edit(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    form = ArtistForm(request.POST or None, instance=artist)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Artiste modifié avec succès.")
            return redirect('catalogue:artist_show', artist_id=artist.id)
        else:    
            messages.error(request, "Échec de la modification de l'artiste !")    
    return render(request, 'artist/edit.html', {
        'form': form,
        'artist': artist,
    })
