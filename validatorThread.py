import threading as td


class ValidatorThread(td.Thread):

    def run(board: str, chunk: tuple) -> bool: # validade do chunk avaliado
        pass