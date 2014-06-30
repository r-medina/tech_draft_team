from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = '77bhx7s6k3o16c'
CONSUMER_SECRET = 'cFVx1Pc89DoIT4SN'
USER_TOKEN = 'f8eb0f21-8238-4f0f-ae9a-58eaa66e437a'
USER_SECRET = 'f58a3f9e-9de0-43f0-b1bb-273d502bc2ba'
RETURN_URL = 'localhost:8000'

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

print application.get_profile()