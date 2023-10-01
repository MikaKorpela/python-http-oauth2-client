import argparse
import json
from rauth import OAuth2Service

parser = argparse.ArgumentParser()
args: argparse.Namespace

parser.add_argument("--client-secret", type=str, required=True)
parser.add_argument("--password", type=str, required=True)
args = parser.parse_args()

authorization_service = OAuth2Service(
    client_id='spring-boot-login',
    client_secret=args.client_secret,
    authorize_url='http://localhost:8080/realms/SpringBootRealm/protocol/openid-connect/token',
    access_token_url='http://localhost:8080/realms/SpringBootRealm/protocol/openid-connect/token',
    base_url='http://localhost:8081'
)

authorization_payload = {
    'grant_type': 'password',
    'username': 'duey',
    'password': args.password
}
ducks_service_session = authorization_service.get_auth_session(data=authorization_payload, decoder=json.loads)

response = oauth_session.get('/api/ducks/1')

response_json = response.json()
print(response_json["uid"])
print(response_json["name"])