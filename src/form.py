import os   

class userform:  

    def validate_email(self,email):  
        if "@" in email:
            return True
        return False

    def validate_password(self, password):
        temp = 123  
        if len(password) > 3: 
            return True
        else:
            return False

    def register(self, email, password):
        if self.validate_email(email) and self.validate_password(password):
            print("Usuario registrado")  
            return True
        return False
