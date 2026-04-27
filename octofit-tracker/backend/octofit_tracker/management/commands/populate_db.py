from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Usuń istniejące dane
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Unikalny indeks na email
        db.users.create_index('email', unique=True)

        # Dane testowe
        users = [
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
            {"name": "dc", "members": ["batman@dc.com", "superman@dc.com"]},
        ]
        activities = [
            {"user_email": "ironman@marvel.com", "activity": "run", "distance": 5},
            {"user_email": "cap@marvel.com", "activity": "cycle", "distance": 20},
            {"user_email": "batman@dc.com", "activity": "swim", "distance": 2},
            {"user_email": "superman@dc.com", "activity": "fly", "distance": 100},
        ]
        leaderboard = [
            {"team": "marvel", "points": 250},
            {"team": "dc", "points": 300},
        ]
        workouts = [
            {"user_email": "ironman@marvel.com", "workout": "bench press", "weight": 100},
            {"user_email": "cap@marvel.com", "workout": "squat", "weight": 120},
            {"user_email": "batman@dc.com", "workout": "deadlift", "weight": 140},
            {"user_email": "superman@dc.com", "workout": "fly", "weight": 0},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
