from flask import Flask
from flask import render_template
import json
from domain_layer.domain_analytics import domain_analytics
from misc.src.data_processing import DP

app = Flask(__name__)
app.config.update(
    DEBUG=True
)

@app.route('/')
def hello_world():
    return render_template('dashboard.html', dictionary=json.dumps(dict(message="Hello World!")))

@app.route('/app/user_top_locations/<userid>/')
def user_top_locations(userid):
    da = domain_analytics()

    dlist = []
    top_locs_data = da.user_activity_hourly(userid)

    for row in top_locs_data:
        dlist += [dict(row)]

    return render_template('charts_test.html', dictionary=json.dumps(dlist, ensure_ascii=False))
    #json.dumps(dlist)

@app.route('/app/dashboard/')
def dashboard():
    # Total Number of Antennas
    # Number of Users per Antenna (avg)
    # Number of Antenna per User (avg)
    # Number of Call/Text events per Day
    da = domain_analytics()

    dlist = []
    userid=''
    top_locs_data = da.user_activity_hourly(userid)

    for row in top_locs_data:
        dlist += [dict(row)]

    return render_template('charts_test.html', dictionary=json.dumps(dlist, ensure_ascii=False))

@app.route('/app/cell_traffic')
def cell_traffic():
    return render_template('all_cells_traffic_heatmap.html')

@app.route('/app/trajectory')
def trajectory():
    return render_template('user_trajectory.html')

@app.route('/app/popular_cells')
def popular_cells():
    return render_template('popular_cells.html')

@app.route('/app/similar_users/<userid>', methods=['GET'])
def similar_users(userid):

    dp = DP()

    userid = int(userid)
    sim_ten = dp.get_sims([userid], euc=True)

    sim_users = dict(
        userid=userid,
        similarusers=str(sim_ten)
    )

    return json.dumps(sim_users)

if __name__ == '__main__':
    app.run()
