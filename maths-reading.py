from asyncore import read
import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
mathscore = df["math score"].to_list()
reading = df["reading score"].to_list()
#Mean for maths score and reading score
maths_mean = statistics.mean(mathscore)
reading_mean = statistics.mean(reading)
#Median for maths score and reading score
maths_median = statistics.median(mathscore)
reading_median = statistics.median(reading)
#Mode for maths score and reading score
maths_mode = statistics.mode(mathscore)
reading_mode = statistics.mode(reading)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of maths score is {}, {} and {} respectively".format(maths_mean, maths_median, maths_mode))
print("Mean, Median and Mode of reading score is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
#Standard deviation for maths score and reading score
maths_std_deviation = statistics.stdev(mathscore)
reading_std_deviation = statistics.stdev(reading)
#1, 2 and 3 Standard Deviations for maths score
maths_first_std_deviation_start, maths_first_std_deviation_end = maths_mean-maths_std_deviation, maths_mean+maths_std_deviation
maths_second_std_deviation_start, maths_second_std_deviation_end = maths_mean-(2*maths_std_deviation), maths_mean+(2*maths_std_deviation)
maths_third_std_deviation_start, maths_third_std_deviation_end = maths_mean-(3*maths_std_deviation), maths_mean+(3*maths_std_deviation)
#1, 2 and 3 Standard Deviations for reading score
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for maths score
maths_list_of_data_within_1_std_deviation = [result for result in mathscore if result > maths_first_std_deviation_start and result < maths_first_std_deviation_end]
maths_list_of_data_within_2_std_deviation = [result for result in mathscore if result > maths_second_std_deviation_start and result <maths_second_std_deviation_end]
maths_list_of_data_within_3_std_deviation = [result for result in mathscore if result >maths_third_std_deviation_start and result < maths_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for reading score
reading_list_of_data_within_1_std_deviation = [result for result in reading if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]
#Printing data for maths score and reading score (Standard Deviation)
print("{}% of data for maths score lies within 1 standard deviation".format(len(maths_list_of_data_within_1_std_deviation)*100.0/len(mathscore)))
print("{}% of data for maths score lies within 2 standard deviations".format(len(maths_list_of_data_within_2_std_deviation)*100.0/len(mathscore)))
print("{}% of data for maths score lies within 3 standard deviations".format(len(maths_list_of_data_within_3_std_deviation)*100.0/len(mathscore)))
print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading)))
