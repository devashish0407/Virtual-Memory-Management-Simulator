from simulator.core import VirtualMemorySimulator


def run_sim(algorithm, refs, virtual_kb=16, physical_kb=2, page_kb=1):
    sim = VirtualMemorySimulator(virtual_kb, physical_kb, page_kb, algorithm)
    sim.run_simulation(refs)
    return sim


def test_fifo_tracks_page_faults_and_final_frames():
    refs = [(0, "R"), (1024, "R"), (2048, "R"), (0, "R")]

    sim = run_sim("FIFO", refs)

    assert sim.get_stats()["Total Memory Accesses"] == 4
    assert sim.get_stats()["Total Page Faults"] == 4
    assert sim.frames == [2, 0]


def test_lru_evicts_least_recently_used_page():
    refs = [(0, "R"), (1024, "R"), (0, "R"), (2048, "R")]

    sim = run_sim("LRU", refs)

    assert sim.get_stats()["Total Page Faults"] == 3
    assert sim.frames == [0, 2]
    assert sim.page_table[1].valid is False


def test_optimal_evicts_page_used_farthest_in_future():
    refs = [(0, "R"), (1024, "R"), (2048, "R"), (0, "R"), (1024, "R")]

    sim = run_sim("Optimal", refs)

    assert sim.get_stats()["Total Page Faults"] == 4
    assert "Evicted VPN 1" in sim.log[2]["Comments"]
    assert sim.frames == [1, 2]
    assert sim.page_table[0].valid is False


def test_tlb_hit_rate_increases_on_repeated_access():
    refs = [(0, "R"), (0, "R"), (0, "R")]

    sim = run_sim("FIFO", refs)

    stats = sim.get_stats()
    assert stats["Total Page Faults"] == 1
    assert stats["TLB Hit Rate"] == 2 / 3


def test_dirty_page_is_tracked_and_written_back_on_eviction():
    refs = [(0, "W"), (1024, "R"), (2048, "R")]

    sim = run_sim("FIFO", refs)

    assert sim.page_table[0].valid is False
    assert 0 not in sim.dirty_pages
    assert "(Dirty page written back)" in sim.log[-1]["Comments"]


def test_invalid_virtual_address_is_logged_without_crashing():
    sim = run_sim("FIFO", [(999999, "R")], virtual_kb=1, physical_kb=1, page_kb=1)

    assert sim.log[0]["Page Fault"] == "N/A"
    assert "Invalid Virtual Address" in sim.log[0]["Comments"]
