juggling = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('l','|'))
def strongify(password):
    '''
    Function to replace characters with similar looking ones to strengthen the password
    '''
    for a,b in juggling:
        password = password.replace(a,b)
    return password

    pass
if __name__ == "__main__":
    unsecure_pass = input("Enter intial Password: ")
    secure_pass = strongify(unsecure_pass)
    print(f'Possible Strengthened Password will be {secure_pass}')