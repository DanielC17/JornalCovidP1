from flask import Flask, render_template, request, url_for
import os
from application.model.entity.noticias import Noticias
from application.model.entity.estados import Estados

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)


lista_noticias = []
lista_noticias.append(Noticias("Secretaria de Estado de Saúde recebe duas ambulâncias", "/img/RJ.png", "25/04/2021", "A primeira ambulância foi entregue no final de marçoA Secretaria de Estado de Saúde (SES) receberá duas ambulâncias zero-quilômetro para atendimento prioritário de casos de Covid-19. A entrega das ambulâncias é fruto de um acordo judicial entre o Ministério Público do Trabalho (MPT-1ªRegião/RJ), e a Legião da Boa Vontade (LBV), que tramitou na 53ª Vara do Trabalho do Rio de Janeiro.\n A primeira ambulância foi entregue no final de março e a segunda chegará até agosto.A ambulância veio em um momento muito especial para a população do nosso estado, e certamente contribuirá para salvar vidas – afirma o secretário de Saúde, Carlos Alberto Chaves."))
lista_noticias.append(Noticias("Secretaria de Estado de Saúde distribui 517 mil doses de vacinas contra Covid-19 neste fim de semana", "/img/RJ.png", "01/05/2021", "A Secretaria de Estado de Saúde (SES) realiza mais uma entrega de vacinas contra a Covid-19 e medicamentos do chamado “kit intubação” neste fim de semana. Ao todo, são 517 mil doses de imunizantes, sendo 273.500 da vacina Oxford/AstraZeneca e 243.500 da Coronavac, além de 47.400 unidades de medicamentos.No domingo (18.04), a partir das 7h, seis aeronaves vão decolar do Grupamento Aeromóvel da Polícia Militar e do 12º BPM, em Niterói, para transportar vacinas e medicamentos. Serão utilizados dois helicópteros do Governo do Estado, um da SES, dois do Corpo de Bombeiros e um da Polícia Civil."))
lista_noticias.append(Noticias("SP encerra abril com queda de 29 nas internações por COVID-19", "/img/SP.png", "30/04/2021", "O Estado de São Paulo encerra o mês de abril com uma redução de 29,8 no número de pessoas internadas pela COVID-19 em relação ao final de março. Nesta sexta-feira (30), são 21.869 pacientes hospitalizados no estado, sendo 10.216 em unidades de terapia intensiva e 11.653 em enfermaria."))
lista_noticias.append(Noticias("SP entrega ao Brasil total do lote de 600 mil vacinas do Butantan", "/img/SP.png", "02/05/2021", "O Governador João Doria acompanhou, nesta sexta-feira (30), o envio de mais uma carga de vacinas do Instituto Butantan contra o coronavírus. Com o carregamento de hoje, São Paulo entrega ao PNI (Programa Nacional de Imunizações) mais 600 mil doses, que fazem parte de um novo lote de 5,4 milhões de vacinas a serem distribuídas para todo o país."))
lista_noticias.append(Noticias("ES não tem mais cidades em risco extremo para a Covid-19", "/img/espiritosanto.png", "28/04/2021", "'Depois de dois meses temos um RT abaixo de 1. Significa que estamos em queda em relação à pandemia. Uma pessoa contagia menos. O RT está em 0,68, então 100 pessoas contagiam 68 pessoas. Fazemos essa medição semanalmente para ver de fato a nossa taxa de transmissão' explicou. Casagrande ainda falou sobre a expectativa de reduzir a média de mortes pelo coronavírus."))
lista_noticias.append(Noticias("ES chega a 9.524 mortes e 436.681 casos confirmados de Covid-19", "/img/espiritosanto.png", "10/04/2021", "O Espírito Santo registrou, até esta sexta-feira (30), 9.524 mortes por Covid-19. O número de casos confirmados chegou a 436.681. O índice de letalidade da doença no estado é de 2,2%. Os dados foram divulgados na plataforma Painel Covid-19, do governo do estado."))
lista_noticias.append(Noticias("Veja lista de comorbidades para vacinação contra Covid-19 no DF", "/img/DF.png", "26/04/2021", "Entre os dias 7 e 18 de maio, está prevista a vacinação de pessoas com comorbidades entre 59 e 55 anos (veja calendário ao fim da reportagem). Para aqueles que têm alguma dessas condições, porém estão abaixo dessa faixa etária, ainda não há data definida para atendimento."))
lista_noticias.append(Noticias("Média móvel de mortes por Covid-19 no DF cai para 43,4", "/img/DF.png", "01/05/2021", "A média móvel de mortes por Covid-19 no Distrito Federal caiu novamente nesta sexta-feira (30/4). O índice – que estava em 45,9 na quinta-feira (29/4) – chegou a 43,4. Foram contabilizados 37 óbitos de moradores da capital, no levantamento diário. Devido ao atraso nas notificações, as mortes não ocorreram, necessariamente, nas últimas 24 horas."))


lista_estados = []
lista_estados.append(Estados("Rio de Janeiro", "RJ", "/img/RJ.png", lista_noticias[0:2] ))
lista_estados.append(Estados("São Paulo", "SP", "/img/SP.png", lista_noticias[2:4]))
lista_estados.append(Estados("Espírito Santo", "ES", "/img/espiritosanto.png", lista_noticias[4:6]))
lista_estados.append(Estados("Brasília", "DF", "/img/DF.png", lista_noticias[6:8]))


from application.controller import home_controller

