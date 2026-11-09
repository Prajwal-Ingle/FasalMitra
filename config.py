"""
FasalMitra AI - Application Configuration & Domain Data
"""
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "best.onnx" if (MODELS_DIR / "best.onnx").exists() else MODELS_DIR / "best.pt"
YAML_PATH = MODELS_DIR / "pests.yaml"
ASSETS_DIR = BASE_DIR / "assets"
SAMPLES_DIR = ASSETS_DIR / "samples"

# App Metadata (Farmer Facing)
APP_NAME = "FasalMitra AI"
APP_HINDI_NAME = "फसल मित्र"
APP_TAGLINE = "Smart Crop Protection & Instant Pest Diagnosis"
APP_VERSION = "2.0.0"

# Default Inference Settings (Kept internally, simplified for users)
DEFAULT_CONF_THRESHOLD = 0.25
DEFAULT_IOU_THRESHOLD = 0.45
INFERENCE_IMAGE_SIZE = 640

# Supported Crops & Agricultural Categories
SUPPORTED_CROPS = {
    "Rice": {
        "scientific_name": "Oryza sativa",
        "icon": "🌾",
        "description": "Essential cereal crop prone to leaf rollers, stem borers, and planthoppers.",
        "pests": [
            "rice leaf roller", "rice leaf caterpillar", "paddy stem maggot", 
            "asiatic rice borer", "yellow rice borer", "rice gall midge", 
            "Rice Stemfly", "brown plant hopper", "white backed plant hopper", 
            "small brown plant hopper", "rice water weevil", "rice leafhopper", 
            "grain spreader thrips", "rice shell pest"
        ]
    },
    "Wheat": {
        "scientific_name": "Triticum aestivum",
        "icon": "🌿",
        "description": "Key winter crop vulnerable to aphids, sawflies, and blossom midges.",
        "pests": [
            "english grain aphid", "green bug", "bird cherry-oataphid", 
            "wheat blossom midge", "penthaleus major", "longlegged spider mite", 
            "wheat phloeothrips", "wheat sawfly", "cerodonta denticornis", "army worm"
        ]
    },
    "Cotton": {
        "scientific_name": "Gossypium hirsutum",
        "icon": "☁️",
        "description": "Commercial fiber crop susceptible to whiteflies, aphids, cutworms, and thrips.",
        "pests": [
            "aphids", "black cutworm", "large cutworm", "yellow cutworm", 
            "Prodenia litura", "Thrips", "Trialeurodes vaporariorum", 
            "Polyphagotars onemus latus", "blister beetle", "mole cricket"
        ]
    },
    "Maize": {
        "scientific_name": "Zea mays",
        "icon": "🌽",
        "description": "High-yield cereal crop threatened by stem borers, fall armyworms, and cutworms.",
        "pests": [
            "corn borer", "army worm", "black cutworm", "wireworm", 
            "grub", "mole cricket", "aphids", "cabbage army worm", "beet army worm"
        ]
    },
    "Tomato": {
        "scientific_name": "Solanum lycopersicum",
        "icon": "🍅",
        "description": "High-value vegetable crop impacted by whiteflies, broad mites, and thrips.",
        "pests": [
            "Trialeurodes vaporariorum", "Polyphagotars onemus latus", "aphids", 
            "Thrips", "Prodenia litura", "flea beetle", "red spider"
        ]
    },
    "Soybean": {
        "scientific_name": "Glycine max",
        "icon": "🌱",
        "description": "Vital oilseed and protein crop vulnerable to blister beetles and pod borers.",
        "pests": [
            "blister beetle", "legume blister beetle", "army worm", 
            "Prodenia litura", "black cutworm", "aphids", "Apolygus lucorum"
        ]
    },
    "Mango": {
        "scientific_name": "Mangifera indica",
        "icon": "🥭",
        "description": "Premier fruit crop prone to oriental fruit flies, hoppers, and shoot borers.",
        "pests": [
            "Dacus dorsalis(Hendel)", "Mango flat beak leafhopper", 
            "Deporaus marginatus Pascoe", "Chlumetia transversa", 
            "Rhytidodera bowrinii white", "Sternochetus frigidus"
        ]
    },
    "Citrus": {
        "scientific_name": "Citrus spp.",
        "icon": "🍊",
        "description": "Fruit orchard trees threatened by leafminers, red mites, rust mites, and scales.",
        "pests": [
            "Papilio xuthus", "Panonchus citri McGregor", "Phyllocoptes oleiverus ashmead", 
            "Icerya purchasi Maskell", "Unaspis yanonensis", "Ceroplastes rubens", 
            "Chrysomphalus aonidum", "Parlatoria zizyphus Lucus", "Nipaecoccus vastalor", 
            "Aleurocanthus spiniferus", "Tetradacus c Bactrocera minax", "Bactrocera tsuneonis", 
            "Phyllocnistis citrella Stainton", "Toxoptera citricidus", "Toxoptera aurantii", 
            "Aphis citricola Vander Goot"
        ]
    }
}

# Organic Biophilic Color Palette (FasalMitra Design System)
COLORS = {
    "canvas": "#F8FAF6",
    "surface": "#FFFFFF",
    "surface_soft": "#F0F5EE",
    "border": "#D5E0D0",
    "border_hover": "#86EFAC",
    "primary": "#166534",
    "primary_hover": "#15803D",
    "primary_soft": "#DCFCE7",
    "accent_gold": "#B45309",
    "accent_gold_soft": "#FEF3C7",
    "text_title": "#112A1A",
    "text_body": "#223829",
    "text_muted": "#526658",
    "alert_crimson": "#DC2626",
    "alert_amber": "#D97706",
    "alert_emerald": "#166534",
    # Bounding box colors for distinct pest visualization
    "box_colors": [
        "#DC2626", "#D97706", "#2563EB", "#7C3AED", 
        "#059669", "#DB2777", "#0891B2", "#CA8A04",
        "#16A34A", "#E11D48", "#0D9488", "#9333EA"
    ]
}
