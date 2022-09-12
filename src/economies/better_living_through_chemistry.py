from economy import Economy

economy = Economy(
    id="BETTER_LIVING_THROUGH_CHEMISTRY",
    numeric_id=2,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "alcohol",
        "mail",
        "aluminium",
        "ammonia",
        "ammonium_nitrate",
        "chlorine",
        "cleaning_agents",
        "copper",
        "electrical_parts",
        "engineering_supplies",
        "food",  # must be in slot 11
        "ethylene",
        "explosives",
        "farm_supplies",
        "fish",
        "food_additives",
        "furniture",
        "glass",
        "grain",
        "hydrochloric_acid",
        "limestone",
        "livestock",
        "timber",
        "lye",
        "milk",
        "methanol",
        "naphtha",
        "oil",
        "packaging",
        "paints_and_coatings",
        "petrol",
        "phosphate",
        "phosphoric_acid",
        "plant_fibres",  # should be cotton?
        "plastics",
        "potash",
        "propylene",
        "rubber",  # includes synthetic rubber, export only
        "salt",
        "sand",
        "soda_ash",
        "steel",
        "sulphur",
        "sulphuric_acid",
        "textiles",
        "tinplate",
        "urea",
        "vehicles",
    ],
)
