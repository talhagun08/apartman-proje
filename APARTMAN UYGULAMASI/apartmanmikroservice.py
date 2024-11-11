from flask import Flask, request, jsonify, render_template
import json



app = Flask(__name__)


sakinler = {}
gelir_gider = {}

@app.route("/", methods=["GET"])
def sayfa():
    return render_template("index.html")

@app.route("/api/daire_sakini_ekle", methods=["POST"])
def sakin_ekle():
    data = request.get_json()
    telefon_no = data["telefon_no"]
    ad = data["ad"]
    soyad = data["soyad"]
    daire_no = data["daire_no"]

    try:
        sakinler["telefon_no"]={
            "ad":ad,
            "soyad":soyad,
            "daire_no":daire_no
        }
        return jsonify({"sonuc":"eklendi"}), 200
    except Exception as e:
        return jsonify({"error": str (e)}) , 500
    
@app.route("/api/gelir_gider_ekle", methods=["POST"])
def gelir_gider_ekle():
    data = request.get_json()
    gelir_miktari = data["gelir_miktari"]
    gider_miktari = data["gider_miktari"]

    try:
        gelir_gider["gelir_miktari"]={
            "gider_miktari":gider_miktari
        }
        return jsonify({"sonuc":"eklendi"}), 200
    except Exception as e :
        return jsonify({"error": str (e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

