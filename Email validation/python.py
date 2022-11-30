def validate_email_id(email_id):
    c=email_id[-10:]
    if c=="@gmail.com":
        print("Valid")
    else:
        print("Invalid")
        
a=input()
validate_email_id(a)
