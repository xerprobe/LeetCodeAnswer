import os

def mkdir(path):
  path=path.strip()
  path=path.rstrip("\\")
  isExists=os.path.exists(path)
  if not isExists:
      os.makedirs(path) 
      print(path+' 创建成功')

def createFile(filePath):
  filePath = path + '\\' + 'pythonCode.py'
  if not os.path.exists(filePath):
    open(filePath,"w+").close()

for i in range(910,911):
  path = os.getcwd() + '\\' + str(i)
  mkdir(path)
  createFile(path)