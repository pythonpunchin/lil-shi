alex = {
  "name": "Alex",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
liam = {
  "name": "Liam",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
audrey = {
  "name": "Audrey",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
students = [alex, liam, audrey]

for x in students:
  print x["name"]
  print x["homework"]
  print x["quizzes"]
  print x["tests"]



def average(numbers):
  import math
  total = sum(numbers)
  total = float(total)
  x = total / len(numbers)
  return x

def get_average(student):
  from math import *
  homework = average(student["homework"])
  tests = average(student["tests"])
  quizzes = average(student["quizzes"])
  homework *= .10
  quizzes *= .30
  tests *= .60
  return homework + quizzes + tests
  g = homework + quizzez + tests
  print g

def get_letter_average():

