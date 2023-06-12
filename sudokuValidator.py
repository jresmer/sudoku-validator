import concurrent.futures as cf


class SudokuValidator:

    @staticmethod
    def __validator_thread(boards: list, results: list) -> None:
        pass

    def working_process(self, boards: list, n_threads: int) -> list:
        n_boards = len(boards)
        results = [1] * n_boards

        if n_boards >= n_threads:
            boards_per_thread = n_boards // n_threads
            remainder = n_boards % n_threads
            acum_boards = []

            current_index = 0
            for i in range(n_threads):
                start_index = current_index
                current_index += boards_per_thread
                if i < remainder: current_index += 1
                acum_boards.append(boards[start_index:current_index:1])

            with cf.ThreadPoolExecutor(max_workers=n_threads) as t_pool:
                future_t = {t_pool.submit(self.__validator_thread, t_boards, results) :
                            t_boards for t_boards in acum_boards}
                
            while 1:
                if future_t.done(): break
        else: 
            pass
            
        return results
