"""
FasalMitra AI - Practical Agricultural Knowledge & Pest Remedy Guide
"""
from typing import Dict, Any, List
from config import SUPPORTED_CROPS

PEST_INTELLIGENCE: Dict[str, Dict[str, Any]] = {
    # --- Rice Pests ---
    "rice leaf roller": {
        "common_name": "Rice Leaf Roller / Folder",
        "hindi_name": "पत्ता लपेटक कीट",
        "scientific_name": "Cnaphalocrocis medinalis",
        "crops": ["Rice"],
        "how_to_spot": "Caterpillars fold leaf edges together and feed inside, turning leaves whitish and papery with longitudinal clear streaks. Severely affected fields appear scorched from a distance.",
        "damage_risk": "Foliage loss reduces grain filling during tillering and panicle emergence.",
        "prevention_organic": "• Release Trichogramma egg cards (2-3 cards per acre).\n• Pass a rope across the crop canopy during early tillering to dislodge feeding larvae into water.\n• Spray 5% Neem Seed Kernel Extract (NSKE) or neem oil (1500 ppm) @ 3-5 ml/L.",
        "natural_predators": "Spiders (Wolf spiders), damsel flies, and mirid bugs naturally hunt leaf rollers in flooded fields.",
        "recommended_treatment": "If more than 1-2 folded leaves per plant are noticed: apply Chlorantraniliprole 18.5% SC @ 60 ml/acre or Flubendiamide 39.35% SC @ 20 ml/acre with 150 liters of water."
    },
    "rice leaf caterpillar": {
        "common_name": "Rice Green Caterpillar",
        "hindi_name": "धान की हरी इल्ली",
        "scientific_name": "Naranga aenescens",
        "crops": ["Rice"],
        "how_to_spot": "Small green caterpillars chew irregular notches along the outer leaf margins, stunting young seedlings.",
        "damage_risk": "Early seedling and tillering stages are most vulnerable.",
        "prevention_organic": "• Keep nursery clean of excessive grassy weeds.\n• Dislodge larvae by running a light rope over young seedlings.\n• Neem oil spray (1500 ppm) @ 3 ml per liter of water.",
        "natural_predators": "Conserve beneficial parasitic wasps and meadow spiders.",
        "recommended_treatment": "Cartap Hydrochloride 50% SP @ 400 g/acre or Bacillus thuringiensis (Bt) @ 400 g/acre."
    },
    "brown plant hopper": {
        "common_name": "Brown Planthopper (BPH)",
        "hindi_name": "भूरा फुदका कीट (माहू)",
        "scientific_name": "Nilaparvata lugens",
        "crops": ["Rice"],
        "how_to_spot": "Tiny brown insects cluster tightly at the base of the rice plant just above water level. Sap sucking causes plants to turn yellow, dry out, and collapse in circular patches called 'Hopperburn'.",
        "damage_risk": "Can destroy entire fields rapidly if left unchecked during late vegetative to grain formation.",
        "prevention_organic": "• Leave 30 cm alleyway paths (skip one row every 2-3 meters) for aeration and sunlight.\n• Drain field water for 3-4 days (alternate wetting and drying) to suppress nymph breeding.\n• Avoid excessive split doses of urea.",
        "natural_predators": "Wolf spiders and mirid bugs are powerful natural allies against planthoppers.",
        "recommended_treatment": "Spray Triflumezopyrim 10% SC @ 95 ml/acre or Pymetrozine 50% WG @ 120 g/acre. Direct the spray nozzle strictly at the base of the stems, not the upper canopy."
    },
    "white backed plant hopper": {
        "common_name": "White-Backed Planthopper",
        "hindi_name": "सफेद पीठ वाला फुदका",
        "scientific_name": "Sogatella furcifera",
        "crops": ["Rice"],
        "how_to_spot": "Small hoppers with a distinctive pale/white stripe down their back. Suck sap from tillers, causing leaf tips to curl and leaves to develop sooty mold.",
        "damage_risk": "Stunts tillering and weakens young rice stands.",
        "prevention_organic": "• Alternate wetting and drying of standing water.\n• Apply balanced potash fertilizers to strengthen tiller walls.",
        "natural_predators": "Ladybird beetles and predatory water bugs.",
        "recommended_treatment": "Spray Dinotefuran 20% SG @ 80 g/acre or Pymetrozine 50% WG @ 120 g/acre."
    },
    "asiatic rice borer": {
        "common_name": "Striped Rice Stem Borer",
        "hindi_name": "तना छेदक सुंडी",
        "scientific_name": "Chilo suppressalis",
        "crops": ["Rice"],
        "how_to_spot": "Larvae bore inside the hollow stem. Young plants show dried central shoots ('Dead Heart'). During heading stage, panicles turn white and remain empty ('White Earhead').",
        "damage_risk": "Direct yield loss through empty, chaffy grain heads.",
        "prevention_organic": "• Clip the top 2 inches of seedling leaf tips before transplanting to eliminate hidden egg masses.\n• Install pheromone traps (5 traps per acre) for early monitoring.\n• Deep summer ploughing to expose hibernating larvae.",
        "natural_predators": "Trichogramma egg parasitoids and dragonflies.",
        "recommended_treatment": "Broadcast Chlorantraniliprole 0.4% GR @ 4 kg/acre or Cartap Hydrochloride 4% GR @ 7.5 kg/acre with 2 inches of standing water."
    },
    "yellow rice borer": {
        "common_name": "Yellow Stem Borer",
        "hindi_name": "पीला तना छेदक",
        "scientific_name": "Scirpophaga incertulas",
        "crops": ["Rice"],
        "how_to_spot": "Produces dead central shoots in vegetative stage and white, sterile earheads at flowering. Moths are yellowish-white with two black dots on forewings.",
        "damage_risk": "Severe crop yield reduction if active at flowering stage.",
        "prevention_organic": "• Use light traps in the field to attract and catch night-flying moths.\n• Clip seedling tips prior to field transplanting.",
        "natural_predators": "Native parasitic wasps and field spiders.",
        "recommended_treatment": "Chlorantraniliprole 18.5% SC @ 60 ml/acre or Fipronil 5% SC @ 400 ml/acre."
    },

    # --- Cotton & Solanaceous Pests ---
    "aphids": {
        "common_name": "Aphids / Plant Lice",
        "hindi_name": "माहू / चेपा कीट",
        "scientific_name": "Aphis gossypii / Rhopalosiphum spp.",
        "crops": ["Cotton", "Wheat", "Maize", "Tomato", "Soybean"],
        "how_to_spot": "Dense colonies of tiny green, yellow, or black soft-bodied insects clustering under leaves and on tender buds. Leaves curl downwards, look crinkled, and sticky honeydew attracts dark sooty mold.",
        "damage_risk": "Weakens plants, stunts growth, and stains cotton lint.",
        "prevention_organic": "• Install bright yellow sticky traps (10-15 per acre) across the crop canopy.\n• Spray Neem oil (1500 ppm) @ 3-5 ml/L mixed with a few drops of mild soap liquid.\n• Spray fermented butter milk (sour chaas) or cow urine solution (10%).",
        "natural_predators": "Ladybird beetles ('Dhaal Keet') and green lacewings consume hundreds of aphids daily.",
        "recommended_treatment": "Spray Acetamiprid 20% SP @ 40 g/acre or Flonicamid 50% WG @ 60 g/acre when colonies cover >15% of terminal shoots."
    },
    "Thrips": {
        "common_name": "Thrips",
        "hindi_name": "चुरड़ा / थ्रिप्स कीट",
        "scientific_name": "Thrips tabaci / Scirtothrips dorsalis",
        "crops": ["Cotton", "Tomato", "Citrus", "Mango"],
        "how_to_spot": "Microscopic slender insects scratching leaf undersides. Leaves curl upwards like a cup ('Murda disease'), developing a silvery-white or bronzed shine underneath.",
        "damage_risk": "Stunts leaf expansion, drops flowers, and transmits viral diseases.",
        "prevention_organic": "• Erect blue sticky traps (15 per acre) near plant tops.\n• Use sprinkler or overhead irrigation where feasible to wash nymphs off leaves.\n• Spray Beauveria bassiana bio-fungus @ 5 g/L.",
        "natural_predators": "Predatory anthocorid bugs and lacewing larvae.",
        "recommended_treatment": "Spray Spinetoram 11.7% SC @ 170 ml/acre or Fipronil 5% SC @ 400 ml/acre."
    },
    "Trialeurodes vaporariorum": {
        "common_name": "Whitefly",
        "hindi_name": "सफेद मक्खी",
        "scientific_name": "Trialeurodes vaporariorum",
        "crops": ["Tomato", "Cotton", "Soybean"],
        "how_to_spot": "Tiny pure-white moth-like insects that flutter up in clouds when plants are shaken. Sap sucking turns foliage chlorotic and yellow.",
        "damage_risk": "Transmits destructive Leaf Curl Viruses and coats leaves in sticky sooty mold.",
        "prevention_organic": "• Set up yellow sticky traps (20 per acre) evenly across the field.\n• Plant barrier crops (2 rows of maize or sorghum) around cotton/tomato borders.\n• Spray neem oil (1500 ppm) @ 4 ml/L every 7-10 days.",
        "natural_predators": "Encarsia formosa parasitic wasps and ladybird beetles.",
        "recommended_treatment": "Spray Pyriproxyfen 10% EC @ 400 ml/acre or Diafenthiuron 50% WP @ 240 g/acre."
    },
    "Prodenia litura": {
        "common_name": "Tobacco Cutworm / Leaf-Eating Caterpillar",
        "hindi_name": "तंबाकू की इल्ली",
        "scientific_name": "Spodoptera litura",
        "crops": ["Cotton", "Tomato", "Soybean", "Maize"],
        "how_to_spot": "Plump dark green/brown caterpillars with yellow and black lateral lines. Young larvae feed together, skeletonizing leaves into white paper-thin nets. Older larvae eat large holes in leaves and fruit.",
        "damage_risk": "Heavy defoliation and direct burrowing into tomato fruit and cotton bolls.",
        "prevention_organic": "• Plant castor or sunflower along field borders as trap crops.\n• Hand-pick and destroy skeletonized leaves harboring newly hatched egg masses.\n• Install pheromone traps (5 per acre) with Spodolure.\n• Spray Spodoptera litura NPV (SINPV) @ 1 ml/L in evening hours.",
        "natural_predators": "Erect bird perches (15-20 per acre) to invite birds like drongos and crows that feed on larvae.",
        "recommended_treatment": "Spray Emamectin Benzoate 5% SG @ 80 g/acre or Chlorantraniliprole 18.5% SC @ 60 ml/acre."
    },
    "black cutworm": {
        "common_name": "Black Cutworm",
        "hindi_name": "काली कतरा सुंडी",
        "scientific_name": "Agrotis ipsilon",
        "crops": ["Cotton", "Maize", "Tomato", "Soybean", "Wheat"],
        "how_to_spot": "Plump greasy dark caterpillars hiding under soil clods during the day. At night, they cut tender seedling stems cleanly at ground level.",
        "damage_risk": "Causes patchy, missing plant stands in newly germinated crops.",
        "prevention_organic": "• Deep summer ploughing to expose soil pupae to bright sun and birds.\n• Flood irrigation drives larvae out of burrows onto the soil surface.\n• Make poison bran bait: 10 kg rice bran + 1 kg jaggery + 250 ml chlorpyrifos scattered along rows.",
        "natural_predators": "Ground beetles (Carabidae) and parasitic nematodes.",
        "recommended_treatment": "Soil drench around the base of plants with Chlorpyrifos 20% EC @ 2.5 ml/L in the late afternoon."
    },

    # --- Maize & Wheat Pests ---
    "corn borer": {
        "common_name": "Maize Stem Borer",
        "hindi_name": "मक्का तना छेदक",
        "scientific_name": "Chilo partellus / Ostrinia nubilalis",
        "crops": ["Maize"],
        "how_to_spot": "Leaves show rows of neat round holes ('shot-holes') as they unroll from the whorl. Plant tassels break over, and stalks have exit holes with sawdust-like frass.",
        "damage_risk": "Weakens stalks, causes lodging, and reduces cob size.",
        "prevention_organic": "• Burn or shred harvest stubble to destroy overwintering larvae.\n• Intercrop maize with cowpea or pulses to suppress moth egg laying.\n• Release Trichogramma chilonis egg cards (50,000 eggs/acre).",
        "natural_predators": "Earwigs and predatory ground beetles.",
        "recommended_treatment": "Apply Carbofuran 3% CG or Chlorantraniliprole 0.4% GR granules directly into the central leaf whorls @ 2 kg/acre."
    },
    "army worm": {
        "common_name": "Fall Armyworm / Armyworm",
        "hindi_name": "सैनिक कीट / फॉल आर्मीवर्म",
        "scientific_name": "Spodoptera frugiperda / Mythimna separata",
        "crops": ["Maize", "Wheat", "Rice", "Soybean"],
        "how_to_spot": "Aggressive foliage grazing leaving only leaf midribs behind. Larvae hide deep inside the central leaf whorl surrounded by heaps of moist saw-dust frass.",
        "damage_risk": "Destroys growing tips and can wipe out young vegetative maize stands.",
        "prevention_organic": "• Push-Pull technique: Plant Napier grass border and Desmodium intercrop.\n• Apply dry sand or wood ash (mixed with neem powder) directly into central whorls.\n• Spray Metarhizium rileyi or Bt kurstaki @ 2 g/L.",
        "natural_predators": "Conserve predatory wasps, earwigs, and field birds.",
        "recommended_treatment": "Spray Spinetoram 11.7% SC @ 0.5 ml/L or Chlorantraniliprole 18.5% SC @ 0.4 ml/L targeted straight into the whorl cup."
    },
    "wheat sawfly": {
        "common_name": "Wheat Stem Sawfly",
        "hindi_name": "गेहूं का सॉफ्लाई कीट",
        "scientific_name": "Cephus cinctus",
        "crops": ["Wheat"],
        "how_to_spot": "Grubs bore inside the hollow stem and chew an internal groove around the base, causing wheat stalks to snap and lodge before harvest.",
        "damage_risk": "Severe pre-harvest lodging makes mechanical harvesting difficult.",
        "prevention_organic": "• Grow solid-stemmed wheat varieties resistant to sawfly entry.\n• Rotate with non-host broadleaf crops (chickpea, mustard, lentils).\n• Tillage after harvest destroys overwintering grubs.",
        "natural_predators": "Native braconid parasitic wasps.",
        "recommended_treatment": "Chemical spray is rarely effective once grubs are inside stems; focus on boundary sprays during adult flight if necessary."
    },
    "english grain aphid": {
        "common_name": "Wheat Grain Aphid",
        "hindi_name": "गेहूं का माहू कीट",
        "scientific_name": "Sitobion avenae",
        "crops": ["Wheat"],
        "how_to_spot": "Dense clusters of green or reddish aphids feeding directly on green wheat earheads and flag leaves during grain filling.",
        "damage_risk": "Sucks milk from developing grain, resulting in shriveled kernels and light bushel weight.",
        "prevention_organic": "• Timely sowing in November to escape late season aphid spikes.\n• Avoid excessive late application of nitrogen fertilizers.\n• Spray neem oil (1500 ppm) @ 3 ml/L on earheads.",
        "natural_predators": "Syrphid fly larvae and ladybird beetles consume high volumes of grain aphids.",
        "recommended_treatment": "If >5 aphids per earhead are found at flowering: spray Thiamethoxam 25% WG @ 40 g/acre or Imidacloprid 17.8% SL @ 60 ml/acre."
    },

    # --- Mango Pests ---
    "Dacus dorsalis(Hendel)": {
        "common_name": "Oriental Fruit Fly",
        "hindi_name": "फल मक्खी",
        "scientific_name": "Bactrocera dorsalis",
        "crops": ["Mango", "Citrus"],
        "how_to_spot": "Female lays eggs under the skin of maturing fruits. Maggots burrow inside, making the fruit turn soft, brown, rot internally, and drop prematurely.",
        "damage_risk": "Destroys export quality and can cause up to 60-80% fruit drop in untreated orchards.",
        "prevention_organic": "• Collect and bury fallen infested fruits in a 2-foot deep pit with lime powder.\n• Install Methyl Eugenol pheromone bottle traps (6-8 traps per acre) 1.5 meters high in tree shade.\n• Plough tree basins in summer to expose pupae to sun.",
        "natural_predators": "Opiine parasitic wasps attack fruit fly maggots inside fallen fruit.",
        "recommended_treatment": "Bait spray on tree trunks and inner canopy: 100 g jaggery + 20 ml Malathion 50% EC dissolved in 20 liters of water. Spray in coarse large droplets (do not blanket spray whole fruit)."
    },
    "Mango flat beak leafhopper": {
        "common_name": "Mango Hopper",
        "hindi_name": "आम का भुनगा / चेपा",
        "scientific_name": "Idioscopus nitidulus",
        "crops": ["Mango"],
        "how_to_spot": "Small wedge-shaped insects that hop rapidly on flower clusters and tender leaves. Sap sucking causes flower buds to turn brown, dry, and drop ('Blossom blight'). Sooty mold covers leaves.",
        "damage_risk": "Severe inflorescence drop prevents fruit set.",
        "prevention_organic": "• Prune dead and dense overlapping branches to allow sunlight into the center of the tree.\n• Spray neem oil @ 3 ml/L prior to flowering.",
        "natural_predators": "Spiders, Chrysoperla, and entomopathogenic fungi.",
        "recommended_treatment": "First spray at flower panicle emergence: Imidacloprid 17.8% SL @ 0.3 ml/L water. Second spray at pea stage if hoppers persist."
    },

    # --- Citrus Pests ---
    "Phyllocnistis citrella Stainton": {
        "common_name": "Citrus Leafminer",
        "hindi_name": "नींबू वर्गीय पत्ता सुरंग कीट",
        "scientific_name": "Phyllocnistis citrella",
        "crops": ["Citrus"],
        "how_to_spot": "Tiny larvae make silvery, shiny serpentine tunnels ('mines') inside new tender leaves. Leaves curl, pucker, and turn brittle. Mines allow Citrus Canker bacteria to enter.",
        "damage_risk": "Severely stunts young saplings and nursery flushes.",
        "prevention_organic": "• Prune off water sprouts and out-of-season suckers.\n• Spray 5% Neem Seed Kernel Extract (NSKE) during each new flush.\n• Regulate irrigation to produce uniform, synchronized flushing.",
        "natural_predators": "Beneficial native eulophid parasitic wasps.",
        "recommended_treatment": "Spray Abamectin 1.9% EC @ 0.5 ml/L or Thiamethoxam 25% WG @ 0.3 g/L during active flush emergence."
    },
    "Panonchus citri McGregor": {
        "common_name": "Citrus Red Mite",
        "hindi_name": "नींबू की लाल मकड़ी",
        "scientific_name": "Panonychus citri",
        "crops": ["Citrus"],
        "how_to_spot": "Tiny reddish mites feeding on leaf surfaces, leaving fine yellow speckling and a grayish, dusty blemish. Heavy attack leads to leaf and fruit drop.",
        "damage_risk": "Causes fruit skin discoloration and premature foliage shed.",
        "prevention_organic": "• Wash tree canopy with a powerful water hose or overhead sprinklers during dry spells.\n• Maintain ground cover crops to reduce orchard dust.",
        "natural_predators": "Predatory phytoseiid mites and Stethorus ladybird beetles.",
        "recommended_treatment": "Spray Propargite 57% EC @ 2 ml/L or Spiromesifen 22.9% SC @ 0.75 ml/L water."
    },
    "mole cricket": {
        "common_name": "Mole Cricket",
        "hindi_name": "झिंगुर / मोल क्रिकेट",
        "scientific_name": "Gryllotalpa gryllotalpa",
        "crops": ["Rice", "Cotton", "Maize", "Tomato"],
        "how_to_spot": "Burrowing underground crickets churn soil, creating raised winding ridges. They sever tender roots and chew stems at soil level.",
        "damage_risk": "Patchy deaths in nursery beds and newly transplanted fields.",
        "prevention_organic": "• Flooding the nursery drives crickets to the surface where birds feed on them.\n• Deep cultivation destroys tunnels and egg chambers.",
        "natural_predators": "Birds, toads, and beneficial soil nematodes.",
        "recommended_treatment": "Apply poison bait (rice bran 10 kg + jaggery 1 kg + chlorpyrifos 250 ml) around field bunds in late afternoon."
    },
    "blister beetle": {
        "common_name": "Blister Beetle",
        "hindi_name": "छाला बनाने वाला भृंग",
        "scientific_name": "Mylabris phalerata",
        "crops": ["Soybean", "Cotton"],
        "how_to_spot": "Conspicuous black and red/yellow banded beetles feeding voraciously on flowers and tender pods. If crushed against skin, they exude cantharidin causing painful blisters.",
        "damage_risk": "Destroys flowers, preventing pod formation in legumes.",
        "prevention_organic": "• Hand-pick beetles in early morning when they are sluggish (wear protective gloves!).\n• Set up light traps to monitor adult swarms.",
        "natural_predators": "Bee flies (Bombyliidae) parasitize blister beetle egg pods.",
        "recommended_treatment": "Dust Malathion 5% DP @ 10 kg/acre or spray Quinalphos 25% EC @ 2 ml/L on flowering crops."
    }
}


def get_pest_details(pest_name: str) -> Dict[str, Any]:
    """Returns friendly agronomic intelligence for a given pest."""
    cleaned = pest_name.strip()
    
    details = None
    if cleaned in PEST_INTELLIGENCE:
        details = dict(PEST_INTELLIGENCE[cleaned])
    else:
        for k, v in PEST_INTELLIGENCE.items():
            if k.lower() == cleaned.lower():
                details = dict(v)
                break

    if details is None:
        title_name = cleaned.replace("_", " ").title()
        details = {
            "common_name": title_name,
            "hindi_name": "फसल कीट",
            "scientific_name": title_name,
            "crops": ["Field Crops"],
            "how_to_spot": f"Feeds on crop foliage, leaf tissues, or shoots. Look for leaf punctures, discoloration, or tiny feeding marks.",
            "damage_risk": "Reduces photosynthetic leaf area and weakens developing plant tissues.",
            "prevention_organic": "• Inspect plant undersides regularly.\n• Spray Neem oil (1500 ppm) @ 3-5 ml per liter of water.\n• Maintain balanced fertilizer and avoid excess nitrogen.",
            "natural_predators": "Native spiders, ladybird beetles, and lacewings provide natural biological suppression.",
            "recommended_treatment": "Consult your local block agricultural extension officer (Krishi Vigyan Kendra) for approved treatments in your district."
        }

    # Add backwards-compatible aliases for tests
    details["symptoms"] = details.get("how_to_spot", "")
    details["ipm"] = {
        "cultural": details.get("prevention_organic", ""),
        "biological": details.get("natural_predators", ""),
        "chemical": details.get("recommended_treatment", "")
    }
    return details


def get_crop_pests(crop_name: str) -> List[str]:
    """Returns the list of verified pests relevant to a specific crop."""
    crop_info = SUPPORTED_CROPS.get(crop_name)
    if crop_info:
        return crop_info.get("pests", [])
    return []

