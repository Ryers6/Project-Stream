from models.data import users
from utils.crud import show_users


def login_system():
    print("Zaloguj się do systemu")
    username = input("Podaj login: ")
    password = input("Podaj hasło: ")
    if username == "1" and password == "1":
        print("Logowanie udane!")
        return True
    else:
        print("Błędny login lub hasło.")
        return False


# login_system()


if __name__ == "__main__":
    if login_system():
        while True:
            print("Menu:")
            print("0. Zakończ program")
            print("1. Wyświetl użytkowników")
            print("2. Dodaj użytkownika")
            print("3. Usuń użytkownika")
            print("4. Aktualizuj użytkownika")
            print("5. Wyświelt firmy streamingowe")
            print("6. Dodaj firmę streamingową")
            print("7. Usuń firmę streamingową")
            print("8. Aktualizuj firmę streamingową")
            print("9. Wyświetl pracowników")
            print("10. Dodaj pracownika")
            print("11. Usuń pracownika")
            print("12. Aktualizuj pracownika")
            print("13. Wyświetl użytkowników danej firmy")
            print("14. Wyświetl pracowników danej firmy")
            print("15. Wyświetl subskrypcje danego klienta")

            menu_option: str = input("Dokonaj wyboru:")
            if menu_option == "0":
                print("Program kończy pracę.")
                break
            if menu_option == "1":
                show_users(users)
