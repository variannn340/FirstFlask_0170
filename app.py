from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kirim", methods=["POST"])
def kirim():
    nama = escape(request.form.get("nama", ""))
    umur = escape(request.form.get("umur", ""))

    return f"""
    <link rel="stylesheet" href="/static/style.css">
    <div class="card">
        <h2>Hasil</h2>
        <div class="hasil">
            <p>Nama: {nama}</p>
            <p>Umur: {umur}</p>
        </div>
        <a class="kembali" href="/">Kembali</a>
    </div>
    """


if __name__ == "__main__":
    app.run(debug=True)