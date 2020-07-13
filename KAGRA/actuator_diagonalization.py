from kontrol import visutils
import ezca
# from kontrol import fakeezca as ezca  # Non-workstation usage
optic = 'BS'
vis = visutils.Vis(optic, ezca)
stage = 'IP'
dofs = ['L', 'T', 'Y']
act_block = 'TEST'
act_suffix = 'OFFSET'
sense_block = 'DAMP'
sense_suffic = 'INMON'
force = [1000, 1000, 1000]
t_avg = 10
t_ramp = 60

vis.actuator_diag(
    stage = stage,
    dofs = dofs,
    act_block = act_block,
    sense_block = sense_block,
    force = force,
    t_avg = t_avg,
    t_ramp = t_ramp
    )
