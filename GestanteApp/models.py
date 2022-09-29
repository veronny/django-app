from django.db import models

# Create your models here.
class Provincia(models.Model):
    cod_dpto = models.CharField('cod_dpto', max_length=2)
    cod_prov = models.CharField('cod_prov', max_length=2)
    desc_prov = models.CharField('desc_prov', max_length=200)
    cod = models.CharField('cod', max_length=4)

    def __str__(self):
        return self.desc_prov

    class Meta:
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'

class Distrito(models.Model):
    cod_dpto = models.CharField('cod_dpto', max_length=2)
    cod_prov = models.ForeignKey('Provincia',verbose_name='provincia',on_delete=models.CASCADE,
    )
    cod_dist = models.CharField('cod_dist', max_length=2)
    desc_dist = models.CharField('desc_dist', max_length=200)
    ubigeo = models.CharField('ubigeo', max_length=6)


    def __str__(self):
        return self.desc_dist

    class Meta:
        verbose_name = 'distrito'
        verbose_name_plural = 'distritos'

class Gestante(models.Model):
    name = models.CharField('nombre', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefono', max_length=15, null=True, blank=True)
    GENDER = (
        ('0', ''),
        ('man', 'homem'),
        ('woman', 'mulher'),
    )
    gender = models.CharField(
        'sexo',
        max_length=5,
        choices=GENDER,
        default='0'
    )
    provincia = models.ForeignKey(
        'provincia',
        verbose_name='provincia',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    distrito = models.ForeignKey(
        'distrito',
        verbose_name='distrito',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    # Captacion
    meta_captacion = models.IntegerField('meta_captacion', null=True, blank=True)
    captacion = models.IntegerField('captacion', null=True, blank=True)
    por_captacion = models.IntegerField('por_captacion', null=True, blank=True)
    # Paquete
    meta_paquete = models.IntegerField('meta_paquete', null=True, blank=True)
    paquete = models.IntegerField('paquete', null=True, blank=True)
    por_paquete = models.IntegerField('por_paquete', null=True, blank=True)
    examen = models.IntegerField('examen', null=True, blank=True)
    por_examen = models.IntegerField('por_examen', null=True, blank=True)
    control = models.IntegerField('control', null=True, blank=True)   
    por_control = models.IntegerField('por_control', null=True, blank=True)
    sulfato = models.IntegerField('sulfato', null=True, blank=True)
    por_sulfato = models.IntegerField('por_sulfato', null=True, blank=True)
    # Violencia
    meta_int_violencia = models.IntegerField('meta_violencia', null=True, blank=True)
    int_violencia = models.IntegerField('int_violencia', null=True, blank=True)
    por_int_violencia = models.IntegerField('por_int_violencia', null=True, blank=True)
    atendido = models.IntegerField('atendido', null=True, blank=True)
    por_atendido = models.IntegerField('por_atendido', null=True, blank=True)
    tamizaje = models.IntegerField('tamizaje', null=True, blank=True)
    por_tamizaje = models.IntegerField('por_tamizaje', null=True, blank=True)
    violencia = models.IntegerField('violencia', null=True, blank=True) 
    por_violencia = models.IntegerField('por_violencia', null=True, blank=True)
    # paquete niño
    meta_paquete_nino = models.IntegerField('meta_paquete_nino', null=True, blank=True)
    paquete_nino = models.IntegerField('paquete_nino', null=True, blank=True)
    por_paquete_nino = models.IntegerField('por_paquete_nino', null=True, blank=True)
    dni_nino = models.IntegerField('dni_nino', null=True, blank=True)
    por_dni_nino = models.IntegerField('por_dni_nino', null=True, blank=True)
    hemoglobina = models.IntegerField('hemoglobina', null=True, blank=True)
    por_hemoglobina = models.IntegerField('por_hemoglobina', null=True, blank=True)
    vacunas = models.IntegerField('vacunas', null=True, blank=True)
    por_vacunas = models.IntegerField('por_vacunas', null=True, blank=True)
    cred_nino = models.IntegerField('cred_nino', null=True, blank=True)
    por_cred_nino = models.IntegerField('por_cred_nino', null=True, blank=True)
    suplementacion = models.IntegerField('suplementacion', null=True, blank=True)
    por_suplementacion = models.IntegerField('por_suplementacion', null=True, blank=True)
    
    
    
    class Meta:
        verbose_name = 'gestante'
        verbose_name_plural = 'gestantes'

    def __str__(self):
        return self.name