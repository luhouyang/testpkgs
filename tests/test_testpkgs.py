import matplotlib.container
from testpkgs.testpkgs import count_words
from collections import Counter
from testpkgs.plotting import plot_words
from testpkgs.dataset import get_flatland
import matplotlib
import pytest


@pytest.fixture
def einstein_counts():
    return Counter({
        'insanity': 1,
        'is': 1,
        'doing': 1,
        'the': 1,
        'same': 1,
        'thing': 1,
        'over': 2,
        'and': 2,
        'expecting': 1,
        'different': 1,
        'results': 1
    })


def test_count_words(einstein_counts):
    expected = einstein_counts

    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein says you're wrong!"


def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    fig = plot_words(einstein_counts)
    assert isinstance(fig,
                      matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"


def test_plot_words_error():
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        list_object = ["Pythons", "are", "non", "venomous"]
        plot_words(list_object)


def test_plot_words_error():
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        list_object = ["Pythons", "are", "non", "venomous"]
        plot_words(list_object)


def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig,
                      matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"


def test_regression():
    """Regression test for Flatland"""
    top_word = count_words(get_flatland()).most_common(1)
    assert top_word[0][0] == "a", "Most common word is not 'a's"
    assert top_word[0][1] == 5, "'a' count has changes"
