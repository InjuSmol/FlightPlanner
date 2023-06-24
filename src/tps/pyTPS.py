from typing import List
from pyTPS_Transaction import pyTPS_Transaction

class pyTPS:
    def __init__(self):
        self.transactions: List[pyTPS_Transaction] = []
        self.numTransactions: int = 0
        self.mostRecentTransaction: int = -1
        self.performingDo: bool = False
        self.performingUndo: bool = False

    def isPerformingDo(self) -> bool:
        return self.performingDo

    def isPerformingUndo(self) -> bool:
        return self.performingUndo

    def hasTransactionToRedo(self) -> bool:
        return (self.mostRecentTransaction + 1) < self.numTransactions

    def hasTransactionToUndo(self) -> bool:
        return self.mostRecentTransaction >= 0

    def addTransaction(self, transaction: pyTPS_Transaction) -> None:
        if (self.mostRecentTransaction < 0) or (self.mostRecentTransaction < (len(self.transactions) - 1)):
            for i in range(len(self.transactions) - 1, self.mostRecentTransaction, -1):
                self.transactions.pop(i)
            self.numTransactions = self.mostRecentTransaction + 2
        else:
            self.numTransactions += 1

        self.transactions.append(transaction)
        self.doTransaction()

    def doTransaction(self) -> None:
        if self.hasTransactionToRedo():
            self.performingDo = True
            transaction = self.transactions[self.mostRecentTransaction + 1]
            transaction.doTransaction()
            self.mostRecentTransaction += 1
            self.performingDo = False

    def undoTransaction(self) -> None:
        if self.hasTransactionToUndo():
            self.performingUndo = True
            transaction = self.transactions[self.mostRecentTransaction]
            transaction.undoTransaction()
            self.mostRecentTransaction -= 1
            self.performingUndo = False

    def clearAllTransactions(self) -> None:
        self.transactions = []
        self.mostRecentTransaction = -1
        self.numTransactions = 0

    def getSize(self) -> int:
        return len(self.transactions)

    def getRedoSize(self) -> int:
        return self.getSize() - self.mostRecentTransaction - 1

    def getUndoSize(self) -> int:
        return self.mostRecentTransaction + 1

    def toString(self) -> str:
        text = "--Number of Transactions: " + str(self.numTransactions) + "\n"
        text += "--Current Index on Stack: " + str(self.mostRecentTransaction) + "\n"
        text += "--Current Transaction Stack:\n"
        for i in range(self.mostRecentTransaction + 1):
            jT = self.transactions[i]
            text += "----" + jT.toString() + "\n"
        return text
