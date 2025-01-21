# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

class Statistics:
    def __init__(self, data):
        self.data = data
        self.mean = self.calculate_mean()
        self.median = self.calculate_median()
        self.mode = self.calculate_mode()
        self.range = self.calculate_range()
        self.variance = self.calculate_variance()
        self.std = self.calculate_std()
        self.min = self.calculate_min()
        self.max = self.calculate_max()
        self.count = self.calculate_count()
        self.percentile = self.calculate_percentile()
        self.frequency_distribution = self.calculate_frequency_distribution()

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        sorted_data = sorted(self.data) 
        n = len(sorted_data) 
        if n % 2 == 0:
            return (sorted_data[n // 2] + sorted_data[n // 2 - 1]) / 2
        else: 
            return sorted_data[n // 2] 
    def calculate_mode(self):
        return max(set(self.data), key=self.data.count) 

    def calculate_range(self):
        return max(self.data) - min(self.data) 

    def calculate_variance(self): 
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data) 

    def calculate_std(self): 
        return self.calculate_variance() ** 0.5 

    def calculate_min(self): 
        return min(self.data)

    def calculate_max(self): 
        return max(self.data)

    def calculate_count(self): 
        return len(self.data)

    def calculate_percentile(self): 
        return self.data

    def calculate_frequency_distribution(self):
        return self.data
    