from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . import models
from .forms import AlbumForm, CustomUserCreationForm

# Create your views here.
def inicio(req):
    if not req.user.is_authenticated:
        return render(req, 'landing.html')
    albums = models.Album.objects.all()
    return render(req, 'inicio.html', {'albums': albums})

@login_required
def profile(req):
    user_profile, created = models.UserProfile.objects.get_or_create(user=req.user)
    user_albums = models.Album.objects.filter(user=req.user)
    return render(req, 'profile.html', {'user_profile': user_profile, 'user_albums': user_albums})

@login_required
def postar(req):
    if req.method == "POST":
        form = AlbumForm(req.POST, req.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = req.user
            album.save()
            messages.success(req, 'Album added successfully!')
            return redirect("inicio")
    else:
        form = AlbumForm()

    return render(req, "postar.html", {"formulario": form})

@login_required
def editar_album(req, album_id):
    album = get_object_or_404(models.Album, id=album_id, user=req.user)
    if req.method == "POST":
        form = AlbumForm(req.POST, req.FILES, instance=album)
        if form.is_valid():
            form.save()
            messages.success(req, 'Album updated successfully!')
            return redirect("inicio")
    else:
        form = AlbumForm(instance=album)

    return render(req, "editar_album.html", {"formulario": form, "album": album})

@login_required
def deletar_album(req, album_id):
    album = get_object_or_404(models.Album, id=album_id, user=req.user)
    if req.method == "POST":
        album.delete()
        messages.success(req, 'Album deleted successfully!')
        return redirect("inicio")
    return render(req, "deletar_album.html", {"album": album})

def album_detail(req, album_id):
    album = get_object_or_404(models.Album, id=album_id)
    return render(req, 'album_detail.html', {'album': album})

def albums(req):
    albums = models.Album.objects.all().order_by('-id')  # Most recent first
    return render(req, 'albums.html', {'albums': albums})

def register(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            models.UserProfile.objects.create(user=user)  # Create profile
            login(req, user)
            messages.success(req, 'Registration successful!')
            return redirect('postar')
    else:
        form = CustomUserCreationForm()
    return render(req, 'register.html', {'form': form})
