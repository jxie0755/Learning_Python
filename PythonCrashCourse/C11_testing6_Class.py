# 使用setUp()来测试
# setUp中的这一个实例,既能够充当测试中的属性,又成为源代码的一个实例, 这样可以多次引用源代码中的方法和属性
# 可以有效简化代码,避免重复创造实例和结果.

from testingClass import AnonymousSurvey
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """针对class的test"""

    # 创建一个setUp(),类似初始化,提供了一个实例和一组输入
    def setUp(self):
        """创造一个调查对象和一组答案,以供使用"""
        # 创造一个属性,作为原代码中的实例
        self.my_survey = AnonymousSurvey("what language did you first learn to code?")
        # 创造另一个,作为测试用的用户输入
        self.uresponses = ['python', 'java', 'C#']

    def test_store_single_response(self):
        """Test single answers"""
        self.my_survey.store_response(self.uresponses[0])  # 作为实例,引用源代码方法
        self.assertIn(self.uresponses[0], self.my_survey.responses)  # 实例成为原代码属性

    def test_store_three_responses(self):
        """Test that three individual answers are stored properly."""
        for response in self.uresponses:
            self.my_survey.store_response(response)
        for response in self.uresponses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()