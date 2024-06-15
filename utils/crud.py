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
    user_name = input("Kogo szukasz?: ")
    for user in users:
        if user["name"] == user_name:
            users.remove(user)
