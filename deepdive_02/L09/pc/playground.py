import constants
import parse_utils
import itertools
from datetime import datetime
from functools import partial

# # see a sample of what is in each file
# for fname in constants.fnames:
#     print(fname)
#     with open(fname) as f:
#         print(next(f),end = '')
#         print(next(f),end = '')
#         print(next(f),end = '')
#     print()

# for fname in constants.fnames:
#     print(fname)
#     with open(fname) as f:
#         reader = csv.reader(f,delimiter = ',',quotechar='"')
#         print(next(reader))
#         print(next(reader))
#     print()


# header row (field names)
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname,include_header=True)
#     print(next(reader),end= '\n')
#
# print('\n\n')

# # just the data
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname)
#     print(next(reader))
#     print(next(reader),end='\n')
#


# reader = parse_utils.csv_parser(constants.fname_update_status)
# for _ in range(3):
#     record = next(reader)
#     record = [str(record[0]),parse_utils.parse_date(record[1]),parse_utils.parse_date(record[2])]
#     print(record)


# for fname,class_name, parser in zip(constants.fnames,constants.class_names,constants.parsers):
#     file_iter = parse_utils.iter_file(fname,class_name,parser )
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()

#

# nt = parse_utils.create_combo_named_tuple_class(constants.fnames,constants.compress_fields)
# print(nt._fields)


# data_iter = parse_utils.iter_combined(constants.fnames,
#                                       constants.class_names,
#                                       constants.parsers,
#                                       constants.compress_fields)
# for row in itertools.islice(data_iter, 5):
#     print(row)
#
# print('-------------------')

# cutoff_date = datetime(2018, 3, 1)
#
#
# def group_key(item):
#     return item.vehicle_make
#
#
# data = parse_utils.filtered_iter_combined(constants.fnames,
#                                           constants.class_names,
#                                           constants.parsers,
#                                           constants.compress_fields,
#                                           key=lambda row: row.last_updated >= cutoff_date)
# data_1,data_2 = itertools.tee(data,2)
#
# data_m = (row for row in data_1 if row.gender =='Male')
# sorted_data_m = sorted(data_m,key=group_key)
# groups_m = itertools.groupby(sorted_data_m,key=group_key)
# group_m_counts = ((g[0],len(list(g[1]))) for g in groups_m)
# print('group_m')
# for row in group_m_counts:
#     print(row)
#
# print()
#
# data_f = (row for row in data_2 if row.gender =='Female')
# sorted_data_f = sorted(data_f,key=group_key)
# groups_f = itertools.groupby(sorted_data_f,key=group_key)
# group_f_counts = ((g[0],len(list(g[1]))) for g in groups_f)
# print('group_f')
# for row in group_f_counts:
#     print(row)


# sorted_data = sorted(data, key=group_key)
#
# groups_1 = itertools.groupby(sorted_data,key=group_key)
#
# groups_2 = itertools.groupby(sorted_data,key=group_key)
# #
# # rg1 = next(groups_1)
# # rg2 = next(groups_2)
# # print(rg1[0],id(rg1[1]))
# # print(rg2[0],id(rg2[1]))
# #
# # print()
# #
# # rg1 = next(groups_1)
# # rg2 = next(groups_2)
# # print(rg1[0],id(rg1[1]))
# # print(rg2[0],id(rg2[1]))
#
#
# group_f = (item for item in groups_1 if item[0][0]=='Female')
# data_f = ((item[0][1],len(list(item[1]))) for item in group_f)
# print('group_f')
# for row in data_f:
#     print(row)
#
#
# group_m = (item for item in groups_2 if item[0][0]=='Male')
#
# data_m = ((item[0][1],len(list(item[1]))) for item in group_m)
# print('group_m')
# for row in data_m:
#     print(row)

cutoff_date = datetime(2018, 3, 1)

def filter_key(cutoff_date, gender,row):
    return row.last_updated>=cutoff_date and row.gender == gender


results_f = parse_utils.group_data(constants.fnames,
                                   constants.class_names,
                                   constants.parsers,
                                   constants.compress_fields,
                                   filter_key= partial(filter_key,cutoff_date,'Famale'),
                                   group_key=lambda row: row.vehicle_make)

results_m = parse_utils.group_data(constants.fnames,
                                   constants.class_names,
                                   constants.parsers,
                                   constants.compress_fields,
                                   filter_key= lambda row :filter_key(cutoff_date,'Male',row),
                                   group_key=lambda row: row.vehicle_make)

print('results_f')
for row in results_f:
    print(row)
print()

print('results_m')
for row in results_m:
    print(row)