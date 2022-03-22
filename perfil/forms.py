from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=35)
    director = forms.CharField(max_length=30)
    length_minutes = forms.IntegerField()
    gender = forms.CharField(max_length=20)
    


class SearchMovie(forms.Form):
    title = forms.CharField(max_length=35)
    director = forms.CharField(max_length=30)
    

class SerieForm(forms.Form):
    title = forms.CharField(max_length=35)
    director = forms.CharField(max_length=30)
    length_minutes = forms.IntegerField()
    gender = forms.CharField(max_length=20)
    seasons = forms.IntegerField()
    
    
class SearchSerie(forms.Form):
    title = forms.CharField(max_length=35)
    director = forms.CharField(max_length=30)
    

class SongForm(forms.Form):
    title = forms.CharField(max_length=35)
    artist = forms.CharField(max_length=30)
    length_minutes = forms.IntegerField()
    gender = forms.CharField(max_length=20)
    
    
class SearchSong(forms.Form):
    title = forms.CharField(max_length=35)
    artist = forms.CharField(max_length=30)