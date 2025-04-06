def desconto_racional(nominal,taxa,tempo):
    return (nominal*taxa*tempo)/(1+taxa*tempo)
def valor_descontado(nominal,taxa,tempo):
    return (nominal) / (1 + taxa * tempo)

def desconto_racional_sem_nominal(vdr,tempo,taxa):
    print(vdr*tempo*taxa)
    return vdr*tempo*taxa

def desconto_racional_sem_taxa(nominal,tempo,desconto):
    vdr = nominal-desconto
    print(round(desconto/(vdr*tempo),4))

def descotos(nominal,taxa,tempo):
    desconto = round((nominal*taxa*tempo)/(1+taxa*tempo),2)
    valor_desc = round((nominal) / (1 + taxa * tempo),2)
    print(f'desconto racional {desconto}')
    print(f'valor recebido {valor_desc}')


descotos(750,0.03,8)
desconto_racional_sem_taxa(20000,3,1820)
desconto_racional_sem_nominal(750,8,0.03)
desconto_racional_sem_taxa(6000,2,1000)