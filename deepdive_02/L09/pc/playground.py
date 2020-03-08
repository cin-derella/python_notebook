import constants
import parse_utils
import itertools
from datetime import datetime

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


data_iter = parse_utils.iter_combined(constants.fnames,
                                      constants.class_names,
                                      constants.parsers,
                                      constants.compress_fields)
for row in itertools.islice(data_iter,5):
    print(row)

print('-------------------')

cutoff_date = datetime(2018,3,1)
filtered_iter = parse_utils.filtered_iter_combined(constants.fnames,
                                      constants.class_names,
                                      constants.parsers,
                                      constants.compress_fields,
                                      key = lambda row : row.last_updated >= cutoff_date)
for row in filtered_iter:
    print(row)