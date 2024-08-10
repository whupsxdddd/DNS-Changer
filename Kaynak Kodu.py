import os, subprocess, time

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

def dns_changer():
    while True:
        os.system('cls')
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

def ipreset():
    os.system('cls')
    print('İşlem Birazdan Başlatılacaktır.Yapıldıktan Sonra Lütfen Bilgisayarı Yeniden Başlatın.')
    time.sleep(2.5)
    os.system('cls')
    os.system('ipconfig /flushdns')

    for say in range(1, 11):
        if say == 10:
            print('İşlem Bitti!')
            time.sleep(4)
            return

def loginpage():
    while True:
        os.system('cls')
        try:
            os.system('cls')
            print('Tüm Sistemler Key İle Çalışmaktadır.Discord = https://discord.gg/M7fun9RqZq')
            print('')
            print('1. DNS Changer')
            print('2. Network Refresh')
            print('')

            x = int(input('Sayı Giriniz : '))
            
            if x == 1:
                os.system('cls')
                dnskeygir = input('Key Giriniz : ')

                if dnskeygir == dns_key:
                    dns_changer()
            elif x == 2:
                os.system('cls')
                ipresetkeygir = input('Key Giriniz : ')

                if ipresetkeygir == ipreset_key:
                    ipreset()
            else:
                print('?')
        except ValueError:
            print('Hata!')

loginpage()
