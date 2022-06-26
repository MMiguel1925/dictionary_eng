from abc import ABC, abstractmethod


class Page(ABC):
    """
    Uma classe abstracta nao pode ser instanciada.
    ela serve apenas para definir uam estrutura: classe mae - classe filho
    """

    @abstractmethod
    def serve(self):
        pass
