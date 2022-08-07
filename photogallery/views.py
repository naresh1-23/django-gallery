from django.shortcuts import render, redirect
from .forms import albumform
from .models import Album, Photos
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_authenticated:
        albums = Album.objects.filter(author=request.user)
        return render(request, 'photogallery/home.html', {'albums': albums})
    else:
        return render(request, 'photogallery/home.html')

@login_required
def album(request):
    if request.method == 'POST':
        form = albumform(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = albumform()
    return render(request, 'photogallery/create_album.html', { 'form': form })

@login_required
def addphoto(request):
    albums = Album.objects.filter(author = request.user)
    if request.method == 'POST':
        name = request.POST['name']
        pic = request.FILES['photofile']
        albumname = Album.objects.get(album_name = request.POST['albumname'])
        photosave = Photos(photoname = name, photo = pic,album = albumname)
        photosave.save()
        return redirect('home')
    return render(request, 'photogallery/addphoto.html', {'albums': albums})

def soloalbum(request, id):
    album_id = id
    album = Album.objects.filter(id = album_id).first()
    photos = Photos.objects.filter(album = album)
    return render(request, 'photogallery/album.html', {'photos': photos})