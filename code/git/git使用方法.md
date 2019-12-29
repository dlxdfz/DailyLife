github作为服务器

# 命令行创建远程仓库
```shell
curl -u dlxdfz https://api.github.com/user/repos -d '{"name": "repos_name"}'
```

# linux创建git免密提交
[参考](https://juejin.im/post/5aeff650f265da0b8070a7e0)
``````
cd ~
cd .ssh
# 生成ssh-key
ssh-keygen -t rsa -C "github 账号注册邮箱"
# 生成rsa文件地址可为：~/.ssh/github_id_rsa，然后会顺带生成~/.ssh/github_id_rsa.pub

# 添加ssh-key
ssh-agent bash
ssh-add ~/.ssh/github_id_rsa

# 设置config文件
# 如果没有config，新建一个
Host github.com[随意取]
HostName github.com[如果是github为服务器]
User dlxdfz[用户名]
IdentityFile ~/.ssh/github_id_rsa

# 在github上添加github_id_rsa.pub
# 测试是否连接成功
ssh -T git@github.com
``````

# github提交本地仓库到remote 空仓库中
```
git init
git remote add origin git@github.com:dlxdfz/repos.git
git pull # 如果仓库非空
git add .
git commit -m "init commit"
git push
```
# remote
```
git remote -v
git remote rm origin
git remote set-url --add --push git@github.com:dlxdfz/repos.git
```
