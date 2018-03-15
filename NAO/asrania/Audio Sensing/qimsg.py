import qi
import sys

app = qi.Application(sys.argv)
app.start()
session = app.session()

app.run()