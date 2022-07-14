import requests
from decouple import config
import base64


if __name__ == '__main__':


	muse_id = '12Chz98pHFMPJEknJQMWvI'
	url_muse = f'https://api.spotify.com/v1/artists/{muse_id}'

	client_str = f'{config("Client_ID")}:{config("Client_Secret")}'

	client_encode = base64.b64encode(client_str.encode("utf-8"))  # Codificado en Bytes
	client_encode = str(client_encode, "utf-8")  # Codificado en String

	token_url = 'https://accounts.spotify.com/api/token'
	params = {'grant_type': 'client_credentials'}
	headers= {'Authorization' : f'Basic {client_encode}'}

	r = requests.post(token_url, data=params, headers=headers)
	print(r.status_code)
	print(r.json())

	token = r.json()['access_token']

	#get muse info

	header_muse = {'Authorization': f'Bearer {token}'}

	r_muse = requests.get(url_muse, headers=header_muse)
	print(r_muse.status_code)
	print(r_muse.json())

