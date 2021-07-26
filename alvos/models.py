from django.core.validators import (
    EmailValidator,
    RegexValidator,
)
from django.utils.html import mark_safe
from django.db import models


VALIDATOR_PLACA = RegexValidator(
    r'[A-Z]{3}[0-9][0-9A-Z][0-9]{2}',
    message='Formato de placa Inválido!',
    code='placainvalida'
)
VALIDATOR_EMAIL = EmailValidator(
    message = 'E-Mail inválido!',
    code='emailinvalido'
)
VALIDADOR_TELEFONE = RegexValidator(
    r'\d{10,11}',
    message='Informe telefone no formato 2199998888, entre 10 e 11 dígitos',
    code='telinfalido'
)


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nascimento =models.DateField()
    alvo = models.BooleanField(default=False)
    militar = models.BooleanField(default=False)
    policial = models.BooleanField(default=False)
    foto = models.ImageField(blank=True, null=True)
    def foto_tag(self):
        if self.foto:
            return mark_safe(
                '<img src="/media/%s" width="150" height="150" />' % (self.foto)
            )
        return mark_safe("")
    foto_tag.short_description = 'Miniatura'

    def __str__(self):
        if self.nome:
            return self.nome
        return None


class Anotacao(models.Model):
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    Nota = models.TextField()


class TipoDocumento(models.Model):
    NomeDocumento = models.CharField(max_length=50)

    def __str__(self):
        if self.NomeDocumento:
            return self.NomeDocumento
        return None


class Documento(models.Model):
    Pessoa = models.ForeignKey('Pessoa', models.CASCADE)
    Tipo = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE)
    numeracao = models.CharField(max_length=50)
    orgao_emissor = models.CharField(max_length=50)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.numeracao:
            return self.numeracao
        return None


class TipoRelacao(models.Model):
    NomeRelacao = models.CharField(max_length=50)
    def __str__(self):
        if self.NomeRelacao:
            return self.NomeRelacao
        return None


class Relacao(models.Model):
    PessoaDe = models.ForeignKey('Pessoa',models.CASCADE,related_name='pessoade')
    Tipo = models.ForeignKey('TipoRelacao', models.CASCADE)
    PessoaAte = models.ForeignKey('Pessoa', models.CASCADE, related_name='pessoaate')
    def __str__(self):
        if self.PessoaDe:
            return " ".join(
              (
                str(self.PessoaDe),
                str(self.Tipo),
                str(self.PessoaAte)
              )  
            )
        return None

class TipoProcedimento(models.Model):
    NomeProcedimento = models.CharField(max_length=50)
    def __str__(self):
        if self.NomeProcedimento:
            return self.NomeProcedimento
        return None


class Procedimento(models.Model):
    Pessoa = models.ForeignKey('Pessoa', models.CASCADE)
    Numeracao = models.CharField(max_length=50, verbose_name='Numeração')
    TipoProcedimento = models.ForeignKey('TipoProcedimento', models.CASCADE)
    Nota = models.TextField(blank=True, null=True)
    def __str__(self):
        if self.Numeracao:
            return self.Numeracao
        return None


class MarcaVeiculo(models.Model):
    NomeMarca = models.CharField(max_length=50)
    def __str__(self):
        if self.NomeMarca:
            return self.NomeMarca
        return None


class ModeloVeiculo(models.Model):
    NomeModelo = models.CharField(max_length=50)
    def __str__(self):
        if self.NomeModelo:
            return self.NomeModelo
        return None


class Veiculo(models.Model):
    Pessoa = models.ForeignKey('Pessoa', models.CASCADE)
    Placa = models.CharField(
        max_length=10,
        validators=[VALIDATOR_PLACA]
    )
    Marca = models.ForeignKey('MarcaVeiculo', models.PROTECT)
    Modelo = models.ForeignKey('ModeloVeiculo', models.PROTECT)
    Ano = models.IntegerField()
    Notas = models.TextField(blank=True, null=True)
    def __str__(self):
        if self.Placa:
            return " ".join(
                (
                str(self.Marca),
                str(self.Modelo),
                str(self.Placa),
                str(self.Ano),
                )
            )
        return None


class Email(models.Model):
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    EMail = models.CharField(
        max_length=255,
        validators=[VALIDATOR_EMAIL]
    )
    Notas = models.TextField(blank=True, null=True)
    def __str__(self):
        if self.EMail:
            return self.EMail
        return None


class Ocorrencia(models.Model):
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    NumeroOcorrencia = models.CharField(max_length=50)
    Data = models.DateField(blank=True, null=True)
    Dinamica = models.TextField(blank=True, null=True)
    def __str__(self):
        if self.NumeroOcorrencia:
            return self.NumeroOcorrencia
        return None


class Telefone(models.Model):
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    numero = models.CharField(
        max_length=11,
        validators=[VALIDADOR_TELEFONE]
    )
    notas = models.TextField()


class EntradaAgenda(models.Model):
    TelefoneRelacioando = models.ForeignKey('Telefone', on_delete=models.CASCADE)
    NomeEntrada = models.CharField(max_length=255)
    PossivelAlvo = models.ForeignKey(
        'Pessoa',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    NomePossivelAlvo = models.CharField(max_length=255, blank=True, null=True)
    NomeArquivo = models.CharField(max_length=255, null=True, blank=True)


class Arquivo(models.Model):
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    Arquivo = models.FileField()
    Notas = models.TextField()
