#!/usr/bin/env python3

from data_structures import (
    get_names,
    get_spiciest_foods,
    print_spicy_foods,
    get_spicy_food_by_cuisine,
    average_heat_level,
)

def test_get_names():
    assert get_names(spicy_foods) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def test_get_spiciest_foods():
    assert get_spiciest_foods(spicy_foods) == [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
    ]

# Add similar test functions for other functions

# Make sure to import spicy_foods from data_structures.py
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]