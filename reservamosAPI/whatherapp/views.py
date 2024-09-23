import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class CityWeatherView(APIView):
    
    RESERVAMOS_API_URL = "https://search.reservamos.mx/api/v2/places"
    
    OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
    

    def get(self, request):
        city_name = request.query_params.get('city')
        if not city_name:
            return Response({"error": "City name is required"}, status=status.HTTP_400_BAD_REQUEST)

        
        # get de las cordenadas  desde la api 
        reservamos_response = self.get_city_coordinates(city_name)
        if not reservamos_response:
            return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        #array de los datos del clima 
        weather_data = []

        # for de las coordenadas para cada ciudad en la primera api 
        for city in reservamos_response:
            weather = self.get_weather_for_city(city['lat'], city['long'])
            if weather:
                weather_data.append({
                    'city': city['display'],
                    'forecast': weather
                })
        
        return Response(weather_data, status=status.HTTP_200_OK)

    def get_city_coordinates(self, city_name):
        #fetch de las cuidades 
        try:
            params = {'q': city_name, 'country': 'MX'}
            response = requests.get(self.RESERVAMOS_API_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None
    
    def get_weather_for_city(self, lat, lon):
        # fetch de las coordenadas 
        #OpenWeather API
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'exclude': 'minutely,hourly,current',
                'units': 'metric',
                'appid': settings.OPENWEATHER_API_KEY 
            }
            response = requests.get(self.OPENWEATHER_API_URL, params=params)
            response.raise_for_status()
            weather_data = response.json().get('daily', [])
            
            # temp maxima y minima de los 7 dias 
            return [
                {'day': i + 1, 'max_temp': day['temp']['max'], 'min_temp': day['temp']['min']}
                for i, day in enumerate(weather_data[:7])
            ]
        except requests.RequestException:
            return None
    

    