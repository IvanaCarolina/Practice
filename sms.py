from twilio.rest import Client 
 
account_sid = 'ACa51ced0fef5dadc1fb01b1367c9ac234' 
auth_token = 'd222096792daef95c2b4d7e4fa5f5b8e' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGa55675b2303c8f48a38ada8f44325842', 
                              body='hello gorgeous <3 love u',      
                              to='+5511998450399' 
                          ) 
print(message.sid)