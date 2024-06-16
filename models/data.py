from datetime import date

users: list[dict] = [
    {"name": "Grzegorz", "surname": "Gal", "count": 3, "company": "Netflix"},
    {"name": "Kamil", "surname": "Gil", "count": 9, "company": "Prime Videos"},
    {"name": "Maciej", "surname": "Galant", "count": 12, "company": "YouTube"},
    {"name": "Piotr", "surname": "Frątczak", "count": 7, "company": "Prime Videos"},
    {"name": "Marek", "surname": "Dybowski", "count": 1, "company": "Netflix"}
]

companies: list[dict] = [
    {"name": "Netflix", "number of users": 256},
    {"name": "Prime Videos", "number of users": 144},
    {"name": "YouTube", "number of users": 1214},
    {"name": "HBO", "number of users": 1989},
    {"name": "StreamON", "number of users": 23655}
]

employees: list[dict] = [
    {"name": "Maciej", "surname": "Galant", "position": "dealer", "company": "Netflix"},
    {"name": "Piotr", "surname": "Frątczak", "position": "manager", "company": "Prime Videos"},
    {"name": "Grzegorz", "surname": "Gal", "position": "boss", "company": "HBO"},
    {"name": "Kamil", "surname": "Gil", "position": "producer", "company": "Prime Videos"},
    {"name": "Marek", "surname": "Dybowski", "position": "executive producer", "company": "YouTube"}
]

subscribers: list[dict] = [
    {"client_name": "Kamil", "client_surname": "Gil", "service": "Prime Videos", "expiry_date": "2024 - 12 - 12"},
    {"client_name": "Grzegorz", "client_surname": "Gal", "service": "Netflix", "expiry_date": "2025 - 1 - 1"},
    {"client_name": "Grzegorz", "client_surname": "Gal", "service": "Prime Videos", "expiry_date": "2025 - 7 - 31"},
    {"client_name": "Kamil", "client_surname": "Gil", "service": "YouTube Premium", "expiry_date": "2024 - 9 - 15"},
    {"client_name": "Maciej", "client_surname": "Galant", "service": "Spotify Premium", "expiry_date": "2025 - 6 - 17"},
    {"client_name": "Piotr", "client_surname": "Frątczak", "service": "HBO", "expiry_date": "2024 - 12 - 31"},
    {"client_name": "Piotr", "client_surname": "Frątczak", "service": "Prime Videos", "expiry_date": "2024 - 8 - 24"},
    {"client_name": "Kamil", "client_surname": "Gil", "service": "Spotify Premium", "expiry_date": "2026 - 5 - 2"}
]
