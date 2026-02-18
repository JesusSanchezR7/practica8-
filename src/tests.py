from form import userform

def test_email():
    form = userform()
    assert form.validate_email("correo.com") == True  

def test_password():
    form = userform()
    assert form.validate_password("123") == True 

def test_register():
    form = userform()
    assert form.register("test@test.com", "123") == True 
