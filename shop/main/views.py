import json
from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Card
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from main.user_service import UserService


cards = [
    {
        'image': 'main/images/dj.png',
        'title': 'django',
        'text': 'Some quick example text to build on the card title.',
        'button': 'Go somewhere'
    },
    {
        'image': 'main/images/dj2.jpg',
        'title': 'hmmmm',
        'text': 'hmmmmmmmmmmmmmmmm',
        'button': 'Go somewhere'
    },
    {
        'image': 'main/images/dj3.jpg',
        'title': 'human&django',
        'text': 'Someone talking about django',
        'button': 'Go somewhere'
    }
]


def home(request):
    db_cards = Card.objects.all().prefetch_related('tags')

    return render(request, 'main/index.html', {
        'cards': cards,
        'db_cards': db_cards
    })

def about(request):
    return render(request, 'main/about.html')


def search(request):
    title = request.GET.get('title', '').strip()

    for card in cards:
        if card['title'].lower() == title.lower():
            return render(request, 'main/search.html', {'card': card})

    return render(request, 'main/not_found.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'main/register.html')

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@require_POST

@require_POST
def register_data(request):
    try:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        avatar = request.FILES.get('avatar')

        if not name or not email or not phone:
            return JsonResponse({
                'success': False,
                'message': 'Заповніть усі обов’язкові поля'
            }, status=400)

        if UserService.get_all_users().filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'message': 'Користувач із таким email вже існує'
            }, status=400)

        user = UserService.create_user(
            name=name,
            email=email,
            phone=phone,
            avatar=avatar
        )

        return JsonResponse({
            'success': True,
            'message': 'Реєстрація успішна!',
            'user_id': user.id
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm()

    return render(request, 'main/create_card.html', {
        'form': form
    })