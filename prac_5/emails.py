def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_email_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_email_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name
# this function will take the users name from the email and place it at the begging.


main()