import random
import pyfiglet

def password_generator():
    password_banner = pyfiglet.figlet_format("PASSWORD")
    generator_banner = pyfiglet.figlet_format("GENERATOR")
    print(password_banner)
    print(generator_banner)

    print('_'*50)
    password_lentgh = int(input('[ * ] Password Length: '))



    uppercase = [chr(i) for i in range(65, 91)]
    lowercase = [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]

    simbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
            '[', ']', '{', '}', '<', '>', '?']

    passwrd = uppercase + lowercase + numbers + simbols

    random_passwrd = ''.join(random.choice(passwrd) for _ in range(password_lentgh))

    return random_passwrd

def main():
    generated_passwrd = password_generator()
    print(f"[ * ] Password generated: {generated_passwrd}")

if __name__ == '__main__':
    main()
