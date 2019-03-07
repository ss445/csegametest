import bottle
import filter
import construct


@bottle.route('/')
@bottle.route('/static/index.html')
def webFront():
    return bottle.static_file('index.html', root='/projects/Project-2')


@bottle.route('/map.js')
@bottle.route('/static/map.js')
def themap():
    return bottle.static_file('map.js', root='/projects/Project-2')


@bottle.route('/data')
@bottle.route('/static/jsonrequest.py')
def data1():
    return construct.data()


@bottle.route('/download')
def download():
    filter.json1Maker()
    filter.json2Maker()

# filter.filterdata1(jsonrequest.get_json1())
# json.stringify(filter.sortmaster(filter.filterdata1(jsonrequest.get_json1())))
# garbage = '[{"date":"2012-05-31T00:00:00.000","month":"May","total_in_tons":"0","type":"Sidewalk Debris"},{"date":"2014-12-31T00:00:00.000","month":"December","total_in_tons":"66.11","type":"Misc. Garbage"},{"date":"2014-05-31T00:00:00.000","month":"May","total_in_tons":"3.15","type":"Misc. Recycling"},{"date":"2013-03-31T00:00:00.000","month":"March","total_in_tons":"5.64","type":"Misc. Recycling"},{"date":"2017-03-31T00:00:00.000","month":"March","total_in_tons":"0","type":"Asphalt Debris"},{"date":"2013-10-31T00:00:00.000","month":"October","total_in_tons":"5000","type":"Asphalt Debris"},{"date":"2016-10-31T00:00:00.000","month":"October","total_in_tons":"900","type":"Yard Waste"},{"date":"2015-03-31T00:00:00.000","month":"March","total_in_tons":"11.81","type":"Recycled Tires"},{"date":"2014-06-30T00:00:00.000","month":"June","total_in_tons":"226.38","type":"Misc. Garbage"},{"date":"2017-01-31T00:00:00.000","month":"January","total_in_tons":"1000","type":"Yard Waste"},{"date":"2017-12-31T00:00:00.000","month":"December","total_in_tons":"316.67","type":"Bottle Bill"}]'
bottle.run(host='0.0.0.0', port=8080, debug=True)
