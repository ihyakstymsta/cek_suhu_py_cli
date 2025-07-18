import requests

API_URL = "http://localhost:3000/api/v1/prediction/7d137abd-feb6-4b59-954e-949c7bffd5ac"

def query(question):
    payload = {"question": f"Assalamu'alaikum. {question}"}
    response = requests.post(API_URL, json=payload)
    return response.json()

# Menampilkan judul
print("="*50)
print("🤖 CHATBOT KELOMPOK 3")
print("="*50)

while True:
    user_input = input("Anda: ")
    if user_input.lower() in ["exit", "keluar", "quit"]:
        print("Chatbot: Wa'alaikumussalam, sampai jumpa!")
        break

    result = query(user_input)
    print("Chatbot:", result.get("text", "Maaf, tidak ada respons."))
    print()
