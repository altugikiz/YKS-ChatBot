import gradio as gr
from modules.assistant_handler import get_assistant_response

def chat_function(message, history):
    """
    Gradio ChatInterface tarafından çağrılan ana fonksiyon.
    Mesajı alır, handler'a gönderir ve cevabı döndürür.
    """
    return get_assistant_response(message, history)

# Arayüzü oluştur
interface = gr.ChatInterface(
    fn=chat_function,
    title="🌊 YKS Buddy - Kişisel Veri Tabanlı Koç",
    description="🔹 YKS hazırlığı için akıllı asistan! Sorularını sor, `yks_datas.jsonl` dosyasındaki bilgilerle sana özel tavsiyeler al.",
    theme="default",
    css="style.css",  # CSS dosyasını harici olarak yüklüyoruz
    examples=[
        ["YKS sınavına nasıl hazırlanmalıyım?"],
        ["TYT ve AYT arasındaki farklar nelerdir?"],
        ["Sürem yetmiyor."],
        ["Matematikte çok zorlanıyorum."],
    ],
    chatbot=gr.Chatbot(
        label="Sohbet",
        bubble_full_width=False,
        avatar_images=(None, "https://i.ibb.co/qJBcS05/image.png") # Asistan için bir avatar
    )
)

if __name__ == "__main__":
    print("Gradio arayüzü başlatılıyor...")
    interface.launch()