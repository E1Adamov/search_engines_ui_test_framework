from typing import Any, List
from multiprocessing.pool import ThreadPool

from utils.parallelization.thread_parameters import ThreadParameters


def run_in_threads(*parameters: ThreadParameters) -> List[Any]:
    future_results = []
    final_results = []
    pool = ThreadPool()

    for parameter in parameters:
        future_result = pool.apply_async(
            func=parameter.target,
            args=parameter.args,
            kwds=parameter.kwargs,
        )
        future_results.append(future_result)

    for future_result in future_results:
        final_result = future_result.get()
        final_results.append(final_result)

    return final_results
