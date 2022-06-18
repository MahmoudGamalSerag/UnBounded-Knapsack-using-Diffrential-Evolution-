import random


def fitness(item):
    sum_w = 0
    sum_p = 0


    for index, i in enumerate(item):
        if i == 0:
            continue
        else:
            sum_w += weights[index]
            sum_p += profits[index]


    if sum_w > C:
        return -1
    else:
        return sum_p


def func1(x):
    # Sphere function, use any bounds, f(0,...,0)=0
    return sum([x[i] ** 2 for i in range(len(x))])



def ensure_bounds(vec, bounds):
    vec_new = []
    for i in range(len(vec)):

        if vec[i] < 0:
            vec_new.append(0)

        if vec[i] > 1:
            vec_new.append(1)

        if 0 <= vec[i] <= 1:
            vec_new.append(vec[i])

    return vec_new


def main(cost_func, bounds, popsize, mutate, recombination, maxiter,C,weights,profits):

    population = []
    parents=[]

    for i in range(popsize):
        parent = []
        for k in range(0, len(weights)):
            k = random.uniform(0, 1)
            parent.append(k)
            population.append(parent)


    for i in range(1, maxiter + 1):
        print('GENERATION:', i)

        gen_scores = []

        for j in range(0, popsize):

            canidates = list(range(0, popsize))
            canidates.remove(j)
            random_index = random.sample(canidates, 3)

            x_1 = population[random_index[0]]
            x_2 = population[random_index[1]]
            x_3 = population[random_index[2]]
            x_t = population[j]


            x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]


            v_donor = [x_1_i + mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
            v_donor = ensure_bounds(v_donor, bounds)



            v_trial = []
            for k in range(len(x_t)):
                crossover = random.random()
                if crossover >= recombination:
                    v_trial.append(v_donor[k])

                else:
                    v_trial.append(x_t[k])



            score_trial = fitness(v_trial)
            score_target = fitness(x_t)

            if score_trial > score_target:
                population[j] = v_trial
                gen_scores.append(score_trial)
                print('   >', score_trial, v_trial)

            else:
                print('   >', score_target, x_t)
                gen_scores.append(score_target)



        gen_avg = sum(gen_scores) / popsize
        gen_best = max(gen_scores)
        gen_sol = population[gen_scores.index(max(gen_scores))]

        print('      > GENERATION AVERAGE:', gen_avg)
        print('      > GENERATION BEST:', gen_best)
        print('         > BEST SOLUTION:', gen_sol, '\n')

    return gen_sol

weights=[]
profits=[]
maxiter=int(input("Enter maximum number of iterations: "))
C = int(input("enter capacity: "))
cost_func = func1
bounds = [(0,1)]
popsize = int(input("enter population size: "))
mutate = float(input("enter mutation factor [0,2]: "))
recombination = float(input("enter recombination rate [0,1]: "))
n = int(input("Enter number of elements : "))
for i in range(0, n):
    w = int(input("Enter weight of {} element : ".format(i+1)))
    p = int(input("Enter profit of {} element : ".format(i+1)))
    weights.append(w)
    profits.append(p)



main(cost_func, bounds, popsize, mutate, recombination, maxiter, C , weights, profits)

