"""Tests for the shared language integration registry."""

from decodability import DECODABILITY_REGISTRY
from decodability.kiswahili import (
    AGGREGATIONS,
    SCORING_METHODS,
    KiswahiliStudentKnowledge,
    extract_words_kiswahili,
)


def test_kiswahili_registry_entry_exposes_the_complete_integration() -> None:
    integration = DECODABILITY_REGISTRY["sw"]

    assert integration == {
        "name": "Kiswahili",
        "extract_words": extract_words_kiswahili,
        "student_knowledge_model": KiswahiliStudentKnowledge,
        # DEPRECATED, pending removal once consumers move to the analysis entries.
        "scoring_methods": SCORING_METHODS,
        "aggregations": AGGREGATIONS,
    }
