import unittest


class MyTest(unittest.TestCase):  # �̳�unittest.TestCase
    def tearDown(self):
        # ÿ����������ִ��֮��������
        print('111')

    def setUp(self):
        # ÿ����������ִ��֮ǰ������
        print('22222')

    @classmethod
    def tearDownClass(self):
        # ����ʹ�� @ classmethodװ����, ����test�����������һ��
        print('4444444')

    @classmethod
    def setUpClass(self):
        # ����ʹ��@classmethod װ����,����test����ǰ����һ��
        print('33333')

    def test_a_run(self):
        self.assertEqual(1, 1)  # ��������

    def test_b_run(self):
        self.assertEqual(2, 2)  # ��������


if __name__ == '__main__':
    unittest.main()  # �������еĲ�������