import pandas as pd

# Lista atualizada de colunas usadas pelo modelo com base no novo dataset
colunas_treinamento_modelo = [
    'Temperatura_Media', 'Cultura_Arroz', 'Cultura_Café', 'Cultura_Milho', 'Cultura_Soja', 'Cultura_Trigo', 
    'Cultura_Batata', 'Cultura_Cana-de-Açúcar', 'Cultura_Uva', 'Quantidade_a_ser_Plantada_Toneladas',
    'Perimetro', 'Tipo_de_Solo_Areia', 'Tipo_de_Solo_Argila', 'Tipo_de_Solo_Silte', 'Tipo_de_Solo_Calcário', 
    'Tipo_de_Solo_Aluvial', 'Tipo_de_Solo_Não usar', 'Tipo_de_Irrigacao_Aspersão', 'Tipo_de_Irrigacao_Gotejamento', 
    'Tipo_de_Irrigacao_Sulcos', 'Tipo_de_Irrigacao_Subirrigação', 'Tipo_de_Irrigacao_Microaspersão', 
    'Tipo_de_Irrigacao_Não usar', 'Frequencia_Irrigacao_Diária', 'Frequencia_Irrigacao_Mensal', 
    'Frequencia_Irrigacao_Semanal', 'Fertilizante_Composto', 'Fertilizante_Fósforo', 'Fertilizante_Nitrogênio', 
    'Fertilizante_Orgânico', 'Fertilizante_Potássio', 'Fertilizante_Nenhum', 'Pragas_Ferrugem', 
    'Pragas_Fungos', 'Pragas_Insetos', 'Pragas_Nenhuma', 'Pragas_Outras', 'Rotacao_de_Culturas_Sim', 
    'Rotacao_de_Culturas_Não', 'Uso_de_Pesticidas_Alto', 'Uso_de_Pesticidas_Moderado', 'Uso_de_Pesticidas_Baixo', 
    'Uso_de_Pesticidas_Nenhum', 'Tecnologia_Utilizada_Alto', 'Tecnologia_Utilizada_Médio', 
    'Tecnologia_Utilizada_Baixo'
]

def completa_dataframe_agricola(valores):
    # Criação do DataFrame com os valores passados pelo usuário
    df = pd.DataFrame([valores], columns=[
        'Cultura', 'Quantidade_a_ser_Plantada_Toneladas', 'Perimetro', 'Frequencia_Irrigacao', 
        'Tipo_de_Solo', 'Tipo_de_Irrigacao', 'Fertilizante', 'Temperatura_Media', 'Pragas', 
        'Rotacao_de_Culturas', 'Uso_de_Pesticidas', 'Tecnologia_Utilizada'
    ])
    
    # Codificação das variáveis categóricas usando get_dummies
    df_encoded = pd.get_dummies(df)

    # Adiciona as colunas que não foram geradas durante a codificação, mas que são esperadas pelo modelo
    for coluna in colunas_treinamento_modelo:
        if coluna not in df_encoded.columns:
            df_encoded[coluna] = 0

    # Reordena as colunas conforme o modelo espera
    df_encoded = df_encoded[colunas_treinamento_modelo]
    
    return df_encoded
