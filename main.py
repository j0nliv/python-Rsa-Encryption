ascii = []
def createAscii():
    for i in range(256):
        ascii.append(chr(i))
def findAsciiChar(num):
    char = ascii[num]
    return char
def findAsciiIndex(char):
    num = ascii.index(char)
    return num

def isPrimeNumber(number):
    if(number > 1):
        if(number > 5):
            if(number % 2 == 0 or number % 3 == 0 or number % 5 == 0):
                return False
            else:
                return True
        elif(number == 5 or number == 3 or number == 2):
            return True
        else:
            return False
    else:
        return False
def isAmongThemPrimeNumber(num1,num2):
    if((num1%2==num2%2) or (num1%3==num2%3) or (num1%5==num2%5)):
        return False
    elif(num1<=1 or num2 <= 1):
        return False
    else:
        return True

def extendedEuclid(e,totient):
    control = False
    i = 1
    while(control == False):
        if((e * i) % totient == 1):
            control = True
        else:
            i+=1
    return i

print("İki Adet Asal Sayı Giriniz. Sayıların büyüklüğü ile güvenlik doğru orantılıdır.")
p = int(input("1. Asal Sayıyı Girin: "))
q = int(input("2. Asal Sayıyı Girin: "))

while(isPrimeNumber(p) is False):
    p = int(input("1. Asal Sayıyı Girin:(Asal olduğundan emin olun)"))
while(isPrimeNumber(q) is False):
    q = int(input("2. Asal Sayıyı Girin:(Asal olduğundan emin olun)"))
    print(q)

n = p*q #modulus

totient = (p-1)*(q-1)
print("1 ile ",totient," arasında bir genel anahtar değeri seçin! Bu değerin ",totient," ile aralarında asal olması durumuna dikkat edin.")
e = int(input("Genel Anahtar: "))

while(isAmongThemPrimeNumber(e,totient) is False or e > totient or e <= 1):
    e = int(input("Hatalı giriş. Tekrar girin: "))
print("GENEL ANAHTAR-->",e,"<--")

d = extendedEuclid(e,totient)

password = input("Şifrelenecek Metni Girin: ")
crypto = ""
createAscii()

for i in password:
    m = findAsciiIndex(i)
    c = pow(m,e) % n
    crypto += findAsciiChar(c % 256)

print("ŞİFRELİ METİN-->",crypto,"<--")