# Esta funcao calcula o IMC de uma pessoa
# recebe como parametros o peso e a altura
def imc(peso, altura):
    calc_imc = float(peso) / (float(altura) * float(altura))
    string_to_return = ''
    if(calc_imc < 16.0):
        string_to_return = 'IMC = ' + str(calc_imc) + ' Magreza grave'
    if(calc_imc >= 16.0 and calc_imc < 17.0):
        string_to_return = 'IMC = ' + str(calc_imc) + ' Magreza moderada'
    if(calc_imc >= 17.0 and calc_imc < 18.5):
        string_to_return ='IMC = ' + str(calc_imc) + ' Magreza leve'
    if(calc_imc >= 18.5 and calc_imc < 25.0):
        string_to_return ='IMC = ' + str(calc_imc) + ' Saudável'
    if(calc_imc >= 25.0 and calc_imc < 30.0):
        string_to_return ='IMC = ' + str(calc_imc) + ' Sobrepeso'      
    if(calc_imc >= 30.0 and calc_imc < 35.0):
        string_to_return ='IMC = ' + str(calc_imc) + ' Obesidade grau 1'          
    if(calc_imc >= 35.0 and calc_imc < 40.0):
        string_to_return = 'IMC = ' + str(calc_imc) + ' Obesidade grau 2'          
    if(calc_imc >= 40.0):
        string_to_return = 'IMC = ' + str(calc_imc) + ' Obesidade mórbida'
    return string_to_return

# Esta funcao recebe como parametros o dia e mes de nascimento
# e retorna o signo 
# entrada dia: 0..31, mes: 0..12
def signo(dia, mes):
    JANEIRO   = 1
    FEVEREIRO = 2
    MARCO     = 3
    ABRIL     = 4
    MAIO      = 5
    JUNHO     = 6
    JULHO     = 7
    AGOSTO    = 8
    SETEMBRO  = 9
    OUTUBRO   = 10
    NOVEMBRO  = 11
    DEZEMBRO  = 12
    if(dia >= 21 and mes == MARCO) or (dia <= 20 and mes == ABRIL):
        return('Áries') 
    elif(dia >= 21 and mes == ABRIL) or (dia <= 20 and mes == MAIO):
        return('Touro') 
    elif(dia >= 21 and mes == MAIO) or (dia <= 21 and mes == JUNHO):
        return('Gêmeos')
    elif(dia >= 21 and mes == JUNHO) or (dia <= 21 and mes == JULHO):
        return('Câncer')
    elif(dia >= 22 and mes == JULHO) or (dia <= 22 and mes == AGOSTO):
        return('Leão') 
    elif(dia >= 23 and mes == AGOSTO) or (dia <= 22 and mes == SETEMBRO):
        return('Virgem')
    elif(dia >= 23 and mes == SETEMBRO) or (dia <= 22 and mes == OUTUBRO):
        return('Libra') 
    elif(dia >= 23 and mes == OUTUBRO) or (dia <= 21 and mes == NOVEMBRO):
        return('Escorpião') 
    elif(dia >= 22 and mes == NOVEMBRO) or (dia <= 21 and mes == DEZEMBRO):
        return('Sagitário')
    elif(dia >= 22 and mes == DEZEMBRO) or (dia <= 20 and mes == JANEIRO):
        return('Capricórnio')
    elif(dia >= 21 and mes == JANEIRO) or (dia <= 19 and mes == FEVEREIRO):
        return('Aquário')
    elif(dia >= 20 and mes == FEVEREIRO) or (dia <= 20 and mes == MARCO):
        return('Peixes')

# Funcao para validar cpf baseada no documento encontrado no seguinte end
# http://gurudoexcel.com/como-e-feito-o-calculo-de-validacao-cpf/
# entrada numero de 11 digitos
def valida_cpf(cpf):    
    str_cpf  = str(cpf)
    digito_1 = int(str_cpf[9])  # primeiro digito verificador
    digito_2 = int(str_cpf[10]) # segundo digito verificador
    acumulador_d1 = 0
    acumulador_d2 = 0
    calculo_digito1 = 0
    calculo_digito2 = 0
    for i in range(0, 9):
        acumulador_d1 += (int(str_cpf[i]) * (10 -i))        
    calculo_digito1 = 11 - (acumulador_d1 % 11)
    
    if (calculo_digito1 == digito_1) or (calculo_digito1 > 9 and digito_1 == 0):
        print('Primeiro digito correto ', digito_1)  
        for i in range(0, 10):
            acumulador_d2 += (int(str_cpf[i]) * (11 -i))  
        calculo_digito2 = 11 - (acumulador_d2 % 11)
        if(calculo_digito2 == digito_2):
            print('Segundo digito correto ', digito_2)
            print('CPF válido! ')  
        else:  
            print('CPF inválido ', calculo_digito2)   
    else:
        print('CPF inválido ', calculo_digito1) 

# Funcao de validacao de cpf baseada em um pseudo código da wikipedia
# https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_f%C3%ADsicas
# entrada: numero com 11 digitos
def valida_cpf_wikip(cpf):
    str_cpf  = str(cpf)             # transforma int em string
    str_cpf_inv = str_cpf[0:-2]     # extrai apenas os 9 primeiros digitos
    str_cpf_inv = str_cpf_inv[::-1] # inverte os valores    
    digito_v1 = 0 
    digito_v2 = 0
    for i in range(0, 9):
        digito_v1 = digito_v1 + int(str_cpf_inv[i]) * (9 - (i % 10))
        digito_v2 = digito_v2 + int(str_cpf_inv[i]) * (9 - ((i + 1) % 10))         
    digito_v1 = (digito_v1 % 11) % 10
    digito_v2 = digito_v2 + digito_v1 * 9
    digito_v2 = (digito_v2 % 11) % 10         
    if (int(str_cpf[9]) == digito_v1 and int(str_cpf[10]) == digito_v2):
        print('CPF válido')
    else: 
        print('CPF inválido')


