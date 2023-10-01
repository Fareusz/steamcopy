from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, Review
from users.models import library, profile
from .forms import ReviewForm

# Create your views here.
@login_required
def remove_game(request, game_id):
    Profile = get_object_or_404(profile, user=request.user)
    game = get_object_or_404(Game, id=game_id)

    if game in library.objects.get(profile=Profile).games.all():
        library.objects.get(profile=Profile).games.remove(game)
    return redirect('homestore')

@login_required
def add_game(request, game_id):
    Profile = get_object_or_404(profile, user=request.user)
    game = get_object_or_404(Game, id=game_id)

    if game not in library.objects.get(profile=Profile).games.all():
        library.objects.get(profile=Profile).games.add(game)
    return redirect('homestore')

@login_required
def rate_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.author = get_object_or_404(profile, user=request.user)
            review.save()   
            return redirect('game', game_id=game.id)
    else:
        form = ReviewForm()
    
    return render(request, 'rate_game.html', {'game': game, 'form': form})


def homestore(request):
    games = Game.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'homestore.html', {'games': games})
    Profile = profile.objects.get(user=request.user)
    ownedgames = library.objects.get(profile=Profile).games.all()
    return render(request, 'homestore.html', {'games': games, 'ownedgames': ownedgames})

def game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    try: 
        positivereviews = Review.objects.filter(game=game, rating=True)
    except Review.DoesNotExist:
        positivereviews = None
    try: 
        negativereviews = Review.objects.filter(game=game, rating=False)
    except Review.DoesNotExist:
        negativereviews = None
    positivereviews_count = Review.objects.filter(game=game, rating=True).count()
    negativereviews_count = Review.objects.filter(game=game, rating=False).count()
    Profile = profile.objects.get(user=request.user)
    ownedgames = library.objects.get(profile=Profile).games.all()
    return render(request, 'game_detail.html', {'game': game, "positivereviews": positivereviews, "negativereviews": negativereviews, "positivereviews_count": positivereviews_count, "negativereviews_count": negativereviews_count, "ownedgames": ownedgames})