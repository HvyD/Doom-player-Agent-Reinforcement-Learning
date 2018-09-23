def value_iteration(env, gamma=1, theta=1e-8):
    V = np.zeros(env.nS)
    delta = 1
    while theta < delta:
        delta = 0
        for state in range(env.nS):
            v = V[state]
            V[state] = max(q_from_v(env, V, state, gamma))
            delta = max(delta, abs(V[state] - v))
    policy = policy_improvement(env, V, gamma)
    
    return policy, V
    
    
    