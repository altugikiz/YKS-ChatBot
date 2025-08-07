import openai
from .config import OPENAI_API_KEY, ASSISTANT_ID, VECTOR_STORE_ID

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_assistant_response(user_message: str, history: list):
    """
    Kullanıcı mesajını alır, OpenAI asistanına gönderir ve yanıtı döndürür.
    Her sohbet için Vector Store'u kullanan yeni bir thread oluşturur.
    """
    if not all([OPENAI_API_KEY, ASSISTANT_ID, VECTOR_STORE_ID]):
        return "Hata: Lütfen .env dosyanızdaki tüm değerleri (API Anahtarı, Asistan ID, Vector Store ID) kontrol edin."

    try:
        # Her yeni sohbet oturumu için bilgi bankamızla ilişkilendirilmiş yeni bir thread oluştur
        thread = client.beta.threads.create(
            tool_resources={"file_search": {"vector_store_ids": [VECTOR_STORE_ID]}},
        )

        # Kullanıcının mesajını bu thread'e ekle
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # Asistanı çalıştır ve yanıtını bekle
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID,
        )

        # Thread'deki mesajları al
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        # En son mesaj asistanın cevabıdır.
        response = messages.data[0].content[0].text.value

        return response

    except Exception as e:
        print(f"Asistanla iletişimde hata oluştu: {e}")
        return "Üzgünüm, bir sistem hatası nedeniyle şu anda yardımcı olamıyorum."