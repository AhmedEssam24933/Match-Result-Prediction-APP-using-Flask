import numpy as np
import pandas as pd
import joblib

df = pd.read_csv(r"dataset\international_matches_for_model.csv")

df["home_team"] = df["home_team"].apply(str.lower)
df["away_team"] = df["home_team"].apply(str.lower) 

team_name = df["home_team"].unique()

def Team(team):
    team_number = range(211)
    teams = dict(zip(team_name,team_number))
    team = teams[f"{team}"]
    return team

def mean_ranks(team):
    team = df[df["home_team"] == f"{team}"]["mean_home_team_rank"].unique()[0]
    return team

def rank_difference(home_rank, away_rank):
    return home_rank - away_rank

def mean_team_home_goals(team):
    team = df[df["home_team"] == f"{team}"]["mean_team_home_goals"].unique()[0]
    return team

def mean_team_away_goals(team):
    team = df[df["away_team"] == f"{team}"]["mean_team_away_goals"].unique()[0]
    return team

def who_will_scored(home_rank, away_rank, mean_home_goals, mean_away_goals):
    if home_rank <=20:
        return 2
    else:
        if away_rank <=20:
            return 0
        elif mean_home_goals - mean_away_goals > 0.4:
            return 2
        elif mean_home_goals - mean_away_goals > 0:
            return 1
        else:
            return 0

def home_team_max_points(team):
    team = df[df["home_team"] == f"{team}"]["home_team_max_points"].unique()[0]
    return team

def points_difference(home_max_points, away_max_points):
    return home_max_points - away_max_points

def check_points_difference(points_diff):
    if points_diff > 0:
        return 1
    else:
        return 0 

def away_team_loss_percentage(team):
    team = df[df["away_team"] == f"{team}"]["away_team_loss_percentage"].unique()[0]
    return team

def preprocess_data(data):
    
    home_team  = data["home_team"].lower()
    
    away_team = data["away_team"].lower()
    
    home_team1 = Team(home_team)
    
    away_team1 = Team(away_team)
    
    home_team_rank = mean_ranks(home_team)
    
    away_team_rank = mean_ranks(away_team)
    
    ranks_difference = rank_difference(home_team_rank, away_team_rank)
    
    mean_home_goals = mean_team_home_goals(home_team)
    
    mean_away_goals = mean_team_away_goals(away_team)
    
    who_will_score = who_will_scored(home_team_rank, away_team_rank, mean_home_goals, mean_away_goals)
    
    home_max_points = home_team_max_points(home_team)
        
    away_max_points = home_team_max_points(away_team)
    
    points_diff = points_difference(home_max_points, away_max_points)
    
    check_points_diff = check_points_difference(points_diff)
    
    loss_percentage_for_away = away_team_loss_percentage(away_team)
    
    final_data = [home_team1, away_team1, home_team_rank, away_team_rank, ranks_difference, mean_home_goals, mean_away_goals,
                 who_will_score, home_max_points, away_max_points, points_diff, check_points_diff, loss_percentage_for_away]
    
    
    return final_data