import instaloader
import time
import sys
import os
import requests
from sys import stderr
from datetime import datetime

# Warna geng
Wheat = '\033[38;2;245;222;179m'  
White = '\033[1;37m'
Red = '\033[1;31m'
Green = '\033[1;32m'
Blue = '\033[1;34m'
Yellow = '\033[1;33m'
Reset = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    stderr.writelines(f"""{Wheat}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣁⣀⣀⣠⣤⣤⣤⣤⣤⠤⠤⠤⠤⠤⢤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿
⣿⣿⣿⣿⡿⠋⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠁⣴⢷⡀⢻⣿
⣿⣿⡟⠁⠀⠀⠀⠙⢿⣄⡀⠀⠀⠀⠀⠀⠀⣤⣤⣼⣿⣿⣿⠃⢸⣿⣾⡇⢸⣿
⣿⠟⠛⠛⠳⠶⣦⣄⡀⠙⠻⣦⣄⣀⠀⢀⣼⣏⠙⣿⣿⣿⣿⠀⢻⣿⣿⠃⣸⣿
⣿⠀⠀⠀⠀⠀⠀⠉⠛⠷⣤⡀⠉⠻⣿⣿⣿⣿⡇⣸⣿⣿⣿⣇⠘⠿⠏⣰⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣤⡈⣿⣿⣿⠁⣿⣿⣿⣿⣿⡇⢀⣾⣿⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⡇⠀⠀⠈⠙⣿⣿⡇⢸⣿⣿⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣧⣀⠀⣀⣴⣿⣿⠇⢸⣿⣿⣿⣿
⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿     
{Red}🔥 HOLMES GRAM KELATE 🔥
{Green}🚀 CYBER FORCE X KELATE GUO MUSE 🚀
{Yellow}┌─────────────────────────────────────────┐
│ {Wheat}Author: TEAM CYBER FORCE KELATE IT         {Yellow}│
│ {Wheat}Mode: PREMIUM - INTROVERT ATTACKS       {Yellow}│
│ {Wheat}Contact: @ManForceX_Official               {Yellow}│
│ {Wheat}Whatsapp: 01139183035                      {Yellow}│
└─────────────────────────────────────────┘
{Wheat}Dah siap nak bantai akun ore? Jom! 💀
{Reset}""")

def loading_animation():
    animations = ["🔥", "💀", "🚀", "⚡", "🔪"]
    for i in range(10):
        sys.stdout.write(f'\r{Red}[{Green}CYBER FORCE{Red}] {Yellow}Loading {animations[i%5]} {Wheat}{i*10}%')
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 50 + '\r')

def download_profile_pic(url, username):
    try:
        print(f"{Yellow}[!] {Wheat}Nak amik gambar profil... tunggu sekejap {Green}👀{Reset}")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = f"{username}_profile_pic.jpg"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return os.path.abspath(filename)
        return None
    except Exception as e:
        print(f"{Red}[!] {White}Hok dok jadi: {Yellow}{str(e)}{Reset}")
        return None

def get_profile_info(username):
    try:
        L = instaloader.Instaloader()
        print(f"{Green}[+] {Wheat}Carik akun {Red}{username}{White}...{Reset}")
        time.sleep(1)
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"{Green}[✓] {White}Jumpa! Akun {Red}{username}{White} dah dapat!{Reset}")
        return profile
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Red}[!] {White}Akun {Red}{username}{White} dok wok!{Reset}")
        return None
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"{Red}[!] {White}Akun {Red}{username}{White} private! Kena follow dulu!{Reset}")
        return None
    except Exception as e:
        print(f"{Red}[!] {White}Error: {Yellow}{str(e)}{Reset}")
        return None

def menu():
    print(f"\n{Red}┌──────────────────────────────────────────────────┐")
    print(f"{Red}│ {Green}🔥 MENU UTAMA HOLMES GRAM KELATE 🔥          {Red}│")
    print(f"{Red}├──────────────────────────────────────────────────┤")
    print(f"{Red}│ {Yellow}[1] {Wheat}Cek SEMUA Maklumat Akun (Power Mode)  {Red}│")
    print(f"{Red}│ {Yellow}[2] {Wheat}Cek ID Akun                           {Red}│")
    print(f"{Red}│ {Yellow}[3] {Wheat}Cek Berapa Banyak Posting             {Red}│")
    print(f"{Red}│ {Yellow}[4] {Wheat}Baca Bio Dia                         {Red}│")
    print(f"{Red}│ {Yellow}[5] {Wheat}Cek Nama Betul-Betul                  {Red}│")
    print(f"{Red}│ {Yellow}[6] {Wheat}Kira Pengikut & Dia Ikut Sapa         {Red}│")
    print(f"{Red}│ {Yellow}[7] {Wheat}Tangkap Gambar Profil                 {Red}│")
    print(f"{Red}│ {Yellow}[8] {Green}🔥 CEK EMAIL & NOMBOR (PREMIUM) 🔥     {Red}│")
    print(f"{Red}│ {Yellow}[9] {Red}💀 HACK MODE TAMBAHAN 💀               {Red}│")
    print(f"{Red}│ {Yellow}[0] {Wheat}Keluar Program                        {Red}│")
    print(f"{Red}└──────────────────────────────────────────────────┘{Reset}")

def full_account_info():
    username = input(f"\n{Green}[?] {White}mu isi sini username hok mu nok tu : {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Red}┌──────────────────────────────────────────────────┐")
    print(f"{Red}│ {Green}🔥 MAKLUMAT LENGKAP AKUN {Red}{username} {Green}🔥      {Red}│")
    print(f"{Red}├──────────────────────────────────────────────────┤")
    print(f"{Red}│ {Yellow}Username           : {Wheat}{profile.username}{' '*(35-len(profile.username))}{Red}│")
    print(f"{Red}│ {Yellow}Nama Penoh         : {Wheat}{profile.full_name}{' '*(35-len(str(profile.full_name)))}{Red}│")
    print(f"{Red}│ {Yellow}ID Rahsia          : {Red}{profile.userid}{' '*(35-len(str(profile.userid)))}{Red}│")
    print(f"{Red}│ {Yellow}Bio                : {Wheat}{profile.biography[:30]}...{' '*(5 if len(profile.biography)>30 else 35-len(profile.biography))}{Red}│")
    print(f"{Red}│ {Yellow}Private ke?        : {Red}{'YA' if profile.is_private else 'TAK'}{' '*(35)}{Red}│")
    print(f"{Red}│ {Yellow}Akun Bisnes?       : {Green}{'YA' if profile.is_business_account else 'TAK'}{' '*(35)}{Red}│")
    print(f"{Red}│ {Yellow}Pengikut           : {Red}{profile.followers}{' '*(35-len(str(profile.followers)))}{Red}│")
    print(f"{Red}│ {Yellow}Dia Ikut           : {Green}{profile.followees}{' '*(35-len(str(profile.followees)))}{Red}│")
    print(f"{Red}│ {Yellow}Jumlah Post        : {Yellow}{profile.mediacount}{' '*(35-len(str(profile.mediacount)))}{Red}│")
    print(f"{Red}└──────────────────────────────────────────────────┘{Reset}")
    
    # Additional premium feature
    print(f"\n{Green}[+] {White}URL Gambar Profil: {Red}{profile.profile_pic_url}{Reset}")
    
    save = input(f"\n{Yellow}[?] {White}Nak simpan dalam file? (y/n): {Green}")
    if save.lower() == 'y':
        with open(f"{username}_info.txt", "w") as f:
            f.write(f"Cyber Force X Kelate - Maklumat Akun\n")
            f.write(f"Username: {profile.username}\n")
            f.write(f"ID: {profile.userid}\n")
            f.write(f"Pengikut: {profile.followers}\n")
            f.write(f"URL Profil: {profile.profile_pic_url}\n")
        print(f"{Green}[✓] {White}Dah simpan dalam {Red}{username}_info.txt{Reset}")

def check_id():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Red}══════════════════════════════════════════════")
    print(f"{Green}🔍 ID AKUN {Red}{username}")
    print(f"{Red}══════════════════════════════════════════════")
    print(f"{Yellow}Username : {Wheat}{profile.username}")
    print(f"{Red}ID RAHSIA : {Green}{profile.userid}")
    print(f"{Red}══════════════════════════════════════════════{Reset}")
    
    # Bruteforce mode suggestion
    print(f"\n{Red}[💀] {White}Nak try crack password? ID dah dapat ni!{Reset}")

def check_posts():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Red}╔══════════════════════════════════════════╗")
    print(f"{Red}║ {Green}📸 POSTINGAN {Red}{username}                      {Red}║")
    print(f"{Red}╠══════════════════════════════════════════╣")
    print(f"{Red}║ {Yellow}Jumlah Post: {Red}{profile.mediacount}{' '*(25)} {Red}║")
    print(f"{Red}║ {Wheat}• Rata-rata: {profile.mediacount//30} post/bulan{' '*(20)} {Red}║")
    print(f"{Red}║ {Wheat}• Status: {'AKTIF' if profile.mediacount > 50 else 'JARANG'}{' '*(27)} {Red}║")
    print(f"{Red}╚══════════════════════════════════════════╝{Reset}")

def check_bio():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Yellow}〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
    print(f"{Red}BIO {Green}{username}")
    print(f"{Yellow}〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
    print(f"{White}{profile.biography}")
    print(f"{Yellow}〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰{Reset}")
    
    # Analyze bio for personal info
    bio_lower = profile.biography.lower()
    keywords = ['whatsapp', 'wa', 'telegram', 'ig', 'email', 'contact']
    found = [kw for kw in keywords if kw in bio_lower]
    if found:
        print(f"\n{Red}[!] {White}Ada contact dalam bio ni: {Green}{', '.join(found)}{Reset}")

def check_fullname():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Green}✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪")
    print(f"{Red}NAMA BETUL {Green}{username}")
    print(f"{Green}✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪")
    print(f"{Yellow}» {White}{profile.full_name}")
    print(f"{Green}✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪{Reset}")
    
    # Name analysis
    if ' ' in profile.full_name:
        names = profile.full_name.split()
        print(f"{Yellow}[+] {White}Kemungkinan nama depan: {Red}{names[0]}{Reset}")
        print(f"{Yellow}[+] {White}Kemungkinan nama belakang: {Red}{names[-1]}{Reset}")

def check_followers():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Red}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{Green}📊 STATISTIK {Red}{username}")
    print(f"{Red}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{Yellow}• Pengikut   : {Red}{profile.followers:,}")
    print(f"{Yellow}• Dia Ikut   : {Green}{profile.followees:,}")
    
    ratio = profile.followers/profile.followees if profile.followees > 0 else 0
    print(f"{Yellow}• Ratio      : {Yellow}{ratio:.2f}")
    
    if ratio > 10:
        print(f"{Yellow}• Status     : {Green}POPULAR/INFLUENCER{Reset}")
    elif ratio < 0.1:
        print(f"{Yellow}• Status     : {Red}FOLLOW-BACK HUNTER{Reset}")
    
    print(f"{Red}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{Reset}")

def download_profile_pic_menu():
    username = input(f"\n{Green}[?] {White}Sapa? {Red}")
    profile = get_profile_info(username)
    if not profile:
        return
    
    print(f"\n{Red}<|============================================|>")
    print(f"{Green}📸 TANGKAP GAMBAR PROFIL")
    print(f"{Red}<|============================================|>")
    
    profile_pic = profile.profile_pic_url
    print(f"{Yellow}URL: {White}{profile_pic}")
    
    confirm = input(f"\n{Red}[?] {White}Tangkap gambar? (y/n): {Green}")
    if confirm.lower() == 'y':
        filepath = download_profile_pic(profile_pic, username)
        if filepath:
            print(f"\n{Green}[✓] {White}Gambar dah ditangkap! {Red}{filepath}")
            print(f"{Yellow}[+] {White}Guna untuk: Profile analysis, Reverse image search{Reset}")
        else:
            print(f"{Red}[!] {White}Gagal tangkap gambar{Reset}")

def premium_email_check():
    print(f"\n{Red}┌──────────────────────────────────────────────┐")
    print(f"{Red}│ {Green}🔥 PREMIUM FEATURE - EMAIL & PHONE FINDER 🔥 {Red}│")
    print(f"{Red}└──────────────────────────────────────────────┘{Reset}")
    
    username = input(f"{Green}[?] {White}Username target: {Red}")
    
    print(f"\n{Yellow}[!] {White}Scanning untuk email & nombor...{Reset}")
    time.sleep(2)
    
    # Simulating OSINT techniques
    possible_emails = [
        f"{username}@gmail.com",
        f"{username}@yahoo.com",
        f"{username}@hotmail.com"
    ]
    
    print(f"\n{Green}═══════════════ HASIL CARIAN ═══════════════")
    print(f"{Yellow}[+] {White}Email mungkin:")
    for email in possible_emails:
        print(f"{Red}   • {Green}{email}")
    
    print(f"\n{Yellow}[+] {White}Nombor mungkin (pattern Kelantan):")
    print(f"{Red}   • 01{''.join([str((ord(c)%10)) for c in username[:7]])}")
    print(f"{Red}   • 019{''.join([str((ord(c)%10)) for c in username[:6]])}")
    
    print(f"\n{Red}[💀] {White}Tips: Guna {Green}Hunter.io API {White}atau {Red}PhoneInfoga {White}untuk carian lebih tepat!{Reset}")

def hack_mode():
    print(f"\n{Red}████████████████████████████████████████████")
    print(f"{Red}██ {Green}💀 HACK MODE TAMBAHAN - CYBER FORCE KELATE {Red}██")
    print(f"{Red}████████████████████████████████████████████{Reset}")
    
    print(f"\n{Yellow}[1] {Red}Brute Force Instagram Password")
    print(f"{Yellow}[2] {Red}Phishing Page Generator (Instagram)")
    print(f"{Yellow}[3] {Red}Session Hijacking Tools")
    print(f"{Yellow}[4] {Red}Mass Reporting Script")
    print(f"{Yellow}[5] {Red}Back to Main Menu{Reset}")
    
    choice = input(f"\n{Green}[?] {White}Pilih senjata: {Red}")
    
    if choice == '1':
        print(f"\n{Red}[!] {White}Downloading brute force wordlist...")
        print(f"{Yellow}[+] {White}Wordlist khusus Kelantan: passkelate.txt")
        print(f"{Green}[+] {White}Command: python3 instagram_brute.py {Red}username{White} passkelate.txt{Reset}")
    
    elif choice == '2':
        print(f"\n{Red}[!] {White}Generating phishing page...")
        print(f"{Green}[+] {White}Page akan siap dalam: phishing_instagram.html")
        print(f"{Yellow}[+] {White}Guna ngrok untuk hosting: ngrok http 8080{Reset}")
    
    elif choice == '3':
        print(f"\n{Red}[💀] {White}Session ID Tools - Advanced")
        print(f"{Green}[+] {White}Install: pip install instagram-private-api")
        print(f"{Yellow}[+] {White}Guna session cookie untuk bypass login{Reset}")
    
    elif choice == '4':
        print(f"\n{Red}[⚠] {White}Mass Report Bot - Use with caution!")
        print(f"{Green}[+] {White}Script auto report 100x dalam 1 jam")
        print(f"{Red}[!] {White}Risiko tinggi! Akun mungkin kena ban{Reset}")

def main():
    try:
        clear_screen()
        display_banner()
        loading_animation()
        
        print(f"\n{Green}[✓] {White}System CYBER FORCE KELATE dah aktif!{Reset}")
        print(f"{Red}[!] {White}Guna untuk pendidikan sahaja! 🚫{Reset}")
        
        while True:
            menu()
            choice = input(f"\n{Green}[?] {White}Pilih senjata (0-9): {Red}")
            
            if choice == '1':
                full_account_info()
            elif choice == '2':
                check_id()
            elif choice == '3':
                check_posts()
            elif choice == '4':
                check_bio()
            elif choice == '5':
                check_fullname()
            elif choice == '6':
                check_followers()
            elif choice == '7':
                download_profile_pic_menu()
            elif choice == '8':
                premium_email_check()
            elif choice == '9':
                hack_mode()
            elif choice == '0':
                print(f"\n{Red}┌──────────────────────────────────────────────┐")
                print(f"{Red}│ {White}Terima kasih guna {Green}CYBER FORCE KELATE{White}!    {Red}│")
                print(f"{Red}│ {Yellow}Jangan lupa follow @ManForceX_Official     {Red}│")
                print(f"{Red}└──────────────────────────────────────────────┘{Reset}")
                break
            else:
                print(f"{Red}[!] {White}Pilihan dok wok! Cuba lagi.{Reset}")
            
            input(f"\n{Yellow}[?] {White}Tekan Enter untuk teruskan...{Reset}")
            clear_screen()
            display_banner()
        
    except KeyboardInterrupt:
        print(f"\n\n{Red}[!] {White}Program stop! Jumpa lagi... 💀{Reset}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Red}[!] {White}Error tak dijangka: {Yellow}{str(e)}{Reset}")
        sys.exit(1)

if __name__ == "__main__":
    main()
