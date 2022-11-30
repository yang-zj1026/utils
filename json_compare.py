import argparse
import json
import dictdiffer
import numpy as np
import csv


def json_compare(ori_file_name, compare_file_name):
    """
        Compare the differences between two json files

        Input:
            ori_file_name: the original json file
            compare_file_name: the json file for comparison
        Output:
            a numpy array with differences between two json files
    """
    with open(ori_file_name) as ori_json_file:
        ori_json_dict = json.load(ori_json_file)

    with open(compare_file_name) as compare_json_file:
        compare_json_dict = json.load(compare_json_file)

    remove_from_list = ['command_line', 'train_dir', 'wandb_group', 'cli_args.train_dir', 'cli_args.wandb_group',
                        'experiments_root', 'git_hash', 'wandb_unique_id']

    diff_list = []
    dict_diff = list(dictdiffer.diff(ori_json_dict, compare_json_dict))
    for diff in dict_diff:
        if diff[1] in remove_from_list:
            continue

        diff_list.append(diff)

    with open('diff.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(np.array(diff_list))

    print(np.array(diff_list))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ori_file", type=str, required=True,
                        help="Original File")
    parser.add_argument("--compare_file", type=str, required=True,
                        help="Compared File")
    args = parser.parse_args()

    ori_file_name = args.ori_file
    compare_file_name = args.compare_file
    json_compare(ori_file_name, compare_file_name)
