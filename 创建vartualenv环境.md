###### 创建vartualenv环境

pip install vartualenv : 安装vartualenv

virtualenv --no-site-packages  -p  python环境路径  文件名 

virtualenv --no-site-packages  文件名 

--no-site-packages   创建一个纯净的虚拟环境

-p 文件历经    == >   指定python版本



###### 进入环境

cd + 文件夹名

cd  scriptsactivate

activate  ： 启动环境

pip install django==1.11  :  安装django1.11版本

deactivate ： 退出环境



##### 创建项目

django-admin startproject dayo1  :  创建一个day01项目

python manage.py runserver  : 启动页面





##### 关联数据库

在数据库创建一个库 如 dj

setting更改配置：

-- --  DATABASES = {

'default': {'ENGINE': 'django.db.backends.mysql',

'NAME': 'dj',

'USER': 'root',

'PASSWORD': '123123',

'HOST': '127.0.0.1',

'PORT': 3306

}}

python manage.py migrate : 迁移数据库

python manage.py createsuperuser ：创建用户



