# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class CheckIn(models.Model):
    cod_checkin = models.CharField(primary_key=True, max_length=6)
    horario = models.DateField()
    documento = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_in'


class CheckOut(models.Model):
    cod_checkout = models.CharField(primary_key=True, max_length=6)
    horario = models.DateField()
    documento = models.BinaryField(blank=True, null=True)
    multa = models.FloatField()
    multa_monto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'check_out'


class Cliente(models.Model):
    run_cliente = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=15)
    apellido_p = models.CharField(max_length=15)
    apellido_m = models.CharField(max_length=15)
    firma = models.BinaryField(blank=True, null=True)
    tipo_usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'cliente'


class Conductor(models.Model):
    cod_conduc = models.CharField(primary_key=True, max_length=6)
    run = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    tipo_licencia = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'conductor'


class Departamento(models.Model):
    cod_depa = models.CharField(primary_key=True, max_length=6)
    num_dormitorios = models.CharField(max_length=15)
    num_banos = models.CharField(max_length=15)
    tipo_depa = models.CharField(max_length=15)
    valor_depaxdia = models.CharField(max_length=15)
    valor_inventario = models.CharField(max_length=15)
    fotos_depa = models.BinaryField(blank=True, null=True)
    inventario_cod_inv = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='inventario_cod_inv')
    mantenimiento_cod_mant = models.ForeignKey('Mantenimiento', models.DO_NOTHING, db_column='mantenimiento_cod_mant')

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inventario(models.Model):
    cod_inv = models.CharField(primary_key=True, max_length=6)
    nom_objeto = models.CharField(max_length=15)
    tipo_objeto = models.CharField(max_length=15)
    estado_objeto = models.CharField(max_length=15)
    valor_objeto = models.BigIntegerField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class Mantenimiento(models.Model):
    cod_mant = models.CharField(primary_key=True, max_length=6)
    reparacion = models.FloatField()
    disponibilidad = models.FloatField()
    remodelacion = models.FloatField()
    limpieza = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mantenimiento'


class Reserva(models.Model):
    cod_reserva = models.CharField(primary_key=True, max_length=6)
    tipo_reserva = models.CharField(max_length=15)
    pago_parcial = models.CharField(max_length=30)
    pago_completo = models.CharField(max_length=30)
    pago_aprobado = models.FloatField()
    run = models.CharField(max_length=8)
    servicios_cod_serv = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='servicios_cod_serv')
    check_in_cod_checkin = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='check_in_cod_checkin')
    check_out_cod_checkout = models.ForeignKey(CheckOut, models.DO_NOTHING, db_column='check_out_cod_checkout')
    departamento_cod_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_cod_depa')
    cliente_run_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_run_cliente')
    zona_cod_zon = models.ForeignKey('Zona', models.DO_NOTHING, db_column='zona_cod_zon')

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicios(models.Model):
    cod_serv = models.CharField(primary_key=True, max_length=6)
    acondicionado = models.CharField(max_length=50)
    tour_cod_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='tour_cod_tour')
    transporte_cod_transp = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='transporte_cod_transp')

    class Meta:
        managed = False
        db_table = 'servicios'


class Tour(models.Model):
    cod_tour = models.CharField(primary_key=True, max_length=6)
    tipo_tour = models.CharField(max_length=15)
    horario = models.DateField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'tour'


class Transporte(models.Model):
    cod_transp = models.CharField(primary_key=True, max_length=6)
    ubicacion = models.CharField(max_length=50)
    horario = models.DateField()
    desde = models.CharField(max_length=50)
    hasta = models.CharField(max_length=50)
    vehiculo_cod_vehi = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_cod_vehi')
    conductor_cod_conduc = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='conductor_cod_conduc')

    class Meta:
        managed = False
        db_table = 'transporte'


class Vehiculo(models.Model):
    cod_vehi = models.CharField(primary_key=True, max_length=6)
    tipo_vehiculo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    patente = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'vehiculo'


class Zona(models.Model):
    cod_zon = models.CharField(primary_key=True, max_length=6)
    ciudad = models.CharField(max_length=20)
    region = models.CharField(max_length=15)
    comuna = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'zona'
