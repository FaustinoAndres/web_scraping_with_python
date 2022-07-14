import requests
from decouple import config


if __name__ == '__main__':


	muse_id = '12Chz98pHFMPJEknJQMWvI'
	url_muse = f'https://api.spotify.com/v1/artists/{muse_id}'

	client_str = f'{config("Client_ID")}:{config("Client_Secret")}'

	r = requests.get(url_muse)
	print(r.status_code)
	print(r.json())
	print(client_str)