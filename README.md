# ChatGpt_Whatsapp

I created an AI which learns from my Whatsapp messages

API_KEY.py dosyasında Open AI'daki kendi API key'inizi girin.

Main.py kısmında 36. satıra Whatsapp'taki kendi isminizi yazınız.

Whatsapp mesajları klasörünün altına Whatsapp'tan elde ettiğiniz txt dosyalarını yerleştirin.
Whatsapp mesajlarını nasıl txt'ye dönüştğreceğinizi bilmiyorsanız şu linkte basiteçe anlatmış (https://youtube.com/shorts/7fbxTMX3fv8?feature=share)

Sonrasında filter.py dosyasını çalıştırdığınızda filtered klasörünün altında verilerin temizkenmiş halini bulabilirsiniz.

NOT: filtered ve Whatsapp mesajları klasörünün altında "filtreli dosyalar bu klasöre gelecek.txt" ve "Kendi mesajlarınızı bu dosyaya yerleştirin.txt" öetin dosyaları var. Onları silebilirsiniz. Zaten içi boş.

Sonraki adımlar için Youtube videomu izleyebilirsiniz.("https://youtu.be/80PyIs0FJ20")

Yeni eklemeler:
Filter.py dosyasındaki non-latins regex'ini kaldırdım. Çünkü, "ç","ö" gibi türkçede bulunan özel harfleri de çıkaruıyordu.
Örnek olmsı açısından "Kendi mesajlarınızı bu dosyaya yerleştirin.txt" dosyasının içine bir mesajlaşma koydum. Yine "filtered" klasörünün altında mesajlaşmaların filtreli halinin bulunduğu bir örnek görebilirsiniz.

Sonrasında main.py'yi çalıştırdığımızda 2 json dosyası çıkıyor karşımıza. "Prepared.json" ve "whatsapp_messages.json". "whatsapp_messages.json" dosyasında syntax hatası var onu göz ünüde bulundurmaya bilirsiniz. Önemli olan Prepared.json dosyası!!!
