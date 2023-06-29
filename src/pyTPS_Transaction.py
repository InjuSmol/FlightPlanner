from abc import ABC, abstractmethod

class pyTPS_Transaction(ABC):
    @abstractmethod
    def doTransaction(self) -> None:
        pass

    @abstractmethod
    def undoTransaction(self) -> None:
        pass

    @abstractmethod
    def toString(self) -> str:
        pass
