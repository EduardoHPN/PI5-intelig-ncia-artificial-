from django import forms 
from recipes.models import *

class ClienteTesteForma(forms.ModelForm):
    class Meta:
        model = ClienteTeste
        fields = "__all__"


        
class ParagrafOneForm(forms.ModelForm):
    class Meta:
        model = ClientParagrafOne
        fields = [
            'ProcessNumer',
            'NumberStickCriminal',
            'CityComarc',
            'TypeAction',
            'PartOuter',
            'NameAcused',
            'Nacionalit',
            'CivilState',
            'Cpf',
            'Address',
            'State',
            'AnoterDefender',
        ]


class DefesaPreliminarForm(forms.ModelForm):
    class Meta:
        model = DefesaPreliminar
        fields = [
            'artigo_crime',
            'data_fato',
            'local_fato',
            'admite_crime',
            'havia_testemunhas',
            'descricao_testemunhas',
            'provas_mencionadas',
            'antecedentes',
            'esta_preso',
            'local_prisao',
            'em_liberdade',
            'alibi_ou_testemunha_defesa',
            'mencionar_defesa_futura',
            'tonalidade',
        ]



class ArgumentacaoJuridicaForm(forms.ModelForm):
    class Meta:
        model = ArgumentacaoJuridica
        fields = [
            # Nulidades ou vícios processuais
            'falha_cumprimento_legal',
            'falha_qual',
            'tratamento_injusto',
            'irregularidade_prisao',
            'direito_ampla_defesa',
            'direito_ampla_defesa_como',
            'defesa_ouvida',
            'defesa_prejuizos',

            # Inexistência de materialidade ou autoria
            'prova_testemunhal_suficiente',
            'testemunhas_falha',
            'laudo_pericial_comprova',
            'laudo_falha_ou_omissao',
            'materialidade_nao_comprovada',
            'materialidade_por_que',
            'alibi_comprova_inocencia',
            'alibi_descricao',
            'acusacao_baseada_em_suposicoes',
            'acusacao_natureza_provas',

            # Excludentes de ilicitude ou culpabilidade
            'estado_necessidade',
            'estado_necessidade_justificativa',
            'legitima_defesa',
            'legitima_defesa_explicacao',
            'erro_tipo_ou_proibicao',
            'erro_explicacao',
            'coercao_moral_irresistivel',
            'coercao_moral_explicacao',
            'outras_causas_excluintes',
            'outras_causas_excluintes_descr',

            # Princípios violados
            'presuncao_inocencia',
            'presuncao_inocencia_como',
            'devido_processo_legal',
            'devido_processo_legal_impactos',
            'proporcionalidade_violada',
            'proporcionalidade_como',
            'cerceamento_defesa',
            'cerceamento_defesa_momento',
            'dignidade_pessoa_humana',
            'dignidade_pessoa_humana_aspecto',
            'tratamento_diferenciado',
            'tratamento_diferenciado_qual',
            'julgamento_imparcial',
            'julgamento_imparcial_como',

            # Outros argumentos
            'circunstancia_relevante',
            'circunstancia_descricao',
            'pena_desproporcional',
            'pena_desproporcional_justificativa',
            'jurisprudencia_favorece',
            'jurisprudencia_descricao',
        ]
