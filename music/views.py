from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album,Song
from django.views.generic import ListView,DetailView

def index(Request):
    all_alb=Album.objects.all()
    
    context={'all_alb':all_alb}
    return render(Request , 'music/index.html',context)


def details(Request,album_id):
    #instead of using try except statement ,django gives this shortcut
    alb=get_object_or_404(Album,pk=album_id)
    return render(Request,'music/details.html',{'alb':alb})

def favorite(request,album_id):
    alb = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=alb.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request , 'music/details.html',{'alb':alb,'error_message':"song does not exist",})
    else:
        if selected_song.is_favorite==False:
            selected_song.is_favorite=True
            selected_song.save()
            return render(request, 'music/details.html', {'alb': alb})
        else:
            if selected_song.is_favorite:
                selected_song.is_favorite = False
                selected_song.save()
                return render(request, 'music/details.html', {'alb': alb})
#above was the way of writing views as function..but django provide us easy way by generic views

"""class IndexView(ListView):  #it inherits from listview class
    template_name='music/index.html'  #it tells that we have to use this template
    context_object_name='all_alb'#get query set function will give automatic name to the list as'object_list'. so to change it to other name we do this
    def get_queryset(self):
        return Album.objects.all()     #it  tells what object list to operate on

class DetailView(DetailView):
    template_name='music/details.html'
    model=Album        #it tells what model are we operating on"""