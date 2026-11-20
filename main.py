0import urllib.request, urllib.parse, json
TOKEN = "9203469643:AAHrfbopdWox4dWr5wrgSFLwf8r2ckZ12l8"
BASE = f"https://api.telegram.org/bot{TOKEN}/"
def call(method, data):
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(BASE + method, data=data)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())
def get_updates(offset):
    try:
        url = BASE + f"getUpdates?timeout=5&offset={offset}"
        with urllib.request.urlopen(url) as r:
            return json.loads(r.read()).get("result", [])
    except:
        return []
print("البوت شغال...")
offset = 0
while True:
    updates = get_updates(offset)
    for u in updates:
        offset = u["update_id"] + 1
        if "message" not in u: continue
        msg = u["message"]
        chat_id = msg["chat"]["id"]
        text = msg.get("text", "")
        if text == "/start":
            call("sendMessage", {"chat_id": chat_id, "text": "👋 Welcome to Ziad AI\n\nDeveloped by Ziad Mohamed Kandil\n📞 Contact: 01147847914\n\nاكتب سؤالك دلوقتي، وانا هجاوبك بسرعة ✅"})
        else:
            call("sendMessage", {"chat_id": chat_id, "text": "✅ إجابتك:\n\n" + text + "\n\nانا Ziad AI، جرب تسألني سؤال تاني."})
