"""
Este archivo contiene las propiedades del material tipo P
el cual corresponde a Silicio
"""

import numpy as np

N_a = 10 ** 16                           #Dopaje del aceptor
w_p = 100 * 10 ** -5                     #Espesor
Eg_p    =  1.12                          #Eg_Si_p
chi_p   =  4.05                          #chi_Si_p
eps_p  =  11.7                           #Perm_Si_p
Nc_p    =  2.8084567603096764e+19        #Nc_Si_p
Nv_p    =  1.8275252657588916e+19        #Nv_Si_p
D_n    =  30.541663218006832             #Dn_Si_p
tn_Si_p    =  6.62029197e-05             #tn_Si_p
L_n    =  0.044966068065331925           #Ln_Si_p
s_n     =  1000                          #S_Si_p
ni_p    =  8484351872.796736             #ni_Si_p
n_0 = 7198.422670142948                  #type p

Ref        =  0                          #Ref
Trans      =  1                          #Trans

alpha_2 = np.array([2.36000000e+06, 2.36378180e+06, 2.36678453e+06, 2.36896642e+06,2.37028572e+06, 2.37070066e+06, 2.37016946e+06, 2.36865036e+06,2.36610160e+06, 2.36248142e+06, 2.35774804e+06, 2.35185969e+06,2.34477462e+06, 2.33645106e+06, 2.32684724e+06, 2.31592140e+06,2.30363176e+06, 2.28993657e+06, 2.27479406e+06, 2.25816246e+06,2.24000000e+06, 2.22029480e+06, 2.19915451e+06, 2.17671663e+06,2.15311870e+06, 2.12849822e+06, 2.10299273e+06, 2.07673974e+06,2.04987676e+06, 2.02254133e+06, 1.99487096e+06, 1.96700317e+06,1.93907548e+06, 1.91122541e+06, 1.88359048e+06, 1.85630821e+06,1.82951613e+06, 1.80335174e+06, 1.77795258e+06, 1.75345616e+06,1.73000000e+06, 1.70769023e+06, 1.68650743e+06, 1.66640079e+06,1.64731948e+06, 1.62921270e+06, 1.61202962e+06, 1.59571944e+06,1.58023134e+06, 1.56551451e+06, 1.55151813e+06, 1.53819139e+06,1.52548347e+06, 1.51334356e+06, 1.50172084e+06, 1.49056450e+06,
       1.47982373e+06, 1.46944771e+06, 1.45938562e+06, 1.44958666e+06,1.44000000e+06, 1.43058301e+06, 1.42132575e+06, 1.41222646e+06,1.40328338e+06, 1.39449474e+06, 1.38585878e+06, 1.37737374e+06,1.36903786e+06, 1.36084937e+06, 1.35280651e+06, 1.34490753e+06,1.33715065e+06, 1.32953411e+06, 1.32205616e+06, 1.31471503e+06,1.30750896e+06, 1.30043618e+06, 1.29349494e+06, 1.28668346e+06,1.28000000e+06, 1.27344272e+06, 1.26700955e+06, 1.26069836e+06,1.25450700e+06, 1.24843334e+06, 1.24247525e+06, 1.23663059e+06,1.23089722e+06, 1.22527301e+06, 1.21975582e+06, 1.21434351e+06,1.20903395e+06, 1.20382500e+06, 1.19871452e+06, 1.19370038e+06,1.18878045e+06, 1.18395258e+06, 1.17921464e+06, 1.17456449e+06,1.17000000e+06, 1.16551860e+06, 1.16111604e+06, 1.15678761e+06,1.15252862e+06, 1.14833438e+06, 1.14420020e+06, 1.14012139e+06,
       1.13609325e+06, 1.13211109e+06, 1.12817022e+06, 1.12426594e+06,1.12039357e+06, 1.11654841e+06, 1.11272576e+06, 1.10892094e+06,1.10512926e+06, 1.10134601e+06, 1.09756652e+06, 1.09378608e+06,1.09000000e+06, 1.08620786e+06, 1.08242630e+06, 1.07867622e+06,1.07497853e+06, 1.07135413e+06, 1.06782394e+06, 1.06440885e+06,1.06112978e+06, 1.05800764e+06, 1.05506332e+06, 1.05231773e+06,1.04979178e+06, 1.04750638e+06, 1.04548243e+06, 1.04374084e+06,1.04230252e+06, 1.04118837e+06, 1.04041929e+06, 1.04001620e+06,1.04000000e+06, 1.04037496e+06, 1.04107878e+06, 1.04203253e+06,1.04315728e+06, 1.04437410e+06, 1.04560405e+06, 1.04676820e+06,
       1.04778761e+06, 1.04858337e+06, 1.04907652e+06, 1.04918815e+06,1.04883931e+06, 1.04795107e+06, 1.04644451e+06, 1.04424069e+06,1.04126067e+06, 1.03742552e+06, 1.03265632e+06, 1.02687412e+06,1.02000000e+06, 1.01197569e+06, 1.00282559e+06, 9.92594791e+05,9.81328355e+05, 9.69071358e+05, 9.55868877e+05, 9.41765986e+05,9.26807760e+05, 9.11039272e+05, 8.94505597e+05, 8.77251811e+05,8.59322987e+05, 8.40764201e+05, 8.21620526e+05, 8.01937037e+05,7.81758810e+05, 7.61130918e+05, 7.40098436e+05, 7.18706438e+05,6.97000000e+05, 6.75027539e+05, 6.52850846e+05, 6.30535055e+05,6.08145302e+05, 5.85746720e+05, 5.63404444e+05, 5.41183609e+05,5.19149348e+05, 4.97366797e+05, 4.75901089e+05, 4.54817360e+05,4.34180743e+05, 4.14056374e+05, 3.94509386e+05, 3.75604914e+05,3.57408092e+05, 3.39984056e+05, 3.23397939e+05, 3.07714875e+05,2.93000000e+05, 2.79299406e+05, 2.66583023e+05, 2.54801738e+05,2.43906438e+05, 2.33848012e+05, 2.24577346e+05, 2.16045329e+05,2.08202849e+05, 2.01000792e+05, 1.94390046e+05, 1.88321500e+05,
       1.82746040e+05, 1.77614554e+05, 1.72877931e+05, 1.68487057e+05,1.64392821e+05, 1.60546109e+05, 1.56897810e+05, 1.53398811e+05,1.50000000e+05, 1.46660736e+05, 1.43374262e+05, 1.40142293e+05,1.36966545e+05, 1.33848733e+05, 1.30790571e+05, 1.27793774e+05,1.24860058e+05, 1.21991137e+05, 1.19188727e+05, 1.16454542e+05,1.13790298e+05, 1.11197709e+05, 1.08678490e+05, 1.06234358e+05,1.03867025e+05, 1.01578208e+05, 9.93696216e+04, 9.72429806e+04,9.52000000e+04, 9.13647301e+04, 8.78417810e+04, 8.46019715e+04,8.16161205e+04, 7.88550468e+04, 7.62895695e+04, 7.38905072e+04,7.16286790e+04, 6.94749036e+04, 6.74000000e+04, 6.53802179e+04,6.34135310e+04, 6.15033436e+04, 5.96530604e+04, 5.78660859e+04,5.61458244e+04, 5.44956806e+04, 5.29190589e+04, 5.14193639e+04,5.00000000e+04, 4.86625982e+04, 4.74016952e+04, 4.62100540e+04,4.50804378e+04, 4.40056097e+04, 4.29783329e+04, 4.19913704e+04,4.10374853e+04, 4.01094408e+04, 3.92000000e+04, 3.83034893e+04,3.74204884e+04, 3.65531404e+04, 3.57035883e+04, 3.48739752e+04,3.40664440e+04, 3.32831379e+04, 3.25261998e+04, 3.17977728e+04,
       3.11000000e+04, 3.04342446e+04, 2.97987512e+04, 2.91909843e+04,2.86084089e+04, 2.80484895e+04, 2.75086910e+04, 2.69864781e+04,2.64793154e+04, 2.59846678e+04, 2.55000000e+04, 2.50231322e+04,2.45533070e+04, 2.40901223e+04, 2.36331762e+04, 2.31820667e+04,2.27363919e+04, 2.22957498e+04, 2.18597385e+04, 2.14279558e+04,2.10000000e+04, 2.05758265e+04, 2.01568210e+04, 1.97447265e+04,1.93412864e+04, 1.89482435e+04, 1.85673412e+04, 1.82003226e+04,1.78489308e+04, 1.75149088e+04, 1.72000000e+04, 1.69052618e+04,1.66290091e+04, 1.63688715e+04, 1.61224784e+04, 1.58874591e+04,1.56614431e+04, 1.54420598e+04, 1.52269385e+04, 1.50137088e+04,1.48000000e+04, 1.45840265e+04, 1.43663425e+04, 1.41480873e+04,1.39304001e+04, 1.37144200e+04, 1.35012864e+04, 1.32921383e+04,1.30881151e+04, 1.28903559e+04, 1.27000000e+04, 1.25178323e+04,1.23432208e+04, 1.21751792e+04, 1.20127213e+04, 1.18548608e+04,1.17006114e+04, 1.15489869e+04, 1.13990011e+04, 1.12496675e+04,
       1.11000000e+04, 1.09493443e+04, 1.07983743e+04, 1.06480958e+04,1.04995147e+04, 1.03536367e+04, 1.02114679e+04, 1.00740139e+04,9.94228069e+03, 9.81727411e+03, 9.70000000e+03, 9.59109038e+03,9.48968193e+03, 9.39453753e+03, 9.30442002e+03, 9.21809228e+03,9.13431715e+03, 9.05185750e+03, 8.96947618e+03, 8.88593606e+03,8.80000000e+03, 8.71074416e+03, 8.61849795e+03, 8.52390407e+03,8.42760524e+03, 8.33024416e+03, 8.23246355e+03, 8.13490612e+03,8.03821458e+03, 7.94303164e+03, 7.85000000e+03, 7.75963298e+03,7.67192628e+03, 7.58674620e+03, 7.50395903e+03, 7.42343108e+03,7.34502864e+03, 7.26861801e+03, 7.19406550e+03, 7.12123739e+03,7.05000000e+03, 6.98021391e+03, 6.91171693e+03, 6.84434114e+03,6.77791864e+03, 6.71228153e+03, 6.64726189e+03, 6.58269183e+03,6.51840343e+03, 6.45422879e+03, 6.39000000e+03, 6.32562137e+03,6.26128600e+03, 6.19725924e+03, 6.13380640e+03, 6.07119281e+03,6.00968379e+03, 5.94954468e+03, 5.89104079e+03, 5.83443746e+03,5.78000000e+03, 5.72790063e+03, 5.67793906e+03, 5.62982190e+03,5.58325576e+03, 5.53794724e+03, 5.49360294e+03, 5.44992946e+03,
       5.40663341e+03, 5.36342139e+03, 5.32000000e+03, 5.27614613e+03,5.23191776e+03, 5.18744314e+03, 5.14285055e+03, 5.09826823e+03,5.05382446e+03, 5.00964749e+03, 4.96586559e+03, 4.92260700e+03,4.88000000e+03, 4.83814486e+03, 4.79702992e+03, 4.75661553e+03,4.71686204e+03, 4.67772982e+03, 4.63917921e+03, 4.60117057e+03,4.56366425e+03, 4.52662061e+03, 4.49000000e+03, 4.45376443e+03,4.41788258e+03, 4.38232475e+03, 4.34706128e+03, 4.31206248e+03,4.27729869e+03, 4.24274022e+03, 4.20835740e+03, 4.17412055e+03,4.14000000e+03, 4.10597740e+03, 4.07207978e+03, 4.03834548e+03,4.00481285e+03, 3.97152025e+03, 3.93850603e+03, 3.90580855e+03,3.87346614e+03, 3.84151718e+03, 3.81000000e+03, 3.77894595e+03,3.74835831e+03, 3.71823334e+03, 3.68856732e+03, 3.65935651e+03,3.63059718e+03, 3.60228559e+03, 3.57441802e+03, 3.54699074e+03,3.52000000e+03, 3.49343880e+03, 3.46728699e+03, 3.44152116e+03,
       3.41611787e+03, 3.39105371e+03, 3.36630525e+03, 3.34184908e+03,3.31766176e+03, 3.29371987e+03, 3.27000000e+03, 3.24647886e+03,3.22313373e+03, 3.19994203e+03, 3.17688120e+03, 3.15392865e+03,3.13106181e+03, 3.10825810e+03, 3.08549494e+03, 3.06274977e+03,3.04000000e+03, 3.01722577e+03, 2.99441810e+03, 2.97157071e+03,2.94867734e+03, 2.92573169e+03, 2.90272752e+03, 2.87965853e+03,2.85651846e+03, 2.83330104e+03, 2.81000000e+03, 2.78661805e+03,2.76319386e+03, 2.73977511e+03, 2.71640946e+03, 2.69314458e+03,2.67002813e+03, 2.64710778e+03, 2.62443120e+03, 2.60204605e+03,2.58000000e+03, 2.55833204e+03, 2.53704645e+03, 2.51613884e+03,2.49560482e+03, 2.47543999e+03, 2.45563997e+03, 2.43620035e+03,2.41711674e+03, 2.39838476e+03, 2.38000000e+03, 2.36195380e+03,2.34422033e+03, 2.32676952e+03, 2.30957125e+03, 2.29259545e+03,2.27581201e+03, 2.25919084e+03, 2.24270184e+03, 2.22631493e+03,2.21000000e+03, 2.19373278e+03, 2.17751222e+03, 2.16134309e+03,2.14523016e+03, 2.12917821e+03, 2.11319200e+03, 2.09727631e+03,2.08143589e+03, 2.06567554e+03, 2.05000000e+03, 2.03441510e+03,
       2.01893080e+03, 2.00355813e+03, 1.98830809e+03, 1.97319171e+03,1.95821998e+03, 1.94340393e+03, 1.92875458e+03, 1.91428293e+03,1.90000000e+03, 1.88591683e+03, 1.87204457e+03, 1.85839439e+03,1.84497746e+03, 1.83180496e+03, 1.81888807e+03, 1.80623795e+03,1.79386579e+03, 1.78178274e+03, 1.77000000e+03, 1.75851758e+03,1.74729092e+03, 1.73626432e+03, 1.72538206e+03, 1.71458844e+03,1.70382774e+03, 1.69304425e+03, 1.68218227e+03, 1.67118609e+03,1.66000000e+03, 1.64858285e+03, 1.63695174e+03, 1.62513833e+03,1.61317430e+03, 1.60109129e+03, 1.58892099e+03, 1.57669504e+03,1.56444512e+03, 1.55220288e+03, 1.54000000e+03, 1.52786103e+03,1.51578213e+03, 1.50375235e+03, 1.49176075e+03, 1.47979639e+03,1.46784832e+03, 1.45590558e+03, 1.44395725e+03, 1.43199237e+03,1.42000000e+03, 1.40797304e+03, 1.39591975e+03, 1.38385226e+03,1.37178269e+03, 1.35972315e+03, 1.34768575e+03, 1.33568262e+03,1.32372588e+03, 1.31182763e+03, 1.30000000e+03, 1.28825683e+03,1.27661887e+03, 1.26510860e+03, 1.25374849e+03, 1.24256103e+03,1.23156868e+03, 1.22079392e+03, 1.21025924e+03, 1.19998711e+03,1.19000000e+03, 1.18030964e+03, 1.17088477e+03, 1.16168334e+03,
       1.15266334e+03, 1.14378275e+03, 1.13499954e+03, 1.12627168e+03,1.11755716e+03, 1.10881394e+03, 1.10000000e+03, 1.09108459e+03,1.08208207e+03, 1.07301804e+03, 1.06391813e+03, 1.05480797e+03,1.04571317e+03, 1.03665935e+03, 1.02767213e+03, 1.01877714e+03,1.01000000e+03, 1.00135998e+03, 9.92850963e+02, 9.84460497e+02,9.76176120e+02, 9.67985373e+02, 9.59875796e+02, 9.51834930e+02,9.43850314e+02, 9.35909491e+02, 9.28000000e+02, 9.20111495e+02,9.12242079e+02, 9.04391970e+02, 8.96561384e+02, 8.88750539e+02,8.80959650e+02, 8.73188935e+02, 8.65438610e+02, 8.57708893e+02,8.50000000e+02, 8.42313044e+02, 8.34652720e+02, 8.27024623e+02,8.19434343e+02, 8.11887472e+02, 8.04389604e+02, 7.96946331e+02,7.89563244e+02, 7.82245936e+02, 7.75000000e+02, 7.67830331e+02,7.60739039e+02, 7.53727539e+02, 7.46797246e+02, 7.39949572e+02,7.33185932e+02, 7.26507741e+02, 7.19916413e+02, 7.13413361e+02,7.07000000e+02, 7.00676633e+02, 6.94439123e+02, 6.88282220e+02,6.82200675e+02, 6.76189240e+02, 6.70242666e+02, 6.64355703e+02,6.58523104e+02, 6.52739619e+02, 6.47000000e+02, 6.41299136e+02,6.35632469e+02, 6.29995581e+02, 6.24384054e+02, 6.18793468e+02,6.13219404e+02, 6.07657445e+02, 6.02103170e+02, 5.96552161e+02,5.91000000e+02, 5.85442824e+02, 5.79879001e+02, 5.74307455e+02,5.68727109e+02, 5.63136889e+02, 5.57535717e+02, 5.51922518e+02,
       5.46296216e+02, 5.40655735e+02, 5.35000000e+02, 5.29330567e+02,5.23659526e+02, 5.18001598e+02, 5.12371508e+02, 5.06783977e+02,5.01253728e+02, 4.95795483e+02, 4.90423965e+02, 4.85153897e+02,4.80000000e+02, 4.74970908e+02, 4.70050897e+02, 4.65218151e+02,4.60450858e+02, 4.55727202e+02, 4.51025371e+02, 4.46323549e+02,4.41599922e+02, 4.36832677e+02, 4.32000000e+02, 4.27087801e+02,4.22112888e+02, 4.17099797e+02, 4.12073061e+02, 4.07057214e+02,4.02076790e+02, 3.97156322e+02, 3.92320346e+02, 3.87593394e+02,3.83000000e+02, 3.78557890e+02, 3.74257550e+02, 3.70082660e+02,3.66016898e+02, 3.62043942e+02, 3.58147471e+02, 3.54311162e+02,3.50518695e+02, 3.46753748e+02, 3.43000000e+02, 3.39244641e+02,3.35488910e+02, 3.31737562e+02, 3.27995347e+02, 3.24267018e+02,3.20557328e+02, 3.16871029e+02, 3.13212873e+02, 3.09587613e+02,3.06000000e+02, 3.02453548e+02, 2.98946808e+02, 2.95477093e+02,2.92041714e+02, 2.88637985e+02, 2.85263217e+02, 2.81914722e+02,2.78589813e+02, 2.75285801e+02, 2.72000000e+02, 2.68730169e+02,2.65475858e+02, 2.62237068e+02, 2.59013797e+02, 2.55806043e+02,2.52613806e+02, 2.49437084e+02, 2.46275877e+02, 2.43130182e+02,
       2.40000000e+02, 2.36885778e+02, 2.33789758e+02, 2.30714635e+02,2.27663099e+02, 2.24637844e+02, 2.21641561e+02, 2.18676942e+02,2.15746681e+02, 2.12853470e+02, 2.10000000e+02, 2.07187721e+02,2.04413108e+02, 2.01671393e+02, 1.98957807e+02, 1.96267583e+02,1.93595952e+02, 1.90938147e+02, 1.88289398e+02, 1.85644939e+02,1.83000000e+02, 1.80351339e+02, 1.77701810e+02, 1.75055795e+02,1.72417673e+02, 1.69791825e+02, 1.67182631e+02, 1.64594471e+02,1.62031726e+02, 1.59498776e+02, 1.57000000e+02, 1.54538924e+02,1.52115651e+02, 1.49729427e+02, 1.47379500e+02, 1.45065116e+02,1.42785523e+02, 1.40539968e+02, 1.38327698e+02, 1.36147959e+02,1.34000000e+02, 1.31882964e+02, 1.29795586e+02, 1.27736497e+02,1.25704328e+02, 1.23697711e+02, 1.21715277e+02, 1.19755657e+02,1.17817484e+02, 1.15899387e+02, 1.14000000e+02, 1.12118119e+02,1.10253205e+02, 1.08404886e+02, 1.06572789e+02, 1.04756541e+02,1.02955771e+02, 1.01170104e+02, 9.93991681e+01, 9.76425911e+01,9.59000000e+01, 9.41710608e+01, 9.24555941e+01, 9.07534594e+01,8.90645161e+01, 8.73886235e+01, 8.57256410e+01, 8.40754280e+01,
       8.24378439e+01, 8.08127481e+01, 7.92000000e+01, 7.75997382e+01,7.60132186e+01, 7.44419764e+01, 7.28875467e+01, 7.13514647e+01,6.98352655e+01, 6.83404843e+01, 6.68686562e+01, 6.54213164e+01,6.40000000e+01, 6.26057864e+01, 6.12379313e+01, 5.98952349e+01,5.85764970e+01, 5.72805177e+01, 5.60060970e+01, 5.47520349e+01,5.35171313e+01, 5.23001864e+01, 5.11000000e+01, 4.99155163e+01,4.87462561e+01, 4.75918841e+01, 4.64520653e+01, 4.53264645e+01,4.42147465e+01, 4.31165762e+01, 4.20316185e+01, 4.09595381e+01,3.99000000e+01, 3.88529483e+01, 3.78194443e+01, 3.68008286e+01,3.57984417e+01, 3.48136243e+01, 3.38477170e+01, 3.29020603e+01,3.19779948e+01, 3.10768612e+01, 3.02000000e+01, 2.93482905e+01,2.85207668e+01, 2.77160016e+01, 2.69325679e+01, 2.61690382e+01,2.54239856e+01, 2.46959826e+01, 2.39836022e+01, 2.32854170e+01,2.26000000e+01, 2.19260898e+01, 2.12630886e+01, 2.06105649e+01,1.99680869e+01, 1.93352228e+01, 1.87115408e+01, 1.80966093e+01,1.74899965e+01, 1.68912706e+01, 1.63000000e+01, 1.57161505e+01,1.51412787e+01, 1.45773386e+01, 1.40262846e+01, 1.34900707e+01,1.29706512e+01, 1.24699802e+01, 1.19900119e+01, 1.15327004e+01,1.11000000e+01, 1.06933082e+01, 1.03117967e+01, 9.95408054e+00,
       9.61877470e+00, 9.30449427e+00, 9.00985429e+00, 8.73346982e+00,8.47395592e+00, 8.22992763e+00, 8.00000000e+00, 7.78281652e+00,7.57713438e+00, 7.38173919e+00, 7.19541659e+00, 7.01695219e+00,6.84513162e+00, 6.67874049e+00, 6.51656443e+00, 6.35738906e+00,6.20000000e+00, 6.04342568e+00, 5.88766575e+00, 5.73296268e+00,5.57955893e+00, 5.42769696e+00, 5.27761923e+00, 5.12956821e+00,4.98378636e+00, 4.84051613e+00, 4.70000000e+00, 4.56248076e+00,4.42820261e+00, 4.29741008e+00, 4.17034768e+00, 4.04725996e+00,3.92839144e+00, 3.81398666e+00, 3.70429013e+00, 3.59954641e+00,3.50000000e+00, 3.40575126e+00, 3.31632379e+00, 3.23109702e+00,3.14945035e+00, 3.07076320e+00, 2.99441500e+00, 2.91978516e+00])
