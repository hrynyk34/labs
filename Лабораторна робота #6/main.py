def calculate_project_estimation(tasks):
    total_a = 0
    total_m = 0
    total_b = 0

    for task in tasks:
        a, m, b = task
        total_a += a
        total_m += m
        total_b += b

    num_tasks = len(tasks)
    p_e = (total_a + 4 * total_m + total_b) / (6 * num_tasks)
    p_sd = (total_b - total_a) / (6 * num_tasks)
    p_se = p_sd

    ci_min = p_e - 2 * p_se
    ci_max = p_e + 2 * p_se

    return ci_min, ci_max

num_tasks = int(input("Введіть кількість завдань: "))
tasks = []

for i in range(num_tasks):
    a = float(input("Оцінка 'a' для завдання {}: ".format(i + 1)))
    m = float(input("Оцінка 'm' для завдання {}: ".format(i + 1)))
    b = float(input("Оцінка 'b' для завдання {}: ".format(i + 1)))
    tasks.append((a, m, b))

ci_min, ci_max = calculate_project_estimation(tasks)

print("95% Довірчий інтервал проекту: {} ... {} оцінка".format(ci_min, ci_max))