from splitwise.service.bill_service_interface import BillServiceInterface
from splitwise.models.bill import Bill

class BillService():
    billDetails = {}   # class level dictionary which can be accessed using self.__class__ 
    def addBill(self,id, groupId, amount, contribution, paidBy):
        bill = Bill()   # created instance of Bill model and setting its value attribute
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill     # If we do self.id => Object medthod & if want to access class object we have do self.__class__
        return bill