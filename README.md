# Python HTTP - OAuth2 Client

Examples in this repository uses ```rauth```, which is a Python OAuth, OAuth2 and Ofly consumer library.

Authentication service used with the examples in this repository is Keycloak server, running in local machine.

## Keycloak Settings

Keycloak has a realm called ```SpringBootRealm```.

The realm has one user called ```duey``` who has a role called ```user``` assigned.

The realm has two clients:
* ```spring-boot-login``` that has no additional settings.
* ```spring-boot-login-public``` that has *client authentication* and *service account roles* enabled and the role called ```user``` assigned.

## Grant Type - Password

This grant type is used, when a human client is accessing the server.

The authorization request must contain ```client-id```, ```client-secret```, ```username``` and ```password```.

The received token contains the role assignment of the user identified by ```username```.

## Grant Type - Client Credentials

This grant type is used, when a machine client is accessing the server.

The authorization request must contain ```client-id``` and ```client-secret```.

The received token contains the role assignment of the client identified by ```client-id```.

