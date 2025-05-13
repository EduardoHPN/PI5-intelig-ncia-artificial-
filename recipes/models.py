from django.db import models

# Create your models here.
 
sexo_choise = (
    ('F', 'Feminino'),
    ('M', 'Masculino')

)

TypeActionChoise = (
    ('AC', 'Ação Penal'),
    ('IP', 'Inquerito Policial')
)


preso = (
    ('S', 'Preso'),
    ('N', 'Não Preso')
)

FUNDAMENTO_ABSOLVICAO_CHOICES = [
        ('inexistencia_fato', 'Inexistência do fato'),
        ('fato_atipico', 'Fato atípico'),
        ('excludente_ilicitude', 'Excludente de ilicitude'),
        ('excludente_culpabilidade', 'Excludente de culpabilidade'),
        ('ausencia_autoria', 'Ausência de indícios suficientes de autoria'),
        ('outro', 'Outro (especificar)'),
]

class ClienteTeste(models.Model):
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField(blank=True, null= True)
    sexo = models.CharField(max_length=1, choices=sexo_choise)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    


class  ClientParagrafOne(models.Model):
    uid = models.CharField(max_length=100, verbose_name="uid user",blank=True, null=True)
    ProcessNumer = models.CharField(max_length=40, verbose_name="Numero do processo")
    NumberStickCriminal = models.CharField(max_length=40, verbose_name=" Numero da vara criminal")
    CityComarc = models.CharField(max_length=40, verbose_name="Numero da comarca")
    TypeAction = models.CharField(max_length=2, choices=TypeActionChoise, verbose_name="Tipo da acusação")
    PartOuter = models.CharField(max_length=40, verbose_name="Parte da autora")
    NameAcused = models.CharField(max_length=40, verbose_name="Nome do acusado")
    Nacionalit = models.CharField(max_length=15, verbose_name="Nacionalidade")
    CivilState = models.CharField(max_length=15, verbose_name="Estado Civíl")
    Cpf = models.CharField(max_length=14, verbose_name="CPF")
    Address = models.CharField(max_length=150, verbose_name="Endereço")
    State = models.CharField(max_length=1, choices=preso, verbose_name="O cliente está preso?")
    AnoterDefender = models.CharField(max_length=40,blank=True, null=True, verbose_name="Nome do advogado de ataque" )


    def __str__(self):
        return self.NameAcused
    




class DefesaPreliminar(models.Model):
    uid = models.CharField(max_length=100, verbose_name="UID do usuário", blank=True, null=True)
    artigo_crime = models.CharField(max_length=50, verbose_name="Artigo ou tipo de crime")
    data_fato = models.DateField(verbose_name="Data do fato")
    local_fato = models.CharField(max_length=150, verbose_name="Local do fato")
    
    admite_crime = models.BooleanField(verbose_name="O acusado admite o crime?")
    
    havia_testemunhas = models.BooleanField(verbose_name="Havia testemunhas no momento do fato?")
    descricao_testemunhas = models.TextField(verbose_name="Informações sobre as testemunhas", blank=True, null=True)

    provas_mencionadas = models.TextField(verbose_name="Provas apresentadas ou mencionadas", blank=True, null=True)

    antecedentes = models.BooleanField(verbose_name="O acusado possui antecedentes criminais?")
    
    esta_preso = models.BooleanField(verbose_name="O acusado está preso atualmente?")
    local_prisao = models.CharField(max_length=100, verbose_name="Local da prisão", blank=True, null=True)
    em_liberdade = models.CharField(max_length=100, verbose_name="Situação se estiver em liberdade", blank=True, null=True)

    alibi_ou_testemunha_defesa = models.TextField(verbose_name="Álibi ou testemunha de defesa", blank=True, null=True)

    mencionar_defesa_futura = models.BooleanField(verbose_name="Deseja mencionar que a defesa será apresentada em momento oportuno?")
    
    TONALIDADE_OPCOES = [
        ('F', 'Formal técnico e objetivo'),
        ('E', 'Enfático e contundente'),
        ('N', 'Neutro'),
    ]
    tonalidade = models.CharField(max_length=1, choices=TONALIDADE_OPCOES, verbose_name="Tom da peça")

    def __str__(self):
        return f"Defesa Preliminar - {self.uid or 'sem UID'}"



class ArgumentacaoJuridica(models.Model):
    uid = models.CharField(max_length=100, verbose_name="UID do usuário", blank=True, null=True)

    # Nulidades ou vícios processuais
    falha_cumprimento_legal = models.BooleanField(default=False, verbose_name="Houve falha no cumprimento das formalidades legais?")
    falha_qual = models.TextField(blank=True, null=True, verbose_name="Se sim, qual falha foi cometida?")
    tratamento_injusto = models.TextField(blank=True, null=True, verbose_name="Defesa considera que o acusado foi tratado de forma injusta ou irregular?")

    irregularidade_prisao = models.TextField(blank=True, null=True, verbose_name="Houve irregularidade no momento da prisão ou apreensão?")
    direito_ampla_defesa = models.BooleanField(default=False, verbose_name="Foi desrespeitado o direito à ampla defesa e contraditório?")
    direito_ampla_defesa_como = models.TextField(blank=True, null=True, verbose_name="Se sim, como?")

    defesa_ouvida = models.BooleanField(default=False, verbose_name="A defesa foi ouvida de forma adequada durante o processo?")
    defesa_prejuizos = models.TextField(blank=True, null=True, verbose_name="Se não, quais prejuízos isso causou?")

    # Inexistência de materialidade ou autoria
    prova_testemunhal_suficiente = models.BooleanField(default=False, verbose_name="A prova testemunhal é suficiente para comprovar a autoria do crime?")
    testemunhas_falha = models.TextField(blank=True, null=True, verbose_name="Se não, qual a contradição ou falha nas testemunhas?")

    laudo_pericial_comprova = models.BooleanField(default=False, verbose_name="O laudo pericial comprova o vínculo do acusado com o fato?")
    laudo_falha_ou_omissao = models.TextField(blank=True, null=True, verbose_name="Se não, explique qual falha ou omissão o laudo apresenta.")

    materialidade_nao_comprovada = models.BooleanField(default=False, verbose_name="A defesa acredita que a materialidade do crime não foi comprovada?")
    materialidade_por_que = models.TextField(blank=True, null=True, verbose_name="Se sim, por quê?")

    alibi_comprova_inocencia = models.BooleanField(default=False, verbose_name="O acusado possui álibi ou outra prova que comprova sua inocência?")
    alibi_descricao = models.TextField(blank=True, null=True, verbose_name="Se sim, qual é?")

    acusacao_baseada_em_suposicoes = models.BooleanField(default=False, verbose_name="A acusação se baseia em provas indiretas ou apenas suposições?")
    acusacao_natureza_provas = models.TextField(blank=True, null=True, verbose_name="Se sim, qual é a natureza das provas?")

    # Excludentes de ilicitude ou culpabilidade
    estado_necessidade = models.BooleanField(default=False, verbose_name="A defesa alega que o acusado agiu em estado de necessidade?")
    estado_necessidade_justificativa = models.TextField(blank=True, null=True, verbose_name="Se sim, qual a situação que justifica o estado de necessidade?")

    legitima_defesa = models.BooleanField(default=False, verbose_name="A defesa invoca legítima defesa?")
    legitima_defesa_explicacao = models.TextField(blank=True, null=True, verbose_name="Se sim, explique como o acusado agiu em legítima defesa.")

    erro_tipo_ou_proibicao = models.CharField(max_length=50, choices=[('erro_tipo', 'Erro de tipo'), ('erro_proibicao', 'Erro de proibição'), ('nao_aplica', 'Não se aplica')], default='nao_aplica', verbose_name="O acusado agiu em erro de tipo ou erro de proibição?")
    erro_explicacao = models.TextField(blank=True, null=True, verbose_name="Se aplicável, como o erro ocorreu?")

    coercao_moral_irresistivel = models.BooleanField(default=False, verbose_name="Houve alguma situação em que o acusado estava em uma situação de coação moral irresistível?")
    coercao_moral_explicacao = models.TextField(blank=True, null=True, verbose_name="Se sim, explique.")

    outras_causas_excluintes = models.BooleanField(default=False, verbose_name="Existem outras causas que excluem a ilicitude ou culpabilidade do acusado?")
    outras_causas_excluintes_descr = models.TextField(blank=True, null=True, verbose_name="Se sim, quais são?")

    # Princípios violados
    presuncao_inocencia = models.BooleanField(default=False, verbose_name="O princípio da presunção de inocência foi violado?")
    presuncao_inocencia_como = models.TextField(blank=True, null=True, verbose_name="Se sim, como?")

    devido_processo_legal = models.BooleanField(default=False, verbose_name="O direito ao devido processo legal foi respeitado?")
    devido_processo_legal_impactos = models.TextField(blank=True, null=True, verbose_name="Se não, quais etapas ou aspectos do processo foram afetados?")

    proporcionalidade_violada = models.BooleanField(default=False, verbose_name="O princípio da proporcionalidade foi desrespeitado?")
    proporcionalidade_como = models.TextField(blank=True, null=True, verbose_name="Se sim, explique como a medida aplicada foi desproporcional.")

    cerceamento_defesa = models.BooleanField(default=False, verbose_name="Houve cerceamento de defesa?")
    cerceamento_defesa_momento = models.TextField(blank=True, null=True, verbose_name="Se sim, em que momento o cerceamento ocorreu?")

    dignidade_pessoa_humana = models.BooleanField(default=False, verbose_name="O princípio da dignidade da pessoa humana foi violado em algum momento do processo?")
    dignidade_pessoa_humana_aspecto = models.TextField(blank=True, null=True, verbose_name="Se sim, em que aspecto?")

    tratamento_diferenciado = models.BooleanField(default=False, verbose_name="O acusado foi tratado de forma diferenciada ou discriminatória durante o processo?")
    tratamento_diferenciado_qual = models.TextField(blank=True, null=True, verbose_name="Se sim, qual o tratamento diferenciado?")

    julgamento_imparcial = models.BooleanField(default=False, verbose_name="O acusado teve direito a um julgamento imparcial?")
    julgamento_imparcial_como = models.TextField(blank=True, null=True, verbose_name="Se não, como isso ocorreu?")

    # Outros argumentos
    circunstancia_relevante = models.BooleanField(default=False, verbose_name="Há alguma outra circunstância que a defesa considera relevante para a absolvição ou redução da pena?")
    circunstancia_descricao = models.TextField(blank=True, null=True, verbose_name="Se sim, qual circunstância?")

    pena_desproporcional = models.BooleanField(default=False, verbose_name="A defesa considera que a pena proposta é desproporcional em relação à gravidade do fato?")
    pena_desproporcional_justificativa = models.TextField(blank=True, null=True, verbose_name="Se sim, explique por quê.")

    jurisprudencia_favorece = models.BooleanField(default=False, verbose_name="Há alguma jurisprudência ou decisão anterior que favorece a defesa?")
    jurisprudencia_descricao = models.TextField(blank=True, null=True, verbose_name="Se sim, qual jurisprudência?")

    def __str__(self):
        return f"Defesa de {self.id}"



from django.db import models

class PedidoDefesaPenal(models.Model):
    uid = models.CharField(max_length=100, verbose_name="UID do usuário", blank=True, null=True)
    # Principais pedidos
    PEDIDO_PRINCIPAL_CHOICES = [
        ('extincao', 'Extinção da ação penal'),
        ('absolvicao_sumaria', 'Absolvição sumária'),
        ('trancamento', 'Trancamento da ação penal'),
        ('arquivamento', 'Arquivamento'),
        ('outro', 'Outro (especificar)'),
    ]
    pedido_principal = models.CharField(max_length=30, choices=PEDIDO_PRINCIPAL_CHOICES)
    outro_pedido_principal = models.CharField(max_length=255, blank=True, null=True)

    # Pedido alternativo
    incluir_absolvicao_como_alternativa = models.BooleanField()

    # Fundamento para absolvição sumária
    FUNDAMENTO_ABSOLVICAO_CHOICES = [
        ('inexistencia_fato', 'Inexistência do fato'),
        ('fato_atipico', 'Fato atípico'),
        ('excludente_ilicitude', 'Excludente de ilicitude'),
        ('excludente_culpabilidade', 'Excludente de culpabilidade'),
        ('ausencia_autoria', 'Ausência de indícios suficientes de autoria'),
        ('outro', 'Outro (especificar)'),
    ]

    # Alterando para ManyToManyField
    fundamentos_absolvicao = models.CharField(
        max_length=255,
        choices=FUNDAMENTO_ABSOLVICAO_CHOICES,
        blank=True,
        null=True
    )

    outro_fundamento_absolvicao = models.CharField(max_length=255, blank=True, null=True)

    # Situação prisional
    esta_preso = models.BooleanField()
    solicitar_alvara = models.BooleanField(default=False)
    pedir_medidas_cautelares = models.BooleanField(default=False)
    medidas_cautelares = models.TextField(blank=True, null=True)

    # Pedidos subsidiários
    incluir_pedido_subsidiario = models.BooleanField(default=False)
    pedido_subsidiario = models.TextField(blank=True, null=True)

    # Não recebimento da denúncia
    requerer_nao_recebimento_denuncia = models.BooleanField(default=False)

    # Prioridade de tramitação
    requerer_prioridade = models.BooleanField(default=False)

    # Provas ou diligências complementares
    requerer_acesso_provas = models.BooleanField(default=False)
    quais_provas = models.TextField(blank=True, null=True)

    # Observações finais
    outros_pedidos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pedido de Defesa Penal #{self.id}"

class FundamentoAbsolvicao(models.Model):
    codigo = models.CharField(max_length=255, choices=FUNDAMENTO_ABSOLVICAO_CHOICES)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao




class DocumentacaoEJurisprudencia(models.Model):
    uid = models.CharField(max_length=100, verbose_name="UID do usuário", blank=True, null=True)
    # 5.1 - Lista de documentos
    certidao = models.TextField(
        blank=True,
        null=True,
        help_text="Descreva a certidão relevante para o caso (ex.: certidão de antecedentes criminais)."
    )
    laudo = models.TextField(
        blank=True,
        null=True,
        help_text="Descreva o laudo técnico ou pericial relevante para o caso (ex.: exame toxicológico, laudo do IML)."
    )
    testemunha_nome = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Nome completo da testemunha, se houver."
    )
    testemunha_qualificacao = models.TextField(
        blank=True,
        null=True,
        help_text="Qualificação da testemunha (ex.: profissão, relação com o réu)."
    )
    jurisprudencias = models.TextField(
        blank=True,
        null=True,
        help_text="Jurispurências específicas já separadas (ex.: número do processo ou ementa)."
    )

    # 5.2 - Jurisprudência de apoio
    incluir_jurisprudencia_apoio = models.BooleanField(
        default=False,
        help_text="Deseja incluir jurisprudências de apoio para a sua tese principal?"
    )
    tese_juridica_apoio = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Qual a tese jurídica que deseja reforçar com jurisprudência? (ex.: ausência de justa causa)."
    )
    julgado_especifico = models.TextField(
        blank=True,
        null=True,
        help_text="Cole o número do HC, REsp ou a ementa do julgado específico que gostaria de citar."
    )

    def __str__(self):
        return f"Documentação e Jurisprudência - Caso #{self.id}"

