# Presenter Vision AI

O Presenter Vision AI é uma aplicação web desenvolvida em Python que utiliza técnicas de visão computacional para analisar aspectos da comunicação em vídeo, como postura, contato visual, enquadramento e detecção de articulações corporais.

O projeto foi desenvolvido como atividade da disciplina de Visão Computacional com o objetivo de aplicar, na prática, bibliotecas como OpenCV e MediaPipe em uma solução voltada para um problema real.

## Motivação

Professores, jornalistas e criadores de conteúdo passam grande parte do tempo em frente à câmera, mas normalmente só conseguem avaliar sua postura e presença depois da gravação. A proposta desta aplicação é fornecer um feedback em tempo real sobre esses aspectos, auxiliando na melhoria da comunicação durante apresentações e gravações.

## Funcionalidades

* Detecção facial em tempo real
* Detecção de articulações corporais
* Identificação da postura do apresentador
* Verificação do enquadramento na câmera
* Análise do contato visual
* Interface web desenvolvida com Flask

## Tecnologias utilizadas

* Python 3.12
* Flask
* OpenCV
* MediaPipe
* HTML
* CSS

## Estrutura do projeto

```text
.
├── app.py
├── detectar_rosto.py
├── detectar_corpo.py
├── teste_camera.py
├── static/
├── templates/
├── requirements.txt
└── README.md
```

http://127.0.0.1:5000


## Próximos passos

Como evolução do projeto, pretende-se adicionar novas funcionalidades, como geração de relatórios, histórico de análises, métricas mais detalhadas sobre expressividade e integração com plataformas de videoconferência.

## Autora

Thaís Silveira

Projeto desenvolvido para a disciplina de Visão Computacional.
