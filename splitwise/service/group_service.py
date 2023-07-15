from splitwise.service.group_service_interface import GroupServiceInterface
from splitwise.models.groups import Group

class GroupService():
    groupDetails = {}   # class level dictionary which can be accessed using self.__class__ 
    def addGroup(self,id, name, members):
        group = Group()   # created instance of Group model and setting its value attribute
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groupDetails[id] = group     # If we do self.id => Object medthod & if want to access class object we have do self.__class__
        return group