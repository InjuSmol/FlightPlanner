from abc import ABC, abstractmethod


class PyTPSTransaction(ABC):
    @abstractmethod
    def do_transaction(self) -> None:
        pass

    @abstractmethod
    def undo_transaction(self) -> None:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
