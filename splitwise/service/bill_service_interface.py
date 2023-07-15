import abc 

#  FORMAL INTERFACE
class BillServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod    # abstract method is used which means anyhow we have to call addBill method with the signatures provided
    def addBill(self,id, groupId, amount, contribution, paidBy):
        pass  # Pass means =>>> do nothing