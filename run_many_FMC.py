import os
import glob

def run_fmc(mtuq_file):
    aux = mtuq_file.split('_')
    name_out = 'best_{}_{}.png'.format(aux[1],aux[2].split('.dat')[0])
    line = '-p \'{}\' {} -pc fclvd'.format(name_out,mtuq_file)
    run_FMC = 'python FMC.py {}'.format(line)
    print(run_FMC)
    os.system(run_FMC)

list_mtuq = glob.glob('mtuq_*')
for file in list_mtuq:
    run_fmc(file)


