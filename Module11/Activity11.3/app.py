from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [{
  "Player": "Bobby Witt",
  "Team": "KC",
  "avg": .345
},
 {
  "Player": "Steven Kwan",
  "Team": "CLE",
  "avg": .330
}, {
  "Player": "Aaron Judge",
  "Team": "NYY",
  "avg": .321
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "Player", # which is the field's name of data key 
    "title": "Player", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Team",
    "title": "Team",
    "sortable": True,
  },
  {
    "field": "avg",
    "title": "Batting Average",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Top 3 MLB Players by Batting Average')


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)