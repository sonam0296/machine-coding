import abc 

#  FORMAL INTERFACE
class UserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod    # abstract method is used which means anyhow we have to call addBill method with the signatures provided
    def addUser(self, id, name):
        pass  # Pass means =>>> do nothing