from datetime import date

users: list[dict] = [
    {"name": "Grzegorz", "surname": "Gal", "watched movies": 3, "company": "Netflix"},
    {"name": "Kamil", "surname": "Gil", "watched movies": 9, "company": "Prime Videos"}
]

companies: list[dict] = [
    {"name": "Netflix", "number of users": 256},
    {"name": "Prime Videos", "number of users": 144},
]

employees: list[dict] = [
    {"name": "Maciej", "surname": "Galant", "position": "dealer", "company": "Netflix"},
    {"name": "Piotr", "surname": "Frątczak", "position": "manager", "company": "Prime Videos"}
]

subscribers: list[dict] = [
    {"client name": "Kamil", "client surname": "Gil", "service": "Prime Videos", "expiry date": "2024 - 12 - 12"},
    {"client name": "Grzegorz", "client surname": "Gal", "service": "Netflix", "expiry date": "2025 - 1 - 1"},
]
