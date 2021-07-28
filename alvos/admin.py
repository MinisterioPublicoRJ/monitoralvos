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
        Anotacao,
        Telefone,
        EntradaAgenda,
        TipoDocumento,
        Arquivo,
        TipoRelacao,
)


class ArquivoInline(nested_admin.NestedTabularInline):
    model = Arquivo
    extra = 1


class OcorrenciaInline(nested_admin.NestedTabularInline):
    model = Ocorrencia
    extra = 1


class EmailInline(nested_admin.NestedTabularInline):
    model = Email
    extra = 1


class DocumentoInline(nested_admin.NestedTabularInline):
    model = Documento
    extra = 1


class ProcedimentoInline(nested_admin.NestedTabularInline):
    model = Procedimento
    extra = 1


class VeiculoInline(nested_admin.NestedTabularInline):
    model = Veiculo
    extra = 1


class RelacaoInline(nested_admin.NestedTabularInline):
    model = Relacao
    fk_name = 'PessoaDe'
    extra = 1


class AnotacaoInline(nested_admin.NestedTabularInline):
    model = Anotacao
    extra = 1


class EntradaAgendaInline(nested_admin.NestedTabularInline):
    model = EntradaAgenda
    extra = 1


class TelefoneInline(nested_admin.NestedTabularInline):
    model = Telefone
    extra = 1
    inlines = [EntradaAgendaInline]


class PessoaAdmin(nested_admin.NestedModelAdmin):
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
        AnotacaoInline,
        ArquivoInline,
        OcorrenciaInline,
        EmailInline,
        RelacaoInline,
        DocumentoInline,
        ProcedimentoInline,
        VeiculoInline,
        TelefoneInline
    ]

    readonly_fields = ['foto_tag']

    list_display = [
        'nome',
        'nascimento',
        'alvo',
        'militar',
        'policial'
    ]

    list_filter = [
        'alvo',
        'militar',
        'policial'
    ]

    search_fields = (
        'anotacao__Nota',
        'nome',
        'documento__numeracao',
        'procedimento__Numeracao',
        'veiculo__Placa',
        'email__EMail',
        'ocorrencia__NumeroOcorrencia',
        'telefone__numero',
        'arquivo__Notas'
    )


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(MarcaVeiculo)
admin.site.register(ModeloVeiculo)
admin.site.register(TipoDocumento)
admin.site.register(TipoRelacao)
