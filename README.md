## 基于python的跳蚤市场
$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构

**基于python的跳蚤市场**：二手交易市场网站，基于<code>Python3.x</code>和<code>Django2.x</code>

项目尽量使用Django内部提供的API，后台管理为Django自带的管理系统django-admin。适合Django的小型实战项目。

## 功能简介：

- 商品浏览：商品的图片，售价，种类，简介以及库存等信息。
- 商品评论：用户在购买了商品后才会出现商品评论的文本框。
- 全文检索：支持对商品种类以及商品名称，简介的检索。
- 登录注册：用户的登录与注册，重置密码，密码发送到注册邮箱。
- 跳蚤使用协议：协议签属才能使用。
- 用户中心：支持用户个人信息，收货地址，修改密码，发布商品，修改个人信息，实名认证，等信息的更新，商品加入购物车，订单生成。
- 消息中心：支持用户回复商家信息。
- 卖家中心：在商品详细信息中通过联系卖家或则在评论区通过用户头像进入。
- 商品下单：在支付接口和企业资质的支持下可完成商品的下单功能，按照原子事务处理，下单异常则终止此次下单过程。
- 后台管理：支持后台管理功能，商品及用户信息的增加，更新与删除，可自定制样式与功能，日志，以及权限的管理和分配。



## 安装：

### 依赖包安装

下载文件进入项目目录之后，使用pip安装依赖包

<code>pip install -Ur requirements.txt</code>

### 数据库配置

数据库默认使用<code>Django</code>项目生成时自动创建的小型数据库<code>sqlite</code>

也可自行配置连接使用MySQL

### 创建超级用户

终端下执行:

<code>./python manage.py createsuperuser</code>

然后输入相应的超级用户名以及密码，邮箱即可。

### 开始运行

终端下执行:

<code>./python manage.py runserver</code>

浏览器打开: <code>http://127.0.0.1</code> 即可进入普通用户入口

浏览器打开: <code>http://127.0.0.1/admin</code> 即可进入超级用户入口


## 感谢：

感谢您的star

### 联系：

#GraduateDesign
