import random 
import string

def gerador_senhas(lenght):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(lenght))
    return senha

# Defina o comprimento da senha

senha_tamanho = 8
nova_senha = gerador_senhas(senha_tamanho)

print(f'Senha gerada: {nova_senha}')


'''
    Explicação:

    Importações:

        Importamos a biblioteca random e o módulo string para facilitar o uso de caracteres.

    Função generate_password:

        Combina letras maiúsculas, minúsculas, dígitos e caracteres de pontuação.

        Usa random.choice para selecionar caracteres aleatórios até atingir o comprimento desejado.

    Geração de Senha:

        Define o comprimento da senha.

        Chama a função para gerar a senha e imprime o resultado.

'''

import random
import string

def validate_password(password, use_uppercase, use_lowercase, use_digits, use_symbols):
    has_upper = any(char.isupper() for char in password) if use_uppercase else True
    has_lower = any(char.islower() for char in password) if use_lowercase else True
    has_digit = any(char.isdigit() for char in password) if use_digits else True
    has_symbol = any(char in string.punctuation for char in password) if use_symbols else True
    valid_length = len(password) >= 6

    return all([has_upper, has_lower, has_digit, has_symbol, valid_length])

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True, max_attempts=1000):
    if length < 6:
        raise ValueError("O comprimento mínimo da senha deve ser 6.")

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    attempts = 0

    while True:
        attempts += 1
        if attempts > max_attempts:
            raise ValueError("Não foi possível gerar uma senha válida com as configurações fornecidas. Tente ajustar as opções de caracteres.")
        
        password = ''.join(random.choice(characters) for i in range(length))
        if validate_password(password, use_uppercase, use_lowercase, use_digits, use_symbols):
            return password

def main():
    print("Gerador de Senhas")
    while True:
        try:
            length = input("Digite o comprimento desejado da senha (mínimo 6): ")

            # Validação da entrada do usuário para garantir que seja um número inteiro válido
            if not length.isnumeric():
                print("O comprimento da senha deve ser um número inteiro.")
                continue

            length = int(length)

            if length < 6:
                print("O comprimento da senha deve ser um número inteiro maior ou igual a 6.")
                continue
            
            break  # Saia do loop se o comprimento da senha for válido
        except ValueError as e:
            print(e)
    
    # Agora pergunte sobre as preferências de caracteres
    use_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    use_lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    use_digits = input("Incluir números? (s/n): ").lower() == 's'
    use_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'

    try:
        new_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"Senha gerada: {new_password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
