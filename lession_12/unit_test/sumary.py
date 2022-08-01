# 1. Intall pytest: pip install pytest

# 2. Identify test files (file with subfix is test_) and test functions (function with subfix is test_).

# 3. Execute all test files / test functions: pytest -v

# 4. Execute specific test files: pytest <file_name> -v

# 5. Execute specific test functions: pytest -k <substring> -v

# 6. Create input for test function: @pytest.fixture

# 7. Conftest.py file allows accessing fixture from multiple test files.

# 8. Execute multiple a test function: @pytest.mark.parametrize

# 9. Stop test execution after n failures: pytest --maxfail=<num>

# 10. Run tests in parallel: pip intall pytest-xdist => pytest -n <num>

# 11. Generate test resuls with xml format: pytest -v --junitxml="<file_name.xml>"
