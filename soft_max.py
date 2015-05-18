# coding: utf-8

execfile("core.py")

def calc_ecpm(algo):
    total = sum(algo.counts) - 10000
    ecpm = 0.0
    for idx, count in enumerate(algo.counts):
        if idx == 0:
            count -= 10000
        if count == 0:
            continue
        ecpm += 1000 * 60 * algo.values[idx] * float(count)/total
    return ecpm

def run_sm(tau, counts, values, arms):
    algo = Softmax(tau, counts, values)
    for t in xrange(10000):
        chosen_arm = algo.select_arm()
        reward = arms[chosen_arm].draw()
        algo.update(chosen_arm, reward)
    return calc_ecpm(algo)

def run():
    data = []
    arm_rates = [0.012, 0.013, 0.013, 0.012, 0.012, 0.012, 0.011, 0.011, 0.011, 0.01, 0.01]
    arms = [BernoulliArm(r) for r in arm_rates]
    counts = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    values = [0.012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in xrange(10):
        tau = 2**(i - 5)
        print tau
        for _ in xrange(10000):
            data.append((tau, run_sm(tau, counts, values, arms)))
    return pandas.DataFrame(data, columns=['tau', 'epcm'])

result = run()
result.boxplot(by="tau")
