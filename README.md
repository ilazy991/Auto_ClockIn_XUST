<div align="center">
<h1 align="center">
某大学自动健康打卡 自用 需要请去源项目看
 </h1>
 

</div>

# 工具简介


**如果觉得好用，顺手点个 Star 吧 ❤**

* [x] 每天上午 11 点 10 分与下午8点自动开始任务。*【运行时间可自定义】*
* [x] 打卡失败将会通过server酱推送执行结果到微信，打卡成功不会提醒。

# 使用说明
1. **Fork 本项目**

2. **点击项目 Settings -> Secrets -> New Secrets 添加以下2个 Secrets。**

| Name       | Value            |
| ---------- | ---------------- |
| USERNAME_TEXT | 某E站账号 |
| PASSWORD_TEXT   | 某E站密码 |


3. **如需微信订阅通知请如下操作**  
1 前往 [sc.ftqq.com](http://sc.ftqq.com/3.version) 点击登入，创建账号（建议使用 GitHub 登录）。  
2 点击点[发送消息](http://sc.ftqq.com/?c=code) ，生成一个 Key。将其增加到 Github Secrets 中，变量名为 `SERVERPUSHKEY`  
3 [绑定微信账号](http://sc.ftqq.com/?c=wechat&a=bind) ，开启微信推送。  


4. **开启 Actions 并触发每日自动执行**

如果需要修改每日任务执行的时间，请修改 `.github/workflows/运行.yml`，找到下如下配置。

```yml
#   push:
#     branches:
#       - main
#   schedule:
#     - cron: '10 3 * * *'
#     - cron: '10 11 * * *'
#取消以上注释
  schedule:
    - cron: '19 10 * * *'
    # cron表达式，Actions时区是UTC时间，所以下午18点要往前推8个小时。
    # 示例： 每天晚上22点30执行 '30 14 * * *'
```
https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows cron语法参考

**请各位使用 Actions 时务必遵守Github条款。不要滥用Actions服务。**

**Please be sure to abide by the Github terms when using Actions. Do not abuse the Actions service.**
# 免责声明

1. 本工具不会记录你的任何敏感信息，也不会上传到任何服务器上。（数据均存在Actions Secrets中或者用户自己的设备上）
2. 本工具不会记录任何执行过程中的数据信息，也不会上传到任何服务器上。
3. 本工具执行过程中产生的日志，仅会在使用者自行配置推送渠道后进行推送。日志中不包含任何用户敏感信息。
4. 如果有人修改了本项目（或者直接使用本项目）盈利恰饭，那和我肯定没关系，我开源的目的单纯是技术分享。
5. 如果你使用了第三方修改的，打包的本工具代码，那你可得注意了，指不定人就把你的数据上传到他自己的服务器了，这可和我没关系。（**网络安全教育普及任重而道远**）
