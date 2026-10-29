import time
import math
import random
import requests
import json
def bigmult():
  numbers=input("What 2 numbers would you like to multiply? Seperate by space.").split()
  a=int(numbers[0])
  b=int(numbers[1])
  c=a*b
  d=a*c
  e=b*c
  f=a*e
  g=b*e
  h=c*e
  i=h*g
  if i>0:
    return math.sqrt(i)
  if i<0:
    return math.sqrt(math.copysign(i, 1))
def fprint(text, t):
  for char in text:
    time.sleep(t)
    print(char, flush=True, end='')
  return 0
def rprint(text):
  for char in text:
    time.sleep(random.random())
    print(char, flush=True, end='')
def dprint(text):
  for char in text:
    time.sleep(0.5)
    print(char, flush=True, end="")
  print()
def asklist(text):
  user_list=[]
  while True:
    r=input(text)
    if r.lower() != "stop" and r.lower() !="end":
      user_list.append(r)
    if r.lower() in ("stop", "end"):
      break
  return user_list
def rvar(vari):
  print(vari)
def mupr(content, num):
  return content*num
def nonbig(a, b):
  c=a*b
  d=a*c
  e=b*c
  f=a*e
  g=b*e
  h=c*e
  i=h*g
  return math.sqrt(abs(i)) 
def get(website, apikey=None):
  try:
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
      "Authorization": f"Bearer {apikey}"
    }
  except NameError:
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
  data=requests.get(website, headers=headers)
  if data.status_code()==200:
    data1=data.json()
    return json.dumps(data1)
  if data.status_code()==404:
      return f"{website} not found. sorry."
