def show_users(users_list: list[dict]) -> None:
    for user in users_list:
        print(f"{user['name']} {user['surname']}, obejrzane filmy i seriale: {user['watched movies']}, na {user['company']}")
