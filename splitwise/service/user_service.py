from splitwise.service.user_service_interface import UserServiceInterface
from splitwise.models.user import User

class UserService():
    userDetails = {}   # class level dictionary which can be accessed using self.__class__ 
    def addUser(self, id, name):
        user = User()   # created instance of user model and setting its value attribute
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user     
        # If we do self.id => Object medthod & if want to access class object we have do self.__class__
        return user