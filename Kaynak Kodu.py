import requests, os, subprocess

webhook = 'https://discord.com/api/webhooks/1271500173390118963/TATvglA4spwIvcMnjlBCWch_KkPOV1bPoGtlxlMBHI5votcZiPnFG0gw53gn1HVhUKqp'
message = 'Giriş Yapıldı!'

def webhookmsg(message):
    try:
        response = requests.post(webhook, json={'content': message})
        if response.status_code == 204:
            os.system('cls')
        else:
            print(f"Webhook message failed, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while sending webhook message: {e}")

def change_dns(dns1, dns2):
    interface_name = "Wi-Fi"  # Wi-Fi adaptörüne odaklanıyoruz
    try:
        # İlk DNS adresini ayarlama
        result = subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', f'name={interface_name}', 'source=static', dns1], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("Error setting primary DNS:", result.stderr)
            return

        # İkinci DNS adresini ekleme
        result = subprocess.run(['netsh', 'interface', 'ip', 'add', 'dns', f'name={interface_name}', dns2, 'index=2'], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("Error setting secondary DNS:", result.stderr)
    except Exception as e:
        print(f"An error occurred while changing DNS: {e}")

import os
import subprocess

def change_dns(primary, secondary):
    try:
        # Ağ bağlantısı adını almak için ipconfig komutunu çalıştır
        result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if 'Ethernet adapter' in line or 'Wireless LAN adapter' in line:
                adapter_name = line.split(':')[1].strip()
                break
        else:
            raise Exception("Ağ adaptörü bulunamadı")

        # DNS ayarlarını değiştirmek için netsh komutunu çalıştır
        subprocess.run(f'netsh interface ip set dns name="{adapter_name}" static {primary}', shell=True)
        subprocess.run(f'netsh interface ip add dns name="{adapter_name}" {secondary} index=2', shell=True)
    except Exception as e:
        print(f"Hata: {e}")

def mainpage():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1. (1.1.1.1 - Cloudflare DNS) (1.0.0.1 - Cloudflare DNS)')
        print('2. (8.8.8.8 - Google DNS) (8.8.4.4 - Google DNS)')
        print('3. (76.76.2.0 - Quad9) (76.76.10.0 - Quad9)')
        print('4. (9.9.9.9 - Quad9) (149.112.112.112 - Quad9)')
        print('5. (208.67.222.222 - OpenDNS) (208.67.220.220 - OpenDNS)')
        print('6. (94.140.14.14 - AdGuard) (94.140.15.15 - AdGuard)')
        print('7. (185.228.168.9 - CleanBrowsing) (185.228.169.9 - CleanBrowsing)')
        print('8. (76.76.19.19 - DNS.Watch) (76.223.122.150 - DNS.Watch)')
        print('')
        try:
            secim = int(input('Lütfen Sayı Giriniz: '))

            if secim == 1:
                change_dns('1.1.1.1', '1.0.0.1')
                print("DNS ayarları Cloudflare DNS olarak değiştirildi!")
            elif secim == 2:
                change_dns('8.8.8.8', '8.8.4.4')
                print("DNS ayarları Google DNS olarak değiştirildi!")
            elif secim == 3:
                change_dns('76.76.2.0', '76.76.10.0')
                print("DNS ayarları Quad9 olarak değiştirildi!")
            elif secim == 4:
                change_dns('9.9.9.9', '149.112.112.112')
                print("DNS ayarları Quad9 olarak değiştirildi!")
            elif secim == 5:
                change_dns('208.67.222.222', '208.67.220.220')
                print("DNS ayarları OpenDNS olarak değiştirildi!")
            elif secim == 6:
                change_dns('94.140.14.14', '94.140.15.15')
                print("DNS ayarları AdGuard olarak değiştirildi!")
            elif secim == 7:
                change_dns('185.228.168.9', '185.228.169.9')
                print("DNS ayarları CleanBrowsing olarak değiştirildi!")
            elif secim == 8:
                change_dns('76.76.19.19', '76.223.122.150')
                print("DNS ayarları DNS.Watch olarak değiştirildi!")
            else:
                print('Lütfen geçerli bir seçim yapınız!')
        except ValueError:
            print('Lütfen geçerli bir numara giriniz!')

def loginpage():
    while True:
        os.system('cls')
        print('Not : Eğer Discord Gelmek İsterseniz = https://discord.gg/M7fun9RqZq (Sadece Yardım!)')
        print('Lütfen Aşağıdaki Kısma Githubdan Aldığınız Keyi Giriniz.')
        print('')
        keygir = input('>>>')

        if keygir in public_keys:
            webhookmsg(message)
            mainpage()
        else:
            print('Hata! Lütfen Düzgün Key Giriniz!')

loginpage()
