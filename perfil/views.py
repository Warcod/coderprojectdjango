from turtle import title
from django.shortcuts import render
from .models import Movies , Series, Songs 
from .forms import MovieForm, SearchSerie, SerieForm, SongForm, forms , SearchMovie

# Create your views here.

def movies(request):
  
    movies = Movies.objects.filter(title__icontains='')
    
    return render(request, 'perfil/movies.html', {'movies' : movies})


def formMovie(request):
    
    if request.method == 'POST':
        
        myForm = MovieForm(request.POST)
        
        if myForm.is_valid():
            
            data = myForm.cleaned_data
            
            movie = Movies(title = data['title'], 
                            director = data['director'],
                            length_minutes = data['length_minutes'],
                            gender = data['gender']
                            )
            
            movie.save()   
        
            mynewForm = MovieForm()
        
            return render(request, 'perfil/formMovie.html', {'myForm' : mynewForm}) 
   
    else:
        myForm = MovieForm()
    
    return render(request, 'perfil/formMovie.html', {'myForm' : myForm})


def searchMovies(request):
    
    if request.GET.get('title'):
        
        title = request.GET.get('title')
        
        movies = Movies.objects.filter(title__icontains=title)

        return render(request, 'perfil/searchMovie.html', {'movies' : movies})
    
    else:
        
        myForm = SearchMovie()
          
    return render(request, 'perfil/searchMovie.html', {'myForm' : myForm})

        


def series(request):
      
    series = Series.objects.filter(title__icontains='')
    
    return render(request, 'perfil/series.html', {'series' : series})



def formSeries(request):
    
    if request.method == 'POST':
        
        myForm = SerieForm(request.POST)
        
        if myForm.is_valid():
            
            data = myForm.cleaned_data
            
            serie = Series(title = data['title'], 
                            director = data['director'],
                            length_minutes = data['length_minutes'],
                            gender = data['gender'],
                            seasons = data['seasons']
                            )
            
            serie.save()   
            
            mynewForm = SerieForm()
        
            return render(request, 'perfil/formSerie.html', {'myForm' : mynewForm}) 
   
    else:
        myForm = SerieForm()
    
    return render(request, 'perfil/formSerie.html', {'myForm' : myForm})


def searchSeries(request):
    
    if request.GET.get('title'):
        
        title = request.GET.get('title')
        
        series = Series.objects.filter(title__icontains=title)

        return render(request, 'perfil/searchSerie.html', {'series' : series})
    
    else:
        
        myForm = SearchSerie()
          
    return render(request, 'perfil/searchSerie.html', {'myForm' : myForm})




def songs(request):
    
    songs = Songs.objects.filter(title__icontains='')
    
    return render(request, 'perfil/songs.html', {'songs' : songs})


def formSongs(request):
    
    if request.method == 'POST':
        
        myForm = SongForm(request.POST)
        
        if myForm.is_valid():
            
            data = myForm.cleaned_data
            
            song = Songs(title = data['title'], 
                            artist = data['artist'],
                            length_minutes = data['length_minutes'],
                            gender = data['gender']
                            )
            
            song.save()   
            
            mynewForm = SongForm()
        
            return render(request, 'perfil/formSong.html', {'myForm' : mynewForm}) 
   
    else:
        myForm = SongForm()
    
    return render(request, 'perfil/formSong.html', {'myForm' : myForm})



def searchSongs(request):
    
    if request.GET.get('title'):
        
        title = request.GET.get('title')
        
        songs = Songs.objects.filter(title__icontains=title)

        return render(request, 'perfil/searchSongs.html', {'songs' : songs})
    
    else:
        
        myForm = SongForm()
          
    return render(request, 'perfil/searchSongs.html', {'myForm' : myForm})