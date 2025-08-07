# 🌊 YKS Buddy - Kişisel YKS Danışman Chatbot

YKS Buddy, YKS (Yükseköğretim Kurumları Sınavı) hazırlığı yapan öğrenciler için geliştirilmiş akıllı bir chatbot'tur. OpenAI'nin Assistant API'si ve File Search özelliğini kullanarak kişiselleştirilmiş YKS danışmanlığı sunar.

## ✨ Özellikler

- 🤖 **OpenAI Assistant API** ile güçlendirilmiş akıllı yanıtlar
- 📚 **Vector Store** teknolojisi ile kişisel veri tabanı
- 🎨 **Modern Gradio arayüzü** ile kullanıcı dostu tasarım
- 📊 **Özel veri seti** ([data/yks_datas.jsonl](data/yks_datas.jsonl)) ile YKS'ye özgü bilgiler
- 💬 **Samimi konuşma tarzı** ile motive edici danışmanlık
- ⚡ **Hızlı kurulum** ve kolay kullanım

## 📁 Proje Yapısı

```
YKS_ChatBot/
├── .env                      # Ortam değişkenleri (gizli)
├── .env.example             # Ortam değişkenleri şablonu
├── app.py                   # Ana uygulama dosyası
├── setup_assistant.py       # OpenAI asistanı kurulum scripti
├── requirements.txt         # Python bağımlılıkları
├── style.css               # Arayüz stil dosyası
├── data/
│   └── yks_datas.jsonl     # YKS veri seti
└── modules/
    ├── __init__.py
    ├── config.py           # Yapılandırma ayarları
    └── assistant_handler.py # OpenAI asistanı yöneticisi
```

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler

```bash
pip install -r requirements.txt
```

### 2. Ortam Değişkenlerini Ayarlama

`.env.example` dosyasını `.env` olarak kopyalayın ve kendi değerlerinizi girin:

```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin:

```env
OPENAI_API_KEY="your_openai_api_key_here"
ASSISTANT_ID="your_assistant_id_here"
VECTOR_STORE_ID="your_vector_store_id_here"
```

### 3. OpenAI Asistanı Kurulumu

Asistanınızı kurmak ve veri tabanınızı oluşturmak için:

```bash
python setup_assistant.py
```

Bu script:
- Yeni bir Vector Store oluşturur
- [`data/yks_datas.jsonl`](data/yks_datas.jsonl) dosyasını yükler
- Asistanınızı yapılandırır
- Size `VECTOR_STORE_ID` verir

### 4. Uygulamayı Başlatma

```bash
python app.py
```

Uygulama başlatıldıktan sonra tarayıcınızda `http://localhost:7860` adresine gidin.

## 🔧 Teknik Detaylar

### Ana Bileşenler

- **[`app.py`](app.py)**: Gradio arayüzü ve ana uygulama mantığı
- **[`modules/assistant_handler.py`](modules/assistant_handler.py)**: OpenAI Assistant API ile iletişim
- **[`modules/config.py`](modules/config.py)**: Güvenli yapılandırma yönetimi
- **[`setup_assistant.py`](setup_assistant.py)**: Tek seferlik kurulum scripti

### Veri Seti

[`data/yks_datas.jsonl`](data/yks_datas.jsonl) dosyası YKS ile ilgili sorular ve cevaplar içerir:

```json
{"prompt": "YKS çok zor, nasıl çalışacağım?", "completion": "Öncelik konuları böl ve günlük hedefler koy. Soru çözerek ilerle!"}
{"prompt": "Matematikte çok zorlanıyorum.", "completion": "Temelden başla ve her gün biraz pratik yap. Basit sorulardan başla!"}
```

### API Akışı

1. Kullanıcı mesajı [`chat_function`](app.py) fonksiyonuna gelir
2. [`get_assistant_response`](modules/assistant_handler.py) çağrılır
3. Yeni bir OpenAI Thread oluşturulur
4. Vector Store ile mesaj işlenir
5. Assistant yanıtı kullanıcıya döndürülür

## 🎨 Arayüz Özellikleri

[`style.css`](style.css) dosyası modern ve etkileyici bir tasarım sunar:

- 🌊 **Okyanus teması** ile dinamik arka plan animasyonları
- 💙 **Mavi tonlarda** modern gradyan renkler
- 💬 **Konuşma baloncukları** ile chat deneyimi
- ⚡ **Hover efektleri** ve geçiş animasyonları

## 📊 Veri Güncelleme

Yeni YKS verileri eklemek için:

1. [`data/yks_datas.jsonl`](data/yks_datas.jsonl) dosyasını düzenleyin
2. [`setup_assistant.py`](setup_assistant.py) scriptini yeniden çalıştırın
3. Yeni `VECTOR_STORE_ID`'yi `.env` dosyasına ekleyin

## 🔐 Güvenlik

- **Ortam değişkenleri**: Hassas bilgiler `.env` dosyasında saklanır
- **Git ignore**: [`.gitignore`](.gitignore) dosyası ile gizli dosyalar korunur
- **API anahtarları**: OpenAI API anahtarınızı güvenli tutun

## 🛠️ Geliştirme

### Yeni özellik ekleme

1. [`modules/`](modules/) klasörüne yeni modül ekleyin
2. [`app.py`](app.py) dosyasında gerekli importları yapın
3. Gradio arayüzüne yeni componentler ekleyin

### Veri seti genişletme

[`data/yks_datas.jsonl`](data/yks_datas.jsonl) dosyasına JSON Lines formatında yeni veriler ekleyin.

## 📝 Lisans

Bu proje kişisel kullanım için geliştirilmiştir. Ticari kullanım öncesinde OpenAI kullanım koşullarını gözden geçirin.

## 🆘 Sorun Giderme

### Yaygın Hatalar

**"Hata: Lütfen .env dosyanızdaki tüm değerleri kontrol edin."**
- `.env` dosyanızda tüm değerlerin dolu olduğundan emin olun

**"OpenAI API hatası"**
- API anahtarınızın geçerli olduğunu kontrol edin
- Kotanızın dolmadığından emin olun

### Destek

Sorularınız için:
1. Önce [requirements.txt](requirements.txt) bağımlılıklarının kurulu olduğundan emin olun
2. `.env` dosyanızdaki değerleri kontrol edin
3. [`setup_assistant.py`](setup_assistant.py) scriptini tekrar çalıştırın

---

**💡 İpucu**: YKS Buddy'nin tüm konuşmaları samimi ve motive edici bir tonda gerçekleşir. "Kanka", "dostum", "koçum" gibi samimi hitaplarla öğrencilere destek olur! 🚀