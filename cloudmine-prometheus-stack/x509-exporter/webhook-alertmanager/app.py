from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    alerts = data.get("alerts", [])
    for alert in alerts:
        print("🚨 ALERTA RECEBIDO:")
        print("Alertname:", alert["labels"].get("alertname"))
        print("Cert:", alert["labels"].get("secret_name"))
        print("Namespace:", alert["labels"].get("secret_namespace"))
        print("Descrição:", alert["annotations"].get("description"))
        print("----")
        # aqui entraria a chamada para API do seu ITSM

    return jsonify({"status": "ok"}), 200
