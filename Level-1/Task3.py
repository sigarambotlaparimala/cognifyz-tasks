def is_valid_email(email):
    if " " in email:
        return False
    
    if email.count("@") != 1:
        return False
    
    local_part, domain_part = email.split("@")
    
    if not local_part or not domain_part:
        return False
    
    if "." not in domain_part:
        return False
    
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False
    
    if ".." in email:
        return False
    
    return True

email = input("Enter email: ")

if is_valid_email(email):
    print("Valid Email")
else:
    print("Invalid Email")