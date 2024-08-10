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

def mainpage():
    while True:
        os.system('cls')
        print('1. (1.1.1.1) (1.0.0.1)')
        print('2. (8.8.8.8) (8.8.4.4)')
        print('')
        try:
            secim = int(input('Lütfen Sayı Giriniz: '))

            if secim == 1:
                change_dns('1.1.1.1', '1.0.0.1')
                print("DNS ayarları 1.1.1.1 ve 1.0.0.1 olarak değiştirildi!")
            elif secim == 2:
                change_dns('8.8.8.8', '8.8.4.4')
                print("DNS ayarları 8.8.8.8 ve 8.8.4.4 olarak değiştirildi!")
            else:
                print('Lütfen Düzgün Seçim Yapınız!')

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
