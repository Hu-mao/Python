from flask import Flask, render_template

app = Flask(__name__)

categories = [
    {"id": "all", "name": "Всі фрукти", "icon": "🍎", "count": 24},
    {"id": "berries", "name": "Ягоди", "icon": "🫐", "count": 5},
    {"id": "citrus", "name": "Цитрусові", "icon": "🍊", "count": 4},
    {"id": "stone", "name": "Кісточкові", "icon": "🍑", "count": 3},
    {"id": "tropical", "name": "Тропічні", "icon": "🍍", "count": 6},
    {"id": "apple", "name": "Яблука та груші", "icon": "🍎", "count": 6},
]

products = [
    {
        "name": "Банани",
        "price": 45,
        "rating": 4.8,
        "reviews": 124,
        "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=300&q=80"
    },
    {
        "name": "Яблука",
        "price": 35,
        "rating": 4.7,
        "reviews": 98,
        "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300&q=80"
    },
    {
        "name": "Апельсини",
        "price": 55,
        "rating": 4.9,
        "reviews": 156,
        "image": "https://images.unsplash.com/photo-1547514701-42782101795e?w=300&q=80"
    },
    {
        "name": "Полуниця",
        "price": 120,
        "rating": 4.9,
        "reviews": 203,
        "image": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=300&q=80"
    },
    {
        "name": "Чорниця",
        "price": 150,
        "rating": 4.8,
        "reviews": 87,
        "image": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=300&q=80"
    },
    {
        "name": "Виноград",
        "price": 95,
        "rating": 4.6,
        "reviews": 64,
        "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?w=300&q=80"
    },
    {
        "name": "Ківі",
        "price": 80,
        "rating": 4.7,
        "reviews": 112,
        "image": "https://images.unsplash.com/photo-1585059895524-72359e06133a?w=300&q=80"
    },
    {
        "name": "Манго",
        "price": 140,
        "rating": 4.9,
        "reviews": 145,
        "image": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=300&q=80"
    }
]


@app.route("/")
def home():
    return render_template(
        "layout.html",
        categories=categories,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)