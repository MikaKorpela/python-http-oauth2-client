import argparse
import json
from rauth import OAuth2Service

parser = argparse.ArgumentParser()
args: argparse.Namespace

parser.add_argument("--client-secret", type=str, required=True)
parser.add_argument("--password", type=str, required=True)
args = parser.parse_args()

oauth_service = OAuth2Service(
    client_id='spring-boot-login',
    client_secret=args.client_secret,
    authorize_url='http://localhost:8080/realms/SpringBootRealm/protocol/openid-connect/token',
    access_token_url='http://localhost:8080/realms/SpringBootRealm/protocol/openid-connect/token',
    base_url='http://localhost:8081'
)

data = {
    'grant_type': 'password',
    'username': 'duey',
    'password': args.password
}
oauth_session = oauth_service.get_auth_session(data=data, decoder=json.loads)

response = oauth_session.get('/api/ducks/1')

response_json = response.json()
print(response_json["uid"])
print(response_json["name"])