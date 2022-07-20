import requests
from decouple import config
import base64
import pandas as pd


def get_token(client_id, client_secret):

	client_str = f'{client_id}:{client_secret}'
	client_encode = base64.b64encode(client_str.encode("utf-8"))
	client_encode = str(client_encode, "utf-8")  # Codificado en String
	token_url = 'https://accounts.spotify.com/api/token'
	params = {'grant_type': 'client_credentials'}
	headers = {'Authorization' : f'Basic {client_encode}'}

	r = requests.post(token_url, data=params, headers=headers)

	if r.status_code == 200:
		token = r.json()['access_token']
	else:
		token = None

	return token


if __name__ == '__main__':


	muse_id = '12Chz98pHFMPJEknJQMWvI'
	url_muse = f'https://api.spotify.com/v1/artists/{muse_id}'

	client_id = config("Client_ID")
	client_secret = config("Client_Secret")
	token = get_token(client_id, client_secret)


	#get muse info

	header_muse = {'Authorization': f'Bearer {token}'}

	r_muse = requests.get(url_muse, headers=header_muse)
	print(r_muse.status_code)
	print(r_muse.json())


	#busqueda

	url_search = 'https://api.spotify.com/v1/search'

	search_params = {'q': 'Muse', 'type': 'artist', 'market': 'CL'}

	search = requests.get(url_search, headers=header_muse, params=search_params)

	print(search.status_code)
	print(search.json())


	df = pd.DataFrame(search.json()['artists']['items'])

	print(df.head())
