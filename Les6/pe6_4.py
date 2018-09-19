def new_password(oldpassword, newpassword):
    return (oldpassword != newpassword) and (len(newpassword) >= 6) and (any(check.isdigit() for check in newpassword))


print(new_password('Password1', 'SuperGoodNewPassword321'))
