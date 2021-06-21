import unittest
from app.models import Pitch, Downvote,User


class DownvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Carey = User(username='lizlisa', password='banana', email='lizlisa@gmail.com')  
        self.pitch_Carey = Pitch(title='love', pitch='This is the ghetto', category='Promotion', user=self.user_Carey)
        self.downvote_Carey = Downvote(downvote='8',pitch=self.pitch_Carey,user=self.user_Carey) 
    def tearDown(self):
        Downvote.query.delete()
        Pitch.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.downvote_carey, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.downvote_carey.downvote, '8')
        self.assertEquals(self.downvote_carey.user, self.user_Carey)
        self.assertEquals(self.downvote_carey.pitch, self.pitch_Carey)

    def test_save_upvote(self):
        self.downvote_vee.save()
        self.assertTrue(len(Downvote.query.all()) > 0)