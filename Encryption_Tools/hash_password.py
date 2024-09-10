import hashlib

def hash_password(password: str, algorithm : str ='SHA256') -> str :
    hash_object = hashlib.new(algorithm)
    hash_object.update(password.encode('UTF-8'))
    return hash_object.hexdigest()

def main():
    password = input("Password : ")
    algorithm = input("SHA algorithm (e.g: SHA1, SHA256 or SHA512 )").lower()
    if algorithm not in hashlib.algorithms_available:
        print(f"{algorithm} is not recognized as valid algorithm from hashlib. \n")
        return

    hashed_password = hash_password(password, algorithm)
    print("\n--- Hashing Result ---")
    print(f"Password      : {password}")
    print(f"Algorithm     : {algorithm}")
    print(f"Hashed Output : {hashed_password}")

if __name__ == "__main__":
    main()