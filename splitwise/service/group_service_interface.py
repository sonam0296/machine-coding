import abc 

#  FORMAL INTERFACE
class GroupServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod    # abstract method is used which means anyhow we have to call addBill method with the signatures provided
    def addGroup(self, id, name, members):
        pass  # Pass means =>>> do nothing