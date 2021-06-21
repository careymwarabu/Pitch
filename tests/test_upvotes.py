import unittest
from app.models import Pitch, Upvote,User


class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Carey = User(username='lizlisa', password='banana', email='lizlisa@gmail.com')  
        self.pitch_carey = Pitch(title='motivation', pitch='This is the ghetto', category='Business', user=self.user_Vee)
        self.upvote_carey = Upvote(upvote='2',pitch=self.pitch_carey,user=self.user_Carey) 
    def tearDown(self):
        Upvote.query.delete()
        Pitch.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.upvote_carey, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.upvote_carey.upvote, '2')
        self.assertEquals(self.upvote_carey.user, self.user_Carey)
        self.assertEquals(self.upvote_carey.pitch, self.pitch_carey)

    def test_save_upvote(self):
        self.upvote_carey.save()
        self.assertTrue(len(Upvote.query.all()) > 0)