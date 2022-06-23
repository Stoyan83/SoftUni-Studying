class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]

email = input()

while email != "End":
    email_parts = email.split("@")
    user_name = email_parts[0]
    domain_name_extension = email_parts[-1]
    extension = domain_name_extension.split(".")

    if len(user_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if len(email_parts) <= 1:
        raise MustContainAtSymbolError("Email must contain @")
    if len(extension) <= 1 or extension[-1] not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")
    email = input()
