from minimal import create_app
import os

os.environ["SESSION_SECRET"]="MySessionSecret" 

app = create_app()
app.run(host="lxfmoore2.cor.rd.hpicorp.net", debug=False)
