from models.data import users, companies, employees, subscribers
from utils.crud import (show_users, add_new_user, delete_user, update_user,
                        show_company, add_new_company, delete_company,
                        update_company, show_employees, add_new_employee,
                        delete_employee, update_employee, show_company_users,
                        show_company_employees, show_client_subscriptions,
                        map_all_companies, map_all_users, map_all_employees)


def login_system():
    print("Zaloguj się do systemu")
    username = input("Podaj login: ")
    password = input("Podaj hasło: ")
    if username == "" and password == "":
        print("Logowanie udane!")
        return True
    else:
        print("Błędny login lub hasło.")
        return False


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
            print("16. Wyświetl mapę wszystkich firm streamingowych")
            print("17. Wyświetl mapę wszystkich użytkowników)")
            print("18. Wyświetl mapę wszystkich pracowników)")

            menu_option: str = input("Dokonaj wyboru:")
            if menu_option == "0":
                print("Program kończy pracę.")
                break
            if menu_option == "1":
                show_users(users)
            if menu_option == "2":
                add_new_user(users)
            if menu_option == "3":
                delete_user(users)
            if menu_option == "4":
                update_user(users)
            if menu_option == "5":
                show_company(companies)
            if menu_option == "6":
                add_new_company(companies)
            if menu_option == "7":
                delete_company(companies)
            if menu_option == "8":
                update_company(companies)
            if menu_option == "9":
                show_employees(employees)
            if menu_option == "10":
                add_new_employee(employees)
            if menu_option == "11":
                delete_employee(employees)
            if menu_option == "12":
                update_employee(employees)
            if menu_option == "13":
                show_company_users(users)
            if menu_option == "14":
                show_company_employees(employees)
            if menu_option == "15":
                show_client_subscriptions(subscribers)
            if menu_option == "16":
                map_all_companies(companies)
            if menu_option == "17":
                map_all_users(users)
            if menu_option == "18":
                map_all_employees(employees)
