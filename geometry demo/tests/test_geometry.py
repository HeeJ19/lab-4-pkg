import pytest
from geometry import Rectangle, Triangle, Shape, area_stats

def test_square_area_zero_and_positive():
    # Arrange
    square_zero = Rectangle(0, 0)
    square_pos = Rectangle(3, 3)
    
    # Act
    area_zero = square_zero.area()
    area_pos = square_pos.area()
    
    # Assert
    assert area_zero == pytest.approx(0)
    assert area_pos == pytest.approx(9)

def test_stats_keys_and_values():
    # Arrange
    r = Rectangle(3, 4)
    t = Triangle(3, 4, 5)
    
    # Act
    stats = area_stats(r, t)
    
    # Assert
    assert isinstance(stats, dict)
    expected_keys = {"n", "total", "mean", "min", "max"}
    assert set(stats.keys()) == expected_keys
    for value in stats.values():
        assert isinstance(value, (int, float))

def test_stats_raises_without_shapes():
    # Assert
    with pytest.raises(ValueError, match="At least one Shape is required"):
        area_stats()
