import unittest
from survey import AnonymousSurvey
class testAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试类"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question="What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Chinese','Japenese']
    def test_store_single_response(self):
        """测试单个答案会被存储"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        for re in self.responses:
            self.my_survey.store_responses(re)
        for re in self.responses:
            self.assertIn(re,self.my_survey.responses)
unittest.main