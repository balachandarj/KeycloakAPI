from keycloak import KeycloakAdmin
import json

keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                               username='admin',
                               password='admin',
                               realm_name="master",                              
                               client_secret_key="1gk3ejBO4I5TqiNgiJ7hQL0Tch6ow2xL",
                               verify=True)

# Opening JSON file
f = open('users.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
for user in data['users']:
    new_user = keycloak_admin.create_user(
        {
        "email": user['email'],
        "username": user['username'],
        "enabled": True,
        "firstName": user['firstName'],
        "lastName": user['lastName']
        })

                    