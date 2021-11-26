from flask import Flask, render_template
import jyserver.Flask as jsf

from descriptor import Descriptor

app = Flask(__name__)

@jsf.use(app) # Connect Flask object to JyServer
class App:
  def __init__(self):
    self.count = 0
    self.url = ""
    self.details = ""

  def print_url(self):
    self.js.document.getElementById("details").innerHTML = f"<p>{self.url}</p>"

  def run(self):
    self.print_url()
    self.url = self.js.document.getElementById("search-box").value
    self.details = Descriptor(str(self.url)).describe()
    self.js.document.getElementById("details").innerHTML = f"<p>{self.details}</p>"


@app.route("/")
@app.route("/home")
def home():
  return App.render(render_template("home.html")) # JyServer "App" render template


if __name__ == '__main__':
  app.run(debug=True)
