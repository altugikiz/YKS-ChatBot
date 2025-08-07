import os
from dotenv import load_dotenv

# Projenin ana dizinindeki .env dosyasını yükle
load_dotenv()

# API anahtarı ve ID'leri ortam değişkenlerinden güvenli bir şekilde al
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")