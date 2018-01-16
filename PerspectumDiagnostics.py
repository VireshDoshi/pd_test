#!/usr/bin/env python

import itertools

def strings_appear_in_multiple_lists(list_in):
    """ This method will print out the list of Strings appearing in multiple
    Lists.

    Input: List of Lists ( 1..n)

    Output: String
    """
    # establish the size of the list
    list_in_len = len(list_in)

    # set the display_string
    display_string = ''

    final_list = []
    for b in range(0,list_in_len -1):
        for a in range(b,list_in_len-1):
            new_list = [ x for x  in list_in[b] if x in list_in[a + 1] ]
            final_list.append(new_list)


    # remove unwated empty lists
    filtered_final_list = [ x for x in final_list if x]

    for list in filtered_final_list:
        # display_string = "'".join(map(str,list))[1:-1]
        display_string = display_string + str(list)[1:-1] + ','

    # strip out the last comma
    display_string = display_string.rstrip(',')

    # print "Strings appearing in multiple lists: {0}".format(display_string)
    return display_string


def number_of_unique_strings(list_in):
    """
    This method will return the number of unique strings in the list given
    :param list_in:
    :return: integer of unique strings
    """

    # lets concatenate all the values into one large list for processing
    merged_list = list(itertools.chain(*list_in))

    # establish the length of items in the set
    merged_set_len = len(set(merged_list))

    # print "number of unique strings: {0}".format(merged_set_len)
    return merged_set_len

def total_number_of_strings_processed(list_in):
    """
    This method will return the number of strings processed
    :param list_in:
    :return: integer of strings processed
    """

    # lets concatenate all the values into one large list for processing
    merged_list = list(itertools.chain(*list_in))
    merged_len = len(merged_list)

    # print "Total number of strings processed {0}".format(merged_len)
    return merged_len

def perspectum_diagnostics_test(list_in):
    """
    This method displays the output to the screen based on the list
    :param list_in:
    :return: print output to the screen
    """
    print "Strings appearing in multiple lists: {0}".format(strings_appear_in_multiple_lists(list_in))
    print "number of unique strings: {0}".format(number_of_unique_strings(list_in))
    print "Total number of strings processed {0}".format(total_number_of_strings_processed(list_in))


if __name__ == '__main__':

    test_list_1 = [['a','b','c','dh'],['a','d','ha','e'],['f','g','h'],['c'],['dh'],['h','ha'],['e'],['d']]
    test_list_2 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
    test_list_3 = [['a'],['f'],['f']]

    perspectum_diagnostics_test(test_list_3)


