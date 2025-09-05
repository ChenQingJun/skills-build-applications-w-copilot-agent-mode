from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', email='test@example.com', team=team)
        self.assertEqual(str(user), 'testuser')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)
        self.assertEqual(str(activity), 'testuser - run')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', email='test@example.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=123)
        self.assertEqual(str(lb), 'testuser - 123')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=30)
        self.assertEqual(str(workout), 'Test Workout')
