import hashlib

def hash_password(password: str, algorithm : str ='SHA256') -> str :
    """
       Hashes a given password using the specified SHA algorithm.

       Args:
           password (str): The password to hash.
           algorithm (str): The SHA algorithm to use for hashing (default is 'SHA256').

       Returns:
           str: The hexadecimal representation of the hashed password.
    """
    hash_object = hashlib.new(algorithm)
    hash_object.update(password.encode('UTF-8'))

    return hash_object.hexdigest()

def main():
    """
       Main function to prompt the user for input and display the hashed password.
    """
    password = input("Password : ")
    algorithm = input("SHA algorithm (e.g: SHA1, SHA256 or SHA512 )").lower()

    if algorithm not in hashlib.algorithms_available:
        print(f"{algorithm} is not recognized as valid algorithm from hashlib. \n")
        return

    # Hashes the password, then display the output
    hashed_password = hash_password(password, algorithm)
    print("\n--- Hashing Result ---")

    print(f"Password      : {password}")
    print(f"Algorithm     : {algorithm}")
    print(f"Hashed Output : {hashed_password}")

if __name__ == "__main__":
    main()