from flask import Flask, render_template, request

app = Flask(__name__)

# Simple recommendation logic based on skin type
def get_recommendations(skin_type):
    products = {
        "oily": [
            {"name": "Niacinamide Serum", "brand": "The Ordinary", "benefit": "Controls oil and minimizes pores"},
            {"name": "Oil-Free Moisturizer", "brand": "Neutrogena", "benefit": "Hydrates without greasiness"},
            {"name": "Salicylic Acid Cleanser", "brand": "CeraVe", "benefit": "Unclogs pores and removes excess oil"},
        ],
        "dry": [
            {"name": "Hyaluronic Acid Serum", "brand": "The Ordinary", "benefit": "Deep hydration for dry skin"},
            {"name": "Rich Moisturizing Cream", "brand": "CeraVe", "benefit": "Restores skin barrier"},
            {"name": "Gentle Hydrating Cleanser", "brand": "La Roche-Posay", "benefit": "Cleanses without stripping moisture"},
        ],
        "combination": [
            {"name": "Balancing Toner", "brand": "Thayers", "benefit": "Balances oily and dry areas"},
            {"name": "Lightweight Moisturizer", "brand": "Cetaphil", "benefit": "Hydrates without clogging pores"},
            {"name": "Gentle Foaming Cleanser", "brand": "CeraVe", "benefit": "Cleanses all skin zones gently"},
        ],
        "sensitive": [
            {"name": "Centella Serum", "brand": "COSRX", "benefit": "Soothes and calms irritated skin"},
            {"name": "Fragrance-Free Moisturizer", "brand": "Vanicream", "benefit": "Gentle hydration for sensitive skin"},
            {"name": "Micellar Water Cleanser", "brand": "Bioderma", "benefit": "Cleanses without irritation"},
        ],
    }
    return products.get(skin_type, [])

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    skin_type = ""
    if request.method == "POST":
        skin_type = request.form.get("skin_type")
        recommendations = get_recommendations(skin_type)
    return render_template("index.html", recommendations=recommendations, skin_type=skin_type)

if __name__ == "__main__":
    app.run(debug=True)