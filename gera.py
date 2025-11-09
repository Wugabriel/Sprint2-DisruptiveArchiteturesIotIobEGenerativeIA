import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

VEICULOS = [
    'Chevrolet Onix', 'Fiat Strada', 'Hyundai HB20', 'Volkswagen Gol', 'Fiat Palio',
    'Volkswagen Polo', 'Chevrolet Tracker', 'Volkswagen T-Cross', 'Jeep Renegade', 'Ford Ka',
    'Renault Kwid', 'Fiat Argo', 'Hyundai Creta', 'Nissan Kicks', 'Toyota Corolla',
    'Honda Civic', 'Chevrolet Celta', 'Fiat Uno', 'Volkswagen Saveiro', 'Jeep Compass',
    'Toyota Hilux', 'Ford Fiesta', 'Honda HR-V', 'Renault Sandero', 'Volkswagen Jetta',
    'Chevrolet Cruze', 'Fiat Toro', 'Duster', 'Mitsubishi L200', 'Caoa Chery Tiggo 5X',
    'Peugeot 208', 'Citroën C3', 'Audi A3', 'BMW 320i', 'Mercedes-Benz C180', 'Tesla Model 3'
]

CORES = [
    'Preto', 'Branco', 'Prata', 'Vermelho', 'Azul', 'Cinza'
]

STATUS_LIST = [
    'Concluída', 
    'Em Andamento',
    'Aguardando Peças',
    'Aguardando Aprovação',
    'Cancelada', 
    'Orçamento Pendente',
    'Em Teste',
    'Pronto para Retirada'
]

DESCRICOES = [
    'Revisão de 10.000 KM, troca de óleo, filtros de ar e alinhamento.',
    'Troca de pastilhas de freio dianteiras e traseiras, discos e fluído.',
    'Diagnóstico elétrico, reparo no alternador e substituição da bateria.',
    'Revisão de 30.000 KM, balanceamento, rodízio de pneus e geometria.',
    'Funilaria e pintura do para-choque dianteiro e porta do motorista.',
    'Limpeza de bicos injetores, troca de velas e cabos.',
    'Substituição da correia dentada e tensor.',
    'Reparo no sistema de arrefecimento: troca de mangueiras e aditivo.',
    'Troca do amortecedor e kit batente dianteiro.',
    'Revisão de caixa de câmbio manual e troca de óleo lubrificante.',
    'Instalação de sensor de estacionamento traseiro.',
    'Higienização do sistema de ar-condicionado e substituição do filtro de cabine.',
    'Verificação e reparo de vazamento de óleo no cárter.',
    'Troca de embreagem e volante do motor.',
    'Substituição da bomba de combustível e filtro de linha.',
    'Diagnóstico e reparo na suspensão traseira (molas e coxins).',
    'Reparo no sistema de ignição (bobina e velas).',
    'Alinhamento a laser e cambagem.',
    'Instalação de engate e parte elétrica.',
    'Troca de pneus e válvulas.',
    'Manutenção do sistema de freio ABS.',
    'Reparo de vidros elétricos: troca do motor e máquina.',
    'Reparo no escapamento e substituição do catalisador.',
    'Revisão de nível de fluídos e calibragem de pneus.',
    'Remoção de amassado sem pintura (PDR) no capô.',
    'Substituição do líquido de arrefecimento e limpeza do radiador.',
    'Diagnóstico de ruído na direção hidráulica e troca de fluido.',
    'Reparo em módulo de injeção eletrônica.'
]

OBSERVACOES = [
    'Próxima revisão em 6 meses ou 10.000 KM.',
    'Cliente aguarda a cotação da peça X antes de autorizar o serviço.',
    'Necessário trocar pneu traseiro direito urgentemente.',
    'Foi identificada folga na suspensão dianteira que deve ser orçada à parte.',
    'Serviço urgente solicitado pelo cliente devido a viagem.',
    'Veículo liberado após teste de rodagem sem ruídos.',
    'Garantia de 90 dias para a parte elétrica.',
    'Peças originais utilizadas conforme solicitação do proprietário.',
    'Revisão de cortesia devido a problemas recorrentes.',
    'Troca do fluido de freio é recomendada na próxima manutenção.',
    'O valor não inclui o serviço de funilaria que será tratado separadamente.',
    'Odor estranho no ar-condicionado resolvido com a higienização.',
    'Verificar o estado da bateria na próxima revisão.',
    'Data de entrega antecipada a pedido do cliente.',
    'Utilizado óleo sintético 5W30.',
    'Alinhamento e balanceamento realizados com sucesso.',
    'Carro necessita de polimento geral.',
    'Motor com pequeno vazamento, monitorar.',
    'Cliente autorizou apenas os itens essenciais da lista.',
    'Orçamento não aprovado. Apenas diagnóstico realizado.',
    'Aguardando a chegada da peça importada (previsão 5 dias úteis).',
    'Necessário troca das palhetas do limpador de para-brisa.',
    'Não foi possível testar o veículo com carga total.',
    'Recomendamos a troca do filtro de combustível.',
    'Cliente solicitou a devolução das peças antigas.',
    'Veículo com quilometragem alta, atentar aos fluídos.',
    'Limpeza interna básica inclusa no pacote de revisão.',
    'Problema intermitente na luz do painel resolvido.',
    'Realizar check-up completo em 1 ano.',
    'Valor do serviço sujeito a alteração caso o câmbio precise ser aberto.',
    'O veículo foi lavado e aspirado após o serviço.',
    'Pequeno risco na lateral esquerda notado na entrada.',
    'Combustível no tanque abaixo da reserva.',
    'Carro de locadora. Seguir rigorosamente o manual.',
    'Check-list de 50 itens realizado e anexo.',
    'Retorno agendado para 30 dias para checagem do reparo.',
    'Pendente troca do escapamento, cliente não autorizou no momento.',
    'Serviço complexo, tempo de espera pode ser estendido.',
    'Apenas a lavagem completa foi autorizada neste momento.'
]

def gerar_placa():
    letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    digito1 = random.randint(0, 9)
    letra_meio = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digitos2 = random.randint(10, 99)
    return f'{letras}{digito1}{letra_meio}{digitos2}'

NUM_OS = 200

data_inicio_simulacao = datetime.now() - timedelta(days=60)
data_fim_simulacao = datetime.now()

data = []
for i in range(1, NUM_OS + 1):
    os_id = i
    status = random.choice(STATUS_LIST)
    veiculo = random.choice(VEICULOS)
    placa = gerar_placa()
    cor = random.choice(CORES)
    descricao = random.choice(DESCRICOES)
    observacoes = random.choice(OBSERVACOES)

    if status in ['Cancelada', 'Orçamento Pendente']:
        valor_total = 0.00
    else:
        valor_total = round(random.uniform(300.00, 3500.00), 2)

    dias_abertura = random.randint(0, (data_fim_simulacao - data_inicio_simulacao).days)
    data_abertura_obj = data_inicio_simulacao + timedelta(days=dias_abertura)
    data_abertura = data_abertura_obj.strftime('%d/%m/%Y')

    data_fechamento = ''
    if status in ['Concluída', 'Cancelada', 'Pronto para Retirada']:
        dias_para_fechar = random.randint(0, 15)
        data_fechamento_obj = data_abertura_obj + timedelta(days=dias_para_fechar)
        if data_fechamento_obj <= datetime.now():
             data_fechamento = data_fechamento_obj.strftime('%d/%m/%Y')
        else:
            data_fechamento = data_abertura

    data.append({
        'ID_OS': os_id,
        'STATUS': status,
        'VEICULO': veiculo,
        'PLACA': placa,
        'COR': cor,
        'DESCRICAO_SERVICO': descricao,
        'VALOR_TOTAL': valor_total,
        'DATA_ABERTURA': data_abertura,
        'DATA_FECHAMENTO': data_fechamento, 
        'OBSERVACOES': observacoes
    })

df = pd.DataFrame(data)
csv_filename = 'os_gera.csv'
df.to_csv(csv_filename, index=False, sep=';', encoding='utf-8')

print(f'CSV gerado com sucesso: {csv_filename}')