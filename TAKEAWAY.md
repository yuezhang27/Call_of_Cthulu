## 关于存档
### 1. 创建 `database.py`

在 `database.py` 中，你可以定义一个字典来存储用户信息和游戏进度。例如：

```python
# database.py
player_data = {
    ('username1', 'password1'): {'progress': 'level1', 'score': 100},
    ('username2', 'password2'): {'progress': 'level2', 'score': 200},
    # 更多玩家数据
}
```

### 2. 在 `game.py` 中访问和修改 `database.py`

在 `game.py` 中，你可以导入 `database.py` 并访问或修改玩家数据。例如：

```python
# game.py
import database

def login(username, password):
    key = (username, password)
    if key in database.player_data:
        return database.player_data[key]
    else:
        return None

def update_progress(username, password, progress, score):
    key = (username, password)
    database.player_data[key] = {'progress': progress, 'score': score}

# 其他游戏逻辑
```

### 3. 数据持久化

如果你希望玩家的进度在程序关闭后仍然保留，你需要将数据保存到文件并在程序启动时读取。这可以通过使用Python的内置模块如 `pickle` 或 `json` 来实现。例如，你可以在 `database.py` 中添加函数来保存和加载数据：

```python
import json

def save_data():
    with open('player_data.json', 'w') as file:
        json.dump(player_data, file)

def load_data():
    global player_data
    try:
        with open('player_data.json', 'r') as file:
            player_data = json.load(file)
    except FileNotFoundError:
        player_data = {}

# 在程序启动时调用 load_data()
# 在程序关闭或者定期调用 save_data() 来保存数据
```

### 4. 注意事项

- 数据安全：由于你使用的是简单的文本文件存储用户名和密码，这种方法在安全性方面有所欠缺。在实际应用中，应该考虑使用加密方法来存储敏感信息。
- 数据结构：如果玩家数量变得非常大，你可能需要考虑更高效的数据存储和访问方法，如数据库系统。
- 错误处理：在实际的应用中，要确保对文件操作和数据访问进行适当的错误处理。


## 升级的处理
> 思路: nested while。外层while始终为True，保证游戏持续的向下进行，但是由于是while，因此可以反复回到外层while那里（等于是可以重置），
> 把初始化的设定放在1层while里面，2层while的上面，这样2层while被打破后，会继续走完这一轮1层while剩下的部分，然后回到1层while的开始。
> 把游戏主干放在2层while里，升级条件为True时打破while，完成save后，回到1层while的循环开始，也就是重置了
```python
def game():
    while True:
        # 初始化或重置游戏状态
        if_level_up = False
        # 其他需要初始化的游戏状态

        while not if_level_up:
            # 游戏逻辑
            # ...

            # 检查是否满足升级条件
            if 满足升级条件:
                if_level_up = True

        # 升级处理
        save_progress()
        # 这里可以添加任何在升级后需要执行的代码

        # 如果需要，可以在这里加入逻辑来判断是否继续游戏或退出

# 游戏入口
game()
```
