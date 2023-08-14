from spartanlog import create_app
import os

os.environ["SESSION_SECRET"]="663ed51eca5db60015f3be19486b5f96"

app = create_app()
app.run(host="lxfmoore2.cor.rd.hpicorp.net", debug=False)
