import pytest

# ================= 1. Fixture：为测试提供模拟数据和环境 =================
# 这是一个模拟的用户数据库，在实际测试中可以用来替代真实的数据库。
@pytest.fixture
def user_db():
    """模拟一个用户数据库，用于登录测试"""
    print("\n--- 正在准备测试数据库... ---")
    # 定义一个包含模拟用户的字典
    db = {
        "admin": {"password": "123456", "role": "administrator"},
        "test_user": {"password": "pytest", "role": "tester"},
        "guest": {"password": "guest123", "role": "visitor"}
    }
    # yield 关键字的作用：将 db 提供给测试函数，并在测试结束后执行清理代码
    yield db
    print("\n--- 清理测试数据库... ---")

# ================= 2. 主要测试逻辑 =================

# ----- 场景一：用参数化测试一个简单的计算器函数 -----
def add(a, b):
    """一个简单的加法函数，用于演示参数化测试"""
    return a + b

# @pytest.mark.parametrize 是参数化的核心，它会让同一个测试函数运行多次，每次使用不同的参数
# 这里，每组数据 (a, b, expected) 都是独立的一条测试用例
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 5, 4),
    (100, -50, 50),
    (1.5, 2.5, 4.0),  # 小数测试
    (0, 9999, 9999),
])
def test_add_function(a, b, expected):
    """测试加法运算是否正确"""
    # Assert 断言：断言实际结果是否等于预期结果
    # 如果不相等，pytest 会清晰地显示出 a, b, expected 和 actual 的值
    assert add(a, b) == expected

# ----- 场景二：登录功能（使用 Fixture 和参数化）-----

# 这是一个模拟的登录接口函数
def login(username, password, database):
    """
    模拟登录逻辑：
    1. 检查用户名是否存在
    2. 检查密码是否匹配
    """
    user = database.get(username)
    if not user:
        return {"code": 404, "message": "用户不存在"}
    if user["password"] != password:
        return {"code": 401, "message": "密码错误"}
    # 若用户名和密码都正确，则返回成功状态（此处模拟生成一个简单的 token）
    return {"code": 0, "message": "登录成功", "token": "mock-jwt-token"}

# 这里，我们使用参数化来测试多种登录场景
# 每一组数据都代表一次独立的登录尝试
@pytest.mark.parametrize("username, password, expected_code, expected_msg", [
    ("admin", "123456", 0, "登录成功"),                # 成功案例
    ("admin", "wrong_password", 401, "密码错误"),      # 密码错误
    ("unknown_user", "any_password", 404, "用户不存在"), # 用户不存在
    ("test_user", "pytest", 0, "登录成功"),             # 另一个成功案例
    ("guest", "guest123", 0, "登录成功"),              # 成功案例
    ("", "123456", 404, "用户不存在"),                 # 边界：用户名为空
])
def test_login(username, password, expected_code, expected_msg, user_db):
    """
    这是一个使用 fixture (user_db) 和参数化的完整测试。
    user_db 参数会自动从上面的 @pytest.fixture 中获取返回值。
    """
    # Act: 调用登录函数
    result = login(username, password, user_db)

    # Assert: 使用断言来验证返回结果是否符合预期
    assert result["code"] == expected_code
    assert result["message"] == expected_msg

    # 如果是登录成功的场景，额外验证 token 字段是否存在且不为空
    if expected_code == 0:
        assert "token" in result
        assert result["token"] is not None
        assert len(result["token"]) > 0

if __name__ == '__main__':
    pytest.main("-s test_demo.py") # 调用pytest的main函数执行测试