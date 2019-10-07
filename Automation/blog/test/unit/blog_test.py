from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My day', 'Luis')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My day by Luis (0 posts)')

    def test_repr_multiple_post(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['Test']
        b2 = Blog('Holis', 'La Yoli')
        b2.posts = ['Test', 'Nawara']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Holis by La Yoli (2 posts)')