"""Executable checks for the granite-net-packet-pipe casebook."""

from __future__ import annotations

from collections import Counter

from . import granite_net_packet_pipe_segment_00
from . import granite_net_packet_pipe_segment_01
from . import granite_net_packet_pipe_segment_02
from . import granite_net_packet_pipe_segment_03
from . import granite_net_packet_pipe_segment_04
from . import granite_net_packet_pipe_segment_05
from . import granite_net_packet_pipe_segment_06
from . import granite_net_packet_pipe_segment_07
from . import granite_net_packet_pipe_segment_08
from . import granite_net_packet_pipe_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from granite_net_packet_pipe_segment_00.iter_granite_net_packet_pipe_00()
    yield from granite_net_packet_pipe_segment_01.iter_granite_net_packet_pipe_01()
    yield from granite_net_packet_pipe_segment_02.iter_granite_net_packet_pipe_02()
    yield from granite_net_packet_pipe_segment_03.iter_granite_net_packet_pipe_03()
    yield from granite_net_packet_pipe_segment_04.iter_granite_net_packet_pipe_04()
    yield from granite_net_packet_pipe_segment_05.iter_granite_net_packet_pipe_05()
    yield from granite_net_packet_pipe_segment_06.iter_granite_net_packet_pipe_06()
    yield from granite_net_packet_pipe_segment_07.iter_granite_net_packet_pipe_07()
    yield from granite_net_packet_pipe_segment_08.iter_granite_net_packet_pipe_08()
    yield from granite_net_packet_pipe_segment_09.iter_granite_net_packet_pipe_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def granite_net_packet_pipe_summary() -> dict:
    return assert_expected()
