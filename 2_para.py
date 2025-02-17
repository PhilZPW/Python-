import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parameters = pd.read_table('2_para.txt')
para = parameters.values
#print(para)

fig, axs = plt.subplots(2,1)

name = np.arange(8)

#GRB1
alpha     = float(para[0,2].split(',')[0])
alpha_low = float(para[0,2].split(',')[1])
alpha_up  = float(para[0,2].split(',')[2])
beta      = float(para[0,3].split(',')[0])
beta_low  = float(para[0,3].split(',')[1])
beta_up   = float(para[0,3].split(',')[2])
E         = float(para[0,4].split(',')[0])
E_low     = float(para[0,4].split(',')[1])
E_up      = float(para[0,4].split(',')[2])
kT        = float(para[0,5].split(',')[0])
kT_low    = float(para[0,5].split(',')[1])
kT_up     = float(para[0,5].split(',')[2])
axs[0].errorbar(name[0], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0',label=r'$\alpha$')
axs[0].errorbar(name[0], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1',label=r'$\beta$')
axs[1].errorbar(name[0], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2',label='E' )
axs[1].semilogy(name[0], E)
axs[1].errorbar(name[0], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3',label='kT')
axs[1].semilogy(name[0], kT)

#GRB2
alpha     = float(para[1,2].split(',')[0])
alpha_low = float(para[1,2].split(',')[1])
alpha_up  = float(para[1,2].split(',')[2])
#beta      = float(para[1,3].split(',')[0])
#beta_low  = float(para[1,3].split(',')[1])
#beta_up   = float(para[1,3].split(',')[2])
E         = float(para[1,4].split(',')[0])
E_low     = float(para[1,4].split(',')[1])
E_up      = float(para[1,4].split(',')[2])
kT        = float(para[1,5].split(',')[0])
kT_low    = float(para[1,5].split(',')[1])
kT_up     = float(para[1,5].split(',')[2])
axs[0].errorbar(name[1], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
#axs[0].errorbar(name[1], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[1], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[1], E)
axs[1].errorbar(name[1], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[1], kT)

#GRB3
alpha     = float(para[2,2].split(',')[0])
alpha_low = float(para[2,2].split(',')[1])
alpha_up  = float(para[2,2].split(',')[2])
beta      = float(para[2,3].split(',')[0])
beta_low  = float(para[2,3].split(',')[1])
beta_up   = float(para[2,3].split(',')[2])
E         = float(para[2,4].split(',')[0])
E_low     = float(para[2,4].split(',')[1])
E_up      = float(para[2,4].split(',')[2])
kT        = float(para[2,5].split(',')[0])
kT_low    = float(para[2,5].split(',')[1])
kT_up     = float(para[2,5].split(',')[2])
axs[0].errorbar(name[2], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
axs[0].errorbar(name[2], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[2], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[2], E)
axs[1].errorbar(name[2], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[2], kT)

#GRB4
alpha     = float(para[3,2].split(',')[0])
alpha_low = float(para[3,2].split(',')[1])
alpha_up  = float(para[3,2].split(',')[2])
#beta      = float(para[3,3].split(',')[0])
#beta_low  = float(para[3,3].split(',')[1])
#beta_up   = float(para[3,3].split(',')[2])
E         = float(para[3,4].split(',')[0])
E_low     = float(para[3,4].split(',')[1])
E_up      = float(para[3,4].split(',')[2])
kT        = float(para[3,5].split(',')[0])
kT_low    = float(para[3,5].split(',')[1])
kT_up     = float(para[3,5].split(',')[2])
axs[0].errorbar(name[3], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
#axs[0].errorbar(name[3], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[3], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[3], E)
axs[1].errorbar(name[3], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[3], kT)

#GRB5
alpha     = float(para[4,2].split(',')[0])
alpha_low = float(para[4,2].split(',')[1])
alpha_up  = float(para[4,2].split(',')[2])
#beta      = float(para[4,3].split(',')[0])
#beta_low  = float(para[4,3].split(',')[1])
#beta_up   = float(para[4,3].split(',')[2])
E         = float(para[4,4].split(',')[0])
E_low     = float(para[4,4].split(',')[1])
E_up      = float(para[4,4].split(',')[2])
kT        = float(para[4,5].split(',')[0])
kT_low    = float(para[4,5].split(',')[1])
kT_up     = float(para[4,5].split(',')[2])
axs[0].errorbar(name[4], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
#axs[0].errorbar(name[4], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[4], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[4], E)
axs[1].errorbar(name[4], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[4], kT)

#GRB6
alpha     = float(para[5,2].split(',')[0])
alpha_low = float(para[5,2].split(',')[1])
alpha_up  = float(para[5,2].split(',')[2])
beta      = float(para[5,3].split(',')[0])
beta_low  = float(para[5,3].split(',')[1])
beta_up   = float(para[5,3].split(',')[2])
E         = float(para[5,4].split(',')[0])
E_low     = float(para[5,4].split(',')[1])
E_up      = float(para[5,4].split(',')[2])
kT        = float(para[5,5].split(',')[0])
kT_low    = float(para[5,5].split(',')[1])
kT_up     = float(para[5,5].split(',')[2])
axs[0].errorbar(name[5], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
axs[0].errorbar(name[5], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[5], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[5], E)
axs[1].errorbar(name[5], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[5], kT)

#GRB7
alpha     = float(para[6,2].split(',')[0])
alpha_low = float(para[6,2].split(',')[1])
alpha_up  = float(para[6,2].split(',')[2])
#beta      = float(para[6,3].split(',')[0])
#beta_low  = float(para[6,3].split(',')[1])
#beta_up   = float(para[6,3].split(',')[2])
E         = float(para[6,4].split(',')[0])
E_low     = float(para[6,4].split(',')[1])
E_up      = float(para[6,4].split(',')[2])
kT        = float(para[6,5].split(',')[0])
kT_low    = float(para[6,5].split(',')[1])
kT_up     = float(para[6,5].split(',')[2])
axs[0].errorbar(name[6], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
#axs[0].errorbar(name[6], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[6], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[6], E)
axs[1].errorbar(name[6], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[6], kT)

#GRB8
alpha     = float(para[7,2].split(',')[0])
alpha_low = float(para[7,2].split(',')[1])
alpha_up  = float(para[7,2].split(',')[2])
#beta      = float(para[7,3].split(',')[0])
#beta_low  = float(para[7,3].split(',')[1])
#beta_up   = float(para[7,3].split(',')[2])
E         = float(para[7,4].split(',')[0])
E_low     = float(para[7,4].split(',')[1])
E_up      = float(para[7,4].split(',')[2])
kT        = float(para[7,5].split(',')[0])
kT_low    = float(para[7,5].split(',')[1])
kT_up     = float(para[7,5].split(',')[2])
axs[0].errorbar(name[7], alpha, yerr=[[alpha_low],[alpha_up]],marker = 'D', alpha=0.5, color='C0')
#axs[0].errorbar(name[7], beta,  yerr=[[beta_low], [beta_up]], marker = 'D', alpha=0.5, color='C1')
axs[1].errorbar(name[7], E,     yerr=[[E_low],    [E_up]],    marker = 'D', alpha=0.5, color='C2')
axs[1].semilogy(name[7], E)
axs[1].errorbar(name[7], kT,    yerr=[[kT_low],   [kT_up]],   marker = 'D', alpha=0.5, color='C3')
axs[1].semilogy(name[7], kT)

#axs[0].set_ylabel(fontsize=15)
#axs[1].set_ylabel(fontsize=15)

axs[0].set_xticks(name)
axs[0].set_xticklabels(('GRB1', 'GRB2', 'GRB3','GRB4','GRB5',\
                      'GRB6','GRB7','GRB8'))
axs[1].set_xticks(name)
axs[1].set_xticklabels(('GRB1', 'GRB2', 'GRB3','GRB4','GRB5',\
                      'GRB6','GRB7','GRB8'))

axs[0].set_xlim(-0.5,7.5)
axs[1].set_xlim(-0.5,7.5)
axs[0].set_ylim(-5,0.5)
axs[1].set_ylim(1e-1,1e3)

#axs[0].grid(True)
#axs[1].grid(True)

axs[0].legend()
axs[1].legend()


#这里分块，阴影
axs[0].axvspan(-0.5, 2.5, color='C9',alpha=0.2)
axs[0].axvspan(2.5, 4.5, color='C8',alpha=0.2)
axs[0].axvspan(4.5, 7.5, color='C7',alpha=0.2)
axs[1].axvspan(-0.5, 2.5, color='C9',alpha=0.2)
axs[1].axvspan(2.5, 4.5, color='C8',alpha=0.2)
axs[1].axvspan(4.5, 7.5, color='C7',alpha=0.2)

#给阴影加文字
axs[0].text(0.5, -4, 'Sample A')
axs[0].text(3, -4, 'Sample B')
axs[0].text(5.5, -4, 'Sample C')
axs[1].text(0.5, 1.5, 'Sample A')
axs[1].text(3, 1.5, 'Sample B')
axs[1].text(5.5,1.5, 'Sample C')

fig.tight_layout()
plt.show()



