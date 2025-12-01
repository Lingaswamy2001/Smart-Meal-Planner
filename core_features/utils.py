import bcrypt

def hash_password(input_pw):
    password = input_pw.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password,salt).decode('utf-8')
    return hashed_password

def check_password(input_pw,db_pw):
    return bcrypt.checkpw(input_pw.encode('utf-8'),db_pw.encode('utf-8'))