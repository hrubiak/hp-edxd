equations_of_state = {'jcpds4':{
                        'name': 'Legacy JCPDS4 style Birch Murnaghan 3-rd order <br>with temperature-dependent bulk modulus',
                        'reference':'',
                        'comment':'',
                        'params':{ 
                        'V_0':      {'symbol':u'V<sub>0</sub>',
                                     'desc':u'Volume at P=10⁵ Pa, T=300 K',
                                     'unit':u'Å³'}, 
                        'K_0':      {'symbol':u'K<sub>0</sub>',
                                     'desc':u'Isothermal bulk modulus at P=10⁵ Pa, T=300 K',
                                     'unit':u'GPa'}, 
                        'Kprime_0': {'symbol':u"K'<sub>0</sub>",
                                     'desc':u'Pressure derivative of K<sub>0</sub>',
                                     'unit':u''}, 
                        'dk0dt': {'symbol':u'dK<sub>0</sub>/dT',
                                     'desc':u'Temperature derivative of K<sub>0</sub>',
                                     'unit':u'GPa/K'}, 
                        'dk0pdt': {'symbol':u"dK'<sub>0</sub>/dT",
                                     'desc':u"Temperature derivative of K'<sub>0</sub>",
                                     'unit':u'1/K'},
                        'alpha_t0': {'symbol':u'α<sub>T</sub>',
                                     'desc':u'Thermal expansion coefficient',
                                     'unit':u'1/K'}, 
                        'd_alpha_dt': {'symbol':u'dα<sub>T</sub>/dT',
                                     'desc':u'Temperature derivative of the thermal expansion coefficient',
                                     'unit':u'1/K²'}
                        }},

                    'bm3':{
                        'name': 'Isothermal Birch Murnaghan 3-rd order',
                        'reference':'',
                        'comment':'',
                        'params':{ 
                        
                        'V_0':      {'symbol':u'V<sub>0</sub>',
                                     'desc':u'Volume at P=10⁵ Pa, T=300 K',
                                     'unit':u'm³/mol'}, 
                        'K_0':      {'symbol':u'K<sub>0</sub>',
                                     'desc':u'Isothermal bulk modulus at P=10⁵ Pa, T=300 K',
                                     'unit':u'Pa'}, 
                        'Kprime_0': {'symbol':u"K'<sub>0</sub>",
                                     'desc':u'Pressure derivative of K<sub>0</sub>',
                                     'unit':u''}
                        }},
                    'slb2':{
                        'name': 'Stixrude Lithgow-Bertelloni 2-nd order',
                        'reference':'L. Stixrude and C. Lithgow-Bertelloni, Thermodynamics of <br> \
                                     mantle minerals – I. Physical properties. <br> \
                                     Geophys. J. Int. (2005) 162, 610–632',
                        'comment':'',
                        'params':{ 
                        
                        'V_0':      {'symbol':u'V<sub>0</sub>',
                                     'desc':u'Volume at P=10⁵ Pa, T=300 K',
                                     'unit':u'm³/mol'}, 
                        'K_0':      {'symbol':u'K<sub>0</sub>',
                                     'desc':u'Isothermal bulk modulus at P=10⁵ Pa, T=300 K',
                                     'unit':u'Pa'}, 
                        'Kprime_0': {'symbol':u"K'<sub>0</sub>",
                                     'desc':u'Pressure derivative of K<sub>0</sub>',
                                     'unit':u''}, 
                        'G_0':      {'symbol':u'G<sub>0</sub>',
                                     'desc':u'Shear modulus at P=10⁵ Pa, T=300 K',
                                     'unit':u'Pa'}, 
                        'Gprime_0': {'symbol':u"G'<sub>0</sub>",
                                     'desc':u'Pressure derivative of G<sub>0</sub>',
                                     'unit':u''}, 
                        'molar_mass': {'symbol':u'μ',
                                     'desc':u'Mass per mole formula unit',
                                     'unit':u'Kg/mol',
                                     'default':0.05}, 
                        'n':        {'symbol':u'n',
                                     'desc':u'Number of atoms per formula unit',
                                     'unit':u'',
                                     'default':1}, 
                        'Debye_0':  {'symbol':u'θ<sub>0</sub>',
                                     'desc':u'Debye Temperature',
                                     'unit':u'K',
                                     'default':300}, 
                        'grueneisen_0': {'symbol':u'γ<sub>0</sub>',
                                     'desc':u'Gruneisen parameter at P=10⁵ Pa, T=300 K',
                                     'unit':u'',
                                     'default':1}, 
                        'q_0':      {'symbol':u'q<sub>0</sub>',
                                     'desc':u'Logarithmic volume derivative of the Gr€uneisen parameter',
                                     'unit':u'',
                                     'default':1}, 
                        'eta_s_0':  {'symbol':u'η<sub>S</sub><sub>0</sub>',
                                     'desc':u'Shear strain derivative of the Gruneisen parameter',
                                     'unit':u''}
                        }},
                    
                    }