# 第二版测试,增加一个测试多个response的测试

from UnittestClass import AnonymousSurvey
import unittest

class TestAnonymousSurvey(unittest.TestCase):
    """针对class的test"""

    def test_store_single_response(self):
        """测试单个答案的储存状况"""

        # 在测试中建立实例
        my_survey = AnonymousSurvey("what language did you first learn to code?")
        my_survey.store_response("python")
        self.assertIn("python", my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        my_survey = AnonymousSurvey("what language did you first learn to code?")
        uresponses = ["python", "java", "C#"]
        for response in uresponses:
            my_survey.store_response(response)
        for response in uresponses:
            self.assertIn(response, my_survey.responses)

unittest.main()
