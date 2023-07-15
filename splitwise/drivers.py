import sys

sys.path.append('/Users/sonamjha/sonam_project/python_projects/machine_coding')

from splitwise.controller.user_controller import UserController
from splitwise.controller.group_controller import GroupController
from splitwise.controller.bill_controller import BillController

from splitwise.service.bill_service import BillService
from splitwise.service.user_service import UserService
from splitwise.service.group_service import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1', 'sonam')
user2 = userController.addUser('user2', 'mukund')
user3 = userController.addUser('user3', 'sandesh')
user4 = userController.addUser('user4', 'resham')
user5 = userController.addUser('user5', 'Sona')

members = [user1, user2, user3, user4, user5]
group1 = groupController.addGroup('Group1', 'Bachelors', members)

# print(group1.getMembers())

paidBy = {'user1': 200, 'user2': 100, 'user3': 50, 'user4': 50, 'user5': 100}
contribution = {'user1': 100, 'user2': 100, 'user3': 100, 'user4': 100, 'user5': 100}

bill = billController.addBill('bill1', group1, 500, contribution, paidBy)

balance = billController.userBalance('user2')
balance = billController.userBalance('user1')
balance = billController.userBalance('user3')
balance = billController.userBalance('user4')

print(balance)