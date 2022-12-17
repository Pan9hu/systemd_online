import uuid
import datetime

from django.db import models
from django.db.models import Model ,CharField ,DateTimeField, TextField, UUIDField, BooleanField, EmailField

class Agent(Model):
    """
    秘钥生成规则: md5(md5(password + timestamp) + salt)
    """
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    secrets_key = CharField(max_length=255, unique=True)
    ctime = DateTimeField(verbose_name="注册时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)
    reg_reason = CharField(max_length=1024, default="自动发现后并注册。", verbose_name="注册方式")
    oper_id = CharField(max_length=40, verbose_name="操作人ID")
    remarks = TextField(default="一般操作。", verbose_name="备注" )

    class Meta:
        db_table = "t_agent"
        verbose_name = "代理工具"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self._id

class Config(Model):
    """
    抽象了 ini 格式的配置文件的存储方式
    例如将下面的 ini 配置:
    [section]
    key = value
    转化为
    section.key = value
    """
    agent_id = CharField(max_length=40, verbose_name="代理工具ID(但该项为模板时，值为'--') ", default='--')
    path = TextField(verbose_name="配置文件路径")
    section = CharField(max_length=255, verbose_name="配置段")
    key = CharField(max_length=255, verbose_name="配置项")
    value = CharField(max_length=1024, verbose_name="配置值")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)
    oper_id = CharField(max_length=40, verbose_name="操作人ID")
    remarks = TextField(default="一般操作。", verbose_name="备注" )
    is_template = BooleanField(default=False, verbose_name="是否为模板字段")

    class Meta:
        db_table = "t_config"
        verbose_name = "配置"
        verbose_name_plural = verbose_name


class ServiceConfig(Model):
    """
    Systemd Online 配置文件
    """
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    is_use = BooleanField(default=False, verbose_name="是否启用")
    cname = CharField(max_length=255, blank=True,verbose_name="别名")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)

    class Meta:
        db_table = "t_service_config"
        verbose_name = "Systemd Online 服务配置(危险) "
        verbose_name_plural = verbose_name


class ConfigTemplate(Model):
    """
    配置文件模板
    """
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=1024, verbose_name="名称")
    owner_id = UUIDField(verbose_name="拥有者ID")
    path = TextField(verbose_name="配置文件路径")
    salt = CharField(max_length=1024, verbose_name="Salt(AES加密, 最大长度=1024")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)

    class Meta:
        db_table = "t_config_template"
        verbose_name = "配置模板"
        verbose_name_plural = verbose_name


class LogItem(Model):
    """
    日志文件
    """
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    content = CharField(max_length=1024, verbose_name="操作内容")
    oper_id = CharField(max_length=40, verbose_name="操作人ID")
    ctime = DateTimeField(verbose_name="操作时间", default=datetime.datetime.now)

    class Meta:
        db_table = "t_log_item"
        verbose_name = "操作日志"
        verbose_name_plural = verbose_name


class Operator(Model):
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=128, verbose_name="姓名")
    no = CharField(max_length=128, verbose_name="工号")
    domain = CharField(max_length=1024, verbose_name="组织架构路径")
    username = CharField(max_length=255, verbose_name="用户名")
    password = CharField(max_length=255, verbose_name="密码(AES对称加密)")
    email = EmailField(max_length=1024, verbose_name="工作邮箱")
    email_backup = EmailField(max_length=1024, verbose_name="备用邮箱")
    phone = CharField(max_length=255, verbose_name="工作手机")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)

    class Meta:
        db_table = "t_operator"
        verbose_name = "操作者"
        verbose_name_plural = verbose_name


class Group(Model):
    _id = CharField(max_length=255, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=1024, verbose_name="名称")
    synopsis = TextField(blank=True, verbose_name="简介")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间", default=datetime.datetime.now)

    class Meta:
        db_table = "t_group"
        verbose_name = "用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        sysnopsis - self.synopsis if len(self.synopsis) > 20 else self.synopsis[0:20] * '...'
        return "{} ({})".format(self.name, self.synopsis)

class OperatorGroupRef(Model):
    uid = CharField(max_length=255, db_column="uid", verbose_name="UID")
    gid = CharField(max_length=255, db_column="gid", verbose_name="GID")

    class Meta:
        db_table = "t_operator_group_ref"
        verbose_name = "用户组关系"
        verbose_name_plural = verbose_name