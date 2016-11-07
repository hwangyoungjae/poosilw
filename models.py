# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CodeArea1Formal(models.Model):
    formalno = models.AutoField(primary_key=True)
    formalarea = models.CharField(max_length=10, blank=True, null=True)
    areacount = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Code_area1_formal'


class CodeArea1Manager(models.Model):
    rawarea = models.CharField(primary_key=True, max_length=20)
    formalno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Code_area1_manager'


class CodeArea2Formal(models.Model):
    formalno = models.AutoField(primary_key=True)
    pformalno = models.IntegerField()
    formalarea = models.CharField(max_length=10, blank=True, null=True)
    areacount = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Code_area2_formal'


class CodeArea2Manager(models.Model):
    rawarea = models.CharField(max_length=20)
    pformalno = models.IntegerField()
    formalno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Code_area2_manager'


class Exprnprogrmexprntysecode(models.Model):
    exprntysecode = models.CharField(db_column='exprnTySeCode', primary_key=True, max_length=8)  # Field name made lowercase.
    exprntysetext = models.CharField(db_column='exprnTySeText', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExprnProgrmExprnTySeCode'


class Exprnprogrmhistory(models.Model):
    no = models.AutoField(primary_key=True)
    kind = models.IntegerField(blank=True, null=True)
    exprnprogrmno = models.IntegerField(db_column='ExprnProgrmno')  # Field name made lowercase.
    exprndstncid = models.CharField(db_column='exprnDstncId', max_length=8)  # Field name made lowercase.
    updatefield = models.CharField(db_column='updateField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    beforedata = models.TextField(db_column='beforeData', blank=True, null=True)  # Field name made lowercase.
    afterdata = models.TextField(db_column='afterData', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnProgrmHistory'


class Exprnprogrmstatus(models.Model):
    status = models.IntegerField(primary_key=True)
    statustext = models.CharField(max_length=6, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnProgrmStatus'


class Exprnprogrms(models.Model):
    no = models.AutoField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    chargermoblphonno = models.CharField(db_column='chargerMoblphonNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    chargernm = models.CharField(db_column='chargerNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chargerrefrnc = models.CharField(db_column='chargerRefrnc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cn = models.TextField(blank=True, null=True)
    exprndstncid = models.CharField(db_column='exprnDstncId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    exprnliverstgdc = models.CharField(db_column='exprnLiverStgDc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exprnprogrmnm = models.CharField(db_column='exprnProgrmNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exprntysecode = models.CharField(db_column='exprnTySeCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    exprntysenm = models.CharField(db_column='exprnTySeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nmprcomumm = models.SmallIntegerField(db_column='nmprCoMumm', blank=True, null=True)  # Field name made lowercase.
    nmprcomxmm = models.SmallIntegerField(db_column='nmprCoMxmm', blank=True, null=True)  # Field name made lowercase.
    onlineresveposblat = models.CharField(db_column='onlineResvePosblAt', max_length=1, blank=True, null=True)  # Field name made lowercase.
    opererabegin = models.DateField(db_column='operEraBegin', blank=True, null=True)  # Field name made lowercase.
    opereraend = models.DateField(db_column='operEraEnd', blank=True, null=True)  # Field name made lowercase.
    opertimemnt = models.SmallIntegerField(db_column='operTimeMnt', blank=True, null=True)  # Field name made lowercase.
    pc = models.IntegerField(blank=True, null=True)
    resveguidance = models.TextField(db_column='resveGuidance', blank=True, null=True)  # Field name made lowercase.
    thumburlcours1 = models.CharField(db_column='thumbUrlCours1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours2 = models.CharField(db_column='thumbUrlCours2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours3 = models.CharField(db_column='thumbUrlCours3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours4 = models.CharField(db_column='thumbUrlCours4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vilageid = models.CharField(db_column='vilageId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rdate = models.DateTimeField(blank=True, null=True)
    mdate = models.DateTimeField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnProgrms'


class Exprnvilageepilougecommentstatus(models.Model):
    status = models.IntegerField(primary_key=True)
    statustext = models.CharField(max_length=6, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageEpilougeCommentStatus'


class Exprnvilageepilougecomments(models.Model):
    no = models.AutoField(primary_key=True)
    bbscttno = models.IntegerField(db_column='bbscttNo')  # Field name made lowercase.
    status = models.IntegerField()
    cn = models.TextField()
    wrter = models.CharField(max_length=20)
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ExprnVilageEpilougeComments'


class Exprnvilageepilougehistory(models.Model):
    no = models.AutoField(primary_key=True)
    kind = models.IntegerField(blank=True, null=True)
    exprnvilageepilougeno = models.IntegerField(db_column='ExprnVilageEpilougeno')  # Field name made lowercase.
    bbscttno = models.IntegerField(db_column='bbscttNo', blank=True, null=True)  # Field name made lowercase.
    updatefield = models.CharField(db_column='updateField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    beforedata = models.TextField(db_column='beforeData', blank=True, null=True)  # Field name made lowercase.
    afterdata = models.TextField(db_column='afterData', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageEpilougeHistory'


class Exprnvilageepilougestatus(models.Model):
    status = models.IntegerField(primary_key=True)
    statustext = models.CharField(max_length=6, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageEpilougeStatus'


class Exprnvilageepilouges(models.Model):
    no = models.AutoField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    bbscttno = models.IntegerField(db_column='bbscttNo', blank=True, null=True)  # Field name made lowercase.
    cn = models.TextField(blank=True, null=True)
    ctrd = models.SmallIntegerField(blank=True, null=True)
    gugun = models.IntegerField(db_column='guGun', blank=True, null=True)  # Field name made lowercase.
    rgsde = models.DateField(blank=True, null=True)
    sj = models.CharField(max_length=255, blank=True, null=True)
    thumburlcours1 = models.CharField(db_column='thumbUrlCours1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours2 = models.CharField(db_column='thumbUrlCours2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours3 = models.CharField(db_column='thumbUrlCours3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours4 = models.CharField(db_column='thumbUrlCours4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vilageid = models.CharField(db_column='vilageId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wrter = models.CharField(max_length=20, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    rdate = models.DateTimeField(blank=True, null=True)
    mdate = models.DateTimeField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageEpilouges'


class Exprnvilagehistory(models.Model):
    no = models.AutoField(primary_key=True)
    kind = models.IntegerField(blank=True, null=True)
    exprnvilageno = models.IntegerField(db_column='ExprnVilageno')  # Field name made lowercase.
    vilageid = models.CharField(db_column='vilageId', max_length=8)  # Field name made lowercase.
    updatefield = models.CharField(db_column='updateField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    beforedata = models.TextField(db_column='beforeData', blank=True, null=True)  # Field name made lowercase.
    afterdata = models.TextField(db_column='afterData', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageHistory'


class Exprnvilagestatus(models.Model):
    status = models.IntegerField(primary_key=True)
    statustext = models.CharField(max_length=6, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilageStatus'


class Exprnvilages(models.Model):
    no = models.AutoField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    adres1 = models.CharField(max_length=255, blank=True, null=True)
    adres2 = models.CharField(max_length=255, blank=True, null=True)
    browse = models.TextField(blank=True, null=True)
    exprnguidance = models.TextField(db_column='exprnGuidance', blank=True, null=True)  # Field name made lowercase.
    fnctcode = models.CharField(db_column='fnctCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnctnm = models.CharField(db_column='fnctNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prcafsmanemail = models.CharField(db_column='prcafsManEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prcafsmanmoblphon = models.CharField(db_column='prcafsManMoblphon', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prcafsmannm = models.CharField(db_column='prcafsManNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prcafsmantlphonno = models.CharField(db_column='prcafsManTlphonNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resveguidance = models.TextField(db_column='resveGuidance', blank=True, null=True)  # Field name made lowercase.
    scnorgn = models.TextField(db_column='scnOrgn', blank=True, null=True)  # Field name made lowercase.
    themanm = models.CharField(db_column='themaNm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    themasecode = models.CharField(db_column='themaSeCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    thumburlcours1 = models.CharField(db_column='thumbUrlCours1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours2 = models.CharField(db_column='thumbUrlCours2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours3 = models.CharField(db_column='thumbUrlCours3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumburlcours4 = models.CharField(db_column='thumbUrlCours4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trnsportguidance = models.TextField(db_column='trnsportGuidance', blank=True, null=True)  # Field name made lowercase.
    useguidance = models.TextField(db_column='useGuidance', blank=True, null=True)  # Field name made lowercase.
    vilagefcltycode = models.CharField(db_column='vilageFcltyCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vilagefcltynm = models.TextField(db_column='vilageFcltyNm', blank=True, null=True)  # Field name made lowercase.
    vilagehmpgennc = models.CharField(db_column='vilageHmpgEnnc', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vilagehmpgurl = models.CharField(db_column='vilageHmpgUrl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vilageid = models.CharField(db_column='vilageId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vilageintrcn = models.TextField(db_column='vilageIntrcn', blank=True, null=True)  # Field name made lowercase.
    vilagekndcode = models.CharField(db_column='vilageKndCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vilagekndnm = models.CharField(db_column='vilageKndNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vilagenm = models.CharField(db_column='vilageNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vilagerprsntvemail = models.CharField(db_column='vilageRprsntvEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vilagerprsntvmoblphon = models.CharField(db_column='vilageRprsntvMoblphon', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vilagerprsntvnm = models.CharField(db_column='vilageRprsntvNm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vilagerprsntvtlphonno = models.CharField(db_column='vilageRprsntvTlphonNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vilageslgn = models.CharField(db_column='vilageSlgn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(max_length=7, blank=True, null=True)
    area1no = models.SmallIntegerField(blank=True, null=True)
    area1name = models.CharField(max_length=10, blank=True, null=True)
    area2no = models.SmallIntegerField(blank=True, null=True)
    area2name = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    epiloguecnt = models.IntegerField(db_column='epilogueCnt', blank=True, null=True)  # Field name made lowercase.
    rdate = models.DateTimeField(blank=True, null=True)
    mdate = models.DateTimeField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExprnVilages'


class Fstvlimgs(models.Model):
    no = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    imgorder = models.IntegerField()
    imgurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'FstvlImgs'


class Fstvlinfos(models.Model):
    no = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    itemvalue = models.TextField()

    class Meta:
        managed = False
        db_table = 'FstvlInfos'


class Fstvls(models.Model):
    cid = models.IntegerField(primary_key=True)
    opererabegin = models.DateField(db_column='operEraBegin', blank=True, null=True)  # Field name made lowercase.
    opereraend = models.DateField(db_column='operEraEnd', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    adres = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fstvls'


class Historykind(models.Model):
    kind = models.IntegerField(primary_key=True)
    kindtext = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HistoryKind'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Members(models.Model):
    no = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20, blank=True, null=True)
    member_pw = models.CharField(max_length=32, blank=True, null=True)
    member_email = models.CharField(max_length=255, blank=True, null=True)
    member_name = models.CharField(max_length=30, blank=True, null=True)
    member_hp = models.CharField(max_length=15, blank=True, null=True)
    member_sex = models.IntegerField(blank=True, null=True)
    member_birth = models.DateField(blank=True, null=True)
    member_status = models.IntegerField(blank=True, null=True)
    rid = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    last_date = models.DateTimeField(blank=True, null=True)
    reg_ip = models.IntegerField(blank=True, null=True)
    last_ip = models.IntegerField(blank=True, null=True)
    recv_email = models.IntegerField(blank=True, null=True)
    recv_sms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'