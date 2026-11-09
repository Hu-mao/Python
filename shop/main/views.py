import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST


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
    return render(request, 'main/index.html', {'cards': cards})


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
def register_data(request):
    try:
        data = json.loads(request.body)

        name = data.get('name', '')
        email = data.get('email', '')
        phone = data.get('phone', '')

        print("\n===== Нова реєстрація =====")
        print(json.dumps(data, ensure_ascii=False, indent=4))
        print("===========================\n")

        return JsonResponse({
            'success': True,
            'message': 'Реєстрація успішна!'
        })

    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({
            'success': False,
            'message': 'Некоректний JSON'
        }, status=400)