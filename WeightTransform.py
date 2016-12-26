import pickle
#with open('Breakout-v0_77.pkl', 'r') as fid:
with open('Pong-v0_141.pkl', 'r') as fid:
#with open('seaquest_178.pkl', 'r') as fid:
#with open('space_invaders_126.pkl', 'r') as fid:
    model_param = pickle.load(fid)

for lay_param in model_param['layer_params_states']:
    w = lay_param['params']
    lay_param['params'] = {'W': w}

#with open('Breakout-v0_77_new.pkl', 'w') as fid:
with open('Pong-v0_141_new.pkl', 'w') as fid:
#with open('seaquest_178_new.pkl', 'w') as fid:
#with open('space_invaders_126_new.pkl', 'w') as fid:
    pickle.dump(model_param, fid)
    

