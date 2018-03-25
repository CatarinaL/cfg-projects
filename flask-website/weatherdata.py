import pandas
import matplotlib as mpl
mpl.use('Agg')
import pprint
#config my pretty print object
pp = pprint.PrettyPrinter(indent=3)

data = pandas.read_csv("weather_year.csv")
#pp.pprint(data[" Mean Humidity"])
pp.pprint(data[["EDT", " Mean Humidity"]].head())
print(data.columns)
#len(data) will give number of rows, data.columns will give column NAMES
#data.*columnname*.head(5) gives first 5 entries, .tail() last
#to change column names:
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

pp.pprint(data[["date", "mean_humidity"]].tail(20))
#dot syntax and std deviation method... (NOTE: using data.std() will give results for all columns)
pp.pprint("Mean Humidity - standard deviation of last 20 entries: " + str(data.mean_humidity.tail(20).std()))


print(data.mean_temp.hist()) #TODO: show plot, this is the object <matplotlib.axes.AxesSubplot at 0.775x0.77>
