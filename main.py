from flask import Flask, render_template

app = Flask(__name__)

games = [
    {
        "rank": 1,
        "name": "Counter-Strike 2",
        "company": "Valve",
        "category": "FPS",
        "price": "Free",
        "reviews": "92% positivas",
        "users": "1,200,000",
        "logo": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg"
    },
    {
        "rank": 2,
        "name": "Baldur’s Gate 3",
        "company": "Larian Studios",
        "category": "RPG",
        "price": "$59.99",
        "reviews": "96% positivas",
        "users": "450,000",
        "logo": "https://cdn.cloudflare.steamstatic.com/steam/apps/1086940/header.jpg"
    },
    {
        "rank": 3,
        "name": "Stardew Valley",
        "company": "ConcernedApe",
        "category": "Indie",
        "price": "$14.99",
        "reviews": "98% positivas",
        "users": "180,000",
        "logo": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg"
    }
]

@app.route("/")
def index():
    return render_template("index.html", games=games)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
