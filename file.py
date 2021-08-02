print('----------------泽丶心理工坊-----------------------')
counts=3
while counts > 0:
      temp = input ("不妨猜一下泽丶心里想的数字：")
      guess = int(temp)
      if guess ==8:
            print("NB，你是泽丶的知音啊！")
            print("略略略，猜对也没有奖励！")
            break
      else:
                  if guess >8:
                        print("哥们，大了！大了！！")
                  else:
                        print("嘿，小了！小了！！")
      counts = counts - 1
print("游戏结束，拜拜^_^")
