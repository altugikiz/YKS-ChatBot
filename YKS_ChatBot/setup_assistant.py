import openai
import os
from dotenv import load_dotenv

# Bu script'i çalıştırmadan önce .env dosyanıza OPENAI_API_KEY ve ASSISTANT_ID'nizi eklediğinizden emin olun!
print("OpenAI Asistan Kurulum ve Güncelleme Script'i Başlatıldı...")

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

if not api_key or not assistant_id:
    print("Hata: Lütfen .env dosyanızda OPENAI_API_KEY ve ASSISTANT_ID değerlerini ayarlayın.")
    exit()

client = openai.OpenAI(api_key=api_key)

try:
    # 1. Vector Store Oluştur
    print("Yeni bir Vector Store oluşturuluyor: 'YKS Bilgi Bankası'")
    vector_store = client.beta.vector_stores.create(name="YKS Bilgi Bankası")

    # 2. Veri Dosyasını Yükle
    file_path = "data/yks_datas.jsonl"
    print(f"'{file_path}' dosyası OpenAI'a yükleniyor...")
    with open(file_path, "rb") as file_stream:
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id, files=[file_stream]
        )
    print("Dosya başarıyla yüklendi ve Vector Store'a eklendi.")
    print(f"-> Durum: {file_batch.status}")

    # 3. Asistanı Güncelle
    print(f"'{assistant_id}' ID'li asistan, yeni Vector Store'u kullanacak şekilde güncelleniyor...")
    assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
        tools=[{"type": "file_search"}] # Asistana 'File Search' aracını kullanma yetkisi ver
    )
    
    print("\n--- ✅ KURULUM BAŞARIYLA TAMAMLANDI! ---")
    print("Lütfen aşağıdaki satırı kopyalayıp .env dosyanıza yapıştırın:")
    print("\n" + f'VECTOR_STORE_ID="{vector_store.id}"' + "\n")

except Exception as e:
    print(f"\n--- ❌ HATA OLUŞTU! ---")
    print(f"İşlem sırasında bir hata meydana geldi: {e}")