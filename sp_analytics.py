from flask import Flask
from flask import render_template
import json
from domain_layer.domain_analytics import domain_analytics

app = Flask(__name__)
app.config.update(
    DEBUG=True
)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/app/user_top_locations/<userid>/')
def user_top_locations(userid):
    da = domain_analytics()

    dlist = []
    top_locs_data = da.user_activity_hourly(userid)

    for row in top_locs_data:
        dlist += [dict(row)]

    return render_template('charts_test.html', dictionary=json.dumps(dlist, ensure_ascii=False))
    #json.dumps(dlist)

if __name__ == '__main__':
    app.run()
