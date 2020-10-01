from scipy.stats import zscore


class Statseg:
    def __init__(self, coordinates, stat_mat, res, eval_func):
        # initialization
        self.coordinates = coordinates
        self.stat_mat = stat_mat
        self.norm_stat_mat = zscore(stat_mat, axis=0)
        self.res = res
        # make var_mat
        self.gen_var_mat()
        
    # calculate k change points and k+1 segments
    def set_point_num(self, k):
        self.cps = self.calc_cps(k)
        self.segments = self.calc_segments(self.cps)
        
    # evaluate based on the function take x and label
    def scoring(self, eval_func):
        val = eval_func(self.norm_stat_mat, self.segments)
        return(val)
        
    # generate variance matrix
    def gen_var_mat(self):
        
