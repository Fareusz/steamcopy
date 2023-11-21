from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, Review, Game_tags, Cart
from users.models import library, profile
from .forms import ReviewForm, SearchForm
from users.views import getcart

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
    cart = getcart(request)
    if game not in cart.games.all():
        cart.games.add(game)



    # if game not in library.objects.get(profile=Profile).games.all():
    #     library.objects.get(profile=Profile).games.add(game)
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
    
    cart = getcart(request)
    return render(request, 'rate_game.html', {'game': game, 'form': form, 'cart': cart})

def search(request):
    games = Game.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['publisher']:
            print(games)
            games = games.filter(publisher=form.cleaned_data['publisher'])
        if form.cleaned_data['developer']:
            games = games.filter(developer=form.cleaned_data['developer'])
        selected_tags = form.cleaned_data['tags']
        if selected_tags:
            games_with_tags = Game_tags.objects.filter(tags__in=selected_tags).distinct()
            games = Game.objects.filter(game_tags__in=games_with_tags).distinct()
        print(form.errors)
        print(games)
    
    cart = getcart(request)
    return render(request, 'search.html', {'form': form, 'games': games, 'cart': cart})

def cart_view(request):
    cart = getcart(request)
    total = float(0.00)
    for game in cart.games.all():
        total += game.price
    return render(request, 'cart.html', {'cart': cart, 'total': total})

def remove_from_cart_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart = getcart(request)

    if game in cart.games.all():
        cart.games.remove(game)

    return redirect('cart')

def homestore(request):
    games = Game.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'homestore.html', {'games': games})
    Profile = profile.objects.get(user=request.user)
    ownedgames = library.objects.get(profile=Profile).games.all()
    cart = getcart(request)
    return render(request, 'homestore.html', {'games': games, 'ownedgames': ownedgames, 'cart': cart})

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
    cart = getcart(request)
    return render(request, 'game_detail.html', {'game': game, 'cart': cart, "positivereviews": positivereviews, "negativereviews": negativereviews, "positivereviews_count": positivereviews_count, "negativereviews_count": negativereviews_count, "ownedgames": ownedgames})


