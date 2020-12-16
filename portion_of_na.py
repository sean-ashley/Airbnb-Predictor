def portion_of_na(column):
    """
    Function that assesses what fraction of a column is NA values
    input : column : pandas series
    output : float : fraction of NA values as a portion of the total number of values in column
    """
    non_na = column.count()
    number_na = len(column) - non_na
    return number_na / len(column)
