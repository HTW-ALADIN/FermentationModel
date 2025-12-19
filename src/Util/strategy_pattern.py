from typing import TypeVar, Generic, Dict

T = TypeVar("T")


class Strategy(Generic[T]):
    strategies: Dict[str, T]

    @staticmethod
    def register_strategy(self, strategy: T):
        self.strategies[type(strategy).__name__]

    @staticmethod
    def select_strategy(self, strategy_name: str):
        return self.strategies[strategy_name]()
