from User import User
from UserDAO import UserDAO
from userSchema import UserBase
import create_tables

if __name__ == '__main__':
    create_tables.create_all()
    
    
    
    
    #U = User(email = "Marcos")
    #U = UserBase(email = "123@gmail.com",createdOn = 1)
    #dt = {"firt_name":"MarcOs"}
    #U.setAll(dt)
    #print(U.getFirstName())
    #D = UserDAO()
    #print(D.findUserByEmail("Ana@gmail.com").getPassword())
    
    #print(D.INSERT({"cpf":6, "firt_name":"Zé", "last_name":"", "email":"@zé", "password":"senha", "type":"admin"}))
    #print(D.UPDATE({"cpf":"10", "firt_name":"Joaquim", "last_name":"", "email":"jq@", "password":"1234", "type":"admin"}, D.WHERE("cpf","=","10")))
    #print(D.findUsers(D.WHERE("password", "=", "123"))[0].getEmail())
    #print(D.SELECT(['firt_name', 'password'], D.WHERE("firt_name", "=", "Marcos").OR("cpf", "=", "123")))
    #print(U.getName())
    #User.find(['firt_name', 'password'], U.WHERE('password', '=', '123').OR("cpf", "<", '5')._extractCommand())
    #print(D.DELETE(D.WHERE("cpf", "=", "10")))