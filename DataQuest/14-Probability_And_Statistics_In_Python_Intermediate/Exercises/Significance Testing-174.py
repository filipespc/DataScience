## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52

mean_differences = []
for x in range(1000):
    group_a = []
    group_b = []
    for each in all_values:
        if np.random.rand() >= 0.5:
            group_a.append(each)
        else:
            group_b.append(each)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

print(all_values)

plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for each in mean_differences:
    sampling_distribution[each] = sampling_distribution.get(each,0) + 1
    
print(sampling_distribution)

## 8. P value ##

frequencies = []

for key,count in sampling_distribution.items():
    if key >= 2.52:
        frequencies.append(count)
        
p_value = np.sum(frequencies)/1000