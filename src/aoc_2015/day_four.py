from hashlib import md5

def find_value_for_key(secret_key,condition='00000'):
    found = False
    val = -1
    while not found:
        val += 1
        str = f'{secret_key}{val}'
        hash_value = md5(str.encode()).hexdigest()
        found = hash_value.startswith(condition)
    return val

if __name__ == "__main__":
    secret_key = 'bgvyzdsv'
    print(f'The value for the secret key {secret_key} is: {find_value_for_key(secret_key)}')
    print(f'The value starting with 6 zeroes for the secret key {secret_key} is: {find_value_for_key(secret_key, "000000")}')
