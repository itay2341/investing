



def get_levels_of_n_days_before(df, n_days_before):
    """
    Get the levels - support and resistance - of n days before
    """
    pass

def get_avg_of_n_days_before(column, n_days_before):
    """
    Get the average of n days before
    """
    pass

def get_std_of_n_days_before(column, n_days_before): 
    """
    Get the standard deviation of n days before
    """
    pass

def get_last_lowest(df):
    """
    Get the last lowest level
    """
    return df.iloc[-1,:].min()

def get_last_highest(df):
    """
    Get the last highest level
    """
    return df.iloc[-1,:].max()