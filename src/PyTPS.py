from PyTPSTransaction import PyTPSTransaction
from typing import List


class PyTPS:
    def __init__(self):
        self.transactions: List[PyTPSTransaction] = []
        self.num_transactions = 0
        self.most_recent_transaction = -1
        self.performing_do = False
        self.performing_undo = False

    def is_performing_do(self) -> bool:
        return self.performing_do

    def is_performing_undo(self) -> bool:
        return self.performing_undo

    def has_transaction_to_redo(self) -> bool:
        return (self.most_recent_transaction + 1) < self.num_transactions

    def has_transaction_to_undo(self) -> bool:
        return self.most_recent_transaction >= 0

    def add_transaction(self, transaction: PyTPSTransaction) -> None:
        if (self.most_recent_transaction < 0) or (self.most_recent_transaction < (len(self.transactions) - 1)):
            for i in range(len(self.transactions) - 1, self.most_recent_transaction, -1):
                self.transactions.pop(i)
            self.num_transactions = self.most_recent_transaction + 2
        else:
            self.num_transactions += 1

        self.transactions.append(transaction)
        self.do_transaction()

    def do_transaction(self) -> None:
        if self.has_transaction_to_redo():
            self.performing_do = True
            transaction = self.transactions[self.most_recent_transaction + 1]
            transaction.do_transaction()
            self.most_recent_transaction += 1
            self.performing_do = False

    def undo_transaction(self) -> None:
        if self.has_transaction_to_undo():
            self.performing_undo = True
            transaction = self.transactions[self.most_recent_transaction]
            transaction.undo_transaction()
            self.most_recent_transaction -= 1
            self.performing_undo = False

    def clear_all_transactions(self) -> None:
        self.transactions = []
        self.most_recent_transaction = -1
        self.num_transactions = 0

    def get_size(self) -> int:
        return len(self.transactions)

    def get_redo_size(self) -> int:
        return self.get_size() - self.most_recent_transaction - 1

    def get_undo_size(self) -> int:
        return self.most_recent_transaction + 1

    def to_string(self) -> str:
        text = "--Number of Transactions: " + str(self.num_transactions) + "\n"
        text += "--Current Index on Stack: " + str(self.most_recent_transaction) + "\n"
        text += "--Current Transaction Stack:\n"
        for i in range(self.most_recent_transaction + 1):
            jt = self.transactions[i]
            text += "----" + jt.to_string() + "\n"
        return text
