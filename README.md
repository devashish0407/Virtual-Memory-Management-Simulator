# Virtual Memory Management Simulator

An interactive operating-systems simulator for visualizing virtual memory address translation, page tables, TLB behavior, page faults, dirty-bit handling, and page replacement algorithms.

## Features

- Simulates virtual-to-physical address translation with configurable virtual memory size, physical memory size, and page size.
- Implements FIFO, LRU, and Optimal page replacement algorithms.
- Models page tables, physical frames, TLB entries, valid bits, dirty bits, offsets, and virtual page numbers.
- Compares algorithm performance using page faults, page fault rate, total accesses, and TLB hit rate.
- Provides step-by-step memory-frame visualization with Streamlit and Altair.
- Exports frame-state simulation logs to CSV for offline analysis.
- Includes pytest coverage for replacement algorithms, TLB hits, dirty-page write-back, invalid addresses, and workload parsing.

## Tech Stack

- Python
- Streamlit
- Pandas
- Altair
- Pytest

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- pytest.ini
|-- simulator
|   |-- core.py
|   |-- data_structures.py
|   `-- __init__.py
|-- utils
|   |-- display_utils.py
|   |-- input_parser.py
|   |-- simulation_runners.py
|   `-- __init__.py
`-- tests
    |-- test_input_parser.py
    `-- test_simulator.py
```

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt
pip install pytest
```

Run the app:

```bash
streamlit run app.py
```

Run tests:

```bash
pytest
```

## Example Workload

```text
0x0000 R, 0x1000 R, 0x2000 W, 0x3000 R, 0x0000 R, 0x1000 R
```

Each entry contains a virtual address and an operation:

- `R`: read operation
- `W`: write operation

