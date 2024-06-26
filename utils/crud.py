import folium
import requests
from bs4 import BeautifulSoup


def show_users(users_list: list[dict]) -> None:
    for user in users_list:
        print(
            f"{user['name']} {user['surname']}, obejrzane filmy i seriale: {user['count']} na {user['company']}")


def add_new_user(users: list) -> None:
    new_name = input("Wprowadź imię: ")
    new_surname = input("Wprowadź nazwisko: ")
    new_count = input("Ile filmów i seriali obejrzałaś/eś?: ")
    company = input("Platforma?: ")
    new_user = {"name": new_name, "surname": new_surname, "count": new_count, "company": company}
    users.append(new_user)


def delete_user(users: list) -> None:
    user_name = input("Kogo szukasz? (imię i nazwisko): ")
    for user in users:
        if f"{user['name']} {user['surname']}" == user_name:
            users.remove(user)


def update_user(users: list) -> None:
    user_name = input("Kogo szukasz? (imię i nazwisko): ")
    for user in users:
        if f"{user['name']} {user['surname']}" == user_name:
            user['name'] = input("Wprowadź nowe imię: ")
            user['surname'] = input("Wprowadź nowe nazwisko: ")
            user['count'] = input("Wprowadź aktualną liczbę obejrzeń: ")
            user['company'] = input("Platforma?: ")
            break


def show_company(companies_list: list[dict]) -> None:
    for company in companies_list:
        print(f"{company['name']}, liczba użytkowników: {company['number of users']}")


def add_new_company(companies: list) -> None:
    new_company_name = input("Wprowadź nazwę firmy: ")
    comapny_NOU = input("Ile użytkowników: ")
    new_company = {"name": new_company_name, "number of users": comapny_NOU}
    companies.append(new_company)


def delete_company(companies: list) -> None:
    company_name = input("Której firmy szukasz?: ")
    for company in companies:
        if company['name'] == company_name:
            companies.remove(company)


def update_company(companies: list) -> None:
    company_name = input("Którą firmę chcesz zaktualizować?: ")
    for company in companies:
        if company['name'] == company_name:
            company['name'] = input("Wprowadź nową nazwę firmy: ")
            company['number of users'] = input("Wprowadź nową liczbę użytkowników: ")
            break


def show_employees(employees_list: list[dict]) -> None:
    for employee in employees_list:
        print(f"{employee['name']} {employee['surname']} jako {employee['position']} w {employee['company']}")


def add_new_employee(employees: list) -> None:
    new_employee_name = input("Wprowadź imię nowego pracownika: ")
    new_employee_surname = input("Wprowadź nazwisko: ")
    new_employee_position = input("Wprowadź stanowisko pracownika: ")
    new_employee_company = input("W jakiej firmie bedzie pracowac?: ")
    new_employee = {'name': new_employee_name, 'surname': new_employee_surname, 'position': new_employee_position,
                    'company': new_employee_company}
    employees.append(new_employee)


def delete_employee(employees: list) -> None:
    employee_name = input("Którego pracownika szukasz? (imię i nazwisko): ")
    for employee in employees:
        if f"{employee['name']} {employee['surname']}" == employee_name:
            employees.remove(employee)


def update_employee(employees: list) -> None:
    employee_name = input("Którego pracownika chcesz zaktualizować? (imię i nazwisko): ")
    for employee in employees:
        if f"{employee['name']} {employee['surname']}" == employee_name:
            employee['name'] = input("Wprowadź nowe imię pracownika: ")
            employee['surname'] = input("Wprowadź nowe nazwisko pracownika: ")
            employee['position'] = input("Wprowadź nowe stanowisko pracownika: ")
            employee['company'] = input("Wprowadź nową platformę?: ")
            break


def show_company_users(users: list[dict]) -> None:
    company_name = input("Wprowadź nazwę firmy: ")
    company_users = [user for user in users if user['company'] == company_name]
    for user in company_users:
        print(f"Użytkownik: {user['name']} {user['surname']}, obejrzane filmy i seriale: {user['count']}")


def show_company_employees(employees: list[dict]) -> None:
    company_name = input("Wprowadź nazwę firmy: ")
    company_employees = [employee for employee in employees if employee['company'] == company_name]
    for employee in company_employees:
        print(f"Pracownik: {employee['name']} {employee['surname']} jako {employee['position']}")


def show_client_subscriptions(subscribers: list[dict]) -> None:
    client_name = input("Wprowadź imię subskrybenta (imię i nazwisko): ")
    for client in subscribers:
        if f"{client['client_name']} {client['client_surname']}" == client_name:
            print(
                f"Klient: {client['client_name']} {client['client_surname']} posiada subskrypcje: {client['service']} do {client['expiry_date']}")

def map_all_companies(companies):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for company in companies:
        url = (f"https://pl.wikipedia.org/wiki/{company['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{company['name']},\n{company['location']}",
                      icon=folium.Icon(color='green')).add_to(map)

    map.save('models/maps/map_companies.html')

def map_all_users(users):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for user in users:
        url = (f"https://pl.wikipedia.org/wiki/{user['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{user['name']},\n{user['location']}",
                      icon=folium.Icon(color='red')).add_to(map)

    map.save('models/maps/map_users.html')

def map_all_employees(employees):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for employee in employees:
        url = (f"https://pl.wikipedia.org/wiki/{employee['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{employee['name']},\n{employee['location']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save('models/maps/map_employees.html')
