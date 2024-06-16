from datetime import date

users: list[dict] = [
    {"name": "Grzegorz", "surname": "Gal", "count": 3, "company": "Netflix"},
    {"name": "Kamil", "surname": "Gil", "count": 9, "company": "Prime Videos"}
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
    {"client_name": "Kamil", "client_surname": "Gil", "service": "Prime Videos", "expiry_date": "2024 - 12 - 12"},
    {"client_name": "Grzegorz", "client_surname": "Gal", "service": "Netflix", "expiry_date": "2025 - 1 - 1"},
]
