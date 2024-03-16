# we will make an api here using flask
# and then we will make some function to handle our data and pridict make the prediction using it

from flask import Flask, request, jsonify
import numpy as np
import pickle
import os
import joblib
import pandas as pd
import json
import requests
import datetime
import pytz
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import xdg.BaseDirectory as xdg

