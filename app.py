from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


# Route POST: dipanggil oleh tombol Kirim
@app.route("/kirim", methods=["POST"])
def kirim():
    nama = escape(request.form.get("nama", ""))
    umur = escape(request.form.get("umur", ""))

    return f"""
    <h2>Hasil</h2>
    <p>Nama: {nama}</p>
    <p>Umur: {umur}</p>
    <a href="/static/index.html">Kembali</a>
    """


if __name__ == "__main__":
    app.run(debug=True)