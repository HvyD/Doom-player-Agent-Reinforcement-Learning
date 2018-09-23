def policy_iteration(env, gamma=1, theta=1e-8):
    policy = np.ones([env.nS, env.nA]) / env.nA
    V = policy_evaluation(env, policy, gamma, theta)
    new_policy = policy_improvement(env, V)
    
    while (new_policy != policy).any():
        policy = copy.copy(new_policy)
        V = policy_evaluation(env, policy, gamma, theta)
        new_policy = policy_improvement(env, V)
        

    return policy, V