import io
import os
import random
import shutil
import string
import subprocess
from flask import Flask, request, send_file, render_template

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

@app.route("/")
def top():
    return render_template("index.html")

def tex2pdf(tex_code) -> str:
    # Generate random file name.
    filename = "".join([random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for i in range(2**5)])
    # Create a working directory.
    os.makedirs(f"tex_box/{filename}", exist_ok=True)
    # .tex -> .pdf
    try:
        # No flag !!!!
        if "flag" in tex_code.lower():
            tex_code = ""
        # Write tex code to file.
        with open(f"tex_box/{filename}/{filename}.tex", mode="w") as f:
            f.write(tex_code)
        # Create pdf from tex.
        subprocess.run(["pdflatex", "-output-directory", f"tex_box/{filename}", f"tex_box/{filename}/{filename}.tex"], timeout=0.5)
    except:
        pass
    if not os.path.isfile(f"tex_box/{filename}/{filename}.pdf"):
        # OMG error ;(
        shutil.copy("tex_box/error.pdf", f"tex_box/{filename}/{filename}.pdf")
    return f"{filename}"

@app.route("/pdf", methods=["POST"])
def pdf():
    # tex to pdf.
    filename = tex2pdf(request.form.get("tex_code"))
    # Here's your pdf.
    with open(f"tex_box/{filename}/{filename}.pdf", "rb") as f:
        pdf = io.BytesIO(f.read())
    shutil.rmtree(f"tex_box/{filename}/")
    return send_file(pdf, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4444)
