import firebase_admin
from firebase_admin import credentials, messaging
from .models import UserToken

cred = credentials.Certificate("/Users/macbook/Documents/seagate/sg/seagateBackEnd/api/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def sendpush(title, msg):
    tokens = UserToken.objects.all()
    allTokens = []
    for tokensList in tokens:
        allTokens.append(tokensList.token)
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title, body=msg),
        tokens=allTokens
    )
    response = messaging.send_multicast(message)
    print('successfully sent message', response)