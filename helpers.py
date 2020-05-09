pops_required = 80

city_district_base = {
    "housing": 0,
    "amenities": 0,
    "energy": 0,
    "minerals": 0,
    "food": 0,
    "trade": 0,
    "goods": 0,
    "alloys": 0,
    "influence": 0,
    "unity": 0,
    "physics": 0,
    "society": 0,
    "engineering": 0,
    "motes": 0,
    "gases": 0,
    "crystals": 0,
    "metals": 0,
    "zro": 0,
    "matter": 0,
    "nanites": 0,
    "admin": 0,
    "naval": 0,
}

city_district_jobs = {
    "housing": 0,
    "amenities": 0,
    "energy": 0,
    "minerals": 0,
    "food": 0,
    "trade": 0,
    "goods": 0,
    "alloys": 0,
    "influence": 0,
    "unity": 0,
    "physics": 0,
    "society": 0,
    "engineering": 0,
    "motes": 0,
    "gases": 0,
    "crystals": 0,
    "metals": 0,
    "zro": 0,
    "matter": 0,
    "nanites": 0,
    "admin": 0,
    "naval": 0,
}

city_district_production = {
    "housing": city_district_base["housing"] + city_district_clerks * clerk_housing,
    "amenities": city_district_base["amenities"] + city_district_clerks * clerk_amenities,
    "energy": city_district_base["energy"] + city_district_clerks * clerk_energy,
    "minerals": city_district_base["minerals"] + city_district_clerks * clerk_minerals,
    "food": city_district_base["food"] + city_district_clerks * clerk_food,
    "trade": city_district_base["trade"] + city_district_clerks * clerk_trade,
    "goods": city_district_base["goods"] + city_district_clerks * clerk_goods,
    "alloys": city_district_base["alloys"] + city_district_clerks * clerk_alloys,
    "influence": city_district_base["influence"] + city_district_clerks * clerk_influence,
    "unity": city_district_base["unity"] + city_district_clerks * clerk_unity,
    "physics": city_district_base["physics"] + city_district_clerks * clerk_physics,
    "society": city_district_base["society"] + city_district_clerks * clerk_society,
    "engineering": city_district_base["engineering"] + city_district_clerks * clerk_engineering,
    "motes": city_district_base["motes"] + city_district_clerks * clerk_motes,
    "gases": city_district_base["gases"] + city_district_clerks * clerk_gases,
    "crystals": city_district_base["crystals"] + city_district_clerks * clerk_crystals,
    "metals": city_district_base["metals"] + city_district_clerks * clerk_metals,
    "zro": city_district_base["zro"] + city_district_clerks * clerk_zro,
    "matter": city_district_base["matter"] + city_district_clerks * clerk_matter,
    "nanites": city_district_base["nanites"] + city_district_clerks * clerk_nanites,
    "admin": city_district_base["admin"] + city_district_clerks * clerk_admin,
    "naval": city_district_base["naval"] + city_district_clerks * clerk_naval,
}
generator_district_production = {
    "housing": generator_district_housing
    + generator_district_technicians * technician_housing,
    "amenities": generator_district_amenities
    + generator_district_technicians * technician_amenities,
    "energy": generator_district_energy
    + generator_district_technicians * technician_energy,
    "minerals": generator_district_minerals
    + generator_district_technicians * technician_minerals,
    "food": generator_district_food + generator_district_technicians * technician_food,
    "trade": generator_district_trade
    + generator_district_technicians * technician_trade,
    "goods": generator_district_goods
    + generator_district_technicians * technician_goods,
    "alloys": generator_district_alloys
    + generator_district_technicians * technician_alloys,
    "influence": generator_district_influence
    + generator_district_technicians * technician_influence,
    "unity": generator_district_unity
    + generator_district_technicians * technician_unity,
    "physics": generator_district_physics
    + generator_district_technicians * technician_physics,
    "society": generator_district_society
    + generator_district_technicians * technician_society,
    "engineering": generator_district_engineering
    + generator_district_technicians * technician_engineering,
    "motes": generator_district_motes
    + generator_district_technicians * technician_motes,
    "gases": generator_district_gases
    + generator_district_technicians * technician_gases,
    "crystals": generator_district_crystals
    + generator_district_technicians * technician_crystals,
    "metals": generator_district_metals
    + generator_district_technicians * technician_metals,
    "zro": generator_district_zro + generator_district_technicians * technician_zro,
    "matter": generator_district_matter
    + generator_district_technicians * technician_matter,
    "nanites": generator_district_nanites
    + generator_district_technicians * technician_nanites,
    "admin": generator_district_admin
    + generator_district_technicians * technician_admin,
    "naval": generator_district_naval
    + generator_district_technicians * technician_naval,
}
mining_district_production = {
    "housing": mining_district_housing + mining_district_miners * miner_housing,
    "amenities": mining_district_amenities + mining_district_miners * miner_amenities,
    "energy": mining_district_energy + mining_district_miners * miner_energy,
    "minerals": mining_district_minerals + mining_district_miners * miner_minerals,
    "food": mining_district_food + mining_district_miners * miner_food,
    "trade": mining_district_trade + mining_district_miners * miner_trade,
    "goods": mining_district_goods + mining_district_miners * miner_goods,
    "alloys": mining_district_alloys + mining_district_miners * miner_alloys,
    "influence": mining_district_influence + mining_district_miners * miner_influence,
    "unity": mining_district_unity + mining_district_miners * miner_unity,
    "physics": mining_district_physics + mining_district_miners * miner_physics,
    "society": mining_district_society + mining_district_miners * miner_society,
    "engineering": mining_district_engineering
    + mining_district_miners * miner_engineering,
    "motes": mining_district_motes + mining_district_miners * miner_motes,
    "gases": mining_district_gases + mining_district_miners * miner_gases,
    "crystals": mining_district_crystals + mining_district_miners * miner_crystals,
    "metals": mining_district_metals + mining_district_miners * miner_metals,
    "zro": mining_district_zro + mining_district_miners * miner_zro,
    "matter": mining_district_matter + mining_district_miners * miner_matter,
    "nanites": mining_district_nanites + mining_district_miners * miner_nanites,
    "admin": mining_district_admin + mining_district_miners * miner_admin,
    "naval": mining_district_naval + mining_district_miners * miner_naval,
}
agriculture_district_production = {
    "housing": agriculture_district_housing
    + agriculture_district_farmers * farmer_housing,
    "amenities": agriculture_district_amenities
    + agriculture_district_farmers * farmer_amenities,
    "energy": agriculture_district_energy
    + agriculture_district_farmers * farmer_energy,
    "minerals": agriculture_district_minerals
    + agriculture_district_farmers * farmer_minerals,
    "food": agriculture_district_food + agriculture_district_farmers * farmer_food,
    "trade": agriculture_district_trade + agriculture_district_farmers * farmer_trade,
    "goods": agriculture_district_goods + agriculture_district_farmers * farmer_goods,
    "alloys": agriculture_district_alloys
    + agriculture_district_farmers * farmer_alloys,
    "influence": agriculture_district_influence
    + agriculture_district_farmers * farmer_influence,
    "unity": agriculture_district_unity + agriculture_district_farmers * farmer_unity,
    "physics": agriculture_district_physics
    + agriculture_district_farmers * farmer_physics,
    "society": agriculture_district_society
    + agriculture_district_farmers * farmer_society,
    "engineering": agriculture_district_engineering
    + agriculture_district_farmers * farmer_engineering,
    "motes": agriculture_district_motes + agriculture_district_farmers * farmer_motes,
    "gases": agriculture_district_gases + agriculture_district_farmers * farmer_gases,
    "crystals": agriculture_district_crystals
    + agriculture_district_farmers * farmer_crystals,
    "metals": agriculture_district_metals
    + agriculture_district_farmers * farmer_metals,
    "zro": agriculture_district_zro + agriculture_district_farmers * farmer_zro,
    "matter": agriculture_district_matter
    + agriculture_district_farmers * farmer_matter,
    "nanites": agriculture_district_nanites
    + agriculture_district_farmers * farmer_nanites,
    "admin": agriculture_district_admin + agriculture_district_farmers * farmer_admin,
    "naval": agriculture_district_naval + agriculture_district_farmers * farmer_naval,
}

capital_building_production = {
    "housing": capital_building_housing
    + capital_building_administrators * administrator_housing
    + capital_building_enforcers * enforcer_housing,
    "amenities": capital_building_amenities
    + capital_building_administrators * administrator_amenities
    + capital_building_enforcers * enforcer_housing,
    "energy": capital_building_energy
    + capital_building_administrators * administrator_energy
    + capital_building_enforcers * enforcer_housing,
    "minerals": capital_building_minerals
    + capital_building_administrators * administrator_minerals
    + capital_building_enforcers * enforcer_housing,
    "food": capital_building_food
    + capital_building_administrators * administrator_food
    + capital_building_enforcers * enforcer_housing,
    "trade": capital_building_trade
    + capital_building_administrators * administrator_trade
    + capital_building_enforcers * enforcer_housing,
    "goods": capital_building_goods
    + capital_building_administrators * administrator_goods
    + capital_building_enforcers * enforcer_housing,
    "alloys": capital_building_alloys
    + capital_building_administrators * administrator_alloys
    + capital_building_enforcers * enforcer_housing,
    "influence": capital_building_influence
    + capital_building_administrators * administrator_influence
    + capital_building_enforcers * enforcer_housing,
    "unity": capital_building_unity
    + capital_building_administrators * administrator_unity
    + capital_building_enforcers * enforcer_housing,
    "physics": capital_building_physics
    + capital_building_administrators * administrator_physics
    + capital_building_enforcers * enforcer_housing,
    "society": capital_building_society
    + capital_building_administrators * administrator_society
    + capital_building_enforcers * enforcer_housing,
    "engineering": capital_building_engineering
    + capital_building_administrators * administrator_engineering
    + capital_building_enforcers * enforcer_housing,
    "motes": capital_building_motes
    + capital_building_administrators * administrator_motes
    + capital_building_enforcers * enforcer_housing,
    "gases": capital_building_gases
    + capital_building_administrators * administrator_gases
    + capital_building_enforcers * enforcer_housing,
    "crystals": capital_building_crystals
    + capital_building_administrators * administrator_crystals
    + capital_building_enforcers * enforcer_housing,
    "metals": capital_building_metals
    + capital_building_administrators * administrator_metals
    + capital_building_enforcers * enforcer_housing,
    "zro": capital_building_zro
    + capital_building_administrators * administrator_zro
    + capital_building_enforcers * enforcer_housing,
    "matter": capital_building_matter
    + capital_building_administrators * administrator_matter
    + capital_building_enforcers * enforcer_housing,
    "nanites": capital_building_nanites
    + capital_building_administrators * administrator_nanites
    + capital_building_enforcers * enforcer_housing,
    "admin": capital_building_admin
    + capital_building_administrators * administrator_admin
    + capital_building_enforcers * enforcer_housing,
    "naval": capital_building_naval
    + capital_building_administrators * administrator_naval
    + capital_building_enforcers * enforcer_housing,
}

possible_colony_designations = [
    {
        "name": "empire capital",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "urban world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "mining world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.2,
        "food_multiplier": 1.0,
    },
    {
        "name": "agri world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.2,
    },
    {
        "name": "generator world",
        "energy_multiplier": 1.2,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "forge world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "industrial world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "refinery world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "tech world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "fortress world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "rural world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "bureaucratic world",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
]
