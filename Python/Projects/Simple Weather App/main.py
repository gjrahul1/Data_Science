from providers.WeatherAPIProvider import WeatherAPIProvider

#Calling Our API Provider 
Provider = WeatherAPIProvider()

#Fetching the endpoint
try:
    api_endpoint_result = Provider.get_weather("Bengaluru")

    #Sorting the results
    location_results = api_endpoint_result.get("location")
    temperature_results = api_endpoint_result.get("current")
    temperature_condition_results = temperature_results.get("condition")

    #Location Details
    _name = location_results.get("name")
    _region = location_results.get("region")
    _country = location_results.get("country")

    #Weather Details
    _temp_c = temperature_results.get("temp_c")

    #Weather Condition Details
    _temperature_condition = temperature_condition_results.get("text")

    #Precieved Temperature
    _feels_like_c = temperature_results.get("feelslike_c")

    print(f"Name:{_name}\n Region:{_region}\n Country:{_country}\n Temperature:{_temp_c}\n Temperature Condition:{_temperature_condition}\n Feels Like:{_feels_like_c}")

except Exception as e:
    print(f"Error: {e}")