import requests
# define function to get your strava data
def get_data(access_token, start_date, end_date, per_page=200, page=1):
 
   activities_url = 'https://www.strava.com/api/v3/athlete/activities'
   headers = {'Authorization': 'Bearer ' + access_token}
   params = {"before": end_date.timestamp(),
             "after": start_date.timestamp(),
             'per_page': per_page, 
             'page': page}
   
   data = requests.get(
       activities_url, 
       headers=headers, 
       params=params
   ).json()
 
   return data