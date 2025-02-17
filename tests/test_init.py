from esphome_glyphsets import defined_glyphsets, unicodes_per_glyphset


def test_defined_glyphsets() -> None:
    """Test defined_glyphsets."""
    assert "GF_Latin_Core" in defined_glyphsets()


def test_unicodes_per_glyphset() -> None:
    """Test unicodes_per_glyphset."""
    assert unicodes_per_glyphset("GF_Latin_Core")
    assert not unicodes_per_glyphset("GF_Latin_Core_Invalid")
