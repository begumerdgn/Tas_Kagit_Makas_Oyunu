import random
import time

user_name = input("Adınız:").upper()
print(f"TAŞ, KAĞIT, MAKAS OYUNUNA HOŞGELDİN {user_name}!\n")


print("""Kurallar:
1. Oyun bilgisayara karşı oynanır.
2. Taş, kağıt, makastan birini seç.
3. Taş>Makas, Makas>Kağıt, Kağıt>Taş.
4. Yukarıdaki kurala göre kazanan belirlenir ya da beraberlik durumu olur.
5. 2 tur galibiyet puanı alan kazanır.\n""")

      
def tas_kagit_makas_Begüm_Erdoğan(choices):
    global computer_points, user_points, round_count
    
    
    while True:
        computer_points = 0
        user_points = 0
        round_count = 0
        answers = ['evet', 'hayır']
        user_selection = input("Oyunu oynamak istiyor musunuz?").lower()
        computer_selection = answers[random.randint(0,1)]
        
        
        if user_selection == "evet" and computer_selection == "evet":
            round_count += 1
            print("Oyun birazdan başlayacak")
            time.sleep(1) 
      
            
            while computer_points < 2 or user_points < 2:
                
            
                while True:
                   user_move = input("Taş, kağıt veya makastan birini seçiniz: ").lower()
                   time.sleep(1)
                   
                   
                   
                   if user_move in ["taş", "kağıt", "makas"]:
                       break
                   
                   else:
                       print("Lütfen geçerli bir seçenek giriniz.")
                   
                   
                computer_move = random.choice(choices)
                print("Bilgisayarın seçimi:", computer_move)
                
            
                if computer_move == user_move:
                    print("Berabere!")
                    
                elif user_move == "taş":
                    if computer_move == "makas":
                        print("Turu kazanan ", user_name + "!\n")
                        user_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                    else:
                        print("Turu kazanan bilgisayar!\n")
                        computer_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                        
                elif user_move == "kağıt":
                    if computer_move == "taş":
                        print("Turu kazanan ", user_name + "!\n")
                        user_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                    else:
                        print("Turu kazanan bilgisayar!\n")
                        computer_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                        
                elif user_move == "makas":
                    if computer_move == "kağıt":
                        print("Turu kazanan ", user_name + "!")
                        user_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                    else:
                        print("Turu kazanan bilgisayar!")
                        computer_points += 1
                        print(f"{user_name}: {user_points}\nbilgisayar: {computer_points}")
                        
                        
                if computer_points == 2:
                    print(round_count,". oyunu kazanan bilgisayar.")
                    time.sleep(1)
                    break
                
                elif user_points == 2:
                    print(round_count,". oyunu kazanan",user_name + ".")
                    time.sleep(1)
                    break
                
        
        elif computer_selection == "hayır" and user_selection == "evet":
            print("Bilgisayar oynamak istemiyor!")
            time.sleep(2)
            break
        
        elif (computer_selection == "evet" and user_selection == "hayır") or \
             (computer_selection == "hayır" and user_selection == "hayır"):
            print("Oyun başlamayacak. Güle Güle :)")
            time.sleep(2)
            break
        
        
choices = ['taş','kağıt','makas']
tas_kagit_makas_Begüm_Erdoğan(choices)
                
            
            
        
    
   
    

    
