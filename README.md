![AutoSwitchProxy](https://socialify.git.ci/zuo-shi-yun/AutoSwitchProxy/image?description=1&descriptionEditable=%E8%87%AA%E5%8A%A8%E5%88%87%E6%8D%A2Clash%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F%E4%BB%A5%E8%8A%82%E7%9C%81%E6%B5%81%E9%87%8F&logo=https%3A%2F%2Fi.postimg.cc%2FW4Q58VCn%2F1.png&name=1&theme=Light)
自动切换Clash代理模式以节省流量。<br/>
(本插件运行于[QChatGPT](https://github.com/RockChinQ/QChatGPT))<br/>

## :muscle:插件功能

- 当发送网络请求时，自动切换为Global模式
- 当网络请求完毕时，自动切换为Rule模式
- Windows系统下自动导入clashAPI配置

## :crossed_swords:安装与配置

- 安装
    - 运行`!plugin get https://github.com/zuo-shi-yun/AutoSwitchProxy.git`
    - 进入插件目录执行`pip install -r requirements.txt`
- 配置
  <details>
    <summary>自动配置(windows系统下)</summary>

    - 运行插件即可自动导入配置。
    - 若多次报错且修改无效，请使用手动配置。
  </details>

  <details>
    <summary>手动配置(通用)</summary>

    1. 获得API配置

        - windows系统：打开clash for windows，general栏下找到Home Directory，点击open Folder，进入`config`
          目录，打开`clash.yaml`，记录`external-controller`和`secret`配置项。
        - linux系统：记录启动时显示的clash dashboard地址以及secret配置项。
    2. 修改插件配置

        - 打开`plugin\AutoSwitchProxy\utils\clash.py`文件。
        - 根据记录的配置项对应修改10行的`external_controller`、12行的`secret`变量。
        - 保存、重启系统。
  </details>

  <details>
  <summary>总是报错“clash api连接失败,请检查clashAPI地址配置是否正确.”</summary>

    - 检查config.yaml文件中是否有`external-controller`和`secret`配置项，若没有请手动添加这两项配置。
    - windows检查Clash主目录下`profiles`文件夹内的配置文件(一堆数字.yml)中的`external-controller`和`secret`配置项，尝试使用该配置项。
    - linux下检查导入机场的配置文件中的`external-controller`和`secret`配置项，尝试使用该配置项。
    - 若还是不对，请搜索“clash如何使用Restful API”,参照结果配置`external-controller`和`secret`
      配置项。([官方文档](https://clash.gitbook.io/doc/restful-api))
  </details>    