from app.main import build_info

def test_build_info_has_keys():
    info = build_info()
    assert "app" in info
    assert "env" in info
    assert "git_sha" in info
