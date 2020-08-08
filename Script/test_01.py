import allure

class Test_01:
    @allure.step('1')
    def test_01(self):
        print('\ntest_01')
        assert True
    @allure.step('2')
    def test_02(self):
        print('\ntest_02')
        assert True
