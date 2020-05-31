# Criminalidade em São Paulo

A __Criminalidade__ é um problema recorrente no Brasil.
Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados 
conseguimos entender melhor o que estpa acontecendo e gerar insights
que direcionem ações capazes de diminuir os índices de criminalidade.

## Como funciona

O usuário pode escolher em que ano deseja realizar a consulta e se desejar ver os dados brutos

### Imagens

![Imagem mapa 01][image_map_01]

![Imagem mapa 02][image_map_02]

### Estrutura:
```text
criminalidade sp
| - data
|   | -- criminalidade_sp.csv
|   | -- criminalidade_sp_2.csv
| - criminalidade.py
```

### Para executar:  
```bash
$ streamlit run criminalide.py
```

## Semana Data Science

Esse projeto foi realizado na _Semana Data Science_, realizada pelo [Carlos Melo][carlos_melo_github] do __Sigmoidal__.
A principal ideia dessa semana era a iniciação na área de Data Science de forma prática.



[image_map_01]: assets/criminalidade01.png
[image_map_02]: assets/criminalidade02.png
[carlos_melo_github]: https://github.com/carlosfab "Github Carlos Melo"
