usuarios = {
    '1982': {
        'nome':'Nicolas Leandro',
        'Senha':'kaalanie123',
        'saldo':'1000.0',
        'historico':[]}
        ,
    '2408':{
        'nome':'Kaalanie Porto',
        'senha':'1408',
        'saldo':'12000.0',
        'historico':[]},

    '2512':{
        'nome':'Margarida Deise',
        'senha':'0704',
        'saldo':'1200.0',
        'historico':[]}
}     

conta = input('DIGITE SUA CONTA: ')

if conta in usuarios:
    dados_usuario = usuarios[conta]
    print(f'Conta encontrada, Bem vindo! {dados_usuario}.')
else:
    print('Conta nao encontrada!')