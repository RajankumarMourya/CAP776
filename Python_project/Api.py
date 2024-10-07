import requests
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim

class Api:
    def location_by_city(self, city):
        """Get latitude and longitude from a city name."""
        try:
            geolocator = Nominatim(user_agent="sunrise_sunset_app")
            location = geolocator.geocode(city)
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except Exception as e:
            return None, None

    def convert(self, utc_time_str, timezone_str):
        """Convert UTC time to local time based on timezone."""
        try:
            # Parse the UTC time string
            utc_time = datetime.fromisoformat(utc_time_str.replace('Z', '+00:00'))
            
            # Local timezone
            local_tz = pytz.timezone(timezone_str)
            
            # Convert UTC to local time
            local_time = utc_time.astimezone(local_tz)
            
            return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
        except Exception as e:
            return utc_time_str  # Return the original string if conversion fails

    def timezone_by_lat_long(self, lat, lng):
        """Get timezone from latitude and longitude."""
        try:
            response = requests.get(f"http://api.geonames.org/timezoneJSON?lat={lat}&lng={lng}&username=faizan_123")
            data = response.json()
            timezone = data.get('timezoneId', 'Asia/Kolkata')  # Default to Asia/Kolkata if not found
            return timezone
        except requests.exceptions.RequestException as e:
            return 'Asia/Kolkata'  # Fallback to Asia/Kolkata

    def sunrise_sunset(self, city):
        """Get sunrise and sunset times for a specified city."""
        latitude, longitude = self.location_by_city(city)
        if not latitude or not longitude:
            print("Invalid location.")
            return

        api_url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
        
        try:
            response = requests.get(api_url)
            data = response.json()
            
            if data['status'] == "OK":
                # Get the UTC sunrise, sunset, and solar noon times from the API
                sunrise_utc = data['results']['sunrise']
                sunset_utc = data['results']['sunset']
                solar_noon_utc = data['results']['solar_noon']
                day_length = int(data['results']['day_length'])  # Day length in seconds

                # Fetch the local timezone based on latitude and longitude
                timezone = self.timezone_by_lat_long(latitude, longitude)

                # Convert UTC times to local times
                sunrise_local = self.convert(sunrise_utc, timezone)
                sunset_local = self.convert(sunset_utc, timezone)
                solar_noon_local = self.convert(solar_noon_utc, timezone)
                
                # Print out the required results
                print(f"Sunrise (Local Time): {sunrise_local}")
                print(f"Sunset (Local Time): {sunset_local}")
                print(f"Solar Noon (Local Time): {solar_noon_local}")
                print(f"Day Length: {day_length // 3600} hours {day_length % 3600 // 60} minutes")
            else:
                print("Failed to fetch sunrise and sunset data.")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}. Check your internet connection.")


if __name__ == "__main__":
    api = Api()
    city = input("Enter city to get sunrise and sunset times: ")
    api.sunrise_sunset(city)
