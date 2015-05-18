execfile("core.py")
arm_rates = [0.012, 0.013, 0.013, 0.012, 0.012, 0.012, 0.011, 0.011, 0.011, 0.01, 0.01]
arms = [BernoulliArm(r) for r in arm_rates]
counts = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
values = [0.012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
algo1 = EpsilonGreedy(0.1, counts, values)
for t in range(1000):
    chosen_arm = algo1.select_arm()
    reward = arms[chosen_arm].draw()
    algo1.update(chosen_arm, reward)

