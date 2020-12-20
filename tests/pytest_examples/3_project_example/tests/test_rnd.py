def test_fixture_dependency(rnd, global_fixture):
    assert isinstance(rnd, float)
    assert global_fixture == 'global fixture'
global_fixture