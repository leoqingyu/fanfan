from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="CoolTech")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

PRODUCTS = {
    "pro-neck-cooler": {
        "id": "pro-neck-cooler",
        "name": "Pro Neck Cooler",
        "subtitle_en": "Flagship Model",
        "subtitle_fr": "Modèle phare",
        "price": 29.99,
        "badge_en": "Best Seller",
        "badge_fr": "Meilleure vente",
        "stock": 5,
        "features_en": ["Semiconductor Cooling", "Brushless Silent Motor", "8-Hour Battery", "Dual Airflow"],
        "features_fr": ["Refroidissement semiconducteur", "Moteur silencieux sans balai", "8h d'autonomie", "Double flux d'air"],
        "description_en": (
            "Professional-grade neck cooling powered by semiconductor (TEC) technology. "
            "Whisper-quiet brushless motors and a dual-airflow design keep you comfortable "
            "for up to 8 hours on a single charge."
        ),
        "description_fr": (
            "Refroidissement cervical professionnel par technologie semiconducteur (TEC). "
            "Des moteurs sans balai ultra-silencieux et un double flux d'air vous gardent "
            "à l'aise jusqu'à 8 heures sur une seule charge."
        ),
        "video_src": "/static/videos/pro-neck-cooler-demo.mp4",
        "thumbnail": "/static/images/pro-neck-cooler.jpg",
        "gallery": [
            "/static/images/pro-neck-cooler-1.jpg",
            "/static/images/pro-neck-cooler-2.jpg",
            "/static/images/pro-neck-cooler-3.jpg",
        ],
    },
    "handheld-ice-fan": {
        "id": "handheld-ice-fan",
        "name": "Handheld Ice Fan",
        "subtitle_en": "Handheld Essential",
        "subtitle_fr": "Essentiel portatif",
        "price": 19.99,
        "badge_en": "Popular",
        "badge_fr": "Populaire",
        "stock": 5,
        "features_en": ["Ice-Cold Airflow", "3-Speed Settings", "USB-C Charging", "Foldable Design"],
        "features_fr": ["Flux d'air glacé", "3 vitesses", "Charge USB-C", "Design pliable"],
        "description_en": (
            "Compact yet powerful handheld fan with an ice-cold airflow diffuser. "
            "Three speed settings, USB-C charging, and a foldable arm make it "
            "the ultimate on-the-go companion."
        ),
        "description_fr": (
            "Ventilateur portatif compact et puissant avec diffuseur à flux d'air glacé. "
            "Trois vitesses, charge USB-C et bras pliable pour une portabilité ultime."
        ),
        "video_src": "/static/videos/handheld-ice-fan-demo.mp4",
        "thumbnail": "/static/images/handheld-ice-fan.jpg",
        "gallery": [
            "/static/images/handheld-ice-fan-1.jpg",
            "/static/images/handheld-ice-fan-2.jpg",
            "/static/images/handheld-ice-fan-3.jpg",
        ],
    },
    "gaming-phone-cooler": {
        "id": "gaming-phone-cooler",
        "name": "Gaming Phone Cooler",
        "subtitle_en": "Gaming Clip-On",
        "subtitle_fr": "Clip Gaming",
        "price": 16.99,
        "badge_en": "New",
        "badge_fr": "Nouveau",
        "stock": 3,
        "features_en": ["TEC Semiconductor Cooling", "RGB Lighting", "Fits 6–7\" Phones", "Plug & Play"],
        "features_fr": ["Refroidissement TEC", "Éclairage RGB", "Compatible 6–7 pouces", "Plug & Play"],
        "description_en": (
            "Clip-on TEC semiconductor cooler engineered for mobile gaming. "
            "Keeps your phone at peak thermal performance with RGB lighting and "
            "plug-and-play USB-C power — no app or pairing required."
        ),
        "description_fr": (
            "Clip de refroidissement TEC semiconducteur conçu pour le gaming mobile. "
            "Maintient votre téléphone à des performances optimales avec éclairage RGB "
            "et alimentation USB-C plug-and-play — sans application ni couplage."
        ),
        "video_src": "/static/videos/gaming-phone-cooler-demo.mp4",
        "thumbnail": "/static/images/gaming-phone-cooler.jpg",
        "gallery": [
            "/static/images/gaming-phone-cooler-1.jpg",
            "/static/images/gaming-phone-cooler-2.jpg",
            "/static/images/gaming-phone-cooler-3.jpg",
        ],
    },
    "portable-mini-ac": {
        "id": "portable-mini-ac",
        "name": "Portable Mini AC",
        "subtitle_en": "Portable AC Unit",
        "subtitle_fr": "Climatiseur portable",
        "price": 329.99,
        "badge_en": "Coming Soon",
        "badge_fr": "Bientôt disponible",
        "stock": 0,
        "features_en": ["Active Cooling", "Water-Cooled Heat Sink", "Silent Mode", "Portable Design"],
        "features_fr": ["Refroidissement actif", "Dissipateur thermique eau", "Mode silencieux", "Design portable"],
        "description_en": (
            "Next-generation portable air conditioning in a pocket-sized form factor. "
            "Reserve yours today and be first in line when this category-defining "
            "product ships."
        ),
        "description_fr": (
            "Climatisation portable nouvelle génération dans un format de poche. "
            "Réservez dès maintenant et soyez le premier à recevoir ce produit "
            "révolutionnaire à sa sortie."
        ),
        "video_src": "/static/videos/portable-mini-ac-demo.mp4",
        "thumbnail": "/static/images/portable-mini-ac.jpg",
        "gallery": [
            "/static/images/portable-mini-ac-1.jpg",
            "/static/images/portable-mini-ac-2.jpg",
            "/static/images/portable-mini-ac-3.jpg",
        ],
    },
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "products": list(PRODUCTS.values())}
    )


@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: str):
    product = PRODUCTS.get(product_id)
    if not product:
        return HTMLResponse(content="Product not found", status_code=404)
    return templates.TemplateResponse(
        "detail.html", {"request": request, "product": product}
    )
