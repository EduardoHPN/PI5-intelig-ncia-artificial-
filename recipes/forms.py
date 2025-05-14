from django import forms 
from recipes.models import *

class ClienteTesteForma(forms.ModelForm):
    class Meta:
        model = ClienteTeste
        fields = "__all__"


class ParagrafOneForm(forms.ModelForm):
    CIVIL_STATE_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    ]

    TypeActionChoise = [
        ('AC', 'Ação Penal'),
        ('IP', 'Inquérito Policial'),
    ]

    CivilState = forms.ChoiceField(
        choices=CIVIL_STATE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Estado Civil'
    )

    TypeAction = forms.ChoiceField(
        choices=TypeActionChoise,
        widget=forms.Select(attrs={'class': 'form-control'}),  # Garante a classe form-control
        label='Tipo de Ação'
    )

    Cpf = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00',
            'inputmode': 'numeric',
            'id': 'id_cpf'
        }),
        label='CPF'
    )

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['TypeAction'].initial = ''

        # Adicionando a classe 'form-control' para os outros campos
        for field_name, field in self.fields.items():
            if field_name not in ['Cpf', 'CivilState', 'TypeAction']:
                field.widget.attrs.update({'class': 'form-control'})


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control', 'rows': 3})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

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
        widgets = {
            # Campos de texto
            'falha_qual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tratamento_injusto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'irregularidade_prisao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'direito_ampla_defesa_como': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'defesa_prejuizos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'testemunhas_falha': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'laudo_falha_ou_omissao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'materialidade_por_que': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'alibi_descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'acusacao_natureza_provas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado_necessidade_justificativa': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'legitima_defesa_explicacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'erro_explicacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'coercao_moral_explicacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'outras_causas_excluintes_descr': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'presuncao_inocencia_como': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'devido_processo_legal_impactos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'proporcionalidade_como': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cerceamento_defesa_momento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dignidade_pessoa_humana_aspecto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tratamento_diferenciado_qual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'julgamento_imparcial_como': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'circunstancia_descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pena_desproporcional_justificativa': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'jurisprudencia_descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adicionando a classe 'form-control' aos campos de input padrão
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # Adicionando classes especiais para campos de Checkbox
        self.fields['falha_cumprimento_legal'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['direito_ampla_defesa'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['defesa_ouvida'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['prova_testemunhal_suficiente'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['materialidade_nao_comprovada'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['estado_necessidade'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['legitima_defesa'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['erro_tipo_ou_proibicao'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['coercao_moral_irresistivel'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['presuncao_inocencia'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['devido_processo_legal'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['proporcionalidade_violada'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['cerceamento_defesa'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['dignidade_pessoa_humana'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['tratamento_diferenciado'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['julgamento_imparcial'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['circunstancia_relevante'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['pena_desproporcional'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['jurisprudencia_favorece'].widget.attrs.update({'class': 'form-check-input'})


class PedidoDefesaPenalForm(forms.ModelForm):
    class Meta:
        model = PedidoDefesaPenal
        fields = [
            'pedido_principal',
            'outro_pedido_principal',
            'incluir_absolvicao_como_alternativa',
            'fundamentos_absolvicao',
            'outro_fundamento_absolvicao',
            'esta_preso',
            'solicitar_alvara',
            'pedir_medidas_cautelares',
            'medidas_cautelares',
            'incluir_pedido_subsidiario',
            'pedido_subsidiario',
            'requerer_nao_recebimento_denuncia',
            'requerer_prioridade',
            'requerer_acesso_provas',
            'quais_provas',
            'outros_pedidos',
        ]

        widgets = {
            'fundamentos_absolvicao': forms.Select(attrs={'class': 'form-control'}),
            'medidas_cautelares': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Descreva as medidas cautelares'}),
            'pedido_subsidiario': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Descreva o pedido subsidiário'}),
            'quais_provas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Informe as provas que deseja acessar'}),
            'outros_pedidos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva outros pedidos'}),
            'pedido_principal': forms.Select(attrs={'class': 'form-control'}),
            'outro_pedido_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe outro pedido principal'}),
            'incluir_absolvicao_como_alternativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'esta_preso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'solicitar_alvara': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pedir_medidas_cautelares': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'incluir_pedido_subsidiario': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'requerer_nao_recebimento_denuncia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'requerer_prioridade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'requerer_acesso_provas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'pedido_principal': 'Pedido Principal',
            'outro_pedido_principal': 'Outro Pedido Principal',
            'incluir_absolvicao_como_alternativa': 'Incluir absolvição como alternativa',
            'fundamentos_absolvicao': 'Fundamentos para absolvição',
            'outro_fundamento_absolvicao': 'Outro fundamento de absolvição',
            'esta_preso': 'Está preso?',
            'solicitar_alvara': 'Solicitar alvará?',
            'pedir_medidas_cautelares': 'Pedir medidas cautelares?',
            'medidas_cautelares': 'Medidas cautelares',
            'incluir_pedido_subsidiario': 'Incluir pedido subsidiário',
            'pedido_subsidiario': 'Pedido subsidiário',
            'requerer_nao_recebimento_denuncia': 'Requerer não recebimento de denúncia',
            'requerer_prioridade': 'Requerer prioridade',
            'requerer_acesso_provas': 'Requerer acesso a provas',
            'quais_provas': 'Quais provas',
            'outros_pedidos': 'Outros pedidos',
        }

class DocumentacaoEJurisprudenciaForm(forms.ModelForm):
    class Meta:
        model = DocumentacaoEJurisprudencia
        fields = [
            'certidao',
            'laudo',
            'testemunha_nome',
            'testemunha_qualificacao',
            'jurisprudencias',
            'incluir_jurisprudencia_apoio',
            'tese_juridica_apoio',
            'julgado_especifico',
        ]
        widgets = {
            'certidao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe a certidão'}),
            'laudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descreva o laudo'}),
            'testemunha_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da testemunha'}),
            'testemunha_qualificacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qualificação da testemunha'}),
            'jurisprudencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Digite as jurisprudências'}),
            'incluir_jurisprudencia_apoio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tese_juridica_apoio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Informe a tese jurídica'}),
            'julgado_especifico': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Informe o julgado específico'}),
        }
        labels = {
            'certidao': 'Certidão',
            'laudo': 'Laudo',
            'testemunha_nome': 'Nome da Testemunha',
            'testemunha_qualificacao': 'Qualificação da Testemunha',
            'jurisprudencias': 'Jurisprudências',
            'incluir_jurisprudencia_apoio': 'Incluir Jurisprudência de Apoio',
            'tese_juridica_apoio': 'Tese Jurídica de Apoio',
            'julgado_especifico': 'Julgado Específico',
        }
