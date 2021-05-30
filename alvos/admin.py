from django.contrib import admin
import nested_admin
from .models import (
        Pessoa,
        Relacao,
        Ocorrencia,
        Email,
        Documento,
        Procedimento,
        Veiculo,
        MarcaVeiculo,
        ModeloVeiculo,
)


class OcorrenciaInline(nested_admin.NestedTabularInline):
    model = Ocorrencia


class EmailInline(nested_admin.NestedTabularInline):
    model = Email


class DocumentoInline(nested_admin.NestedTabularInline):
    model = Documento


class ProcedimentoInline(nested_admin.NestedTabularInline):
    model = Procedimento


class VeiculoInline(nested_admin.NestedTabularInline):
    model = Veiculo


class RelacaoInline(nested_admin.NestedTabularInline):
    model = Relacao
    fk_name = 'PessoaDe'


class PessoaAdmin(admin.ModelAdmin):
    fields = (
        'nome',
        'nascimento',
        'alvo',
        'militar',
        'policial',
        'foto_tag',
        'foto',
    )

    inlines = [
        OcorrenciaInline,
        EmailInline,
        RelacaoInline,
        DocumentoInline,
        ProcedimentoInline,
        VeiculoInline,
    ]
    readonly_fields = ['foto_tag']


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(MarcaVeiculo)
admin.site.register(ModeloVeiculo)
