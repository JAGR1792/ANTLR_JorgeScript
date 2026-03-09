from __future__ import annotations

import statistics
import time

from eval_visitor import EvalVisitor
from main import execute


SIZES = [10, 30, 60]
REPEATS = 2


def micelio_for(n: int) -> str:
    return f"""para i = 0 hasta {n - 1} {{
  imp i
}}\n"""


def micelio_while(n: int) -> str:
    return f"""var i = 0
mientras (i < {n}) {{
  imp i
  i = i + 1
}}\n"""


def micelio_for_en(n: int) -> str:
    elems = ", ".join(str(i) for i in range(n))
    return f"""var xs = [{elems}]
para x en xs {{
  imp x
}}\n"""


def run_micelio(code: str) -> float:
    visitor = EvalVisitor(base_dir=".")
    t0 = time.perf_counter()
    execute(code, visitor)
    return time.perf_counter() - t0


def run_python_for(n: int) -> float:
    t0 = time.perf_counter()
    for i in range(n):
        print(i)
    return time.perf_counter() - t0


def run_python_while(n: int) -> float:
    t0 = time.perf_counter()
    i = 0
    while i < n:
        print(i)
        i += 1
    return time.perf_counter() - t0


def run_python_for_en(n: int) -> float:
    xs = list(range(n))
    t0 = time.perf_counter()
    for x in xs:
        print(x)
    return time.perf_counter() - t0


def median_time(samples: list[float]) -> float:
    return statistics.median(samples)


def benchmark_case(name: str, n: int, micelio_builder, py_runner) -> tuple[float, float, float]:
    micelio_samples: list[float] = []
    python_samples: list[float] = []

    for rep in range(REPEATS):
        print(f"\n--- {name} | n={n} | repeticion {rep + 1}/{REPEATS} | Micelio ---")
        micelio_samples.append(run_micelio(micelio_builder(n)))

        print(f"\n--- {name} | n={n} | repeticion {rep + 1}/{REPEATS} | Python ---")
        python_samples.append(py_runner(n))

    micelio_t = median_time(micelio_samples)
    python_t = median_time(python_samples)
    ratio = micelio_t / python_t if python_t > 0 else float("inf")
    return micelio_t, python_t, ratio


def main() -> None:
    print("Comparativa con impresion real en pantalla (imp/print)")
    print(f"Tamanos: {SIZES} | Repeticiones por caso: {REPEATS}")

    cases = [
        ("for numerico", micelio_for, run_python_for),
        ("while", micelio_while, run_python_while),
        ("for en lista", micelio_for_en, run_python_for_en),
    ]

    rows: list[tuple[str, int, float, float, float]] = []
    for name, mic_builder, py_runner in cases:
        for n in SIZES:
            m, p, r = benchmark_case(name, n, mic_builder, py_runner)
            rows.append((name, n, m, p, r))

    print("\n===== RESUMEN (mediana) =====")
    print("caso | n | micelio_s | python_s | ratio")
    for name, n, m, p, r in rows:
        print(f"{name} | {n} | {m:.6f} | {p:.6f} | {r:.2f}x")


if __name__ == "__main__":
    main()
