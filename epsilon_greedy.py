# coding: utf-8

try_num = 10000
epsilon = 0.1

execfile("core.py")
arm_rates = [0.012, 0.013, 0.013, 0.012, 0.012, 0.012, 0.011, 0.011, 0.011, 0.01, 0.01]
arms      = [BernoulliArm(r) for r in arm_rates]
counts    = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
values    = [0.012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
algo1     = EpsilonGreedy(epsilon, counts, values)
total     = 0
for t in range(try_num):
    chosen_arm = algo1.select_arm()
    reward     = arms[chosen_arm].draw()
    total      += reward
    algo1.update(chosen_arm, reward)

print total / try_num * 100
