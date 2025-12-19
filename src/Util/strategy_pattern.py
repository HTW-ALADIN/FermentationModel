from typing import TypeVar, Generic, Dict

T = TypeVar("T")


class Strategy(Generic[T]):
    strategies: Dict[str, T]

    @staticmethod
    def register_strategy(strategy: T):
        Strategy.strategies[type(strategy).__name__]

    @staticmethod
    def select_strategy(strategy_name: str):
        return Strategy.strategies[strategy_name]()
