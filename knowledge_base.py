CLASS_NAMES = [
    "Rice Leaf Roller","Rice Leaf Caterpillar","Paddy Stem Maggot",
    "Asiatic Rice Borer","Yellow Rice Borer","Rice Gall Midge",
    "Rice Stemfly","Brown Plant Hopper","White Backed Plant Hopper",
    "Small Brown Plant Hopper","Rice Water Weevil","Rice Leafhopper",
    "Dragonfly","Ladybird Beetle","Spider"
]

# Telugu names mapping for each pest (Corrected)
TELUGU_NAMES = {
    "Rice Leaf Roller": "ఆకు మడత పురుగు",
    "Rice Leaf Caterpillar": "వరి ఆకు గొంగళి పురుగు",
    "Paddy Stem Maggot": "వరి కాండ మగ్గు పురుగు",
    "Asiatic Rice Borer": "ఆసియా వరి కాండ తొలిచే పురుగు",
    "Yellow Rice Borer": "పసుపు వరి కాండ తొలిచే పురుగు",
    "Rice Gall Midge": "వరి గాల్ ఈగ / గాలి ఈగ",
    "Rice Stemfly": "వరి కాండ ఈగ",
    "Brown Plant Hopper": "గోధుమ రంగు దూకుడు పురుగు",
    "White Backed Plant Hopper": "తెల్ల వీపు దూకుడు పురుగు",
    "Small Brown Plant Hopper": "చిన్న గోధుమ దూకుడు పురుగు",
    "Rice Water Weevil": "వరి నీటి వీవిల్",
    "Rice Leafhopper": "వరి ఆకు దూకుడు పురుగు",
    "Dragonfly": "తుమ్మెద",
    "Ladybird Beetle": "లేడీబర్డ్ బీటిల్",
    "Spider": "సాలీడు"
}

# Minimal pest information used by the backend and frontend (Telugu te corrected; English left as-is)
pest_info = {
    "Rice Leaf Roller": {
        "en": {
            "impact": "Causes leaf rolling and defoliation leading to 10–20% yield loss.",
            "eggs": "Laid singly or in small groups on the underside of rice leaves and hatch in 4–6 days.",
            "control": "Use pheromone traps, apply neem oil early, encourage natural parasitoids.",
            "pesticide": "Spinosad or Lambda-cyhalothrin"
        },
        "te": {
            "impact": "ఆకులు మడతపడి తినబడటం వల్ల 10–20% వరకు దిగుబడి నష్టం కలుగుతుంది.",
            "eggs": "వరి ఆకుల అడుగు భాగంలో ఒంటరిగా లేదా చిన్న గుంపులుగా గుడ్లు పెడతాయి.",
            "control": "ఫెరోమోన్ ట్రాప్‌లు, ప్రారంభ దశలో నీమ్ నూనె, సహజ శత్రువుల ప్రోత్సాహం.",
            "pesticide": "స్పినోసాడ్ లేదా లాంబ్డా‑సైహాలోత్రిన్"
        }
    },

    "Rice Leaf Caterpillar": {
        "en": {
            "impact": "Feeds on leaf tissue forming window-like patches and reduces photosynthesis.",
            "eggs": "Laid in clusters on the underside of leaves and hatch within 3–5 days.",
            "control": "Neem spray, removal of infested leaves, encourage spiders and wasps.",
            "pesticide": "Neem oil or Bacillus thuringiensis (Bt)"
        },
        "te": {
            "impact": "ఆకులపై రంధ్రాలు ఏర్పడి ఫోటోసింథసిస్ తగ్గుతుంది.",
            "eggs": "ఆకుల కింద గుంపులుగా గుడ్లు పెడతాయి.",
            "control": "నీమ్ స్ప్రే, దెబ్బతిన్న ఆకుల తొలగింపు, సహజ శత్రువులు.",
            "pesticide": "నీమ్ నూనె లేదా బి.టి"
        }
    },

    "Paddy Stem Maggot": {
        "en": {
            "impact": "Larvae bore into stems causing dead hearts and wilting.",
            "eggs": "Laid near the base of seedlings in moist soil.",
            "control": "Field sanitation and timely granular insecticide application.",
            "pesticide": "Fipronil or Carbofuran (granules)"
        },
        "te": {
            "impact": "కాండలో దాడి చేసి మొక్కలు ఎండిపోతాయి.",
            "eggs": "తడి నేలలో నార్ల అడుగున గుడ్లు పెడతాయి.",
            "control": "పొలం పరిశుభ్రత మరియు కణిక మందులు.",
            "pesticide": "ఫిప్రోనిల్ లేదా కార్బోఫ్యూరాన్"
        }
    },

    "Asiatic Rice Borer": {
        "en": {
            "impact": "Stem borer causing white ears and severe yield loss.",
            "eggs": "Laid in clusters on leaves and stems covered with hair-like scales.",
            "control": "Resistant varieties, release Trichogramma wasps.",
            "pesticide": "Diflubenzuron or Dichlorvos"
        },
        "te": {
            "impact": "కాండ తొలిచే పురుగు వల్ల దిగుబడి తీవ్రంగా తగ్గుతుంది.",
            "eggs": "ఆకులు మరియు కాండలపై గుంపులుగా గుడ్లు పెడతాయి.",
            "control": "నిరోధక రకాలు, ట్రైకోగ్రామా విడుదల.",
            "pesticide": "డైఫ్లూబెంజ్యూరాన్ లేదా డైక్లోర్వోస్"
        }
    },

    "Yellow Rice Borer": {
        "en": {
            "impact": "Causes dead hearts and white ear heads resulting in 30–50% yield loss.",
            "eggs": "Laid in masses on leaf sheaths and hatch in about one week.",
            "control": "Pheromone traps and synchronized planting.",
            "pesticide": "Isoprocarb or Phenthoate"
        },
        "te": {
            "impact": "డెడ్ హార్ట్ మరియు తెల్ల ముళ్లు ఏర్పడి భారీ నష్టం.",
            "eggs": "ఆకు షీతులపై గుంపులుగా గుడ్లు పెడతాయి.",
            "control": "ఫెరోమోన్ ట్రాప్‌లు మరియు సమకాలీన నాట్లు.",
            "pesticide": "ఐసోప్రోకార్బ్ లేదా ఫెన్థోయేట్"
        }
    },

    "Rice Gall Midge": {
        "en": {
            "impact": "Induces gall formation instead of panicle leading to crop failure.",
            "eggs": "Laid on young leaves or leaf sheaths of tillers.",
            "control": "Use resistant varieties and remove affected tillers.",
            "pesticide": "Imidacloprid or Dimethoate"
        },
        "te": {
            "impact": "గింజల బదులు గాల్‌లు ఏర్పడి పంట నష్టం కలుగుతుంది.",
            "eggs": "చిన్న ఆకులపై లేదా షీతులపై గుడ్లు పెడతాయి.",
            "control": "నిరోధక రకాలు మరియు దెబ్బతిన్న మొక్కల తొలగింపు.",
            "pesticide": "ఇమిడాక్లోప్రిడ్ లేదా డైమెథోయేట్"
        }
    },

    "Rice Stemfly": {
        "en": {
            "impact": "Larval feeding damages stem tissues and reduces tillering.",
            "eggs": "Laid near the base of plants in wet soil.",
            "control": "Crop rotation and field sanitation.",
            "pesticide": "Chlorpyrifos or Triazophos"
        },
        "te": {
            "impact": "కాండ నష్టం వల్ల కిటుకు తగ్గుతుంది.",
            "eggs": "తడి నేలలో మొక్క అడుగున గుడ్లు పెడతాయి.",
            "control": "పంట మార్పిడి మరియు పరిశుభ్రత.",
            "pesticide": "క్లోర్పిరిఫోస్ లేదా ట్రియాజోఫోస్"
        }
    },

    "Brown Plant Hopper": {
        "en": {
            "impact": "Sucks sap and spreads viral diseases like grassy stunt.",
            "eggs": "Inserted into leaf sheaths and stem tissues.",
            "control": "Water management and resistant varieties.",
            "pesticide": "Imidacloprid or Acetamiprid"
        },
        "te": {
            "impact": "మొక్క సారం పీల్చి వైరస్ వ్యాధులు వ్యాప్తి చేస్తుంది.",
            "eggs": "ఆకు షీతుల లోపల గుడ్లు పెడతాయి.",
            "control": "నీటి నిర్వహణ మరియు నిరోధక రకాలు.",
            "pesticide": "ఇమిడాక్లోప్రిడ్ లేదా ఆసెటామిప్రిడ్"
        }
    },

    "White Backed Plant Hopper": {
        "en": {
            "impact": "Causes plant yellowing and stunting similar to BPH.",
            "eggs": "Inserted into leaf sheaths along the midrib.",
            "control": "Avoid excess nitrogen and monitor regularly.",
            "pesticide": "Carbosulfan or Dimethoate"
        },
        "te": {
            "impact": "మొక్కలు పసుపు రంగు తీసుకుని ఎదుగుదల తగ్గుతుంది.",
            "eggs": "ఆకుల మధ్య నరంలో గుడ్లు పెడతాయి.",
            "control": "అధిక నత్రజని నివారించాలి.",
            "pesticide": "కార్బోసల్ఫాన్ లేదా డైమెథోయేట్"
        }
    },

    "Small Brown Plant Hopper": {
        "en": {
            "impact": "Weakens plants and transmits viral diseases.",
            "eggs": "Laid on leaf surfaces and young stems.",
            "control": "Field sanitation and conservation of predators.",
            "pesticide": "Malathion or Quinalphos"
        },
        "te": {
            "impact": "మొక్క బలహీనమై వైరస్ వ్యాధులు వ్యాప్తి.",
            "eggs": "ఆకులు మరియు చిన్న కాండలపై గుడ్లు.",
            "control": "పొలం పరిశుభ్రత మరియు సహజ శత్రువులు.",
            "pesticide": "మలాథియన్ లేదా క్వినాల్ఫోస్"
        }
    },

    "Rice Water Weevil": {
        "en": {
            "impact": "Larvae feed on roots causing stunting and yield loss.",
            "eggs": "Laid in waterlogged soil near rice plants.",
            "control": "Intermittent drainage and resistant varieties.",
            "pesticide": "Fipronil GR or Carbofuran"
        },
        "te": {
            "impact": "లార్వాలు వేర్లను తిని మొక్క ఎదుగుదల తగ్గిస్తాయి.",
            "eggs": "నీటితో నిండిన నేలలో గుడ్లు.",
            "control": "మధ్య మధ్యలో నీరు వదలాలి.",
            "pesticide": "ఫిప్రోనిల్ GR లేదా కార్బోఫ్యూరాన్"
        }
    },

    "Rice Leafhopper": {
        "en": {
            "impact": "Transmits tungro virus causing major yield loss.",
            "eggs": "Inserted into leaf veins and leaf tissues.",
            "control": "Weed control and resistant varieties.",
            "pesticide": "Thiamethoxam or Imidacloprid"
        },
        "te": {
            "impact": "టుంగ్రో వైరస్ వ్యాప్తి వల్ల పంట నష్టం.",
            "eggs": "ఆకుల నరాల్లో గుడ్లు పెడతాయి.",
            "control": "కలుపు నియంత్రణ మరియు నిరోధక రకాలు.",
            "pesticide": "థియామెథోక్సామ్ లేదా ఇమిడాక్లోప్రిడ్"
        }
    },

    "Dragonfly": {
        "en": {
            "impact": "Beneficial predator that controls mosquitoes and rice pests.",
            "eggs": "Laid in or near water bodies, have aquatic nymph stage that lasts several months to years.",
            "control": "Protect aquatic habitats and avoid unnecessary pesticide use.",
            "pesticide": "Not applicable – beneficial insect"
        },
        "te": {
            "impact": "దోమలు మరియు పీడకాలను తిని పంటకు మేలు చేస్తుంది.",
            "eggs": "నీటిలో లేదా నీటి దగ్గర గుడ్లు పెట్టి దీర్ఘ నింఫ దశ ఉంటుంది.",
            "control": "జలవాతావరణాన్ని కాపాడాలి.",
            "pesticide": "వర్తించదు – ఉపకారక పురుగు"
        }
    },

    "Ladybird Beetle": {
        "en": {
            "impact": "Feeds on aphids and soft-bodied pests, highly beneficial.",
            "eggs": "Laid on leaves close to aphid colonies.",
            "control": "Avoid broad-spectrum insecticides.",
            "pesticide": "Not applicable – beneficial insect"
        },
        "te": {
            "impact": "ఆఫిడ్లను తిని పంటకు మేలు చేస్తుంది.",
            "eggs": "ఆహారం దగ్గర ఆకులపై గుడ్లు పెడతాయి.",
            "control": "విస్తృత మందులు నివారించాలి.",
            "pesticide": "వర్తించదు – ఉపకారక పురుగు"
        }
    },

    "Spider": {
        "en": {
            "impact": "Controls many pest species naturally and maintains balance.",
            "eggs": "Egg sacs are attached to plants or soil surface.",
            "control": "Maintain vegetation and avoid chemical sprays.",
            "pesticide": "Not applicable – beneficial organism"
        },
        "te": {
            "impact": "అనేక పీడకాలను సహజంగా నియంత్రిస్తుంది.",
            "eggs": "మొక్కలపై లేదా నేలపై గుడ్ల సంచులు ఉంటాయి.",
            "control": "కీటకనాశకాలు వాడకూడదు.",
            "pesticide": "వర్తించదు – ఉపకారక జీవి"
        }
    }
}
